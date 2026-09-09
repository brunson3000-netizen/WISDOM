"""Run the offline synthetic check block and emit one reviewable JSON receipt."""
import hashlib
import io
import json
import platform
import tempfile
import time
import unittest
from datetime import datetime, timezone
from pathlib import Path

import tcgl_offline as t

ROOT = Path(__file__).resolve().parent


def main():
    log = io.StringIO()
    suite = unittest.defaultTestLoader.discover(str(ROOT), pattern='test_tcgl_offline.py')
    result = unittest.TextTestRunner(stream=log, verbosity=2).run(suite)
    cases = json.loads((ROOT / 'fixtures.json').read_text())['cases']
    checks = []
    start = time.perf_counter()
    for case in cases:
        errors = t.validate_card(case['card'])
        checks.append({'id': case['id'], 'structurally_valid': not errors,
                       'expected_structural_validity': case['expected_structural_validity'],
                       'matches_expected': (not errors) == case['expected_structural_validity'],
                       'errors': errors, 'semantic_judgment': 'not_evaluated'})
    elapsed = time.perf_counter() - start
    # Controlled retrieval probe: two reports of one event, not replication.
    with tempfile.TemporaryDirectory() as temp:
        db = Path(temp) / 'simulation.sqlite'
        first = t.make_record(cases[0]['card'], 'synthetic-T1', 'fixture-reviewer-A', candidate_id='fixture-existing-candidate')
        duplicate = next(c for c in cases if c['id'] == 'duplicate_source_report')
        second = t.make_record(duplicate['card'], 'synthetic-T2', 'fixture-reviewer-B', candidate_id='fixture-second-report')
        t.append_record(db, first)
        t.append_record(db, second)
        index = t.build_index(t.read_records(db))
    hashes = {name: hashlib.sha256((ROOT / name).read_bytes()).hexdigest()
              for name in ['tcgl_offline.py', 'test_tcgl_offline.py', 'fixtures.json', 'example_card.json', 'CONTRACT.md', 'evaluate.py']}
    receipt = {
        'mode': 'simulation', 'generated_at': datetime.now(timezone.utc).isoformat(),
        'python': platform.python_version(), 'input_sha256': hashes,
        'tests_run': result.testsRun, 'tests_successful': result.wasSuccessful(),
        'test_log': log.getvalue(), 'fixture_checks': checks,
        'structural_fixture_check_seconds': elapsed,
        'retrieval_probe': {'records': index['records_count'], 'unique_source_events': len(index['source_events']),
                            'E-1_reports': len(index['source_events']['E-1']['record_ids']),
                            'unresolved_links': index['unresolved_related_candidates']},
        'limits': ['Synthetic software checks only; no live maturity or authority changes.',
                   'Semantic labels were authored by the parent reviewer, not independently measured predictions.',
                   'Runtime is one local measurement, not human recording burden or comparative model cost.',
                   'No reference resolution, authenticated identity, budget enforcement, or tamperproof storage.']}
    print(json.dumps(receipt, indent=2))
    return 0 if result.wasSuccessful() and all(c['matches_expected'] for c in checks) else 1


if __name__ == '__main__':
    raise SystemExit(main())
