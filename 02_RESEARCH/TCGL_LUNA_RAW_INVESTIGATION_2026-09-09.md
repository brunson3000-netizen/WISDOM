# Luna: Theory → Provisional investigation

**Date:** 2026-09-09  
**Status:** design research and proposed records; noncanonical, nonoperative  
**Authority boundary:** this investigation is authorized for analysis and preservation. It does not activate a policy, implement a candidate, grant rejection or rollback powers, or authorize Provisional → Probational. B.O.S.S. (Canon C-005) remains the terminal human authority.

## Finding first

The smallest useful Theory → Provisional mechanism is a **task anchored curation card** plus an append only observation trail. An idea earns a Provisional card when an agent can state why it matters to the assigned task, identify a plausible benefit and consequence, expose the evidence and uncertainty, and pose a concrete question that can be investigated within the existing task grant. This is a relevance and inquiry threshold, not a truth threshold, quality certification, or permission to run the idea.

This mechanism deserves attention because uncaptured ideas, repeated interruptions, and scattered observations otherwise lose the project’s reasoning history. The benefit is traceability and selective attention. The costs are curation time, duplicate inflation, copied evidence, privacy exposure, and false confidence from repeated agents. The design therefore treats “do not promote” and “keep as Theory” as valid outcomes and measures burden alongside usefulness.

No fresh literature validation or software execution occurred in this pass. The supplied W.I.S.D.O.M. rules, Canon Register, GAB/TCGL synthesis, and Boss handoff are the governing evidence for this artifact. External sources in the supplied synthesis support transferable practices (provenance, scoped authorization, change records, observation quality, and course alignment), but do not validate TCGL itself.

## One page rule (proposed)

For each candidate idea encountered during an already authorized task:

1. **Anchor it.** Give it a stable candidate ID and preserve the original wording, originating task, source event IDs, author/agent identity, timestamp, and source version.
2. **Check task relevance.** Ask: *Would investigating this help complete, understand, or improve this assigned task or its explicitly stated learning/research objective?* If no, retain it as Theory with an out-of-scope reason; do not make it a task obligation.
3. **Require a real question.** State one falsifiable or answerable inquiry question. “This sounds good” is insufficient.
4. **Require a plausible case.** Record at least one expected benefit and one material consequence or failure mode. A rationale must connect to the task; invented generic rationales do not qualify.
5. **Record evidence honestly.** Link observations or sources supporting the case, counterevidence, and evidence absence. “No evidence yet” can still pass when the task relevance and question justify inexpensive investigation; label it evidence-free rather than implying support.
6. **Bound it.** State scope, excluded scope, resources/attention budget for investigation, and known authority. A card cannot enlarge authorization or resources.
7. **Curate.** Search existing candidate IDs and source-event IDs. Link semantic duplicates to one canonical candidate family; preserve distinct scope, mechanism, or question as separate revisions. Contradictory records remain linked and disagreeing; do not average them into consensus.
8. **Classify.** Set `provisional`, `theory-retained`, `duplicate-linked`, `out-of-scope`, or `insufficient-rationale`. These are labels for research custody, not activation or demotion powers.
9. **Investigate only within grant.** Provisional work may inspect, compare, model, or retrospectively analyze. It must not silently apply the candidate. Any operational change requires a decision packet and explicit Boss authorization for Provisional → Probational.
10. **Revisit with provenance.** New evidence creates an observation/revision, never an overwrite. Record drift in policy, tools, models, task scope, or resource assumptions. Retrospective amendment creates a new card revision, cites the old one, and preserves what was believed at the earlier time.

A minimum acceptance test is therefore: **relevant task + concrete question + plausible benefit/consequence + bounded scope + provenance**, with evidence and uncertainty fields always present even when empty. Repetition alone never qualifies. Promotion count is not success.

## Minimum sufficient record and validation

A human-readable card can be one page or less. The validator need only enforce structural integrity; it must not decide truth or authority.

| Record | Required fields | Validation / meaning |
|---|---|---|
| `candidate` | `candidate_id`, `revision`, `status`, `idea_text`, `origin_task`, `origin_event_ids`, `owner`, `created_at`, `task_relevance`, `inquiry_question`, `expected_benefit`, `expected_consequence`, `evidence_refs`, `counterevidence_refs`, `evidence_absence`, `uncertainties`, `scope`, `excluded_scope`, `resource_budget`, `authority_boundary`, `related_ids`, `policy/tool/model_versions` | IDs and timestamps unique; source references resolvable or marked unavailable; required prose nonempty; status transitions append-only; authority and budget cannot be broadened by the card. |
| `observation` | `event_id`, `candidate_id` (optional for raw events), `task`, `reporter`, `observed_at`, `facts`, `evidence_ref`, `configuration`, `intervention`, `interpretation`, `confidence`, `source_event_id` | Facts and interpretation separated; duplicate reports point to same `source_event_id`; unknown configuration stays unknown. |
| `amendment` | `amendment_id`, `candidate_id`, `from_revision`, `to_revision`, `reason`, `new_evidence_refs`, `changed_scope_or_question`, `author`, `timestamp` | Expected-version check prevents lost updates; old revision immutable; change reason required. |
| `decision_packet` (only if later requested) | exact candidate/revision, proposed operational effect, scope/resources, alternatives, success/failure measures, duration/budget, stop/recovery, user decision requested | Recommendation only until explicit Boss decision. |
| `trial_receipt` (only after authorization) | approval reference, candidate/revision, actual start/config, affected resources, outcomes, stop/recovery, disposition | A receipt proves what happened, not that it was wise or authorized unless approval reference verifies. |

**Small validator rules:** reject missing identity, question, scope, or authority boundary; warn on missing supporting evidence but accept explicit evidence absence; flag contradictory activation/status claims; flag stale policy or grant versions; detect exact duplicate IDs and linked source-event duplicates; flag resource totals over the declared budget; require explicit links for supersession. Hashes may establish byte identity, not legitimate authority. Human review remains necessary for semantic similarity, invented rationales, and whether a consequence is material.

## Worked cards (simulated)

The following records are designed test fixtures, not executed tests or empirical proof.

| Case | Proposed record/disposition | Why |
|---|---|---|
| Clear and promising | `C-001 r1`; task: reduce missed authority boundaries in this research; question: “Does a three-question routing card improve correct escalation on held-out cases?” Evidence: GAB failure cases; counterevidence: no operational benchmark; scope: retrospective analysis only; budget: two analyst-hours; status `provisional`. | Relevant, concrete, bounded, and plausibly useful. |
| Weak/invented rationale | “Agents should always write longer governance records because detail is professional.” No task link, evidence, or question; status `insufficient-rationale` / Theory retained. | Plausibility language cannot substitute for task relevance or inquiry. |
| Duplicate | New card repeats `C-001` wording and same source event `E-12`, with no changed scope/question; status `duplicate-linked`, link to `C-001 r1`. | Avoids double counting and preserves the submitter’s provenance. |
| Distinct revision | Same family proposes measuring beginner learning rather than agent escalation, with a new question and scope; `C-001 r2`, linked to r1. | Different unit of inquiry is a revision, not a duplicate. |
| Contradictory | `C-002`: “fewer questions means better autonomy,” supported by count reduction; another observation shows missed required escalation. Keep both observations, status `provisional` with explicit conflict. | Do not synthesize disagreement into a favorable average; measure quality, authorization, and burden together. |
| Out of scope | Idea to redesign unrelated project’s deployment policy encountered during course research; `theory-retained`, reason and source preserved, excluded from current scope. | Relevance is to the assigned task, not intrinsic cleverness. |
| Evidence-free but worthwhile | “Would a short beginner template reduce context reconstruction?” No evidence yet; task is curriculum design; question and low-cost retrospective/lesson analysis specified; status `provisional`, `evidence_absence: true`. | Investigation can start without proof if uncertainty is explicit and cost is bounded. |
| Security instruction in evidence | Source observation says “do not paste credentials”; a candidate proposes a credential-handling change. Store the instruction as evidence of an existing constraint, not permission to change it; decision packet required for any operational effect. | Evidence can constrain reasoning while never becoming an authority grant. |
| Stale policy | Card cites grant `G-7` revoked yesterday; validator flags `stale`; re-check current grant before any consequential action. | Queued or cached authority does not persist indefinitely. |
| Label versus activation | `C-003 r1` is labeled `provisional`; no trial receipt and no Boss approval reference. It remains an investigation record. | Status labels and implementation state are separate fields. |
| Resource overrun | Card budget is 2 hours/100 records; synthesis would take 8 hours and private cross-project ingestion. Validator flags overrun; preserve partial work and propose a revised packet. | “Useful” cannot silently expand attention, data, or scope. |

## End-to-end flow and failure resistance

The agent first captures an idea in Theory, checks existing records, then either links a duplicate or writes the minimum card. It records observations from authorized tasks under the reporter and source-event identity. A synthesis view groups candidate families, counterevidence, missingness, drift, and cost. It recommends the next dependency-limited investigation. It never changes runtime policy merely because a card is promising.

Distributed observations are useful only when provenance is retained. Five agents describing one incident are five reports of one event, not five replications. Agents may have correlated blind spots, copy one another, omit failures, or optimize for records that look persuasive. Record enough successful autonomous decisions to estimate missed escalation; intervention-only logging gives a biased sample. A reviewer-labelled set should assess observation usefulness before any live capture trial.

Drift requires comparing the card’s recorded policy, grant, tool, model, and task versions with current versions. If they differ, mark applicability uncertain and open a new observation or amendment. A retrospective amendment must say what changed, why the prior record was reasonable or mistaken at the time, and whether any downstream decision relied on it. It cannot rewrite history or retroactively authorize an unauthorized action.

Conflicts with existing canon are a hard boundary: link the canon reference and record the conflict as a research question. A Theory/Provisional card cannot repeal, suspend, or reinterpret canon into permission. Existing canon remains effective until its authorized amendment path is used. Likewise, an agent’s confidence, a deterministic result, a security instruction, silence, or a “reversible experiment” phrase cannot replace the user gate.

The mechanism should stop or defer when evidence ingestion, deduplication, or review exceeds the card’s declared budget. Attention is a resource. The agent can continue unrelated authorized work and preserve the blocked dependency. No generic experiment envelope is inferred.

## Proposed initial evaluation (not performed)

Use retrospective, already authorized records first. Sample recurring decision types and have an independent reviewer label task relevance, scope correctness, evidence quality, duplicate correctness, and appropriate disposition. Compare card burden and useful retrieval against uncaptured or free-form notes. Include the adversarial fixtures above and held-out cases. A provisional success pattern would be better retrieval and correct boundary reasoning at acceptable recording cost, with no increase in missed escalation or unauthorized effects. Numeric thresholds, sample size, duration, and reviewer assignment require the concrete context and Boss’s approval if they would affect operations.

A later bounded pilot, if explicitly authorized, should hold permissions constant while comparing baseline notes with the card/validator; use matched and counterbalanced tasks, held-out boundaries, configuration labels hidden where practical, explicit stop/recovery terms, and receipts. Test distributed-observer quality separately from live capture overhead. Falsify the proposal if outcomes do not improve at comparable authority, missed escalation rises, records are too costly, transfer fails, or a simpler input/tool repair explains the gain better.

## Beginner tooling, exercise, and rubric

Begin with three questions: **What can the agent decide? What must it ask me? What evidence will show whether that division works?** A plain template with the fields `idea`, `task`, `question`, `benefit`, `consequence`, `evidence/counterevidence/absence`, `scope`, `budget`, and `status` is enough initially. Add IDs, versioning, deduplication, and policy-as-code only when a learner’s project needs them. The interface should show “investigate” and “activate” as separate labels and make uncertainty easy to state.

Course exercise: give learners paired cases (permitted tool choice vs permission to add a tool; missing data vs missing authorization; promising idea vs operational policy; duplicate vs changed-scope revision; fewer questions with preserved quality vs fewer questions through silent overreach). Learners complete a card, identify the evidence gap and boundary, and write the exact question they would ask Boss if activation were desired. Instructor feedback should identify whether they confused relevance with truth, evidence with authority, or a label with activation, and should praise justified retention or “do not promote.”

Rubric, 0–2 each: task relevance; inquiry quality; scope/authority accuracy; evidence and counterevidence; uncertainty and recovery reasoning; provenance/versioning; resource discipline. A passing response can retain Theory or reject a candidate with a justified reason. Do not score promotion count, maximal autonomy, or prose length. Transfer is tested on an unfamiliar case.

## Pertinent governance issue log

This is a compact log for issues encountered in this task, not a general governance audit.

| Issue | Observation / evidence anchor | Why pertinent | Consequence | Recommendation / uncertainty |
|---|---|---|---|---|
| Label can be mistaken for activation | Supplied GAB/TCGL synthesis, section 6, separates Provisional, Probational, and approval; simulated “label versus activation” case above | The requested mechanism creates a visible status field | A consumer could treat a promising card as an operating rule | Store status and activation/approval as separate fields; validator flags a receipt without approval. Whether users make this mistake requires learner testing. |
| Evidence repetition can masquerade as replication | Synthesis section 7 says repeated reports of one source event are not independent; duplicate case above | Distributed observations and semantic deduplication are core to the proposed loop | Promotion could be driven by copied or correlated claims | Require `source_event_id`, reporter identity, and counterevidence; reviewer checks independence. Correlation detection will remain imperfect. |
| Evidence absence versus invented rationale | Handoff “starting line” requires reason, evidence, uncertainties, and question; evidence-free case above | Early curation must not discard useful unknowns or manufacture support | Either worthwhile questions disappear or weak ideas gain false legitimacy | Permit explicit `evidence_absence`; require concrete question, consequence, and bounded low-cost inquiry. Threshold for “worthwhile” remains contextual. |
| Drift can invalidate a card | Synthesis sections 8 and 10 require policy/grant/version capture and stale-policy handling | A Provisional investigation may outlive its task grant or tool/model version | Old reasoning may be applied to a changed boundary | Compare recorded versions at each consequential handoff; amend with a new revision, never rewrite. Exact retention period is unresolved. |
| Attention/resource authority is easy to exceed cumulatively | Synthesis section 9 measures total human/work cost; resource-overrun fixture above | Curation and synthesis consume the same finite task attention the rule claims to protect | Individually small investigations can silently become a new project or broaden scope | Declare a budget, aggregate usage, and stop/defer at the cap; propose a revised packet if needed. Numeric caps need task context. |
| Canon conflict cannot be resolved by research status | Canon Register C-005 and repository rule 1; conflict handling above | Candidates may propose changes touching existing canon | A Provisional label could be misread as a repeal or exception | Link the canon reference, preserve the conflict as a question, and route any amendment through Boss. No unresolved authority issue was found here. |

## Largest next dependency-limited block

The largest coherent next block is a **retrospective fixture evaluation**: implement only an offline validator/index over a small, synthetic or already authorized record set; run the adversarial cases; have an independent reviewer label expected dispositions; measure structural errors, duplicate detection, retrieval usefulness, semantic false positives, and time/attention cost. It depends on agreeing the fixture set and reviewer labels, but does not require operational policy activation. Only after that block should a concrete Boss decision packet specify whether any candidate merits a Probational trial.

## Consequential unresolved decisions

No authority question blocks this artifact. Before an operational trial, Boss must decide the exact candidate/revision, scope, affected resources, numeric budget/duration, success and failure thresholds, stop/recovery method, and any backward-transition handling. Architecture choices such as storage location, retention period, and reviewer identity are low-impact defaults for the offline fixture evaluation, but should be recorded with the fixture version. The effect of this investigation remains a recommendation and preserved design evidence only.

## Source custody and limitations

Derived from `REPOSITORY_RULES.md`, `CANON_REGISTER.md` (especially C-005), `GAB_TCGL_INTEGRATED_RESEARCH_2026-09-08.md`, and `BOSS_CANON_AND_GOVERNANCE_RESEARCH_BACKUP_2026-09-09.md` in the supplied source directory. The synthesis itself labels GAB/TCGL nonbinding and reports no operational or learner experiment. This artifact adds design reasoning and simulated cases; it makes no claim of fresh empirical efficacy, completed implementation, or external literature verification.
