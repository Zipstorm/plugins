#!/usr/bin/env python3
"""Validate the source scaffold without network access or third-party packages."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any, Dict, List

sys.path.insert(0, str(Path(__file__).resolve().parent))

from common import (  # noqa: E402
    PORTABLE_SCHEMA_ID,
    ROOT,
    ValidationError,
    load_json,
    resolve_repo_path,
    validate_package_path,
    validate_plugin_name,
    validate_portable_manifest,
    validate_semver,
)


ADAPTER_IDS = ("codex", "claude-code", "cursor", "antigravity")
COMPONENT_KEYS = {
    "skills",
    "hooks",
    "agents",
    "subagents",
    "commands",
    "instructions",
    "rules",
    "mcpOverrides",
    "permissions",
    "packagingMetadata",
}
FORBIDDEN_RUNTIME_FILES = {"SKILL.md", "mcp.json", ".mcp.json", "hooks.json"}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValidationError(message)


def validate_suite() -> Dict[str, Any]:
    suite = load_json(ROOT / "release" / "suite.json")
    require(suite.get("schemaVersion") == 1, "suite.schemaVersion must be 1")
    validate_semver(suite.get("suiteVersion"), "suite.suiteVersion")
    require(
        suite.get("agentPluginsSpecVersion") == "1.0.0",
        "suite must target Agent Plugins 1.0.0",
    )
    artifacts = suite.get("artifacts")
    require(isinstance(artifacts, list), "suite.artifacts must be an array")
    expected_profiles = {"portable", "codex", "claude-code", "cursor", "antigravity"}
    profiles = {artifact.get("profile") for artifact in artifacts}
    require(profiles == expected_profiles, "suite must declare exactly the five scaffold profiles")
    names = [artifact.get("name") for artifact in artifacts]
    require(len(names) == len(set(names)), "artifact names must be unique")
    for artifact in artifacts:
        validate_plugin_name(artifact.get("name"), "artifact.name")
        adapter = artifact.get("adapter")
        require(
            (artifact["profile"] == "portable" and adapter is None)
            or adapter == artifact["profile"],
            "artifact adapter must match its non-portable profile",
        )
    return suite


def validate_adapters(suite: Dict[str, Any]) -> None:
    artifacts = {artifact["profile"]: artifact for artifact in suite["artifacts"]}
    for adapter_id in ADAPTER_IDS:
        adapter_dir = ROOT / "adapters" / adapter_id
        descriptor = load_json(adapter_dir / "adapter.json")
        require(descriptor.get("id") == adapter_id, "adapter id does not match its directory")
        require(
            descriptor.get("artifactName") == artifacts[adapter_id]["name"],
            "adapter artifactName drifted from suite.json",
        )
        require(descriptor.get("status") == "scaffold", "adapters must remain scaffold status")
        components = descriptor.get("components")
        require(isinstance(components, dict), "adapter components must be an object")
        require(set(components) == COMPONENT_KEYS, "adapter component slots are incomplete")
        for name, component in components.items():
            require(isinstance(component, dict), "adapter component must be an object")
            status = component.get("status")
            require(status in {"planned", "implemented"}, "invalid component status")
            if status == "implemented":
                require(
                    set(component) == {"status", "sourcePath", "packagePath"},
                    "implemented components require sourcePath and packagePath",
                )
                source = resolve_repo_path(
                    adapter_dir,
                    component["sourcePath"],
                    "{}.{}.sourcePath".format(adapter_id, name),
                )
                require(source.exists(), "implemented adapter source is missing")
                validate_package_path(
                    component["packagePath"],
                    "{}.{}.packagePath".format(adapter_id, name),
                )
            else:
                require(
                    set(component) == {"status"},
                    "planned components must not point to loadable files",
                )
        implemented = {
            name for name, component in components.items() if component["status"] == "implemented"
        }
        expected = {"packagingMetadata"} if adapter_id == "codex" else set()
        require(
            implemented == expected,
            "only Codex packaging metadata may be implemented in the basic scaffold",
        )


def validate_manifests(suite: Dict[str, Any]) -> None:
    version = suite["suiteVersion"]
    portable = load_json(ROOT / "plugin.json")
    validate_portable_manifest(portable, "plugin.json")
    require(portable["name"] == "recruiting", "root portable manifest name must be recruiting")
    require(portable.get("version") == version, "root portable manifest version drift")

    codex_root = ROOT / "plugins" / "recruiting-codex"
    codex_portable = load_json(codex_root / "plugin.json")
    validate_portable_manifest(codex_portable, "Codex portable plugin.json")
    require(codex_portable["name"] == "recruiting-codex", "Codex portable name drift")
    require(codex_portable.get("version") == version, "Codex portable version drift")

    native = load_json(codex_root / ".codex-plugin" / "plugin.json")
    allowed = {
        "id", "name", "version", "description", "skills", "apps", "mcpServers",
        "interface", "author", "homepage", "repository", "license", "keywords",
    }
    require(not set(native) - allowed, "Codex native manifest has unsupported fields")
    require(native.get("name") == "recruiting-codex", "Codex native name drift")
    require(native.get("version") == version, "Codex native version drift")
    require("skills" not in native, "Codex scaffold must not declare skills")
    require("mcpServers" not in native, "Codex scaffold must not declare MCP servers")
    require("apps" not in native, "Codex scaffold must not declare apps")
    author = native.get("author")
    require(isinstance(author, dict) and bool(author.get("name")), "Codex author is required")
    interface = native.get("interface")
    require(isinstance(interface, dict), "Codex interface is required")
    for field in ("displayName", "shortDescription", "longDescription", "developerName", "category"):
        require(isinstance(interface.get(field), str) and bool(interface[field]), "missing Codex interface field")
    require(interface.get("capabilities") == [], "Codex scaffold cannot claim capabilities")
    require(interface.get("defaultPrompt") == [], "Codex scaffold cannot advertise prompts")


def validate_marketplace() -> None:
    marketplace = load_json(ROOT / ".agents" / "plugins" / "marketplace.json")
    require(isinstance(marketplace.get("name"), str), "marketplace name is required")
    plugins = marketplace.get("plugins")
    require(isinstance(plugins, list) and len(plugins) == 1, "marketplace must contain one entry")
    entry = plugins[0]
    require(entry.get("name") == "recruiting-codex", "marketplace plugin name drift")
    require(
        entry.get("source") == {"source": "local", "path": "./plugins/recruiting-codex"},
        "marketplace source must use the repo-local Codex plugin",
    )
    require(
        entry.get("policy")
        == {"installation": "AVAILABLE", "authentication": "ON_INSTALL"},
        "marketplace policy drift",
    )
    require(entry.get("category") == "Productivity", "marketplace category drift")


def validate_compatibility(suite: Dict[str, Any]) -> None:
    matrix = load_json(ROOT / "release" / "compatibility.json")
    require(matrix.get("schemaVersion") == 1, "compatibility schemaVersion must be 1")
    require(matrix.get("suiteVersion") == suite["suiteVersion"], "compatibility version drift")
    clients = matrix.get("clients")
    require(isinstance(clients, list), "compatibility clients must be an array")
    by_id = {client.get("id"): client for client in clients}
    require(set(by_id) == {"portable", *ADAPTER_IDS}, "compatibility client set drift")
    artifacts = {artifact["profile"]: artifact["name"] for artifact in suite["artifacts"]}
    for client_id, client in by_id.items():
        require(client.get("artifact") == artifacts[client_id], "compatibility artifact drift")
        require(client.get("packageStatus") == "scaffold-no-skills", "invalid package status")
        components = client.get("components")
        require(isinstance(components, dict), "compatibility components must be an object")
        require(components.get("skills") == "planned", "skills must remain planned")
        require(components.get("portableManifest") == "implemented", "portable manifest missing")
        expected_native = "implemented" if client_id == "codex" else (
            "not-applicable" if client_id == "portable" else "planned"
        )
        require(components.get("nativeManifest") == expected_native, "native status drift")


def validate_no_runtime_components() -> None:
    excluded_parts = {".git", "dist", "__pycache__"}
    violations: List[str] = []
    for path in ROOT.rglob("*"):
        if any(part in excluded_parts for part in path.parts):
            continue
        if path.is_file() and path.name in FORBIDDEN_RUNTIME_FILES:
            violations.append(str(path.relative_to(ROOT)))
        if path.is_file() and path.suffix in {".md", ".json", ".py", ".yml", ".yaml"}:
            try:
                text = path.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                continue
            placeholder_marker = "[" + "TODO:"
            if placeholder_marker in text:
                violations.append("{} contains a TODO placeholder".format(path.relative_to(ROOT)))
    require(not violations, "runtime/placeholder files are forbidden: {}".format(", ".join(violations)))


def validate_schema_files() -> None:
    for path in sorted((ROOT / "schemas").rglob("*.json")):
        load_json(path)
    upstream = load_json(ROOT / "schemas" / "agent-plugins" / "1.0.0" / "plugin.schema.json")
    require(upstream.get("$id") == PORTABLE_SCHEMA_ID, "vendored schema id drift")


def validate() -> None:
    suite = validate_suite()
    validate_adapters(suite)
    validate_manifests(suite)
    validate_marketplace()
    validate_compatibility(suite)
    validate_no_runtime_components()
    validate_schema_files()


def main() -> None:
    try:
        validate()
    except ValidationError as error:
        print("Validation failed: {}".format(error), file=sys.stderr)
        raise SystemExit(1)
    print("Repository scaffold validation passed")


if __name__ == "__main__":
    main()
