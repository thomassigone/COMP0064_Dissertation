# Third-party notices

This repository combines original research software and documentation with benchmark metadata, retained evaluation records, third-party build tooling, and bounded excerpts derived from third-party Android applications. The root [MIT licence](LICENSE) applies only where Thomas Louis Sigone holds the relevant rights; it does not relicense third-party material.

## Author-owned material

Copyright (c) 2026 Thomas Louis Sigone.

Original project source code and repository documentation are made available under the root MIT licence unless a file or directory states more specific terms. The separately published minimal evidence bundle has its own notice: author-owned bundle metadata is CC BY 4.0, its E4 extraction script is MIT, and embedded third-party material retains its upstream terms.

## Ghera benchmark

The frozen study identifies Ghera at revision [`ea1dbe234e4d3433161a3b85e96648913a36e83c`](https://bitbucket.org/secure-it-i/android-app-vulnerability-benchmarks/src/ea1dbe234e4d3433161a3b85e96648913a36e83c/). Ghera is BSD 3-Clause licensed, Copyright (c) 2017 Kansas State University. Its [revision-specific licence](https://bitbucket.org/secure-it-i/android-app-vulnerability-benchmarks/src/ea1dbe234e4d3433161a3b85e96648913a36e83c/LICENSE) applies to Ghera source and manifest material, including bounded decompiled excerpts retained inside applicable evidence records.

Repository files under `android-vulnerability-agent/benchmarks/stage_r/ghera/` and `android-vulnerability-agent/evaluation/evidence/stage_t/` principally preserve derived benchmark metadata, provenance, hashes, mappings, and evaluation records. Their inclusion does not imply that Ghera or its APKs were authored by Thomas Louis Sigone. The public evidence release includes the BSD notice and maps its five Ghera trace excerpts explicitly.

## MotionLock and F-Droid material

The public evidence release contains bounded decompiled MotionLock 1.3 (22) source and manifest excerpts in its FDROID-20 trace. MotionLock revision [`68a746fb592d94401d5cffcf711680050357a4df`](https://gitlab.com/divested-mobile/motionlock/-/tree/68a746fb592d94401d5cffcf711680050357a4df) is AGPL-3.0-or-later licensed; the [revision-specific licence](https://gitlab.com/divested-mobile/motionlock/-/blob/68a746fb592d94401d5cffcf711680050357a4df/LICENSE) and detailed excerpt mapping are included in that release.

F-Droid and other third-party application records in this repository are limited to the retained identities, versions, hashes, acquisition metadata, manifest material, and evaluation observations needed for research audit. Each application remains subject to its own upstream terms. F-Droid security ground truth is `UNKNOWN` and manual status is `UNADJUDICATED`; inclusion is not a vulnerability adjudication or a transfer of ownership. No third-party APK is distributed in Git or in the minimal evidence release.

## Other third-party components

- Python packages named in `android-vulnerability-agent/requirements.lock` retain their respective upstream licences.
- Gradle wrapper components included with the controlled synthetic Android projects are Gradle project material distributed under the [Apache License 2.0](https://github.com/gradle/gradle/blob/master/LICENSE).
- Android SDK, ADB, Jadx, provider SDKs, Android platform material, and other external tools are not relicensed by this repository.
- Product names, application names, trademarks, and logos remain the property of their respective owners.

The [minimal public evidence release](https://github.com/thomassigone/COMP0064_Dissertation/releases/tag/evidence-v1.0.0) provides the complete third-party notice and licence copies for the embedded Ghera and MotionLock trace material it distributes.
