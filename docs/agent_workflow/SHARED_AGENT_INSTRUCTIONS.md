# Shared task cooperation

Complete the assigned narrow task through implementation, independent review and repair. Follow project instructions and existing authority. KEEP does not authorize merge, publication, installation, spending or other reserved actions.

## Roles

- Operator: the human who authorizes the task and holds final authority and reserved decisions.
- Architect: the team lead who defines assignments, clarifies scope within the Operator's delegation and receives escalations.
- Coordinator: the architect unless TASK.md explicitly names another coordinator and its delegated responsibilities.
- Coding agent: implements and validates the assigned work and handles routine local coordination.
- Reviewer: independently examines the assigned work and evidence; does not implement the fixes it reviews.

## Records and startup

Use one absolute shared folder containing:

- TASK.md: objective, scope, acceptance criteria, baseline, assignments, workspace paths and actual limits. The coder may record the architect's assignment without changing its meaning. Label its provenance: an Operator quotation, an architect's instruction under delegated authority, or an agent's recommendation.
- IMPLEMENTATION_STATUS.md: written only by the coding agent.
- REVIEW_STATUS.md: written only by the reviewer.

TASK.md names the available escalation channel to the coordinator, including Operator relay when direct contact is unavailable. A responsible owner is the person assigned to resolve a dependency; if none is known, the architect identifies the next actor without assigning unauthorized work.

Record scope rulings and escalation dispositions in a Decisions section of TASK.md. Name one TASK.md writer: the architect when it has access, otherwise the coder transcribing attributed instructions without changing their meaning. Other agents write their own status records. Send the escalation through the named available channel; a file update alone is not delivery.

Reuse equivalent existing files and name them in TASK.md. All agents read the same shared records, not worktree copies. Preserve prior rounds; timestamp updates and state the next actor/action. Preserve unrelated work; use separate worktrees before concurrent repository writes and isolate test outputs where they could conflict.

Prove shared access: coder posts READY with a unique token; reviewer replies with that token and its own; coder acknowledges. In its first entry each actor records its actual session identity and model where exposed, its workspace (path, branch or detached HEAD, baseline) and the SHA-256 of each instruction file it read; a path mention is not proof that a file loaded. Record available wait, session-status and resume tools. Writing a file does not wake an ended session.

## Handoffs

Identify every request, acknowledgement and verdict by task, round and exact checkpoint; each task/round pair identifies one request. Include evidence and the next actor/action. Use a full commit for a clean artifact or an immutable snapshot/manifest covering all relevant changes.

Allow one outstanding review request. Freeze its artifact during review. Before modifying relevant content, explicitly withdraw the outstanding request in the implementation record and notify the reviewer through the available channel. Submit the completed repair as one new checkpoint and round; do not repeatedly interrupt review with incremental edits. Any relevant change supersedes the previous request. Ignore stale or duplicate handoffs; never transfer KEEP to changed material. A REVISE keeps the repair duty open; ending a turn does not discharge it. After the next owner acknowledges a completed milestone, polling of that request ends.

Coder implements and requests review → reviewer records REVISE or KEEP → coder repairs and resubmits, or completes required final validation and authorized checkpointing, then records matching KEEP under the completion rule. A failed gate blocks only the transition that requires it. If the artifact is unchanged, record a gate-status update against the existing checkpoint and round, with evidence and the blocked transition; this is not a new review request. Preserve an existing artifact KEEP unless new evidence invalidates its findings. Never present artifact KEEP as passage of the failed gate or as task completion. A relevant artifact repair requires a new review round. It does not authorize diagnosis or repair of unrelated failures; continue unaffected authorized work.

## Evidence and validation

Validation covers the authorized changed behavior and its directly affected connections. A repository-wide run is required only when an applicable authorized task or release requirement specifically requires it; if that requirement conflicts with the Operator's scope or testing limit, report the conflict before running it.

Reuse passing evidence when the relevant implementation, test inputs and execution conditions remain applicable. A new commit identifier, records-only change, or desire for additional confidence is not by itself a reason to rerun. Repeat only the failed check after its repair or a check invalidated by a specific relevant change; a demonstrated intermittent defect can justify targeted repetition. Broad repetition follows the Operator's existing approval rule. Keep active edits out of a validation checkout. A rerun that tooling mechanically forces is disclosed as a tooling conflict, not presented as new engineering need.

Committing exactly the reviewed content, or adding records-only updates that do not alter governed behavior, acceptance evidence or the reviewed artifact, does not require renewed substantive review. Record the correspondence between the reviewed snapshot/manifest and final commit. Preserve accurate identity and hash bindings required by applicable tooling; an identity update is not a reason to repeat the content review or tests. If records themselves are the reviewed deliverable or affect a decision or gate, assess their actual change rather than exempting them by filename.

Integration and troubleshooting follow the documentation-first policy (`DOCUMENTATION_FIRST_POLICY.md` in this folder, or the project's own copy of it). Keep its reference map and the exact error, version, cause, remedy and open questions in the task records and handoff. Record each duty outcome as completed, cancelled, failed, interrupted or uncertain; dependent work proceeds only on evidence that its completion conditions were met.

## Findings and disagreements

A blocking finding must identify an authorized in-scope requirement and a demonstrated violation: a reproduction, a concrete code path or another verifiable demonstration. A runnable reproduction is useful but not mandatory. Reviewer requests do not expand the assignment. Agents must not add acceptance conditions beyond existing authorized requirements without new Operator direction. Distinguish optional improvements from defects; identify required checks that could not be completed rather than treating uncertainty as proof of success.

Separate a correct reviewed change from a failed external acceptance gate. For an unrelated failure, use sufficient existing evidence, preserve the limitation, and refer its disposition to the responsible owner through the architect; do not require exhaustive proof of non-causation. Further diagnosis must resolve a specific dependency of this task within its existing authority. Unrelated defects do not expand this task. If a defect prevents an acceptance criterion from being met, escalate that dependency instead of dismissing it as out of scope. A genuine regression or a required unresolved gate still blocks the affected claim; uncertainty is never relabeled success.

If a finding remains disputed after a response and reconsideration with no new evidence, record both positions and refer it to the architect. Continue unaffected work; do not repeat the same argument or repair blindly. The architect clarifies scope or arranges the needed evidence within existing authority and records the ruling in TASK.md Decisions. Its scope ruling binds both agents within the Operator's delegation; the reviewer must reassess findings against that scope and remove out-of-scope demands as blockers. The reviewer retains independent judgment on whether the in-scope requirements are met. The architect cannot compel KEEP, waive requirements or override the Operator. A dispute about the ruling's authority goes to the Operator. An unresolved in-scope blocker or authority dispute follows the blocked-work exit below; do not repeat the same review loop.

## Waiting and recovery

After every handoff, both agents check the other record. Detect updates by any change in the record's bytes (for example its SHA-256), not by matching a heading pattern, and start each own entry on a new line with a `## ` heading and a clock-read UTC time. Act on an actionable response; otherwise wait 30 seconds using a supported tool, check again and repeat. Do not end because a handoff is finished or invent a polling cutoff. The reviewer also waits after its KEEP until the coder's matching KEEP.

When available, check session status while waiting. If the other session has stopped, use an authorized resume tool with the pending action. Do not start a duplicate worker. Silence alone does not prove a session stopped. Only yield to background notification if it has been shown to reactivate the session.

After 10 checks without an update, during startup or later, request status once through available means and inspect session status if possible. Keep checking; five minutes is a coordination check, not a work deadline. Do not repeatedly send the same alert. Escalate a confirmed interruption or contradictory state with the pending action.

For a confirmed interruption, unavailable waiting capability, genuine blocker or actual platform/authority limit, preserve the pending action and notify the coordinator through available means. If human recovery is necessary, provide one exact instruction and destination. Do not silently poll a known unrecoverable session or label blocked work KEEP. Honor Operator stops and real deadlines.

On restart, read TASK.md and both records and continue the pending action, reusing valid evidence. A replacement must have the role assigned and the predecessor stopped or its writes isolated. If both agents are waiting, follow the recorded next action; escalate conflicting records to the coordinator. Never bypass a denied action through another agent.

## Blocked-work exit

For a known blocker that cannot be resolved within the current authority or an unresolved dispute requiring a ruling, record BLOCKED in your own status record with the checkpoint, evidence, affected work, pending action, next actor and resume condition. Notify the coordinator through the named channel, using Operator relay if necessary. Continue unaffected authorized work; once none remains actionable, each agent records its own cleanup and ends its session. Do not wait for matching KEEP, the other agent's cleanup or a future ruling in order to exit blocked work. Never write the other agent's status or imply that its cleanup is confirmed. BLOCKED is a stopped state, not successful completion; preserve existing verdicts and evidence and do not record CLOSEOUT_COMPLETE.

This explicit exit takes precedence over the waiting and successful-completion loops. A slow or silent peer alone is not this blocker; peer waiting, polling and recovery above remain unchanged. The duty holder owns peer-status checking, request delivery, acknowledgment tracking and recovery within the grant. The Operator performs only a necessary physical/interface action agents cannot perform, or makes a reserved decision. The duty holder supplies the complete action, records its outcome and resumes coordination. Resume affected work only when the recorded blocker is resolved or authorized direction changes it; read the decision and status records and reuse valid evidence.

## Completion

For successful completion:

1. After reviewer KEEP, the coder finishes required validation using applicable existing evidence and completes authorized checkpointing before recording its own KEEP. If checkpointing is not authorized, retain the reviewed immutable snapshot/manifest and report that reserved action separately.
2. If checkpointing changes the identifier without changing reviewed content, the coder records the correspondence and evidence of equivalence, such as matching relevant content hashes or a content diff. The reviewer confirms that equivalence in its own record before cleanup. This confirms identity; it is not a new substantive review round or reason to rerun tests. Preserve any exact candidate, ancestry and hash bindings required by applicable tooling; content equivalence does not waive them.
3. Both agents record KEEP for the same round and final checkpoint, or retain the original reviewer KEEP with its explicit equivalence confirmation linking it to the coder's final checkpoint. A relevant content change requires a new review round under the shared review-reuse rule.
4. Each agent stops and verifies only its own task-created processes or wakeups and records CLEAN, or CLEAN — none created. Leave unrelated resources alone; late callbacks must respect completion and exit.
5. The reviewer may finish after its CLEAN. The coder uses the same waiting/recovery rules until both CLEAN records exist, then records CLOSEOUT_COMPLETE with the final checkpoint, both verdicts, any equivalence confirmation, validation, cleanup and remaining limitations or approvals. Distinguish reviewed, committed, published and installed states.
6. Before ending a completed or blocked task, the builder and adversarial reviewer must each deliver their own handoff as one ZIP directly in the Operator’s Downloads folder, staged inside their own workspace; never a folder of loose files. The ZIP holds a concise Markdown handoff, only the supporting files the recipient needs, and their SHA-256 values. Include conclusions and verdict, the exact checkpoint, a concise evidence summary, unresolved questions or blockers, and the next actor/action. State ‘None’ when there are no unresolved questions. Use a unique filename containing the task ID, agent role and timestamp. Report the absolute file path to the Operator. A shared status record alone does not satisfy this delivery requirement. Read the ZIP back and verify its members before reporting it. If delivery fails, report the failure and the preserved file’s location rather than claiming delivery.

A known blocker follows the blocked-work exit instead of this successful-completion sequence.

## Codex goal continuity — Luna

Revision: 2026-10-03. Use a task-scoped Codex goal for Luna's cooperative review when supported. This supplements Waiting and recovery; it changes no role, authority, evidence or completion rule. The Operator has reported that this workflow improves continuity.

### Activate and record

The architect fills the two placeholders below and includes the command in Luna's startup dispatch. Submit it in Luna's Codex thread, not a shell. A supported goal-setting tool may activate the same assigned objective directly. Record the task, shared path, goal text and observed activation state in REVIEW_STATUS.md; do not claim activation from file contents alone. A matching active goal needs no replacement. Missing goal support does not block otherwise authorized work: retain the existing waiting/recovery procedure and disclose the limitation.

```text
/goal Complete my independent reviewer assignment for <TASK_ID> using <ABSOLUTE_SHARED_FOLDER>\TASK.md, IMPLEMENTATION_STATUS.md and REVIEW_STATUS.md. Review each current immutable checkpoint against the authorized requirements; publish evidence-backed KEEP or actionable REVISE in my own record and review submitted repairs. Coordinate directly with the builder through the shared records. When waiting, use the supported 30-second wait and recovery procedure; check fresh records without busywork or repeated tests. Continue through required checkpoint-equivalence confirmation, my own cleanup and my one-ZIP Downloads handoff. Success requires the shared reviewer-completion conditions, not merely an intermediate verdict. Preserve independent judgment, scope and all approval limits. If a genuine blocker leaves no authorized work actionable, record BLOCKED with evidence, next actor and resume condition, notify the coordinator, complete my own cleanup and handoff, then stop without claiming success. Honor Operator stops, pauses and platform limits.
```

### Coordinate without unnecessary relay

Both agents still check and acknowledge peer records. Luna's goal cannot guarantee that Opus is active. Check available session evidence before diagnosing a stopped peer; silence alone is insufficient. Do not create overlapping pollers, artificial activity, repeated alerts or unnecessary tests to keep a session alive. A supported wait followed by a fresh record check is sufficient while waiting is appropriate.

### Finish or stop honestly

An intermediate verdict is not successful reviewer completion. Apply Completion, including any equivalence confirmation, own CLEAN record and own one-ZIP Downloads handoff. The reviewer need not wait for the coder's later CLOSEOUT_COMPLETE after satisfying her own completion obligations.

Blocked-work exit overrides waiting and goal continuation. A failed external gate may preserve artifact KEEP while blocking the next transition. Once no unaffected authorized work remains, write the blocked handoff and exit; do not wait indefinitely for a ruling or commit that cannot currently happen. Do not mark blocked work successful to terminate a goal. If an active goal remains after a blocked exit, report the state and the exact pause action needed through the available channel; never invent a completed or paused state.

For supported Codex builds, `/goal` displays the current goal; `/goal pause`, `/goal resume` and `/goal clear` manage it. Respect user/system control of those transitions. Budget limits and interruptions are not successful completion and must not be bypassed by timers, hooks, new sessions or renewed goals. Resume only under the existing recovery and authority rules, then reread the shared records. Do not treat a goal as a cross-session wake guarantee.

Official command reference, checked 2026-10-03: https://developers.openai.com/cookbook/examples/codex/using_goals_in_codex ("Goals are available starting in Codex 0.128.0"). The evidence observed on this Windows host is recorded in the launch briefs.
