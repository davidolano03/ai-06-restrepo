# Partial formalization: validated algebra checkpoint

Source: NBER Working Paper 22252, revised June 2017, 87 PDF pages. Exact source pins are in audit/source_provenance.json. This is not an accepted formalization or a final validation report.

## Proved scope

MainTheorems.lean and transparent support Specs in PaperInterface.lean contain three conditional algebraic results: solve a three-equation linear response system; construct its solution; and construct positive productivity with a negative wage response. ProofInterface.lean pairs each Spec with an exact-type theorem endpoint.

The response coordinates w,r,ell denote candidate log wage, rental and employment changes; g denotes fixed-factor productivity; z denotes the task-demand shock. The equations are explicit proof-level premises, not assumptions of the primitive paper model. No Lean derivative is claimed. The wage decomposition is w = g + (1-s) z/(sigma+epsilon); for automation z=-Lambda, displacement can dominate positive productivity.

## Open source obligations

All original named statements remain open: Propositions 1–9, Corollaries 1–2, Lemmas A1–A3, Propositions B1–B4 and Lemma B1 (19 results). None receives complete source theorem credit. No scope exclusion is claimed. Governing assumptions and definitions still require exact source-facing semantic routes. The independent source-only reviewer was interrupted before saving a completed inventory; no independent inventory acceptance is claimed.

Remaining work: full nonlinear task production/equilibrium semantics; existence and uniqueness; justification of differentiability and the linearized system; integral definitions and positivity of Lambda; productivity formula and capital-stock wage threshold; dynamic accumulation/BGP stability/endogenous innovation; heterogeneous skill inequality; creative destruction; welfare and all appendix results. The three support Specs are not equivalent replacements for Props2–3.

## Workflow and reproduction

Entered via scripts/paper_contribution.py new. The fresh clone revision is 2db7d108cd3a2cb10148974bb2a77856e7d87428. Lean v4.30.0-rc2 and lake-manifest.json pin the foundations. Only .lake/packages dependencies were reused through a local junction; no other run's paper results were copied.

On this Windows host use the bundled Python runtime, add the toolchain bin to PATH, and set PYTHONPATH to this repository plus the external python-compat directory. That directory supplies conservative msvcrt file-lock compatibility and an os.fchmod adapter; upstream checks were not edited. Process-scoped safe.directory entries are needed for reused package paths. See audit/environment.ps1 and audit/run_commands.md.

Intake freeze, source-map preparation, all source-to-Lean semantic judgments, native graph audit, final adversarial audit and accepted closure receipt are NOT completed. No acceptance is inferred from compilation. The first session was interrupted at the usage limit; after resumption the proof build and fast check completed with exit code 0. The remaining limitations are mathematical and semantic scope, not an unexecuted build. Future work should first finish source-only intake routes and full source Specs before graph-backed closeout.
