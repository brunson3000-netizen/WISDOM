# Offline prototype contract — task-local implementation, no promotion

Location: 06_EXPERIMENTS/TCGL_OFFLINE_V1/ in the WISDOM repository. Local staging: /workspace/scratch/3c1c95d7633b/luna_tcgl/prototype/.

Implement a Python-standard-library offline research recorder and index. All persisted records carry mode=simulation. There is no promotion, activation, approval, external fetch, execution-of-evidence, or live policy integration operation. Structural validation is explicitly not semantic approval. This contract is an implementation choice for the authorized offline subtask, not project policy.

## Card JSON contract

Exact fields (reject extra keys at all object levels):
- idea: nonempty string
- task_anchor: nonempty string describing the observation/problem/gap and its task relevance
- inquiry: nonempty string describing question and next authorized investigation
- expected_effects: {benefit: nonempty string, adverse: nonempty string}
- evidence: {supporting: list of nonempty strings, against: list of nonempty strings, absence: string or null, uncertainty: nonempty string, source_event_ids: list of distinct nonempty strings}. If supporting empty, absence must be nonempty. Reference strings are opaque: do not resolve them. If supporting nonempty, absence can describe other gaps or be null.
- scope: {applies_to: nonempty string, limits: nonempty string, grant_ref: nonempty string}. This records a claimed grant reference; it does not verify authority or enforce aggregate budgets.
- related_candidates: list of distinct nonempty strings
- proposed_disposition: one of investigate, retain_theory, link_existing, defer. These are simulated recommendations, not TCGL maturity states. link_existing requires at least one related candidate.

## Python API (tcgl_offline.py)

validate_card(card) -> list[str] errors; never raises on arbitrary JSON types.
make_record(card, task_id, reporter, candidate_id=None, revision=1, parent_record_id=None, change_reason=None) -> dict. Generates UUID-based record_id/candidate_id if needed, UTC timestamp; schema_version=1 (int, not bool), mode=simulation. Exact top-level keys: schema_version, mode, record_id, candidate_id, revision, parent_record_id, change_reason, task_id, reporter, created_at, card. Only positive int revisions, no bool; revision 1 has null parent/reason; later revisions require nonempty parent/reason. Reject malformed records at append even if callers bypass make_record. Scope and originating task cannot change within a candidate revision chain: a distinct inquiry scope uses another linked candidate.
append_record(db_path, record) -> dict receipt. Validate BEFORE creating any database. SQLite transaction (BEGIN IMMEDIATE): record_id unique, candidate+revision unique, first revision=1, subsequent exactly current+1 and parent matches last record_id; previous task_id and scope unchanged. Preserve all old records; no UPDATE/DELETE public API. Use parameterized SQL; no eval, shell, network, or file content execution. Roll back on errors. Storage errors are errors, not 'empty success'. SQLite append-only through this API is not a tamperproof archive.
read_records(db_path) -> list[dict] in insertion order; read-only, fail if store absent, never initialize a missing store. Validate stored record structure, detect inconsistent histories; fail visibly if corrupt. Read-only operations shouldn't alter store.
build_index(records) -> dict with records_count, candidates mapping each ID to latest record/revision/idea/proposed_disposition, source_events mapping each source ID to unique record IDs and candidate IDs, unresolved_related_candidates list; field semantic_judgment=not_evaluated, authority=not_checked, mode=simulation. Exact source matching only, no semantic duplicate certification. Revisions reusing one source remain one source event, not independent replication.

## CLI

check CARD: JSON {valid:bool, errors:[], semantic_judgment:not_evaluated, authority:not_checked, mode:simulation}; exit 0 valid, 1 invalid.
record CARD --store PATH --task TASK --reporter REPORTER [--candidate ID] [--expected-revision N] [--reason TEXT]: create revision expected+1 (expected default 0); compare current head against expected inside transaction, obtain parent safely; no silent overwrite. Exit 1 on conflict/invalid. Parent can implement via read then append expected checks transaction.
index --store PATH: JSON index. Missing DB is error.
CLI errors JSON, nonzero; malformed JSON/duplicate keys/NaN/Infinity rejected. Do not add a default store or overwrite input. Record output is a receipt, not an authority decision.

Keep implementation small. No dependency installs or generalized governance framework. Root independently supplies fixtures, tests, course exercise and report. Implementation agent owns tcgl_offline.py and IMPLEMENTATION_NOTES.md only. Note pertinent encountered issues, not a general audit.
