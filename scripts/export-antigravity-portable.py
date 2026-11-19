"""Export the marketplace plugin as an Agent Plugins 1.0 directory."""
import argparse
import json
import shutil
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("package", type=Path, help="Native Antigravity package directory")
    parser.add_argument("output", type=Path, help="New directory outside the package")
    args = parser.parse_args()
    package, output = args.package.resolve(), args.output.resolve()
    if output == package or package in output.parents or output.exists():
        parser.error("Choose a new directory outside the native package.")
    native = json.loads((package / "plugin.json").read_text())
    license_file = package / "LICENSE.md"
    if native.get("license") == "Proprietary" and not license_file.is_file():
        parser.error("The proprietary plugin must include LICENSE.md.")
    config = json.loads((package / "mcp_config.json").read_text())["mcpServers"]
    manifest = {"$schema": "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json"}
    manifest.update({key: native[key] for key in ("name", "version", "description", "author", "homepage", "repository", "keywords")})
    if "license" in native:
        manifest["license"] = native["license"]
    servers = {name: {"type": "streamable-http", "url": server["serverUrl"]} for name, server in config.items()}
    output.mkdir(parents=True)
    for directory in ("skills", "references", "assets"):
        shutil.copytree(package / directory, output / directory)
    shutil.copyfile(package / "THIRD_PARTY_NOTICES.md", output / "THIRD_PARTY_NOTICES.md")
    notice_links = "[Third-party notices](THIRD_PARTY_NOTICES.md)"
    if license_file.is_file():
        shutil.copyfile(license_file, output / "LICENSE.md")
        notice_links = f"[Plugin license](LICENSE.md) · {notice_links}"
    (output / "plugin.json").write_text(json.dumps(manifest, indent=2) + "\n")
    (output / "mcp.json").write_text(json.dumps({
        "$schema": "https://agent-plugins.org/schemas/1.0.0/mcp.schema.json",
        "mcpServers": servers,
    }, indent=2) + "\n")
    (output / "README.md").write_text(
        f"# {native['displayName']}\n\n{native['description']}\n\n"
        "Install this directory in a client that supports Agent Plugins 1.0 and remote HTTP MCP servers. "
        f"Connect with your SeekOut account. [Documentation]({native['homepage']})\n\n{notice_links}\n"
    )


if __name__ == "__main__":
    main()
