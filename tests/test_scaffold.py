from __future__ import annotations

import hashlib
import json
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import build as builder  # noqa: E402
import validate as validator  # noqa: E402
from common import all_files, content_digest, load_json, sha256_file  # noqa: E402


FIXED_SHA = "0123456789abcdef0123456789abcdef01234567"
EXPECTED_ARTIFACTS = {
    "recruiting",
    "recruiting-codex",
    "recruiting-claude-code",
    "recruiting-cursor",
    "recruiting-antigravity",
}


class ScaffoldTests(unittest.TestCase):
    def test_source_scaffold_is_valid(self) -> None:
        validator.validate()

    def test_build_is_byte_for_byte_deterministic(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            base = Path(temporary)
            first = base / "first"
            second = base / "second"
            builder.build(first, FIXED_SHA)
            builder.build(second, FIXED_SHA)

            first_files = {
                path.relative_to(first).as_posix(): hashlib.sha256(path.read_bytes()).hexdigest()
                for path in all_files(first)
            }
            second_files = {
                path.relative_to(second).as_posix(): hashlib.sha256(path.read_bytes()).hexdigest()
                for path in all_files(second)
            }
            self.assertEqual(first_files, second_files)

    def test_expected_manifest_only_artifact_structure(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            output = Path(temporary) / "dist"
            release = builder.build(output, FIXED_SHA)
            self.assertEqual(
                {entry["name"] for entry in release["artifacts"]}, EXPECTED_ARTIFACTS
            )

            names = set()
            for entry in release["artifacts"]:
                package = output / entry["packagePath"]
                manifest = load_json(package / "plugin.json")
                names.add(manifest["name"])
                self.assertEqual(manifest["version"], "0.1.0")
                self.assertFalse((package / "skills").exists())
                self.assertFalse((package / "mcp.json").exists())
                self.assertFalse((package / ".mcp.json").exists())
                self.assertEqual(
                    load_json(package / "metadata" / "artifact.json")["workflowContracts"],
                    {},
                )

                native_manifest = package / ".codex-plugin" / "plugin.json"
                self.assertEqual(native_manifest.exists(), entry["name"] == "recruiting-codex")
                self.assertEqual(
                    content_digest(all_files(package), package), entry["contentSha256"]
                )
                archive = output / entry["archivePath"]
                self.assertEqual(sha256_file(archive), entry["archiveSha256"])
                with zipfile.ZipFile(archive) as handle:
                    self.assertEqual(
                        sorted(handle.namelist()),
                        sorted(path.relative_to(package).as_posix() for path in all_files(package)),
                    )
            self.assertEqual(names, EXPECTED_ARTIFACTS)

    def test_release_checksums_match_archives(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            output = Path(temporary) / "dist"
            builder.build(output, FIXED_SHA)
            lines = (output / "CHECKSUMS.sha256").read_text(encoding="utf-8").splitlines()
            self.assertEqual(len(lines), 5)
            for line in lines:
                expected, relative = line.split("  ", 1)
                self.assertEqual(expected, sha256_file(output / relative))

    def test_generated_release_metadata_has_required_benchmark_identity(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            output = Path(temporary) / "dist"
            builder.build(output, FIXED_SHA)
            release = load_json(output / "release-manifest.json")
            self.assertEqual(release["sourceSha"], FIXED_SHA)
            self.assertEqual(release["suiteVersion"], "0.1.0")
            self.assertEqual(release["agentPluginsSpecVersion"], "1.0.0")
            self.assertEqual(release["compatibilityMatrixVersion"], 1)
            self.assertEqual(release["workflowContracts"], {})
            for artifact in release["artifacts"]:
                self.assertRegex(artifact["archiveSha256"], r"^[0-9a-f]{64}$")
                self.assertRegex(artifact["contentSha256"], r"^[0-9a-f]{64}$")


if __name__ == "__main__":
    unittest.main()
