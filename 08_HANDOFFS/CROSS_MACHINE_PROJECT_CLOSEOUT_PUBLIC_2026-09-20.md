# Cross-machine project closeout — public handoff

Date: 2026-09-20

Status: bounded reconciliation evidence captured; divergent backup copies remain preserved.

## Verified publication state

- WISDOM `main` and the Linux/GitHub reconciliation branch resolve to the same published commit:
  `86ade30e3719e39bb1431a5d7e9feeb1f615b036`.
- SWARM `main` resolves to `b667c5c444f303f7b4d4208ccf78fd7f9917ff14`.
- SWARM-WORKSPACE `main` resolves to `cd1a761ecf506a04df96fb6a0a925d7adf1f7955`.
- No force-push, reset, deletion, or conflict discard was used.

## Cross-machine findings

- The active Linux project source agrees with the published SWARM repository head.
- Older external-drive AI mirror sets remain five commits behind that source. They were not
  overwritten or silently selected as canonical.
- The external-drive SWARM copies agree with one another at the observed repository head,
  while preserving their untracked evidence.
- The available Windows-formatted media was bounded-scanned as archive storage; no live Windows
  project worktree was available for verification. Windows branch, worktree, and newer-file
  state therefore remain unverified.
- A dirty NIM engineering worktree with no configured upstream remains preserved and unsynced.

## Repository verification matrix

The bounded live-ref check found the following clean repositories equal to their configured
GitHub branch heads: FEDERATION, FORK, GAME, LabTOOLS, NIM usage-pulse-clean, S.W.A.R.M.-OS,
S.P.A.R.K., SWARM-Universe, USAGE_PULSE, WISDOM, the sanitized closeout branch, and the
standalone Universe Bible preservation branch.

Two clean local copies were intentionally reported as unverified rather than guessed into
alignment: the NIM LabTOOLS candidate has no upstream configured, and the S.W.A.R.M.-OS local
bootstrap archive has no upstream configured. The separate NIM engineering worktree has local
changes and no upstream, and remains preserved without synchronization.

## Recovery posture

The closeout is backup-ready as an evidence package: repository identities, published refs,
mirror divergence, and the missing Windows observation are recorded without claiming that
unverified copies are current. Any future mirror update must be a separately reviewed,
non-deleting dry-run against an explicitly selected source and target.

This public handoff intentionally omits machine-local paths, filesystem identifiers, backup
state internals, and credential-related details. The detailed local-only evidence remains in
the operator worktree and was not published.
