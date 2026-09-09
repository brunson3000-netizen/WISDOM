# Offline prototype implementation notes

Implemented `tcgl_offline.py` against `CONTRACT.md` using only Python standard library and SQLite. The store is simulation mode only: it has no promotion, activation, approval, policy loading, external fetch, or runtime integration.

## Pertinent implementation governance issues

- **A declaration is not authority.** `scope.grant_ref` is stored as an opaque reference and never verified; `build_index` reports `authority: not_checked`. This follows the contract because a card cannot prove its own grant.
- **Structural status is not semantic merit.** The validator checks shape, references, and history only; it reports `semantic_judgment: not_evaluated`. Human/reviewer judgment remains outside this offline mechanism.
- **Revision safety protects history, not legitimacy.** SQLite transactions enforce one next revision, matching parent, and stable task/scope. The API has no update/delete, but SQLite remains a mutable local file rather than a tamperproof archive.
- **Resource and stale-policy claims remain unknown.** No budget arithmetic or current-policy resolver is implemented, so the prototype does not infer overruns or staleness from self-reported fields.

## Smoke verification

The module was syntax-compiled and exercised with disposable JSON/card inputs: valid check, invalid extra-key check, append/read/index, revision append, duplicate source-event indexing, and expected-revision conflict. These are smoke checks of code paths, not empirical validation of TCGL or semantic curation.

Known boundary: `record` reads the store before its transactional append to obtain the head, then the append transaction rechecks the parent and revision. Concurrent callers therefore receive a conflict rather than silently overwriting; a missing store is initialized only by a valid append.

Additional smoke result: revision 2 appended successfully with matching parent and unchanged task/scope; a mismatched expected revision returns a JSON error and nonzero exit. A scope mutation is rejected and transaction rollback preserves the prior record.

## Parent review and corrections

The preceding sections are Luna's initial implementation account. Parent-authored contract tests and code inspection found gaps beyond those smoke checks. The tested successor validates UTC timestamp syntax and exact integer schema versions; handles malformed disposition types without raising; verifies expected revision even for a missing candidate; opens index reads with SQLite read-only mode; validates stored payload/column agreement and history before appending; rejects unrelated databases; chooses highest revision independently of input ordering; and preserves a copied card rather than a mutable caller reference. SQLite enforces candidate/revision uniqueness as well as record identity.

The initial test harness assumed errors were printed on stdout. That was an unwarranted test assumption: the contract required JSON errors, not a particular stream. Tests now accept stderr for operational errors, and the README documents the stream convention. Timestamp acceptance was an actual implementation defect. Subsequent assertions that the same store did not exist cascaded from that defect; they were not three independent storage defects.

Eighteen contract tests, including the fifteen synthetic fixture cases, pass in the final captured evaluation. See RESULTS.json for exact input hashes, interpreter, and output. Remaining semantic, authorization, authenticated-identity and real-world burden limits are intentional and documented, not successful validations.
