# Windows launch briefs (visible cooperative pair)

Operational convention. The Operator launches every working agent in a visible window; no agent, script or architect launches, resumes or replaces one in the background. The architect fills the placeholders per task, then gives the Operator a short explanation and one copyable block per action. Command forms were checked against the installed `--help` of Claude Code 2.1.288 and codex-cli 0.160.0 (2026-10-03) and used in the FEDERATION fresh-pair verification; see `WINDOWS_EXECUTION_PROFILE.md`.

## Placeholders

| Placeholder | Meaning |
|---|---|
| `<BUILDER_WT>` | Builder's own task worktree (or project folder, for a non-Git project) |
| `<REVIEWER_WT>` | Reviewer's separate worktree, detached until an exact intake is copied |
| `<SHARED>` | Task shared home outside the repository, holding `TASK.md` and both status records |
| `<DOWNLOADS>` | Added only when the task's `TASK.md` grants the Downloads ZIP destination |
| `<TASK>` / `<ASSIGNMENT>` | Task ID and the assignment file in `<SHARED>` |

## Builder (Claude Code)

```powershell
Set-Location '<BUILDER_WT>'; claude.cmd --add-dir '<SHARED>' --add-dir '<DOWNLOADS>'
```

Omit `--add-dir '<DOWNLOADS>'` when the task grants no Downloads destination.

## Reviewer (Codex)

```powershell
Set-Location '<REVIEWER_WT>'; codex.cmd --cd '<REVIEWER_WT>' --add-dir '<SHARED>' --add-dir '<DOWNLOADS>'
```

Codex treats added directories as writable. Add only these task paths; never the whole user profile. If Codex prints `Error: failed to open daemon process: Access is denied. (os error 5)`, record the error and rerun the same command with `--no-daemon` appended.

## First message to each agent

```text
You are the <builder|reviewer> for <TASK>. Read <SHARED>\TASK.md, <SHARED>\<ASSIGNMENT>, both status records, the project's AGENTS.md (and CLAUDE.md if present), and in docs/agent_workflow/: SHARED_AGENT_INSTRUCTIONS.md, your role sheet, WINDOWS_EXECUTION_PROFILE.md and DOCUMENTATION_FIRST_POLICY.md. In your first status entry record your session identity and model where exposed, your workspace path, branch or detached HEAD and baseline, $PSVersionTable.PSVersion, the interpreter you verified, and the SHA-256 of each instruction file you read. Then complete the READY token exchange before any edit.
```

## Recovering an ended session (visible, Operator-run)

The duty holder prepares the exact command and the pending action; the Operator runs it in a visible window. Use it only for a confirmed ended session, never to start a duplicate writer.

```powershell
Set-Location '<BUILDER_WT>'; claude.cmd --resume '<session-id>' --add-dir '<SHARED>'
```

```powershell
Set-Location '<REVIEWER_WT>'; codex.cmd resume '<session-id>' --cd '<REVIEWER_WT>' --add-dir '<SHARED>'
```

When the session ID is not recorded, do not guess it. `codex.cmd resume --cd '<REVIEWER_WT>' --add-dir '<SHARED>'` (no ID) opens Codex's own session picker, and `claude.cmd --resume` (no ID) opens Claude Code's; the Operator picks the session by its visible title and working directory. Do not use `--last` unless the Operator confirms the most recent session is the intended one.

Automatic wake of an agent whose turn has ended is not provided, with or without a goal. This visible, Operator-run resume is the supported recovery.

## Reviewer goal (Codex `/goal`)

The procedure is in `SHARED_AGENT_INSTRUCTIONS.md` ("Codex goal continuity"); this section only adds the launch step and the evidence observed on this host.

**Launch step.** The architect fills `<TASK_ID>` and `<ABSOLUTE_SHARED_FOLDER>` in the shared sheet's `/goal` template and gives it to the Operator with the reviewer's launch command. The Operator pastes it into the reviewer's Codex window (the Codex prompt, not PowerShell), then pastes the first message. The reviewer records the goal text and the state it observes in `REVIEW_STATUS.md`. For a resumed session, `/goal` alone shows whether a goal is already active; a matching active goal is reused, and a paused goal is not resumed without the Operator.

**Evidence on this host (2026-10-03), with its limits:**
- **Documented:** "Goals are available starting in Codex 0.128.0"; `/goal <objective>` sets a goal, `/goal` shows it, `/goal pause`, `/goal resume` and `/goal clear` manage it (https://developers.openai.com/cookbook/examples/codex/using_goals_in_codex, read 2026-10-03).
- **Installed:** codex-cli 0.160.0 lists the feature `goals` as stable and enabled (`codex.cmd features list`).
- **Reported:** the Operator reports that the Linux workflow using `/goal` improves continuity. That is an Operator report about Linux, not a Windows observation.
- **Not yet recorded on Windows:** a goal carrying a review duty across turn endings in this workflow. The first reviewer to use it records what it observes. Until then, treat `/goal` as supported by documentation and installed version, not as proven here.

A goal does not wake an ended session, does not keep the builder running, and never replaces the waiting, recovery and blocked-exit rules. If `/goal` is unavailable, the pair works under those rules and records the limitation. One goal per reviewer session; never a second session for the same role.

## Handoff delivery

Each actor stages its handoff inside its own workspace and delivers one uniquely named ZIP directly in `<DOWNLOADS>` (for example `<PROJECT>__<TASK>__<ROLE>__TO-<DESTINATION>__<YYYYMMDDTHHMMSSZ>__HANDOFF.zip`). The ZIP holds a concise Markdown handoff, only the supporting files the recipient needs, and their SHA-256 values. The actor reads it back before reporting the path. It is never a folder of loose files (Operator direction, 2026-10-03).
