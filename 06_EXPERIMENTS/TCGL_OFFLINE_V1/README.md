# TCGL offline prototype v1

**Implemented research tool; simulation only. No TCGL promotion or live policy activation.**

This tool records hypothetical curation decisions, preserves revisions, and groups reports by source event. It checks whether a record is complete and consistent. An agent or reviewer still decides whether its idea deserves investigation. A valid record is not approval.

From this directory, run the complete offline check block:

```bash
python3 evaluate.py
```

It uses disposable temporary stores, runs the contract tests, checks all synthetic cases, and returns a JSON receipt with source hashes. It requires Python 3.10 or newer with its standard SQLite module; the recorded run identifies the exact tested interpreter. No package installation or external service is used.

To inspect the example card without creating a store:

```bash
python3 tcgl_offline.py check example_card.json
```

To try the recorder, choose a disposable store path explicitly:

```bash
python3 tcgl_offline.py record example_card.json --store /tmp/wisdom-tcgl-demo.sqlite --task demo --reporter learner
python3 tcgl_offline.py index --store /tmp/wisdom-tcgl-demo.sqlite
```

The record receipt provides its candidate ID. For a revision, provide that ID with `--candidate`, the current revision with `--expected-revision`, and the reason with `--reason`. Conflicts fail instead of overwriting history. Task/scope changes use a new linked candidate; v1 does not decide whether a wording change is semantically harmless. Only the explicit store is written. The prototype has no command to adopt policy, change live maturity, delete records, or execute source text.

## Files and interpretation

| File | Purpose |
| --- | --- |
| [CONTRACT.md](CONTRACT.md) | This task's implemented interface and limits; not adopted project policy. |
| [tcgl_offline.py](tcgl_offline.py) | Structural validator, append/revision recorder and index. |
| [example_card.json](example_card.json) | Complete editable synthetic card. |
| [fixtures.json](fixtures.json) | Fifteen complete fictional cases and reviewer labels. |
| [test_tcgl_offline.py](test_tcgl_offline.py) | Independent contract, storage, concurrency and input checks. |
| [evaluate.py](evaluate.py) | One-command evaluation and receipt generation. |
| [RESULTS.json](RESULTS.json) | Captured executed results for the identified inputs. |
| [EXERCISE.md](EXERCISE.md) | Candidate learner exercise, assessment and instructor feedback. |
| [REVIEW_AND_NEXT_DECISION.md](REVIEW_AND_NEXT_DECISION.md) | Corrections, evidence limits and concrete next decision. |
| [IMPLEMENTATION_NOTES.md](IMPLEMENTATION_NOTES.md) | Luna's implementation notes, with parent corrections appended. |

Fields distinguish idea, task anchor, inquiry, expected effects, evidence/uncertainty, scope, relations and proposed disposition. Identity, revision, timestamp and reporter are stored separately. Missing evidence is allowed when explicitly described; it does not make a vague rationale convincing. Supporting references and grant references remain opaque text. The tool neither visits them nor verifies their authority.

`investigate`, `retain_theory`, `link_existing`, and `defer` are simulated recommendations. They are not maturity transitions. Exact source-event matches identify repeated reports, not independent replication or semantic duplicate ideas. Reports with different IDs may still describe one real event; reconciliation remains a judgement task.

Valid CLI checks return JSON on stdout. Operational/parse errors return JSON on stderr and nonzero exit; help is ordinary CLI text. Structural failures in `check` return their error list on stdout with exit 1. Indexing uses read-only database access. The API validates stored content and history before extending it. A database owner can still alter or replace the file: this is not an authenticated or tamperproof governance service.

The prototype intentionally omits runtime policy integration, authorization resolution, aggregate resource telemetry, semantic scoring and automated promotion. It is suitable for this offline research block. Live use and a Probational governance experiment are separate decisions.
