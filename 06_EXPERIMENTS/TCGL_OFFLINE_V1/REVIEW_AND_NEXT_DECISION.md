# Offline implementation review and next decision

2026-09-09 · T2P-OFFLINE-V1 · **Noncanonical; no live promotion performed.**

## Completed block

Boss authorized proceeding end to end after the consolidated Luna investigation, with applicable governance issues logged only as encountered. The earlier instruction “don't promote anything” remains a boundary. This block implemented and evaluated the offline recorder, structural validator, revision history, index, complete synthetic cases, learner exercise, assessment and instructor-feedback proposal. Research preservation is already authorized in WISDOM; repository placement is not policy adoption.

Luna medium produced the code and initial notes in one implementation assignment. The parent independently wrote the contract fixtures and tests, inspected the result, corrected the identified gaps and ran the combined evaluation. No additional model or external compute provider was needed. This observed outcome does not establish the cheapest sufficient model or a comparative advantage over another workflow.

## Executed evidence

- **18 tests passed**, including the structural matrix of **15 complete synthetic cases**. The captured run used Python **3.12.13**.
- Verified revision conflicts, competing appends, history preservation, unchanged read bytes, missing/corrupt store errors, stored column/payload consistency, scope/task boundaries, hostile evidence as literal data, and unrelated-store protection.
- The retrieval probe recorded two reports of E-1 and returned one source event, both report identities, and no unresolved link. It did not infer independent replication.
- Structurally complete but semantically weak and stale-grant cases remain valid records with semantic judgment **not evaluated** and authority **not checked**. Their acceptance is intentional; it demonstrates the boundary of this tool.
- [RESULTS.json](RESULTS.json) preserves the exact input SHA-256 hashes and test log. Local execution time is not human recording burden, comparative cost, curation accuracy or governance efficacy.

Initial tests exposed a timestamp-validation defect; additional failures about store existence cascaded from it. One harness error assumed the wrong output stream and was corrected as a test defect. Review identified and repaired revision-precondition, malformed-type, read-only, integrity and index-order gaps. The final captured run is of the corrected implementation, not the initial smoke version.

## Pertinent issue log

| Encountered issue | Evidence | Action / limit |
| --- | --- | --- |
| A complete card can look approved | Weak and stale-grant fixtures structurally pass | Outputs explicitly leave semantics and authority unchecked; no promotion/activation API. |
| Timestamp text was accepted without validation | First independent test run | UTC syntax now required; coincident valid timestamps remain allowed. |
| Caller expectations could be ignored for a new candidate | Parent code inspection and added regression | Nonzero expected revision on an absent candidate now fails before creating a store. |
| A mutable store can disagree with its serialized history | Parent inspection and corruption regression | Read/append validate column-payload agreement and chain integrity; this is not tamperproof against a store owner who rewrites all content consistently. |
| Evidence can contain apparent instructions | Hostile-source fixture roundtrip | Quoted content is stored literally; no evaluation, shell or external fetch mechanism. Downstream language-model ingestion remains outside this test. |
| A restrictive schema can become bureaucracy | Raw research required many mandatory fields | Eight author-facing sections group the required content; identifiers are generated. Real author burden remains unmeasured. |
| Reviewer assumptions can create false defects | Initial test required error JSON on stdout | Test corrected; stderr behavior documented. Keep test defects distinct from product defects. |

No wider project audit, private corpus ingestion, learner experiment, live authority check or policy amendment occurred.

## Trial status update — 2026-09-09

Boss explicitly approved the packet below. The [authorized task-local trial](../TCGL_TASK_TRIAL_2026-09-09/AUTHORIZATION_AND_START.md) completed one pass with [three Provisional selections](../TCGL_TASK_TRIAL_2026-09-09/CURATION_CARDS.md) and is now ended; see [closeout](../TCGL_TASK_TRIAL_2026-09-09/CLOSEOUT.md). No Canon adoption or renewal occurred. The following proposal text is preserved as the historical decision packet; its pending-approval wording describes the earlier state.

## Proposed next decision: a real, task-local trial

**Not approved or started.** This packet is prepared because moving from simulation to actual curation would cross Boss's explicit “don't promote anything” limit. The offline software checks alone do not authorize it.

Candidate **T2P-CARD-V1** is the investigated selection rule and compact card in the [consolidated review](../../02_RESEARCH/TCGL_LUNA_INVESTIGATION_REVIEW_2026-09-09.md). Its content is pinned in that review's commit `cb76dbc720187a78ff5166794ad84991e3b8cae7`; this trial packet supplies the proposed experimental terms. No maturity label is inferred from its implementation or location.

The requested decision would explicitly recognize the investigated mechanism as Provisional and authorize one task-local Probational trial. Within that trial, the agent could make actual Theory → Provisional curation decisions for eligible ideas. This is a specific exception to the earlier no-promotion restriction, not a general promotion grant.

| Term | Proposed limit |
| --- | --- |
| Task | One retrospective pass over this thread's already-saved WISDOM GAB/TCGL research. |
| Sources | Integrated GAB/TCGL report, raw Luna investigation, consolidated review and this offline result; only their noncanonical Theory-labelled hypotheses. Exclude user decisions, Canon and anything already carrying another maturity state. |
| Activation | Only after explicit Boss approval; record the approval reference, candidate version and actual start before making the first live curation entry. |
| Rule | Select only a task-relevant observation/problem/gap with an answerable inquiry, expected benefit and adverse consequence, honest evidence/uncertainty and an inquiry fitting the grant. Proof of remedy effectiveness is unnecessary. |
| Scope | At most five task-local curation records; no wider project applicability or delegation inferred. |
| Method | Short human-readable cards in a separate trial directory, preserving original sources. The simulation-only Python tool stays unchanged and is not repurposed for live authority. |
| Resource bound | One pass, at most 30 minutes of active work; the current assistant only, no additional agent/provider, new spending, credentials, private data or unrelated audit. Stop at the first reached limit. |
| Evidence | Original reference/version, task, reporter, inquiry, effects, evidence for/against/absence, uncertainty, applicable scope, disposition and reason. Record elapsed time, count and any actual correction or intervention. |
| Success | Every selected record traces to an eligible Theory and stays task-local; every record contains the agreed evidence; at least one actionable next inquiry is identified within the task. Review burden and usefulness remain observations, not validated efficacy claims. |
| Failure / stop | Stop live classification if eligibility, scope or authority cannot be established, if required provenance is lost, or if either resource limit is reached. Preserve completed records and report the specific issue; do not stall independent already-authorized work. |
| Expiry | Ends after the pass or either limit. No renewal or future-task default. Existing records remain historical evidence; expiry is not automatic demotion or deletion. |
| Recovery | Stop using the trial mechanism; preserve cards with trial-ended status separate from maturity. If a classification was wrong, recommend its correction to Boss rather than erase history or invent a demotion power. No runtime policy/tool effects need rollback. |
| Disposition | Return one concise report and a recommendation to retain, revise or stop. Boss decides any further trial, maturity change or Canon adoption. No downstream Probational activation of the curated ideas. |

Alternative: keep all dispositions simulated and continue only offline research. That provides more structural coverage but cannot establish how actual curation affects a real task. The recommendation is the small live trial above, because further synthetic checks do not answer the remaining usefulness and burden questions.

No user decision is needed for the completed code, test, exercise or repository backup. **The only requested next input is whether Boss authorizes this bounded live trial and its explicitly scoped promotions.**
