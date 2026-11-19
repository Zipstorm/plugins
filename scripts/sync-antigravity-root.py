"""Build the files Antigravity reads when installing from the repository URL."""

import argparse
import json
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Report stale files without writing.")
    args = parser.parse_args()

    root = Path(__file__).resolve().parent.parent
    package = Path("plugins/antigravity")
    manifest = json.loads((root / package / "plugin.json").read_text())
    manifest["logo"] = (package / manifest["logo"]).as_posix()
    manifest["skills"] = ["./" + (package / "skills").as_posix()]
    files = {
        root / ".antigravity-plugin/plugin.json": (json.dumps(manifest, indent=2) + "\n").encode(),
        root / "mcp_config.json": (root / package / "mcp_config.json").read_bytes(),
        root / "rules/AGENTS.md": (root / package / "rules/AGENTS.md").read_bytes(),
    }
    stale = [path for path, data in files.items() if not path.is_file() or path.read_bytes() != data]
    if args.check and stale:
        names = ", ".join(path.relative_to(root).as_posix() for path in stale)
        parser.exit(1, f"Run python3 scripts/sync-antigravity-root.py to update {names}\n")
    for path in stale:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(files[path])


if __name__ == "__main__":
    main()
