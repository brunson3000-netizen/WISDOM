# Case 001 — Initial Foibles, Challenges, Recoveries, and Shenanigans Trace

**Status:** ACTIVE EDUCATIONAL EVIDENCE  
**Case:** `CASE_001_LONGITUDINAL_AI_LEARNER.md`  
**Cutoff:** 2026-09-06  
**Evidence mode:** mixed retrospective reconstruction and same-day prospective capture

## Purpose

Preserve the messy parts of the learning process before they disappear behind successful outcomes.

"Foible" and "shenanigans" are informal research labels here. Each event should still be reducible to a real technical, cognitive, workflow, governance, or interface issue.

## Observations

### O-001 — Learning by attempting a real system

**Observation:** The learner began contemporary AI-assisted engineering through ambitious real projects rather than a predefined tutorial path.

**Why it matters:** Authentic goals exposed real dependencies quickly: repositories, authority, state, tooling, tests, model delegation, compute, provenance, and handoffs became necessary because the project demanded them.

**Candidate lesson:** Goal-driven learning may create strong motivation and transfer, but it can also expose advanced complexity before foundational concepts have stabilized.

**Counterpoint:** This trajectory may not generalize to learners who want smaller, bounded uses of AI.

**Confidence:** High for this case; low for generalization.

### O-002 — Parallel ambition creates synchronization cost

**Observation:** Multiple active projects and workstreams progressed in parallel. The operator's branching itself was productive, but agents frequently pushed reconciliation, state tracking, and handoff burden back onto the operator.

**Candidate lesson:** Parallel work is not inherently a defect. The engineering problem is whether the system makes the human remember and reconcile everything manually.

**Research question:** How early should learners be taught branches, worktrees, durable work identity, and explicit project state?

### O-003 — Agents can re-prove settled facts until they lose the plot

**Observation:** The operator repeatedly noticed agents revisiting already validated state instead of isolating what remained broken or uncertain.

**Effect:** Context and attention were spent on settled material, increasing the chance of losing the active problem.

**Candidate lesson:** A good AI workflow needs a notion of "known-good baseline" plus explicit invalidation conditions.

**Counter-risk:** Treating a prior conclusion as permanently settled can preserve stale or dependency-invalidated assumptions.

### O-004 — Governance can start governing itself

**Observation:** Constitutional/governance work produced increasingly elaborate rules for what happens when prior governance mechanisms fail. The design began reproducing the recursive branching problem it was intended to control.

**Recovery:** The operator recognized the loop and forced a state change: stop adding theory, freeze the current model, run evidence, and terminate genuinely unresolved branches at the operator unless an authorized deterministic resolver already exists.

**Candidate lesson:** More rules can reduce autonomy or increase ambiguity depending on where they are added. Governance itself needs falsification and stopping criteria.

### O-005 — A complete-looking handoff can be incomplete

**Observation:** In G.A.M.E. fixture/handoff work, a parent register was omitted because it was treated as superseded even though later material depended on it, and a promised regression fixture set had not actually been built.

**Effect:** Downstream work received a package that looked complete while required dependencies were missing.

**Candidate lesson:** Handoff quality is an executable property, not a prose-quality property. Dependency closure and artifact custody matter.

**Shenanigans signal:** "Looks finished" is not the same state as "all required artifacts are present."

### O-006 — More models do not automatically create more independent roles

**Observation:** Governance research found that abundant model instances did not automatically satisfy requirements for distinct formal project roles or independent authority.

**Candidate lesson:** Capability supply, perspective supply, role identity, and authority are different things.

**Shenanigans signal:** Ten AI windows can still be one kind of evidence source rather than ten independent authorities.

### O-007 — Telemetry invites overclaim if the question is not precise

**Observation:** Harness research produced cases where trial results were described more broadly than the evidence justified: timeout behavior, concurrency, route selection, fixture readiness, and health-based routing each risked being treated as proof of more than was actually measured.

**Candidate lesson:** Preserve the distinction between observation, inference, and conclusion. Instrumentation is not automatically interpretation.

**Shenanigans signal:** A dashboard full of numbers can create false confidence if the experiment did not actually test the claim being made.

### O-008 — A command-line tool can decide it wants to be a GUI

**Observation:** During compute-harness work, an attempted help/invocation path unexpectedly opened a GUI instead of remaining headless.

**Recovery:** The path was abandoned and the exact invocation boundary was treated as a separate engineering problem.

**Candidate lesson:** Tool behavior must be observed, not assumed from the tool's category or name.

**Shenanigans signal:** "CLI" is a hypothesis until the exact command behaves like one.

### O-009 — Long pasted terminal blocks are an operator-environment hazard

**Observation:** On the learner's Linux Mint setup, long pasted command blocks can become visually mangled or appear truncated, making it difficult to know whether the terminal received exactly what was intended.

**Recovery:** Operator workflow changed toward short blocks, one consolidated safe operation, or writing longer scripts/files first.

**Candidate lesson:** The execution interface is part of the system. Instructions that are theoretically correct but fragile to paste are not operationally good instructions.

### O-010 — `set -e` turned a paste into an escape hatch

**Observation:** A repository-intake block designed with `set -e` and explicit `exit 1` logic was pasted directly into an interactive terminal. When a check failed, the shell exited and the terminal window closed.

**Root issue:** A pattern appropriate inside a script was used carelessly in an interactive operator context.

**Recovery:** Interactive instructions stopped using shell-exit behavior that could kill the operator's terminal.

**Candidate lesson:** Code safety depends on execution context, not merely on whether each command is individually valid.

**Shenanigans signal:** "Fail fast" can become "close the user's terminal fast."

### O-011 — Nano saved the lesson, not the file

**Observation:** A provenance file was opened in Nano using a relative path from the wrong working-directory context. Nano retained the buffer but failed to write the requested path with `No such file or directory`.

**Recovery:** Use the absolute repository path when recovering an unsaved buffer.

**Candidate lesson:** Working directory is hidden state. Interfaces that hide context can turn correct filenames into incorrect locations.

### O-012 — A style checker tried to edit history

**Observation:** `git diff --cached --check` flagged trailing whitespace inside an imported, hash-verified G.A.M.E. research artifact.

**Conflict:** Removing the whitespace would make the local style check happy but would destroy byte-for-byte identity with the source evidence.

**Recovery:** Validate W.I.S.D.O.M.-authored metadata separately and preserve immutable imported evidence unchanged.

**Candidate lesson:** Validation rules need scope. A generally useful quality check can be wrong for an evidence-preservation boundary.

**Shenanigans signal:** Sometimes the linter is the thing that needs to be told to behave.

### O-013 — Local truth and shared truth are different until synchronized

**Observation:** W.I.S.D.O.M. initially existed only as a local Git repository. ChatGPT could not directly inspect or write that local state through the GitHub connector until a GitHub repository was created, linked, and pushed.

**Candidate lesson:** "It is in Git" does not answer where it is, who can see it, or whether local and remote states agree.

### O-014 — Cross-project reuse can silently become cross-project contamination

**Observation:** G.A.M.E. and S.W.A.R.M. work repeatedly had to distinguish useful research transfer from accidentally importing another project's authority, terminology, or operative policy.

**Candidate lesson:** Reuse the general lesson only after separating evidence from authority and local project truth.

**Shenanigans signal:** Copying a good rule into the wrong authority context can turn good advice into bad governance.

## Emerging challenge classes

The observations currently cluster into:

- conceptual foibles — confusing evidence, authority, state, or role;
- AI-agent foibles — over-expansion, rechecking settled state, overclaiming, complete-looking but incomplete handoffs;
- governance foibles — recursive rules and authority leakage;
- tool foibles — unexpected GUI behavior, hidden working-directory state, inappropriate validation scope;
- operator-interface foibles — long paste fragility and execution-context mismatch;
- project-system foibles — synchronization, provenance, parallel-work reconciliation, cross-project contamination.

The taxonomy is provisional. It should be changed if later evidence clusters better another way.

## Research implication

These events should not be sanitized out of the educational evidence corpus.

A polished final workflow teaches what worked. A preserved failure/recovery pair can also teach:

1. what looked reasonable;
2. what actually happened;
3. how the mismatch was detected;
4. what changed afterward; and
5. whether the fix generalized.
