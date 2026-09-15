# Agentic Vulnerability Finder for Android Applications

**MSc Information Security Dissertation — COMP0064**<br>
**University College London**<br>
**Thomas Louis Sigone**<br>
**Supervisor: Arthur Gervais**<br>
**2026**

## Overview

Android static and decompiled evidence can identify a suspicious component or code path, but a plausible vulnerability hypothesis is not evidence that an attacker produced the claimed security effect. This dissertation investigates whether open-ended, APK-grounded vulnerability discovery can be combined with restricted, auditable, evidence-backed validation.

The system creates a bounded evidence workspace from an APK. An LLM agent explores it and proposes speculative findings with evidence references. Deterministic host code resolves those references, normalises each finding and derives its available validation capabilities. Proposed validation actions pass through host policy and restricted typed operations, and the resulting observations are preserved as typed evidence.

A host-controlled evaluator—not a provider success claim—assigns the final lifecycle status from the recorded evidence and implemented predicates. The design therefore separates what the agent proposed, what it was allowed to test, what it observed and what the evidence permitted the evaluator to conclude. Host control makes this decision path inspectable; it does not make every predicate an inherently sound or effect-specific security oracle.

## Architecture

```text
APK
 ↓
Bounded APK Evidence Workspace
 ↓
Open-Ended Discovery
 ↓
Normalisation & Capability Routing
 ↓
Finding-Driven Restricted Validation
 ↓
Typed Observations
 ↓
Host-Controlled Lifecycle Evaluation
 ↓
Finding Status & Evidence
```

### Stage P: open-ended discovery

“Open-ended” describes hypothesis formation: output is not constrained to a predefined vulnerability category or benchmark target. The model can inspect only bounded APK-derived evidence through exactly the registered read-only workspace operations. Findings remain hypotheses with host-resolved evidence references. A source citation establishes where the model saw evidence; it does not establish that the model’s security conclusion is correct. Discovery is bounded, not unrestricted.

### Stage Q: restricted validation

Stage Q investigates one normalised finding at a time. Deterministic routing constructs a finding-specific capability view, from which the model may propose actions. Host policy, typed schemas, prerequisites, budgets and executor checks decide whether an action can run. Recorded observations remain separate from the model’s assessment, and the host-controlled evaluator owns the lifecycle decision. Execution success and vulnerability status are separate: a tool may run successfully without demonstrating the claimed effect.

| Lifecycle status | Meaning |
| --- | --- |
| `VALIDATED` | The frozen host evaluator accepted adequate, unconflicted supporting evidence under its implemented decision rules. |
| `NOT_VALIDATED` | An adequate route produced decisive contradictory evidence under the applicable rules. |
| `INCONCLUSIVE` | The available or attempted investigation did not produce sufficient admissible evidence for a positive or negative decision, or an unresolved operational failure prevented one. |
| `UNSUPPORTED` | The required validation route was unavailable under the implemented capability model. |

`NOT_ENTERED` is an evaluation-side marker for discovery-only findings, not a fifth Stage Q lifecycle outcome. A `VALIDATED` result is a frozen evaluator decision on recorded evidence, not independent human reproduction of an exploit. `INCONCLUSIVE` and `UNSUPPORTED` do not mean that an application is safe, and failed execution alone does not imply `NOT_VALIDATED`.

## Repository guide

- [`apk_workspace/`](android-vulnerability-agent/apk_workspace/) builds the deterministic APK/Jadx evidence workspace.
- [`discovery/`](android-vulnerability-agent/discovery/) implements Stage P; [`validation/`](android-vulnerability-agent/validation/) implements finding-driven Stage Q and lifecycle evaluation.
- [`validator/`](android-vulnerability-agent/validator/) contains the restricted operation registry and execution capabilities; [`pipeline/`](android-vulnerability-agent/pipeline/) connects the stages.
- [`architecture/`](android-vulnerability-agent/architecture/) defines typed contracts and capability mappings.
- [`benchmarks/`](android-vulnerability-agent/benchmarks/) and [`evaluation/`](android-vulnerability-agent/evaluation/) preserve corpus definitions, runners, freezes and retained results.
- [`config/`](android-vulnerability-agent/config/) records provider/configuration data; [`apps/`](android-vulnerability-agent/apps/) contains controlled synthetic Android applications.
- [`docs/`](android-vulnerability-agent/docs/) and [`tests/`](android-vulnerability-agent/tests/) contain design documentation and regression/contract tests.

The [subproject README](android-vulnerability-agent/README.md) contains the detailed implementation history, setup guidance and stage-level commands.

## Requirements and quick start

The project uses Python 3.12 with dependencies pinned in [`requirements.lock`](android-vulnerability-agent/requirements.lock). Workspace construction requires Jadx. Dynamic validation requires the Android SDK, ADB and a controlled emulator; the final evaluation used Android API 35 on `arm64-v8a`, but not every offline or development path requires that exact device configuration. Credentials are required only for live hosted-provider paths. Scripted, replay and offline paths do not universally require provider credentials, and credentials are intentionally excluded from the repository.

```bash
git clone https://github.com/thomassigone/COMP0064_Dissertation.git
cd COMP0064_Dissertation/android-vulnerability-agent

python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.lock
python -m pip install -r requirements-test.lock
python -m pip check
```

The canonical provider-, device- and credential-free clean-clone test command is:

```bash
python -m pytest -q
```

Pytest executes the repository's `unittest.TestCase` classes and all 42 pytest-style functions in one run. Tests marked `external_evidence` require downloaded APK datasets or private `.artifacts` records and must skip when their prerequisites are absent. Run that class separately, after acquiring and hash-verifying the APKs identified by the frozen Ghera and F-Droid manifests, with `python -m pytest -q -m external_evidence`. The default clean-clone suite does not require the private raw evidence tree.

From the repository root, `python3 scripts/validate_repository.py` checks tracked JSON and internal Markdown links. It preserves an exact allowlist for seven immutable post-freeze console captures that contain literal multiline output, and reports links to omitted APKs or private `.artifacts` separately from genuine broken repository links.

See the detailed [subproject README](android-vulnerability-agent/README.md) and design documents below for pipeline and evaluation commands.

## Final evaluation and reproducibility

The authoritative experiment is the T.4.1 / Stage U Amendment-002 evaluation. It covers E1 documented Ghera targets, E2 target-relative controls, E3 unadjudicated F-Droid applications, E4 mode comparison, E5 provider portability and E6 repeatability. Earlier Stage T runs, the original Stage U E1, Amendment-001, pilots and development smokes are historical or diagnostic and are not mixed into the final denominators.

The final case-level progression was **60 documented targets → 28 matched by discovery → 2 assigned `VALIDATED` by the frozen evaluator**; conditional validation among discovered target cases was 2/28. The two outcomes are evaluator decisions, not independently reproduced exploits, and the preserved traces do not directly establish every claimed effect-level observation. `INCONCLUSIVE` and `UNSUPPORTED` outcomes are not negative vulnerability findings.

The repository preserves pinned benchmark manifests, APK hashes and provenance where applicable, versioned configuration, frozen plans, scoring/evaluator records, tests, finding/run tables and machine-readable final reports. Saved observations support audit or replay with the matching evaluator version. They do not guarantee identical future model responses, identical emulator timing or state, or reproduction of a security effect absent from the original trace.

## Public evidence release

The [minimal public dissertation evidence v1.0.0](https://github.com/thomassigone/COMP0064_Dissertation/releases/tag/evidence-v1.0.0) contains six representative frozen trace closures and a deterministic 48-attempt E4 audit extract. Its ZIP SHA-256 is `1e17fa3f79d2ddb2d77d1fac281483693328289d80622abcbaf4903248fdde3a`; `RUN_LOCATORS.csv` inside the archive maps the dissertation examples to stable bundle paths. This compact release is separate from the private approximately 3.55-GB Amendment-002 raw archive.

## Dataset and artifact boundary

The frozen study uses 60 pinned lean Ghera vulnerable cases, 59 corresponding Ghera Secure APKs and three synthetic controls, plus 30 version-pinned F-Droid applications with `UNKNOWN` security ground truth and `UNADJUDICATED` manual status. Ghera Secure variants are controls for their documented removed target, not claims that each APK is globally vulnerability-free. F-Droid outputs are neither confirmed vulnerabilities nor prevalence estimates.

Third-party APKs need not be redistributed in the submitted Git archive. The repository retains applicable identities, versions, hashes, manifests, labels and acquisition provenance in the frozen [Ghera manifest](android-vulnerability-agent/evaluation/evidence/stage_t/ghera-manifest.json) and [F-Droid manifest](android-vulnerability-agent/evaluation/evidence/stage_t/fdroid-manifest.json). The complete raw attempt tree is stored locally beneath `android-vulnerability-agent/.artifacts/`, is excluded from Git, and therefore is not available from the public repository or a plain `git archive`. Tracked final summaries remain under the [Amendment-002 final report](android-vulnerability-agent/evaluation/evidence/stage_u/amendment-002/final-report/).

## Scope, ethics and limitations

The project targets Android application-layer weaknesses under an ordinary, unprivileged application-layer attacker model. Evaluation used a controlled emulator and synthetic or benchmark applications. Root/kernel/platform compromise, custom-ROM attacks, physical access and hardware side channels are outside scope. Do not use the tooling against third-party systems without authorisation.

Bounded decompilation and search can miss relevant evidence; discovery is stochastic; available capabilities limit what can be tested; and generic evaluator predicates do not provide an effect-specific oracle for every claim. Results are specific to the frozen corpus, device and provider configuration, while F-Droid security ground truth remains unadjudicated.

## Licensing and citation

Original project software is provided under the [MIT License](LICENSE). [Third-party notices](THIRD_PARTY_NOTICES.md) identify the separate terms covering Ghera, MotionLock, benchmark material, embedded source excerpts, dependencies and build tooling; third-party evidence is not blanket-relicensed. Repository citation metadata is provided in [CITATION.cff](CITATION.cff).

## Documentation

- [Final architecture and threat model](android-vulnerability-agent/docs/stage-m-final-architecture.md)
- [Stage P open-ended discovery](android-vulnerability-agent/docs/stage-p-hybrid-open-ended-discovery.md)
- [Stage Q finding-driven validation](android-vulnerability-agent/docs/stage-q-finding-driven-validation.md)
- [Stage S provider portability](android-vulnerability-agent/docs/stage-s-multi-provider-portability.md)
- [Stage U Amendment-002 final report and evidence](android-vulnerability-agent/evaluation/evidence/stage_u/amendment-002/final-report/)
- [Submission manifest](SUBMISSION_MANIFEST.md)

## Author

Thomas Louis Sigone<br>
MSc Information Security<br>
University College London
