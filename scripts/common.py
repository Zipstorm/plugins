#!/usr/bin/env python3
"""Shared, dependency-free validation and serialization helpers."""

from __future__ import annotations

import hashlib
import json
import re
import subprocess
from pathlib import Path, PurePosixPath
from typing import Any, Dict, Iterable, List


ROOT = Path(__file__).resolve().parents[1]
PORTABLE_SCHEMA_ID = "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json"
PORTABLE_FIELDS = {
    "$schema",
    "name",
    "version",
    "description",
    "author",
    "homepage",
    "repository",
    "license",
    "keywords",
    "extensions",
}
PLUGIN_NAME_RE = re.compile(
    r"^(?!.*(?:--|\.\.))[a-z0-9](?:[a-z0-9.-]*[a-z0-9])?$"
)
SEMVER_RE = re.compile(
    r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)"
    r"(?:-(?:0|[1-9]\d*|\d*[A-Za-z-][0-9A-Za-z-]*)"
    r"(?:\.(?:0|[1-9]\d*|\d*[A-Za-z-][0-9A-Za-z-]*))*)?"
    r"(?:\+[0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*)?$"
)


class ValidationError(ValueError):
    """Raised for an invalid repository or package contract."""


def load_json(path: Path) -> Dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as error:
        raise ValidationError("missing JSON file: {}".format(path)) from error
    except json.JSONDecodeError as error:
        raise ValidationError("invalid JSON in {}: {}".format(path, error)) from error
    if not isinstance(value, dict):
        raise ValidationError("{} must contain a JSON object".format(path))
    return value


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(value, indent=2, sort_keys=True, ensure_ascii=True) + "\n",
        encoding="utf-8",
    )


def validate_semver(value: Any, label: str) -> None:
    if not isinstance(value, str) or SEMVER_RE.fullmatch(value) is None:
        raise ValidationError("{} must be strict SemVer".format(label))


def validate_plugin_name(value: Any, label: str) -> None:
    if (
        not isinstance(value, str)
        or not 1 <= len(value) <= 64
        or PLUGIN_NAME_RE.fullmatch(value) is None
    ):
        raise ValidationError("{} is not a valid Agent Plugins name".format(label))


def validate_portable_manifest(manifest: Dict[str, Any], label: str) -> None:
    unknown = sorted(set(manifest) - PORTABLE_FIELDS)
    if unknown:
        raise ValidationError("{} has unknown fields: {}".format(label, ", ".join(unknown)))
    if manifest.get("$schema") != PORTABLE_SCHEMA_ID:
        raise ValidationError("{} has the wrong Agent Plugins schema".format(label))
    validate_plugin_name(manifest.get("name"), "{}.name".format(label))
    if "version" in manifest:
        validate_semver(manifest["version"], "{}.version".format(label))
    for field in ("description", "homepage", "repository", "license"):
        if field in manifest and not isinstance(manifest[field], str):
            raise ValidationError("{}.{} must be a string".format(label, field))
    author = manifest.get("author")
    if author is not None:
        if not isinstance(author, dict) or set(author) - {"name", "email", "url"}:
            raise ValidationError("{}.author has an invalid shape".format(label))
        if not all(isinstance(value, str) for value in author.values()):
            raise ValidationError("{}.author values must be strings".format(label))
    keywords = manifest.get("keywords")
    if keywords is not None and (
        not isinstance(keywords, list)
        or not all(isinstance(value, str) for value in keywords)
    ):
        raise ValidationError("{}.keywords must be an array of strings".format(label))
    extensions = manifest.get("extensions")
    if extensions is not None and (
        not isinstance(extensions, dict)
        or not all(isinstance(value, dict) for value in extensions.values())
    ):
        raise ValidationError("{}.extensions values must be objects".format(label))


def resolve_repo_path(base: Path, raw_path: str, label: str) -> Path:
    candidate = (base / raw_path).resolve()
    try:
        candidate.relative_to(ROOT.resolve())
    except ValueError as error:
        raise ValidationError("{} escapes the repository".format(label)) from error
    return candidate


def validate_package_path(raw_path: str, label: str) -> PurePosixPath:
    path = PurePosixPath(raw_path)
    if path.is_absolute() or not path.parts or ".." in path.parts or "." in path.parts:
        raise ValidationError("{} must be a contained package-relative path".format(label))
    return path


def source_sha() -> str:
    result = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        cwd=str(ROOT),
        check=True,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    value = result.stdout.strip().lower()
    if re.fullmatch(r"[0-9a-f]{40}", value) is None:
        raise ValidationError("git did not return a full source SHA")
    return value


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def content_digest(files: Iterable[Path], base: Path) -> str:
    digest = hashlib.sha256()
    for path in sorted(files, key=lambda item: item.relative_to(base).as_posix()):
        relative = path.relative_to(base).as_posix().encode("utf-8")
        digest.update(relative)
        digest.update(b"\0")
        digest.update(path.read_bytes())
        digest.update(b"\0")
    return digest.hexdigest()


def all_files(root: Path) -> List[Path]:
    return [path for path in root.rglob("*") if path.is_file()]
