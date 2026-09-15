# Submission Manifest

**Project:** Agentic Vulnerability Finder for Android Applications<br>
**Author:** Thomas Louis Sigone<br>
**Programme:** MSc Information Security<br>
**Institution:** University College London<br>
**Module:** COMP0064<br>
**Submission:** 15 September 2026

## Repository state

This documentation pass began on branch `main` at HEAD `92667e842f0eee70068cfceee6559c6d2596e99d`, the report-bearing editorial commit identified by the final dissertation evidence baseline. The working tree already contained the untracked local `dissertation/` directory, which is not part of this documentation commit. This manifest and the revised `README.md` form a documentation-only commit on top of that report-bearing identity. A plain Git archive contains them when that documentation commit is selected as the archive commit.

The historically distinct identities remain:

- T.4.1 implementation baseline: `a40311432736c0a96de6e05bdb4faed7dab91376`, recorded by [`final-freeze-t4.1.json`](android-vulnerability-agent/evaluation/evidence/stage_t/final-freeze-t4.1.json).
- Amendment-002 execution commit: `25a3f790ff2c85c248c4f62832d39a231978753c`.
- Report-bearing editorial commit and documentation-pass base: `92667e842f0eee70068cfceee6559c6d2596e99d`.
- Final result and freeze identities: the [Amendment-002 freeze](android-vulnerability-agent/evaluation/evidence/stage_u/amendment-002/final-freeze-v5.json), [execution binding](android-vulnerability-agent/evaluation/evidence/stage_u/amendment-002/execution-binding.json) and [artifact manifest](android-vulnerability-agent/evaluation/evidence/stage_u/amendment-002/final-report/artifact-manifest.json). These records preserve the applicable hashes and must not be replaced by the current HEAD identity.

## Tracked code and artifact material

A Git archive of the selected submission commit contains only files tracked by that commit. The tracked repository contains:

- source code for the APK-grounded Android vulnerability-analysis pipeline;
- typed architecture contracts and the restricted operation/evaluator implementation;
- automated regression and contract tests;
- source for controlled synthetic Android applications;
- benchmark metadata, pinned corpus definitions and acquisition records;
- evaluation runners, versioned provider/configuration records and frozen plans;
- retained machine-readable results, finding/run tables and final-report summaries;
- design, implementation and evaluation documentation; and
- Python dependencies pinned in [`android-vulnerability-agent/requirements.lock`](android-vulnerability-agent/requirements.lock).

No APK binary is tracked at the inspected HEAD. Publicly available third-party datasets and APKs are not unnecessarily redistributed. The repository instead preserves the applicable identities, versions, hashes, labels, manifests and acquisition information required to identify evaluated artifacts. Ghera provenance is recorded in the [frozen Ghera manifest](android-vulnerability-agent/evaluation/evidence/stage_t/ghera-manifest.json) and related [benchmark provenance](android-vulnerability-agent/benchmarks/stage_r/ghera/); F-Droid identities and acquisition provenance are recorded in the [frozen F-Droid manifest](android-vulnerability-agent/evaluation/evidence/stage_t/fdroid-manifest.json) and [Stage L corpus records](android-vulnerability-agent/benchmarks/stage_l/). The F-Droid sample has `UNKNOWN` security ground truth and `UNADJUDICATED` manual status; it is not a labelled vulnerability dataset.

## Raw execution evidence outside Git

`android-vulnerability-agent/.artifacts/` is present locally and excluded by `android-vulnerability-agent/.gitignore`. At inspection it occupied approximately 15 GB on disk across final and historical artifacts. The final Amendment-002 subtree, `.artifacts/stage_u/amendment_002/`, occupied approximately 4.1 GB on disk; its preserved final audit records 283,248 files and 3,552,862,876 bytes of file content (approximately 3.55 GB).

This ignored tree contains the raw attempt material referenced by Appendix H. It is **not** included in the public GitHub repository or in a plain `git archive`. The tracked repository contains the final-report summaries and retained repository evidence under [`evaluation/evidence/stage_u/amendment-002/`](android-vulnerability-agent/evaluation/evidence/stage_u/amendment-002/), but those files do not make Appendix H's `.artifacts/...` trace paths retrievable from GitHub alone.

The delivery decision is therefore explicit: determine whether the UCL submission should include the final Amendment-002 raw subtree as a separate archive. Do not silently add the complete 15 GB local `.artifacts/` tree to the primary code archive.

## Reproduction boundary

Detailed setup and run instructions are in [`android-vulnerability-agent/README.md`](android-vulnerability-agent/README.md) and the linked design documents. API credentials are intentionally excluded. Frozen saved observations can be replayed or audited using the matching evaluator version, but future LLM responses, device timing and emulator state are not guaranteed to be bit-for-bit identical. Replay cannot reproduce a security effect that was not observed in the original trace.
