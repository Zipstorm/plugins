# Release policy

## Versions and channels

All artifacts in a suite release use the same strict SemVer from `release/suite.json`:

- Stable: `X.Y.Z`, Git tag `suite/vX.Y.Z`.
- Beta: `X.Y.Z-beta.N`, Git tag `suite/vX.Y.Z-beta.N`.
- Canary: `X.Y.Z-canary.YYYYMMDD.shortsha`, Git tag with the same version after `suite/v`.

Breaking workflow contract or packaging changes require a major version; backward-compatible workflows or adapter capabilities require a minor version; fixes that preserve contracts and packaging use a patch. Pre-release precedence follows SemVer.

## Release invariants

Build from a clean, reviewed, scoped Git tag. Never replace an archive attached to an existing tag/version. Publish all five archives together with `release-manifest.json` and `CHECKSUMS.sha256`. A corrected build gets a new SemVer; a canary is never promoted by moving or rewriting its tag.

## Required provenance

Consumers and the future benchmark repository must record:

- suite version;
- artifact name;
- harness profile;
- Agent Plugins specification version;
- workflow contract version map (empty in this scaffold);
- compatibility matrix schema version;
- full source commit SHA;
- artifact content SHA-256; and
- archive SHA-256.

The generated release manifest contains every field. The digest is outside the artifact to avoid a self-referential digest.

## Release check

```sh
make clean
make check
make build
(cd dist && sha256sum -c CHECKSUMS.sha256)
```

On macOS, use `shasum -a 256` to verify individual entries if `sha256sum` is unavailable.
