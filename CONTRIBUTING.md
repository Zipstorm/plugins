# Contributing

Run `make check` before opening a change.

Keep portable Agent Plugins fields and components separate from native adapters. Do not add a client file merely to reserve a name: declare the slot as `planned` in its adapter until a real, validated implementation exists. Once implemented, give it an explicit `sourcePath` and contained `packagePath`; the builder copies only declared components.

Do not add credentials, customer or tenant configuration, backend endpoints, benchmark cases, or benchmark implementation here. Do not add MCP configuration until a real integration contract and authentication approach are approved.

Future workflow changes should keep shared inputs, outputs, invariants, safety rules, evidence requirements, and rubrics in one workflow contract while giving each harness a standalone build-time profile. Contract and profile work is intentionally outside the initial scaffold.

Version changes must update the suite, checked-in portable and Codex manifests, compatibility matrix, tests, and release notes together. Generated `dist/` files are not committed.
