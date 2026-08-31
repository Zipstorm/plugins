#!/usr/bin/env python3
"""Build deterministic manifest-only artifacts for every declared profile."""

from __future__ import annotations

import argparse
import shutil
import sys
import tempfile
import zipfile
from pathlib import Path
from typing import Any, Dict, List

sys.path.insert(0, str(Path(__file__).resolve().parent))

from common import (  # noqa: E402
    ROOT,
    ValidationError,
    all_files,
    content_digest,
    load_json,
    resolve_repo_path,
    sha256_file,
    source_sha,
    validate_package_path,
    validate_plugin_name,
    validate_semver,
    write_json,
)


FIXED_ZIP_TIME = (1980, 1, 1, 0, 0, 0)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT / "dist")
    parser.add_argument("--source-sha", help="full 40-character source commit SHA")
    parser.add_argument("--clean", action="store_true", help="remove the output and exit")
    return parser.parse_args()


def safe_remove_output(output: Path) -> None:
    resolved = output.resolve()
    forbidden = {Path("/").resolve(), ROOT.resolve(), ROOT.parent.resolve()}
    if resolved in forbidden or len(resolved.parts) < 3:
        raise ValidationError("refusing to remove unsafe output path: {}".format(resolved))
    if resolved.exists():
        shutil.rmtree(str(resolved))


def portable_manifest(
    suite: Dict[str, Any], artifact: Dict[str, Any]
) -> Dict[str, Any]:
    return {
        "$schema": "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json",
        "author": suite["author"],
        "description": (
            "Manifest-only {} foundation for the recruiting plugin suite; "
            "no skills or MCP servers are included."
        ).format(artifact["profile"]),
        "keywords": ["recruiting", "agent-plugin", artifact["profile"]],
        "name": artifact["name"],
        "version": suite["suiteVersion"],
    }


def copy_declared_components(adapter_dir: Path, package_dir: Path) -> None:
    descriptor = load_json(adapter_dir / "adapter.json")
    for component_name, component in sorted(descriptor["components"].items()):
        if component["status"] != "implemented":
            continue
        source = resolve_repo_path(
            adapter_dir,
            component["sourcePath"],
            "{}.{}.sourcePath".format(descriptor["id"], component_name),
        )
        if not source.exists():
            raise ValidationError("declared component source does not exist: {}".format(source))
        package_path = validate_package_path(
            component["packagePath"],
            "{}.{}.packagePath".format(descriptor["id"], component_name),
        )
        destination = package_dir.joinpath(*package_path.parts)
        destination.parent.mkdir(parents=True, exist_ok=True)
        if source.is_file():
            shutil.copyfile(str(source), str(destination))
        elif source.is_dir():
            shutil.copytree(str(source), str(destination))
        else:
            raise ValidationError("component source must be a regular file or directory")


def write_status(package_dir: Path, artifact: Dict[str, Any]) -> None:
    package_dir.joinpath("PACKAGE-STATUS.md").write_text(
        "# Package status\n\n"
        "This is the `{}` manifest-only scaffold. It contains no skills, workflow "
        "implementations, hooks, agents, commands, rules, permissions, or MCP "
        "connections.\n".format(artifact["name"]),
        encoding="utf-8",
    )


def write_deterministic_zip(package_dir: Path, archive_path: Path) -> None:
    archive_path.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(str(archive_path), "w", compression=zipfile.ZIP_STORED) as archive:
        for path in sorted(all_files(package_dir), key=lambda item: item.relative_to(package_dir).as_posix()):
            relative = path.relative_to(package_dir).as_posix()
            info = zipfile.ZipInfo(relative, date_time=FIXED_ZIP_TIME)
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            info.compress_type = zipfile.ZIP_STORED
            archive.writestr(info, path.read_bytes())


def validate_suite_for_build(suite: Dict[str, Any]) -> None:
    validate_semver(suite.get("suiteVersion"), "suiteVersion")
    if suite.get("agentPluginsSpecVersion") != "1.0.0":
        raise ValidationError("only Agent Plugins 1.0.0 is supported")
    artifacts = suite.get("artifacts")
    if not isinstance(artifacts, list) or not artifacts:
        raise ValidationError("suite.artifacts must be a non-empty list")
    names = []
    profiles = []
    for artifact in artifacts:
        if not isinstance(artifact, dict):
            raise ValidationError("each suite artifact must be an object")
        validate_plugin_name(artifact.get("name"), "artifact.name")
        names.append(artifact["name"])
        profiles.append(artifact.get("profile"))
    if len(names) != len(set(names)) or len(profiles) != len(set(profiles)):
        raise ValidationError("artifact names and profiles must be unique")


def build(output: Path, commit_sha: str) -> Dict[str, Any]:
    if len(commit_sha) != 40 or any(char not in "0123456789abcdef" for char in commit_sha):
        raise ValidationError("source SHA must be 40 lowercase hexadecimal characters")
    suite = load_json(ROOT / "release" / "suite.json")
    validate_suite_for_build(suite)

    output = output.resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    staging = Path(tempfile.mkdtemp(prefix="agent-plugins-build-", dir=str(output.parent)))
    try:
        packages_root = staging / "packages"
        archives_root = staging / "archives"
        release_entries: List[Dict[str, Any]] = []
        for artifact in suite["artifacts"]:
            package_dir = packages_root / artifact["name"]
            package_dir.mkdir(parents=True)
            write_json(package_dir / "plugin.json", portable_manifest(suite, artifact))
            if artifact["adapter"] is not None:
                copy_declared_components(ROOT / "adapters" / artifact["adapter"], package_dir)
            metadata = {
                "schemaVersion": 1,
                "suiteVersion": suite["suiteVersion"],
                "artifactName": artifact["name"],
                "harnessProfile": artifact["profile"],
                "packageMode": artifact["packageMode"],
                "status": "scaffold-no-skills",
                "sourceSha": commit_sha,
                "workflowContracts": {},
                "agentPluginsSpecVersion": suite["agentPluginsSpecVersion"],
                "compatibilityMatrixVersion": 1,
            }
            write_json(package_dir / "metadata" / "artifact.json", metadata)
            write_status(package_dir, artifact)

            archive_name = "{}-{}.zip".format(artifact["name"], suite["suiteVersion"])
            archive_path = archives_root / archive_name
            write_deterministic_zip(package_dir, archive_path)
            release_entries.append(
                {
                    "name": artifact["name"],
                    "harnessProfile": artifact["profile"],
                    "packageMode": artifact["packageMode"],
                    "packagePath": "packages/{}".format(artifact["name"]),
                    "archivePath": "archives/{}".format(archive_name),
                    "contentSha256": content_digest(all_files(package_dir), package_dir),
                    "archiveSha256": sha256_file(archive_path),
                }
            )

        release_manifest = {
            "schemaVersion": 1,
            "suiteVersion": suite["suiteVersion"],
            "sourceSha": commit_sha,
            "agentPluginsSpecVersion": suite["agentPluginsSpecVersion"],
            "compatibilityMatrixVersion": 1,
            "workflowContracts": {},
            "artifacts": release_entries,
        }
        write_json(staging / "release-manifest.json", release_manifest)
        checksums = "".join(
            "{}  {}\n".format(entry["archiveSha256"], entry["archivePath"])
            for entry in release_entries
        )
        (staging / "CHECKSUMS.sha256").write_text(checksums, encoding="utf-8")

        safe_remove_output(output)
        staging.rename(output)
        return release_manifest
    except Exception:
        if staging.exists():
            shutil.rmtree(str(staging))
        raise


def main() -> None:
    args = parse_args()
    if args.clean:
        safe_remove_output(args.output)
        print("Removed build output: {}".format(args.output.resolve()))
        return
    commit_sha = args.source_sha or source_sha()
    manifest = build(args.output, commit_sha)
    print(
        "Built {} deterministic scaffold artifacts in {}".format(
            len(manifest["artifacts"]), args.output.resolve()
        )
    )


if __name__ == "__main__":
    main()
