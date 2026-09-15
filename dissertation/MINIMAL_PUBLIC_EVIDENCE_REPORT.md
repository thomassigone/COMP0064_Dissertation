# Minimal public evidence release-candidate report

## Scope and authority

This report documents a local release candidate for the evidence cited directly by the dissertation. The authority is Stage U Amendment-002 under the T.4.1 frozen configuration. Nothing in the complete private `android-vulnerability-agent/.artifacts/stage_u/amendment_002/` tree was edited, regenerated, committed, pushed, or published.

## Selected public evidence

Six trace directories contain 18 byte-identical frozen records:

| Bundle directory | Frozen run | Why selected |
| --- | --- | --- |
| `traces/e1-sqlite/` | `run-c66fc1b9522d040bad26e8e7` | Supports the SQLite action/observation/predicate account in Table 5.8 and Appendix H, including the absence of a recorded database mutation. |
| `traces/e1-external-storage/` | `run-dbafc6cb0b2882447a0c146d` | Supports the external-storage source/log-path account and the absence of SSN-content readback. |
| `traces/e1-tls/` | `run-3031d4756409497b31b2b14a` | Supports the capability-unavailable route and `UNSUPPORTED` outcome for both duplicate TLS hypotheses. |
| `traces/e1-dynamic-receiver/` | `run-ec8d974d6a2fc0b731e847ff` | Supports Appendix H's package/launch observations, rejected implicit-intent proposals, failed execution, and `INCONCLUSIVE` status. |
| `traces/e2-secure-control/` | `run-e454743f419b7de10fe3006e` | Supports the matched target-relative Secure control's completed run and absence of a normalised finding. |
| `traces/e3-fdroid-20/` | `run-83d147bd6d5bb91778a2a65a` | Supports Section 5.5's manifest/source observations, policy-rejected investigation, and `INCONCLUSIVE` status; F-Droid truth remains unknown and unadjudicated. |

For every trace, `request.json` establishes case/APK/configuration identity, `run-manifest.json` establishes terminal state and runner integrity values, and `attempt-result.json` contains the materially necessary Stage P and Q record. The latter includes observations, actions, capability/feasibility decision, assessment where present, predicates, termination, execution status, and lifecycle outcome. This three-file closure makes each cited path interpretable without publishing its complete workspace.

The E4 audit consists of:

- `audits/e4-attempt-summary.csv` - 48 row-oriented logical-attempt records.
- `audits/e4-attempt-summary.json` - the same records with aggregate and validation metadata.
- `audits/build-e4-summary.py` - a standard-library extractor/validator that reads the private E4 tree without modifying it.

`RUN_LOCATORS.csv`, `CITATION.cff`, `REDACTIONS.md`, `THIRD_PARTY_NOTICES.md`, the two files under `LICENSES/`, `provenance/freeze-identities.json`, and `MANIFEST.sha256` provide navigation, citation, privacy review, third-party attribution/licensing, provenance, and released-file integrity. The E4 script requires Python 3.9 or later and uses only the standard library; the documented command invokes `python3`.

## Dependency-closure and exclusion decisions

The trace files named above were retained because none is self-sufficient alone: the attempt result needs the request for the APK/configuration identity and the terminal manifest for the runner-recorded result hash. `attempt-start.json` was excluded because its run, attempt, resume, and start fields repeat the terminal manifest/result. Separate `report-ready.json`, discovery summaries/traces, validation summaries/traces, and observation exports were excluded because the selected `attempt-result.json` already embeds the evidence required to follow these six outcomes.

Complete Jadx workspaces, APKs, resources, device setup/teardown files, unrelated experiment runs, and separate raw provider transports were excluded. No E4 raw attempt tree was copied; the deterministic audit extract retains only the dissertation-facing fields and each source record's relative path and SHA-256. The full Amendment-002 tree remains private.

## Redactions and privacy

No redaction was required, so all 18 frozen trace records remain byte-identical to their originals. A fresh scan of the complete release candidate found no API credential, authorization header, bearer token, private-key marker, local absolute path, personal account identifier, APK, or binary. `diagnostics@startup.com` and `attacker@example.com` were the only email-shaped values and were retained as controlled evidence-bearing benchmark/input literals, not personal contact details. Provider/profile protocol metadata embedded in an attempt result was retained to preserve the original record and help interpret the action path; no separate raw provider request was added.

The attempt results embed bounded decompiled source and manifest extracts of varying length, including complete bounded class-file reads of up to 141 lines. `THIRD_PARTY_NOTICES.md` now maps each embedded extract to its source project and frozen revision. The five Ghera trace records are covered by the preserved BSD 3-Clause notice from Kansas State University at revision `ea1dbe234e4d3433161a3b85e96648913a36e83c`. The FDROID-20 extracts are from MotionLock 1.3 (22), revision `68a746fb592d94401d5cffcf711680050357a4df`, licensed AGPL-3.0-or-later. Revision-specific upstream URLs and verbatim licence copies are included.

Bundle-specific documentation and metadata are licensed under CC BY 4.0 to the extent owned by Thomas Louis Sigone; `audits/build-e4-summary.py` is MIT licensed. The notices expressly exclude the byte-identical mixed-provenance trace files from any blanket relicensing and preserve the upstream terms for embedded third-party material.

## E4 validation

The extractor found exactly 48 E4 runs and 16 per arm. It reproduced Chapter 5 Table 5.4:

| Arm | Complete | Matched target cases | Finding rows | Q outcomes |
| --- | ---: | ---: | ---: | --- |
| Deterministic static | 16/16 | 0/16 | 0 | Not run |
| Discovery only | 16/16 | 6/16 | 16 | `NOT_ENTERED` |
| Full pipeline | 16/16 | 3/16 | 9 | 5 `INCONCLUSIVE`; 4 `UNSUPPORTED` |

Direct raw-array extraction also reproduced five Stage P static signals in each arm. The tracked frozen summary contains five for deterministic static but zero in each HYBRID top-level summary field, matching the dissertation's explicit qualification. Tool calls, provider turns, runtime, token totals, and recorded cost values reconcile to `final-report/ablation-summary.csv`. A second generation into a temporary directory produced byte-identical CSV and JSON outputs.

## Package and integrity results

- Staging directory: `dissertation-evidence-v1/`
- Archive: `dist/dissertation-evidence-v1.zip`
- Released files: 30 total; `MANIFEST.sha256` covers the other 29.
- Uncompressed file bytes: 960,085 bytes; allocated directory size: approximately 1,004 KiB.
- Compressed archive: 166,427 bytes; allocated size: approximately 164 KiB.
- Local release-candidate archive SHA-256: `b21aed03154a3e37ca273d449d05683e3507e78eac1ee6f5f894a2ac8840cca7`.
- Archive integrity: `unzip -t` passed; extraction succeeded; the extracted manifest passed in full.
- Navigation: all six bundle-relative locators resolve to the required three files.
- Structure: no symlinks and no absolute or parent-traversal archive entries were found.
- Data validation: all 20 JSON files parse; `CITATION.cff` parses as YAML; E4 contains exactly 48 records and validated aggregates.
- Source fidelity: all 18 selected trace files compare byte-for-byte with their frozen originals; every E4 request/result passes the runner manifest's canonical-request/result checks. Both included licence copies compare byte-for-byte with the revision-specific source used for the check.

The private raw tree still has the Appendix I inventory values of 283,248 files and 3,552,862,876 bytes, and its newest file modification time remains 13 September 2026, before this task. The documented full-tree digest `06705d83cb93fa72a62fdea7210415f9177abe37838f7bf1fbc3f1fe36eddd69` is preserved in the bundle as a value from the tracked audit. An independent recomputation matched the file and byte counts but did not reproduce that digest using several plausible path bases; the repository does not preserve the original full-tree digest command. This is a path-canonicalisation/procedure ambiguity and remains unresolved rather than being silently reported as a successful independent digest check.

## Proposed dissertation-reference replacements

These are proposed edits only; the dissertation source was not changed.

### Chapter 5, Section 5.5, FDROID-20 source note

Replace the raw-run-only locator with:

> Public evidence bundle `<RELEASE_URL>` (tag `<RELEASE_TAG>`, archive SHA-256 `<ARCHIVE_SHA256>`), `traces/e3-fdroid-20/attempt-result.json`; frozen run `run-83d147bd6d5bb91778a2a65a`. The application's security ground truth remains `UNKNOWN` and manual status `UNADJUDICATED`.

### Chapter 5, Section 5.6 and Table 5.4 source

Replace “raw E4 attempts” in the source text with:

> Public evidence bundle `audits/e4-attempt-summary.csv` and `audits/e4-attempt-summary.json`, generated by `audits/build-e4-summary.py` from the private raw E4 records and reconciled to the frozen final-report run table. The bundle is available at `<RELEASE_URL>` (tag `<RELEASE_TAG>`, archive SHA-256 `<ARCHIVE_SHA256>`).

### Chapter 5, Section 5.7 trace-locator sentence

Replace the last locator sentence before the SQLite discussion with:

> Appendix H maps the representative cases to their frozen run IDs and bundle-relative paths. The selected request, terminal-manifest and attempt-result records are independently inspectable in the minimal public evidence bundle at `<RELEASE_URL>` (tag `<RELEASE_TAG>`, archive SHA-256 `<ARCHIVE_SHA256>`).

### Appendix H path block

Replace the `.artifacts/.../RUN-ID/...` construction block and following locator sentence with:

> In the minimal public evidence bundle, `RUN_LOCATORS.csv` maps each dissertation-facing case and frozen run ID to a stable bundle-relative trace directory. Each directory contains `request.json`, `run-manifest.json` and `attempt-result.json`. The bundle is available at `<RELEASE_URL>` (tag `<RELEASE_TAG>`, archive SHA-256 `<ARCHIVE_SHA256>`).

Replace Appendix H's final availability sentence with:

> The public bundle contains the six selected attempt results and their necessary request/terminal-manifest context. Complete raw attempt trees, decompiled workspaces, device records, unrelated runs and separate provider transports remain in the private archive and are not represented as publicly available.

### Appendix I public-availability paragraphs

Retain the existing code-repository paragraph, then replace the raw-tree availability paragraph with:

> A minimal public evidence bundle containing the six directly cited traces and a deterministic 48-attempt E4 audit extract is available at `<RELEASE_URL>` (tag `<RELEASE_TAG>`, archive SHA-256 `<ARCHIVE_SHA256>`). It is intentionally not the complete raw archive. The approximately 3.55-GB raw Amendment-002 attempt tree remains separately preserved and private; access for examination or institutional preservation is handled independently of the public release.

Add after Table I.2:

> The raw-tree digest in Table I.2 identifies the complete private archive; it is not the digest of the minimal public bundle.

## Unresolved risks and evidence dependencies

1. The public bundle cannot reproduce effects absent from the saved traces, such as SQLite database mutation, SSN content readback, or TLS interception.
2. The E4 summary can be audited as released, but regenerating it requires private access to all 48 E4 attempt records plus the tracked matching final-report files.
3. The preserved full-tree digest could not be independently reproduced from the prose algorithm because the original path-base/canonicalisation command is absent. File count, byte count, source mtimes, selected-file equality, and all 256 request/result manifest checks remain independently inspectable, but this digest limitation should be resolved before claiming a fresh full-tree hash verification.

## Release placeholders

- GitHub Release URL: `<RELEASE_URL>`
- Release tag: `<RELEASE_TAG>`
- Published archive SHA-256: `<ARCHIVE_SHA256>`

The complete raw archive remains private and is not included in this release candidate.
