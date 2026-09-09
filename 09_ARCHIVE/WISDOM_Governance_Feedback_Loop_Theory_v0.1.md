# W.I.S.D.O.M. — Governance Feedback Loop

Research synthesis and pilot design · 2026-09-08 · v0.1

**Status: Theory.** Proposed designs below are noncanonical. No probationary policy has been activated. This is a targeted research synthesis and implementation path, not experimental evidence that the approach improves learning. The supplied mission is the source of the W.I.S.D.O.M. theory; external sources support individual foundations, not the complete proposal.

The proposed benefit: teach beginners to turn personal goals into bounded AI work, diagnose outcomes, and improve the correct part of the system. Start with their useful project; introduce governance in proportion to its actual decisions and risks.

## Research foundation

| Established work | What transfers | Limit of the analogy |
| --- | --- | --- |
| [NIST AI RMF Core](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/) | Governance spans the AI lifecycle; measurement and management inform continuing review. | This voluntary framework does not establish that governance is the dominant cause of poor agent performance or prescribe this beginner curriculum. |
| [NASA systems design](https://www.nasa.gov/reference/4-0-system-design-processes/) | Trace stakeholder needs into requirements and design; revisit upstream choices when downstream evidence challenges them. | Aerospace process volume is not an appropriate default for a hobby project. |
| [Google SRE postmortems](https://sre.google/sre-book/postmortem-culture/) | Preserve incident evidence, investigate contributing conditions, and assign follow-up actions without blame. | A retrospective is not automatically a causal experiment; successful runs also need examination. |
| [MIT STPA resources](https://psas.scripts.mit.edu/home/books-and-handbooks/) | Examine control relationships and potential loss scenarios proactively. | Feedback does not remove the need for initial hazard analysis. A conceptual feedback diagram proves neither mathematical stability nor completeness. |
| [Open Policy Agent decision logs](https://www.openpolicyagent.org/docs/management-decision-logs) | Associate decisions with policy revisions, inputs, results, and identities; mask sensitive fields. | A policy decision log does not prove the action was executed or the enforcement boundary could not be bypassed. |
| [Carnegie Mellon course alignment](https://www.cmu.edu/teaching/assessment/basics/alignment.html) | Align learning objectives, practice, and assessment. | Alignment supports course design; this source does not validate W.I.S.D.O.M.'s proposed teaching sequence. |

**Synthesis:** the components have established precedents. The distinctive hypothesis to test is whether combining them into a small, recurring learner workflow improves independent diagnosis and useful project outcomes at acceptable effort.

## Corrections to the theory

1. **Governance is a coordinating structure, not an explanation for everything.** Missing capability, faulty tools, poor task design, and environmental changes can persist under excellent policy. Diagnose interacting causes; allow “unknown.”
2. **The chain is a traceability model, not a compulsory sequence.** Architecture can expose impossible preferences and force reconsideration. Existing tools and external constraints also shape what can be authorized.
3. **Separate two loops.** Execution operates within current authority. Improvement proposes and tests changes to that authority. Evidence never authorizes its own amendment.
4. **Observability is partial.** Logs record selected events, not a model's internal causes. Agent explanations and inferred human preferences remain hypotheses until checked against behavior or confirmed by the person.
5. **One severe incident can justify immediate containment.** Do not require recurrence before responding. Distinguish a bounded protective response from a permanent general rule.
6. **Measure excessive and insufficient restraint together.** Fewer questions can mean better delegation or silent unauthorized action. Faster completion can hide rework or lower quality.
7. **“Reversible” needs an operational test.** A recoverable file edit and a local command with external effects are different. Define resource scope, permitted effects, and a demonstrated recovery path.

## Minimum formal model and terminology

Use three learner-facing artifacts: **work agreement, run record, change proposal**. Their purpose is to reduce repeated ambiguity, not demand elaborate constitutional writing.

| Term | Working meaning |
| --- | --- |
| Intent | Desired outcome and tradeoffs confirmed by the person. |
| Policy | Durable rule identifying authority, scope, constraints, and amendment ownership. |
| Instruction | Guidance for carrying out a task; it does not itself supply missing permission. |
| Control | Mechanism that checks or restricts actual behavior. |
| Evidence | Recorded observation with provenance and stated limits. |
| Diagnosis | Testable explanation of contributing conditions. |
| Amendment | Proposed policy change, effective only through the applicable adoption process. |

Working relationship: outcome depends on the task, model, supplied context, effective policy, enforced controls, environment, and randomness. Recording their identities supports comparison; it does not isolate their causal contributions.

Execution: agreed intent → bounded task → permitted action → checked result.

Improvement: evidence → competing diagnoses → proposed change → bounded test → authorized adoption, rejection, or further investigation.

Keep project status separate from empirical confidence. Use W.I.S.D.O.M.'s Theory, Provisional, Probational, and Canon labels through its governing adoption process; repetitions, files, and successful tests do not silently promote anything. A proposed Probational trial should identify scope, owner, review date, stop conditions, and rollback.

## Downward propagation and drift

For beginners, combine operator/project rules into one agreement, put task-specific details in its task section, and demonstrate one real action boundary. Add workflow, agent, and delegation layers only when their separate responsibilities become useful.

Proposed advanced mechanism: preserve authoritative policy centrally; produce a versioned task packet containing relevant obligations, actual grants, prohibitions, escalation routes, and source references. Downstream grants must stay within the issuer's authority. A reference or hash identifies text; neither ensures retrieval, understanding, nor enforcement.

Resolve machine-readable scope and permissions deterministically where possible. Have the responsible person review ambiguous prose translations. Put enforcement at the action boundary. Revalidate current authority before consequential effects, including actions queued before a revocation. Record both the task's original configuration and any later authorization decision.

Detect three different drifts: changed policy/configuration, changed behavior under apparently identical configuration, and changed user expectations. Use version checks for the first, repeated reference tasks for the second, and direct preference review for the third. None substitutes for the others.

## Minimum useful evidence

Record one task/run entry plus separate records for retries, interventions, and consequential actions when needed. Store configuration details once and reference them.

| Record | Minimum proposed fields |
| --- | --- |
| Configuration | ID; exact policy/instruction snapshots or resolvable versions; reported model/provider identity; tool/environment versions; relevant settings; unknowns. |
| Run | Task ID; run ID; configuration ID; input reference; time; expected result; observed outcome; independent check; evidence reference. |
| Event | Run ID; event/attempt ID; actor; action and target; authorization decision/reference where applicable; result; intervention and reason, if any. |
| Change | Observation references; competing explanations; proposed layer/change; test and thresholds; approval; result; adoption decision. |

Use honest “unknown” values when a platform hides model revisions or instructions. Preserve agent reports separately from tool receipts and human observations. Never treat a self-reported success as sufficient proof. Logs need enough coverage to reveal missing runs, not just selected successes.

Start with four measurements: verified task success, unnecessary interventions, missed required escalations, and combined work/rework/recordkeeping time. Define denominators: unnecessary escalations per eligible autonomous decision, missed escalations per decision requiring escalation, and successes per attempted task. Report counts alongside rates and severity. Review sampled autonomous actions to find missed escalations; intervention logs alone cannot reveal them.

Add tokens, latency, retries, disagreements, or tool errors only when they answer a specific diagnosis. Keep private content out of teaching records unless necessary and appropriately permitted. Use redacted or synthetic examples where possible.

## Ready-to-use pilot materials

**Work agreement**

```text
My goal and observable success:
Allowed resources and actions:
Actions requiring my approval:
Actions prohibited:
Stop/escalate when:
Recovery method:
Agreement version and person authorized to amend it:
```

**Run record**

```text
Task/run and configuration:
Expected result / actual result:
Evidence and who checked it:
Intervention or missed escalation, with reason:
Work + rework + recording time:
Unknowns:
```

**Change proposal**

```text
Observation and supporting run IDs:
Possible causes, including a non-governance explanation:
Smallest proposed change and affected layer:
Expected improvement and possible new failure:
Comparison tasks, measures, and thresholds chosen in advance:
Stop condition / rollback / review date:
Result and limitations:
Authorized decision: adopt / reject / continue investigating:
```

Elicit personal policy through concrete contrasts: may the assistant rename a disposable copy, overwrite an original, or send the result? Ask what difference changes the person's answer. Present inferred preferences for confirmation. Contextual or inconsistent preferences are useful findings, not learner defects.

## Pilot experiment

Start with one useful learner project, such as organizing disposable sample files, then assess transfer to a different task such as preparing a sourced research note. Give both conditions the same basic protections. Compare ordinary task guidance with the three-artifact feedback method.

First test usability: can a beginner complete the records and explain the distinctions without constant help? Then use matched task sets, counterbalanced order, repeated runs, and multiple beginners for comparative testing. Keep model/tool configuration stable where possible. Treat the founder's experience as a case study, not population evidence.

Predefine an improvement target for unnecessary interventions and a maximum acceptable recording burden. Keep output quality and missed-required-escalation measures as guardrails. Select thresholds after a usability baseline but before comparative results are examined. No universal numerical threshold is established by this research.

Review outcomes against a fixed rubric, preferably with configuration labels hidden from the reviewer. Keep failed and abandoned attempts. Retain unseen transfer tasks. Before/after improvement alone is confounded by practice and task difficulty. A small pilot can support feasibility; zero observed serious errors does not establish safety.

Test alternatives explicitly: compare a policy clarification with a tool repair or better task input when each could explain the failure. Change one factor at a time where practical. If multiple factors change, limit the attribution claim.

Reject or simplify the method if it adds substantial overhead without better independent diagnosis or verified outcomes. Also reject the strong claim that governance was the bottleneck when a capability/tool change explains the improvement.

## Path into the finished class

| Placement | Lesson and exercise | Evidence of learning |
| --- | --- | --- |
| First useful task | Translate a personal goal into the work agreement; distinguish permission from instruction. | Student predicts which actions may proceed and explains why. |
| Early project | Compare expected and actual results; capture one correction in a run record. | Student separates observation from explanation. |
| Intermediate | Diagnose paired failures caused by policy, context, and tools. | Student tests competing causes rather than rewriting every prompt. |
| Intermediate project | Propose one change and compare outcomes. | Student reports benefits, regressions, effort, and uncertainty. |
| Optional advanced track | Delegation, versioned policy packets, deterministic controls, revocation, and action receipts. | Student demonstrates permitted action, denied action, and stale-authority handling. |
| Capstone | Run a personally useful project, retain evidence, test an improvement, then attempt an unfamiliar transfer task. | Student can improve or responsibly reject a change without instructor diagnosis. |

Build each lesson from a learner decision, a worked example, guided practice, independent practice, and feedback. This implements objective/practice/assessment alignment while keeping the proposed governance sequence subject to testing. [Course alignment basis](https://www.cmu.edu/teaching/assessment/basics/alignment.html).

Proposed rubric: score each dimension 0–2 (absent, supported with help, independently demonstrated): clear intent/authority; trustworthy evidence; competing diagnoses; appropriate intervention layer; fair validation and uncertainty; justified adoption/rollback. Judge successful reasoning even when an experiment finds no improvement. Do not reward longer policies or fewer questions by themselves. Calibrate scoring before setting a passing total.

The class uses the same process: version lessons and rubrics, record specific misconceptions and instructor interventions, propose a revision, test on comparable tasks, and monitor transfer and learner burden. Keep learner mistakes usable for improvement without penalizing honest reporting. Curriculum improvement and changes to learner permissions remain separate decisions.

## Candidate policy wording for later sharpening

> Within an explicitly adopted pilot scope, W.I.S.D.O.M. will use proportionate work agreements, attributable execution evidence, and bounded improvement experiments. Reviews will examine contributing causes across human assumptions, tasks, models, tools, architecture, and policy. Proposed changes will identify expected benefit, possible harm, validation, amendment authority, and rollback. Evidence may support adoption but cannot grant it. Teaching will assess independent diagnosis and useful outcomes while measuring the burden of governance itself.

This wording is **Theory**, not an operative requirement. Next adoption target: a bounded Probational curriculum pilot after the user sharpens and explicitly adopts its terms. No source-project constitution is imported as student doctrine.

Delivered here: research crosswalk, corrected formal model, terminology, evidence design, three templates, pilot protocol, lesson placement, rubric, and curriculum feedback method. Still unperformed: learner trials, software instrumentation, course production, and policy adoption. Those are the proposed next stages, not claimed results.
