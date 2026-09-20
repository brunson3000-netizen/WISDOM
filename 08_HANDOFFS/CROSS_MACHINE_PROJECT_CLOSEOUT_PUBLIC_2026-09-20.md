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

## External recovery evidence

- Both redundant external Git bundles were independently verified as valid complete-history
  bundles containing the preserved SWARM refs.
- Both Project Backup volumes contain the same bounded weekly archive set for weeks 35–38 of
  2026, with per-week manifests and verification markers present.
- The older mirror sets remain evidence copies; their existence and valid bundles do not prove
  that they contain the newest active-primary AI commits.

## Local preservation package

Three projects without a clean GitHub-upstream proof were captured into a local-only,
checksummed preservation package. Each package contains a complete Git bundle, a compressed
working-tree snapshot, tracked-worktree/index patches, an untracked-file manifest, a receipt,
and SHA-256 verification. The package was independently re-verified after creation. It was
not published because it contains machine-local recovery material.

Both external Project Backup volumes passed all weekly archive checksum manifests for
2026-W35 through 2026-W38. The corresponding manifests are byte-identical across the two
volumes.

A non-deleting checksum dry-run from the active primary AI source found 7,698 itemized
differences to each older CURRENT mirror and 879 differences to the older active mirror.
The dry-run reported additions and updates only; no deletion option was used and no target
was modified. These differences include Git metadata and preserved untracked material, so
they remain subject to explicit source/target selection before any write-sync.

An additive timestamped mirror attempt was subsequently interrupted at Operator direction.
Its partial destination was not cleaned up, resumed, overwritten, or treated as verified.
The existing verified recovery sets remain the usable backup set; the partial copy is preserved
as a separately documented evidence artifact for later review.

The other mounted legacy archive volumes were bounded-scanned read-only. They contain games,
emulator/media archives, personal archives, or a RescueZilla disk image; no Git repository was
found within the scan depth. They are not current project-sync targets, and their high capacity
usage means no write or reclassification was attempted.

## Recovery posture

The closeout is backup-ready as an evidence package: repository identities, published refs,
mirror divergence, and the missing Windows observation are recorded without claiming that
unverified copies are current. Any future mirror update must be a separately reviewed,
non-deleting dry-run against an explicitly selected source and target.

This public handoff intentionally omits machine-local paths, filesystem identifiers, backup
state internals, and credential-related details. The detailed local-only evidence remains in
the operator worktree and was not published.
