# S.W.A.R.M. Retrospective Harvest

**Status:** RAW RETROSPECTIVE HARVEST — NONCANONICAL
**Harvest date:** 2026-09-06
**Purpose:** collection for later research/adjudication; presence here is not adoption

## RX-20260906-0101 — Authority before workflow

- **Source project/thread:** S.W.A.R.M. — constitutional/governance development
- **Source date / period:** late Aug–Sep 2026
- **Provenance pointer:** S.W.A.R.M. Constitution/AFAD work; W.I.S.D.O.M. governance-research mandate
- **Observation:** Project work repeatedly separated who may decide from how work is performed. Operator remains root authority; proposals, authorizations, executions, and results are distinct.
- **Possible educational value:** Transferable lesson: workflow efficiency cannot repair an undefined or leaking authority model.
- **Tags:** `GOVERNANCE`, `AI_WORKING_METHOD`, `POSSIBLE_CONSTITUTIONAL_PRINCIPLE`
- **Known status:** Unadjudicated
- **Contradiction / counterevidence:** Very small tasks may not need explicit formal authority artifacts.
- **Later research question:** What is the minimum authority model a beginner project needs?
- **Confidence in reconstruction:** high
- **Duplicate / related IDs:** None

## RX-20260906-0102 — Canonical ROOT/branch/HEAD must be explicit

- **Source project/thread:** S.W.A.R.M. — repository convergence
- **Source date / period:** around 2026-08-27 to 2026-08-29
- **Provenance pointer:** Repository convergence analysis; read-only audit establishing `/home/chromikey/AI`, branch `ground-zero-preservation-v1`, HEAD `b5720d7` at that time
- **Observation:** A beginner-relevant confusion arose around which repository root, branch, and state were authoritative. Branch recency was not itself authority.
- **Possible educational value:** Potential foundational Git lesson: know the authoritative root, branch, HEAD, and evidence-only areas before asking AI to change a project.
- **Tags:** `ENGINEERING_PROCEDURE`, `TOOLS_WORKFLOW`, `LEARNER_EVENT`, `FAILURE_RECOVERY`
- **Known status:** Unadjudicated
- **Contradiction / counterevidence:** Teaching full Git topology too early could overwhelm a learner whose project has only one branch.
- **Later research question:** What minimum Git state vocabulary prevents the most common AI-assisted repository mistakes?
- **Confidence in reconstruction:** high
- **Duplicate / related IDs:** None

## RX-20260906-0103 — Repository sprawl can pass validation while being operationally wrong

- **Source project/thread:** S.W.A.R.M. — convergence audit
- **Source date / period:** 2026-08-27 to 2026-08-31
- **Provenance pointer:** Whole-project convergence audit: 23 local branches, 4 tags, 22 worktrees, 8 dirty worktrees; later report noted missing registered paths despite validation pass
- **Observation:** The project accumulated many branches/worktrees, with dirty/unregistered state and ambiguity about canonical work, while some validation still passed.
- **Possible educational value:** Strong negative-evidence case: a green validation result can miss the operational truth the human actually needs.
- **Tags:** `NEGATIVE_EVIDENCE`, `ENGINEERING_PROCEDURE`, `TOOLS_WORKFLOW`, `GOVERNANCE`
- **Known status:** Unadjudicated
- **Contradiction / counterevidence:** None recorded in this pass.
- **Later research question:** Which repository invariants should be verified causally rather than by presence/checklist tests?
- **Confidence in reconstruction:** high
- **Duplicate / related IDs:** None

## RX-20260906-0104 — Decision records can lag implementation state

- **Source project/thread:** S.W.A.R.M. — project-records validation
- **Source date / period:** 2026-08-27 to 2026-08-31
- **Provenance pointer:** Whole-project convergence audit: last Operator decision record lagged multiple substantive commits while `PROJECT_RECORDS_VALIDATION` still passed
- **Observation:** Durable governance/decision records fell behind repository reality even though the validation mechanism reported success.
- **Possible educational value:** Potential lesson in stale metadata, false assurance, and the need to validate relationships rather than only files.
- **Tags:** `NEGATIVE_EVIDENCE`, `GOVERNANCE`, `ENGINEERING_PROCEDURE`
- **Known status:** Unadjudicated
- **Contradiction / counterevidence:** None recorded in this pass.
- **Later research question:** How can project records prove they refer to current state rather than merely exist?
- **Confidence in reconstruction:** high
- **Duplicate / related IDs:** None

## RX-20260906-0105 — Free availability increases utilization, not authority

- **Source project/thread:** S.W.A.R.M. — Free Compute / economic governance
- **Source date / period:** 2026-09-03 to 2026-09-04
- **Provenance pointer:** Free-compute policy and HARD_ZERO closeout; canonical-local work around commits `4b7b8705`, `87b02af6` per project record
- **Observation:** Free routes were made desirable to use but never allowed to create spending authority. Unknown billing or quota state fails closed; no silent paid fallback.
- **Possible educational value:** Excellent causal example for separating resource desirability from permission.
- **Tags:** `GOVERNANCE`, `AI_WORKING_METHOD`, `TOOLS_WORKFLOW`, `POSSIBLE_CONSTITUTIONAL_PRINCIPLE`
- **Known status:** Unadjudicated
- **Contradiction / counterevidence:** A classroom implementation could be too complex if learners do not yet use external providers.
- **Later research question:** At what point should economic authority become an explicit beginner lesson?
- **Confidence in reconstruction:** high
- **Duplicate / related IDs:** None

## RX-20260906-0106 — HARD_ZERO setting does not mint authority

- **Source project/thread:** S.W.A.R.M. — economic policy
- **Source date / period:** 2026-09-04
- **Provenance pointer:** Ratified HARD_ZERO clause in project history
- **Observation:** HARD_ZERO became Operator-selectable; ON/OFF controls posture but neither state independently creates paid authority.
- **Possible educational value:** Potential lesson that configuration flags constrain behavior but do not replace authority or policy.
- **Tags:** `GOVERNANCE`, `ENGINEERING_PROCEDURE`, `AI_WORKING_METHOD`
- **Known status:** Unadjudicated
- **Contradiction / counterevidence:** Could be too project-specific unless translated to a general 'configuration is not authorization' principle.
- **Later research question:** Which common beginner settings are mistakenly treated as permission?
- **Confidence in reconstruction:** high
- **Duplicate / related IDs:** None

## RX-20260906-0107 — Request identity and attempt identity differ

- **Source project/thread:** S.W.A.R.M. — Telemetry V1
- **Source date / period:** 2026-09-04
- **Provenance pointer:** Telemetry V1 frozen design
- **Observation:** Telemetry explicitly separated the user's logical request from individual execution attempts/retries.
- **Possible educational value:** Potential foundational observability lesson for understanding retries, failures, provider switching, and what actually happened.
- **Tags:** `ENGINEERING_PROCEDURE`, `TOOLS_WORKFLOW`, `AI_WORKING_METHOD`
- **Known status:** Unadjudicated
- **Contradiction / counterevidence:** Premature telemetry detail can distract from simpler single-call projects.
- **Later research question:** What is the simplest experiment that makes request-vs-attempt identity visibly useful?
- **Confidence in reconstruction:** high
- **Duplicate / related IDs:** None

## RX-20260906-0108 — Canonical semantics should not be invented to satisfy telemetry

- **Source project/thread:** S.W.A.R.M. — Dev Compute / Agent Foundation sequencing
- **Source date / period:** 2026-09-04 to 2026-09-05
- **Provenance pointer:** Dev Compute telemetry closeout and canonical inspection
- **Observation:** Development Compute was explicitly prevented from defining canonical Agent admission/attempt semantics merely because telemetry wanted them; authority-bearing semantics were deferred until Agent Foundation stabilized.
- **Possible educational value:** Potential architecture lesson: downstream instrumentation must not accidentally define upstream domain truth.
- **Tags:** `ENGINEERING_PROCEDURE`, `GOVERNANCE`, `AI_WORKING_METHOD`
- **Known status:** Unadjudicated
- **Contradiction / counterevidence:** None recorded in this pass.
- **Later research question:** How can learners recognize when a convenience layer is starting to own semantics it should only observe?
- **Confidence in reconstruction:** high
- **Duplicate / related IDs:** None

## RX-20260906-0109 — Provider-reported metadata cannot mint economic truth

- **Source project/thread:** S.W.A.R.M. — NIM Milestone A correction
- **Source date / period:** 2026-08-30 to 2026-08-31
- **Provenance pointer:** NIM Milestone A correction bundle
- **Observation:** A correction addressed provider-reported OpenRouter pricing incorrectly creating `FREE_VERIFIED`, alongside poisoned credential replacement and non-independent provider transitions.
- **Possible educational value:** Strong example of untrusted/external metadata being evidence rather than authority.
- **Tags:** `GOVERNANCE`, `NEGATIVE_EVIDENCE`, `FAILURE_RECOVERY`, `AI_WORKING_METHOD`
- **Known status:** Unadjudicated
- **Contradiction / counterevidence:** None recorded in this pass.
- **Later research question:** What other external metadata fields are commonly mistaken for authoritative policy state?
- **Confidence in reconstruction:** high
- **Duplicate / related IDs:** None

## RX-20260906-0110 — Passing suites can miss cross-path causal defects

- **Source project/thread:** S.W.A.R.M. — engineering-tool gap retrospective
- **Source date / period:** 2026-08-31
- **Provenance pointer:** Historical engineering tool-gap retrospective
- **Observation:** Large passing test suites still missed authority-bypass, second-control-plane, and TOCTOU defects across multiple execution paths.
- **Possible educational value:** Potential lesson that test count is not equivalent to coverage of causal behavior; motivates mutation/property/fault testing when appropriate.
- **Tags:** `NEGATIVE_EVIDENCE`, `ENGINEERING_PROCEDURE`, `RESEARCH_NEEDED`
- **Known status:** Unadjudicated
- **Contradiction / counterevidence:** None recorded in this pass.
- **Later research question:** Which lightweight falsification techniques give beginners the best intuition for tests that can pass while behavior is still wrong?
- **Confidence in reconstruction:** high
- **Duplicate / related IDs:** None

## RX-20260906-0111 — Exact model/workload identity matters

- **Source project/thread:** S.W.A.R.M. — harness experiments
- **Source date / period:** 2026-09-06
- **Provenance pointer:** Harness research review and Sonnet next-pass instructions
- **Observation:** A throttled Kimi candidate that was skipped for Nemotron Super could not legitimately count as a Kimi trial; model/fixture identity and replacements had to remain explicit.
- **Possible educational value:** Potential experiment-design lesson: preserve what actually ran, not what was intended to run.
- **Tags:** `NEGATIVE_EVIDENCE`, `POSSIBLE_EXPERIMENT`, `AI_WORKING_METHOD`, `ENGINEERING_PROCEDURE`
- **Known status:** Unadjudicated
- **Contradiction / counterevidence:** None recorded in this pass.
- **Later research question:** How should classroom experiments record intended versus actual execution?
- **Confidence in reconstruction:** high
- **Duplicate / related IDs:** None

## RX-20260906-0112 — One observed skip does not prove a system-level benefit

- **Source project/thread:** S.W.A.R.M. — harness review
- **Source date / period:** 2026-09-06
- **Provenance pointer:** Harness research return review
- **Observation:** One health-based skip did not prove reduced branching or cost, and short six-job experiments without timeout/retry/cancellation could not support endurance or threshold claims.
- **Possible educational value:** Teachable example of claim calibration and resisting overgeneralization from thin evidence.
- **Tags:** `NEGATIVE_EVIDENCE`, `POSSIBLE_EXPERIMENT`, `PEDAGOGY`, `AI_WORKING_METHOD`
- **Known status:** Unadjudicated
- **Contradiction / counterevidence:** None recorded in this pass.
- **Later research question:** What minimum evidence supports moving from 'observed once' to a general claim?
- **Confidence in reconstruction:** high
- **Duplicate / related IDs:** None

## RX-20260906-0113 — Preserve invalid attempts and raw evidence

- **Source project/thread:** S.W.A.R.M. — experiment harness
- **Source date / period:** 2026-09-06
- **Provenance pointer:** Sonnet next-harness experiment pass
- **Observation:** The experiment protocol explicitly retained failed calls, retries, replacements, recovery/isolation evidence, raw ledgers, hashes, and distinct written/tested/reviewed/committed/executed/accepted states.
- **Possible educational value:** Potential general method for making AI-assisted experiments auditable and for teaching that failed attempts are data, not trash.
- **Tags:** `ENGINEERING_PROCEDURE`, `AI_WORKING_METHOD`, `POSSIBLE_EXPERIMENT`
- **Known status:** Unadjudicated
- **Contradiction / counterevidence:** None recorded in this pass.
- **Later research question:** Which evidence fields are essential for beginner experiments and which are advanced overhead?
- **Confidence in reconstruction:** high
- **Duplicate / related IDs:** None

## RX-20260906-0114 — Retire live mechanisms without erasing historical evidence

- **Source project/thread:** S.W.A.R.M. — Forge V3 retirement
- **Source date / period:** 2026-09-05
- **Provenance pointer:** Forge V3 audit and bounded retirement decision; local commit `e90adcb91afae5aae1a02a98d31b9dec206f2598` reported in project history
- **Observation:** The retirement removed six audited live paths while preserving hundreds of historical references and avoiding history rewrite.
- **Possible educational value:** Potential lesson in separating current architecture from historical provenance: deprecate/retire without falsifying the record.
- **Tags:** `ENGINEERING_PROCEDURE`, `GOVERNANCE`, `FAILURE_RECOVERY`
- **Known status:** Unadjudicated
- **Contradiction / counterevidence:** None recorded in this pass.
- **Later research question:** How should beginners distinguish delete, retire, supersede, and archive?
- **Confidence in reconstruction:** high
- **Duplicate / related IDs:** None

## RX-20260906-0115 — Model escalation should be purpose-driven

- **Source project/thread:** S.W.A.R.M./W.I.S.D.O.M. — operator model usage
- **Source date / period:** Sep 2026
- **Provenance pointer:** Project history: light-model-first / reserve Fable/Astra for critical architecture; local qwen3.5:4b used only for minimal seam tests
- **Observation:** The Operator developed a practical escalation pattern: use light/free/local models where adequate, escalate stronger models for harder architecture/review.
- **Possible educational value:** Potential AI-working lesson: match model capability/cost to task rather than treating the strongest model as default.
- **Tags:** `AI_WORKING_METHOD`, `TOOLS_WORKFLOW`, `PRODUCT`
- **Known status:** Unadjudicated
- **Contradiction / counterevidence:** Model capabilities and pricing change; a static model ladder would age quickly.
- **Later research question:** Can the course teach capability-based escalation without tying it to specific vendors/models?
- **Confidence in reconstruction:** medium
- **Duplicate / related IDs:** None

## RX-20260906-0116 — Correction itself can create new defects

- **Source project/thread:** S.W.A.R.M./G.A.M.E. governance research
- **Source date / period:** Aug–Sep 2026
- **Provenance pointer:** Governance closeouts and branch-guard research mandate
- **Observation:** The projects explicitly tracked correction-induced failures: solving one defect could introduce another branch, authority leak, or procedural burden.
- **Possible educational value:** Potential general debugging/governance lesson: evaluate the side effects of a fix, not merely whether the original symptom disappeared.
- **Tags:** `NEGATIVE_EVIDENCE`, `FAILURE_RECOVERY`, `GOVERNANCE`, `ENGINEERING_PROCEDURE`
- **Known status:** Unadjudicated
- **Contradiction / counterevidence:** None recorded in this pass.
- **Later research question:** What simple post-fix check helps learners look for newly introduced failure modes?
- **Confidence in reconstruction:** high
- **Duplicate / related IDs:** None
