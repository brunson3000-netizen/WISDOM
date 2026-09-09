"""Independent contract tests. Fixtures are synthetic, never live promotions."""
import copy
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
import sqlite3
from concurrent.futures import ThreadPoolExecutor

import tcgl_offline as t

ROOT = Path(__file__).resolve().parent
FIXTURES = json.loads((ROOT / 'fixtures.json').read_text())['cases']
BASE = json.loads((ROOT / 'example_card.json').read_text())


class OfflineContract(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.db = Path(self.temp.name) / 'records.sqlite'

    def record(self, **kwargs):
        return t.make_record(copy.deepcopy(BASE), 'T-1', 'reviewer', **kwargs)

    def cli(self, *args):
        return subprocess.run([sys.executable, str(ROOT / 'tcgl_offline.py'), *map(str, args)], cwd=self.temp.name, capture_output=True, text=True)

    def test_complete_synthetic_fixture_matrix(self):
        for case in FIXTURES:
            with self.subTest(case=case['id']):
                errors = t.validate_card(case['card'])
                self.assertEqual(not errors, case['expected_structural_validity'])

    def test_arbitrary_json_types_fail_without_crashing(self):
        for value in [None, True, 5, 'text', [], {'idea': []}]:
            with self.subTest(value=value):
                self.assertTrue(t.validate_card(value))
        for key in BASE:
            card = copy.deepcopy(BASE)
            card[key] = None
            self.assertTrue(t.validate_card(card), key)
        for value in [[], {}, 1, True]:
            card = copy.deepcopy(BASE)
            card['proposed_disposition'] = value
            self.assertTrue(t.validate_card(card))

    def test_invalid_records_cannot_create_a_store(self):
        for field, value in [('mode', 'live'), ('revision', True), ('schema_version', True), ('schema_version', 1.0), ('created_at', 'yesterday'), ('created_at', '2026-09-09'), ('record_id', '')]:
            record = self.record()
            record[field] = value
            with self.subTest(field=field):
                with self.assertRaises((ValueError, TypeError)):
                    t.append_record(self.db, record)
                self.assertFalse(self.db.exists())
        record = self.record()
        record['activate'] = True
        with self.assertRaises((ValueError, TypeError)):
            t.append_record(self.db, record)
        self.assertFalse(self.db.exists())

    def test_history_preserved_and_same_timestamp_allowed(self):
        first = self.record(candidate_id='candidate-1')
        t.append_record(self.db, first)
        second = self.record(candidate_id='candidate-1', revision=2, parent_record_id=first['record_id'], change_reason='Add counterevidence')
        second['created_at'] = first['created_at']
        second['card']['evidence']['against'] = ['fixture:new-conflict']
        t.append_record(self.db, second)
        self.assertEqual(t.read_records(self.db), [first, second])

    def test_duplicate_identity_and_revision_cannot_overwrite(self):
        first = self.record(candidate_id='candidate-1')
        t.append_record(self.db, first)
        for record in [first, self.record(candidate_id='candidate-1')]:
            with self.assertRaises(Exception):
                t.append_record(self.db, record)
            self.assertEqual(t.read_records(self.db), [first])

    def test_revision_gap_parent_and_scope_errors_preserve_history(self):
        first = self.record(candidate_id='candidate-1')
        t.append_record(self.db, first)
        revisions = [
            self.record(candidate_id='candidate-1', revision=3, parent_record_id=first['record_id'], change_reason='Skip'),
            self.record(candidate_id='candidate-1', revision=2, parent_record_id='wrong', change_reason='Wrong parent'),
        ]
        altered_scope = self.record(candidate_id='candidate-1', revision=2, parent_record_id=first['record_id'], change_reason='Expand')
        altered_scope['card']['scope']['applies_to'] = 'Whole organization'
        revisions.append(altered_scope)
        altered_task = copy.deepcopy(altered_scope)
        altered_task['card']['scope'] = copy.deepcopy(first['card']['scope'])
        altered_task['task_id'] = 'another-task'
        revisions.append(altered_task)
        for record in revisions:
            with self.assertRaises(Exception):
                t.append_record(self.db, record)
            self.assertEqual(t.read_records(self.db), [first])

    def test_competing_appends_have_one_winner(self):
        first = self.record(candidate_id='candidate-1')
        t.append_record(self.db, first)
        competitors = [self.record(candidate_id='candidate-1', revision=2, parent_record_id=first['record_id'], change_reason='Concurrent evidence') for _ in range(2)]
        def attempt(record):
            try:
                t.append_record(self.db, record)
                return True
            except Exception:
                return False
        with ThreadPoolExecutor(max_workers=2) as pool:
            self.assertEqual(sum(pool.map(attempt, competitors)), 1)
        records = t.read_records(self.db)
        self.assertEqual(len(records), 2)
        self.assertEqual(records[0], first)

    def test_read_and_index_do_not_change_store_bytes(self):
        t.append_record(self.db, self.record())
        before = hashlib.sha256(self.db.read_bytes()).hexdigest()
        index = t.build_index(t.read_records(self.db))
        self.assertEqual(index['semantic_judgment'], 'not_evaluated')
        self.assertEqual(index['authority'], 'not_checked')
        self.assertEqual(index['mode'], 'simulation')
        self.assertEqual(hashlib.sha256(self.db.read_bytes()).hexdigest(), before)

    def test_missing_and_corrupt_stores_do_not_become_empty_success(self):
        with self.assertRaises(Exception):
            t.read_records(self.db)
        self.assertFalse(self.db.exists())
        self.db.write_bytes(b'not a sqlite database')
        before = self.db.read_bytes()
        with self.assertRaises(Exception):
            t.read_records(self.db)
        self.assertEqual(self.db.read_bytes(), before)

    def test_shared_events_and_unresolved_links_are_visible(self):
        first = self.record(candidate_id='candidate-1')
        first['card']['related_candidates'] = ['missing-candidate']
        second = self.record(candidate_id='candidate-2')
        t.append_record(self.db, first)
        t.append_record(self.db, second)
        index = t.build_index(t.read_records(self.db))
        self.assertEqual(index['records_count'], 2)
        self.assertEqual(len(index['source_events']), 1)
        self.assertEqual(set(index['source_events']['E-1']['candidate_ids']), {'candidate-1', 'candidate-2'})
        self.assertEqual(len(index['source_events']['E-1']['record_ids']), 2)
        self.assertIn('missing-candidate', index['unresolved_related_candidates'])

    def test_hostile_evidence_is_preserved_as_data(self):
        card = next(x['card'] for x in FIXTURES if x['id'] == 'instruction_in_source')
        record = t.make_record(card, 'T-1', 'reviewer')
        t.append_record(self.db, record)
        self.assertEqual(t.read_records(self.db)[0]['card'], card)
        self.assertEqual(sorted(p.name for p in Path(self.temp.name).iterdir()), ['records.sqlite'])

    def test_valid_cli_card_is_not_semantic_or_authority_approval(self):
        card = next(x['card'] for x in FIXTURES if x['id'] == 'fluent_but_ungrounded')
        file = Path(self.temp.name) / 'card.json'
        file.write_text(json.dumps(card))
        result = self.cli('check', file)
        self.assertEqual(result.returncode, 0, result.stderr + result.stdout)
        output = json.loads(result.stdout)
        self.assertTrue(output['valid'])
        self.assertEqual(output['semantic_judgment'], 'not_evaluated')
        self.assertEqual(output['authority'], 'not_checked')
        self.assertFalse(self.db.exists())

    def test_malformed_cli_inputs_and_missing_store(self):
        file = Path(self.temp.name) / 'bad.json'
        for content in ['{', '{"idea":"a","idea":"b"}', 'NaN', 'Infinity']:
            file.write_text(content)
            result = self.cli('check', file)
            self.assertNotEqual(result.returncode, 0)
            self.assertIsInstance(json.loads(result.stdout or result.stderr), dict)
        result = self.cli('index', '--store', self.db)
        self.assertNotEqual(result.returncode, 0)
        self.assertIsInstance(json.loads(result.stdout or result.stderr), dict)
        self.assertFalse(self.db.exists())

    def test_cli_roundtrip_and_stale_expected_revision(self):
        args = ['record', ROOT / 'example_card.json', '--store', self.db, '--task', 'T-1', '--reporter', 'reviewer', '--candidate', 'candidate-1']
        first = self.cli(*args)
        self.assertEqual(first.returncode, 0, first.stdout + first.stderr)
        stale = self.cli(*args)
        self.assertNotEqual(stale.returncode, 0)
        revised = self.cli(*args, '--expected-revision', '1', '--reason', 'New evidence')
        self.assertEqual(revised.returncode, 0, revised.stdout + revised.stderr)
        self.assertEqual(len(t.read_records(self.db)), 2)
        indexed = self.cli('index', '--store', self.db)
        self.assertEqual(indexed.returncode, 0, indexed.stdout + indexed.stderr)
        self.assertEqual(json.loads(indexed.stdout)['records_count'], 2)

    def test_new_candidate_cannot_ignore_expected_revision(self):
        args = ['record', ROOT / 'example_card.json', '--store', self.db, '--task', 'T-1', '--reporter', 'reviewer', '--candidate', 'absent']
        for expected in ['-1', '5']:
            result = self.cli(*args, '--expected-revision', expected)
            self.assertNotEqual(result.returncode, 0)
            self.assertFalse(self.db.exists())

    def test_stored_column_corruption_blocks_read_and_append(self):
        first = self.record(candidate_id='candidate-1')
        t.append_record(self.db, first)
        with sqlite3.connect(self.db) as db:
            db.execute('UPDATE records SET task_id=?', ('tampered',))
        before = self.db.read_bytes()
        with self.assertRaises(ValueError):
            t.read_records(self.db)
        with self.assertRaises(ValueError):
            t.append_record(self.db, self.record(candidate_id='candidate-2'))
        self.assertEqual(self.db.read_bytes(), before)

    def test_unrelated_database_is_not_modified(self):
        with sqlite3.connect(self.db) as db:
            db.execute('CREATE TABLE unrelated (value TEXT)')
        before = self.db.read_bytes()
        with self.assertRaises(ValueError):
            t.append_record(self.db, self.record())
        self.assertEqual(self.db.read_bytes(), before)

    def test_index_selects_highest_revision_not_input_order(self):
        first = self.record(candidate_id='candidate-1')
        second = self.record(candidate_id='candidate-1', revision=2, parent_record_id=first['record_id'], change_reason='New evidence')
        self.assertEqual(t.build_index([second, first])['candidates']['candidate-1']['revision'], 2)


if __name__ == '__main__':
    unittest.main(verbosity=2)
