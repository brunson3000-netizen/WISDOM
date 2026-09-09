#!/usr/bin/env python3
"""Small offline simulation recorder for Theory -> Provisional research."""
import argparse, copy, json, os, sqlite3, sys, uuid
from datetime import datetime, timezone, timedelta
from pathlib import Path

_CARD_KEYS = {"idea","task_anchor","inquiry","expected_effects","evidence","scope","related_candidates","proposed_disposition"}
_EFFECT_KEYS = {"benefit","adverse"}
_EVIDENCE_KEYS = {"supporting","against","absence","uncertainty","source_event_ids"}
_SCOPE_KEYS = {"applies_to","limits","grant_ref"}
_TOP_KEYS = {"schema_version","mode","record_id","candidate_id","revision","parent_record_id","change_reason","task_id","reporter","created_at","card"}
_DISPOSITIONS = {"investigate","retain_theory","link_existing","defer"}


def _nonempty(x): return isinstance(x, str) and bool(x.strip())
def _list_strings(x): return isinstance(x, list) and all(_nonempty(v) for v in x)
def _distinct(xs): return len(xs) == len(set(xs)) if isinstance(xs, list) else False

def validate_card(card):
    """Return structural errors; never raise for arbitrary input."""
    e=[]
    if not isinstance(card, dict): return ["card must be an object"]
    extra=set(card)-_CARD_KEYS; missing=_CARD_KEYS-set(card)
    if extra: e.append("card has extra keys: "+", ".join(sorted(extra)))
    if missing: e.append("card missing keys: "+", ".join(sorted(missing)))
    for k in ("idea","task_anchor","inquiry"):
        if k in card and not _nonempty(card[k]): e.append(f"{k} must be a nonempty string")
    x=card.get("expected_effects")
    if not isinstance(x,dict): e.append("expected_effects must be an object")
    else:
        if set(x)-_EFFECT_KEYS: e.append("expected_effects has extra keys")
        if _EFFECT_KEYS-set(x): e.append("expected_effects missing keys")
        for k in _EFFECT_KEYS:
            if k in x and not _nonempty(x[k]): e.append(f"expected_effects.{k} must be nonempty")
    x=card.get("evidence")
    if not isinstance(x,dict): e.append("evidence must be an object")
    else:
        if set(x)-_EVIDENCE_KEYS: e.append("evidence has extra keys")
        if _EVIDENCE_KEYS-set(x): e.append("evidence missing keys")
        for k in ("supporting","against"):
            if k in x and not _list_strings(x[k]): e.append(f"evidence.{k} must be a list of nonempty strings")
        if "absence" in x and x["absence"] is not None and not isinstance(x["absence"],str): e.append("evidence.absence must be a string or null")
        if "supporting" in x and isinstance(x["supporting"],list) and not x["supporting"] and not _nonempty(x.get("absence")): e.append("evidence.absence required when supporting is empty")
        if "uncertainty" in x and not _nonempty(x["uncertainty"]): e.append("evidence.uncertainty must be nonempty")
        if "source_event_ids" in x:
            if not _list_strings(x["source_event_ids"]): e.append("evidence.source_event_ids must be a list of nonempty strings")
            elif not _distinct(x["source_event_ids"]): e.append("evidence.source_event_ids must be distinct")
    x=card.get("scope")
    if not isinstance(x,dict): e.append("scope must be an object")
    else:
        if set(x)-_SCOPE_KEYS: e.append("scope has extra keys")
        if _SCOPE_KEYS-set(x): e.append("scope missing keys")
        for k in _SCOPE_KEYS:
            if k in x and not _nonempty(x[k]): e.append(f"scope.{k} must be nonempty")
    x=card.get("related_candidates")
    if not _list_strings(x): e.append("related_candidates must be a list of nonempty strings")
    elif not _distinct(x): e.append("related_candidates must be distinct")
    if not isinstance(card.get("proposed_disposition"), str) or card["proposed_disposition"] not in _DISPOSITIONS: e.append("proposed_disposition invalid")
    if card.get("proposed_disposition")=="link_existing" and not card.get("related_candidates"): e.append("link_existing requires related_candidates")
    return e


def _utc(): return datetime.now(timezone.utc).isoformat().replace("+00:00","Z")
def _uuid(): return str(uuid.uuid4())

def make_record(card, task_id, reporter, candidate_id=None, revision=1, parent_record_id=None, change_reason=None):
    errors=validate_card(card)
    if errors: raise ValueError("invalid card: " + "; ".join(errors))
    if not _nonempty(task_id) or not _nonempty(reporter): raise ValueError("task_id and reporter must be nonempty strings")
    if candidate_id is not None and not _nonempty(candidate_id): raise ValueError("candidate_id must be nonempty when supplied")
    if isinstance(revision,bool) or not isinstance(revision,int) or revision<1: raise ValueError("revision must be a positive integer")
    if revision==1 and (parent_record_id is not None or change_reason is not None): raise ValueError("revision 1 requires null parent_record_id and change_reason")
    if revision>1 and (not _nonempty(parent_record_id) or not _nonempty(change_reason)): raise ValueError("later revisions require parent_record_id and change_reason")
    return {"schema_version":1,"mode":"simulation","record_id":_uuid(),"candidate_id":candidate_id if candidate_id is not None else _uuid(),"revision":revision,"parent_record_id":parent_record_id,"change_reason":change_reason,"task_id":task_id,"reporter":reporter,"created_at":_utc(),"card":copy.deepcopy(card)}

def _record_errors(r):
    e=[]
    if not isinstance(r,dict): return ["record must be an object"]
    if set(r)!=_TOP_KEYS: e.append("record keys do not exactly match contract")
    if type(r.get("schema_version")) is not int or r["schema_version"]!=1: e.append("schema_version must be integer 1")
    if r.get("mode")!="simulation": e.append("mode must be simulation")
    for k in ("record_id","candidate_id","task_id","reporter","created_at"):
        if not _nonempty(r.get(k)): e.append(f"{k} must be nonempty")
    try:
        stamp = datetime.fromisoformat(r.get("created_at", "").replace("Z", "+00:00"))
        if stamp.utcoffset() != timedelta(0): raise ValueError("UTC required")
    except (AttributeError, TypeError, ValueError):
        e.append("created_at must be a UTC ISO timestamp")
    rev=r.get("revision")
    if isinstance(rev,bool) or not isinstance(rev,int) or rev<1: e.append("revision must be positive integer")
    if rev==1 and (r.get("parent_record_id") is not None or r.get("change_reason") is not None): e.append("revision 1 parent/reason must be null")
    if isinstance(rev,int) and rev>1 and (not _nonempty(r.get("parent_record_id")) or not _nonempty(r.get("change_reason"))): e.append("later revision parent/reason required")
    e.extend("card: "+x for x in validate_card(r.get("card")))
    return e

def _connect(path):
    db=sqlite3.connect(path)
    db.row_factory=sqlite3.Row
    return db

def append_record(db_path, record):
    e=_record_errors(record)
    if e: raise ValueError("invalid record: "+"; ".join(e))
    db=_connect(db_path)
    try:
        db.execute("BEGIN IMMEDIATE")
        tables = {row[0] for row in db.execute("SELECT name FROM sqlite_master WHERE type='table'")}
        if not tables:
            db.execute("CREATE TABLE records (record_id TEXT UNIQUE NOT NULL, candidate_id TEXT NOT NULL, revision INTEGER NOT NULL, task_id TEXT NOT NULL, scope TEXT NOT NULL, payload TEXT NOT NULL, created_order INTEGER PRIMARY KEY AUTOINCREMENT, UNIQUE(candidate_id, revision))")
        elif tables != {"records", "sqlite_sequence"}:
            raise ValueError("store does not match offline recorder schema")
        _read_from_db(db)  # Validate history before extending it, inside this transaction.
        if db.execute("SELECT 1 FROM records WHERE record_id=?",(record["record_id"],)).fetchone(): raise ValueError("record_id already exists")
        row=db.execute("SELECT record_id,revision,task_id,scope FROM records WHERE candidate_id=? ORDER BY revision DESC LIMIT 1",(record["candidate_id"],)).fetchone()
        if row is None:
            if record["revision"]!=1: raise ValueError("first revision must be 1")
        else:
            if record["revision"]!=row["revision"]+1: raise ValueError("revision must be exactly current+1")
            if record["parent_record_id"]!=row["record_id"]: raise ValueError("parent_record_id does not match current head")
            if record["task_id"]!=row["task_id"] or json.dumps(record["card"]["scope"],sort_keys=True,separators=(",",":"))!=row["scope"]: raise ValueError("task_id and scope cannot change in revision chain")
        db.execute("INSERT INTO records(record_id,candidate_id,revision,task_id,scope,payload) VALUES(?,?,?,?,?,?)",(record["record_id"],record["candidate_id"],record["revision"],record["task_id"],json.dumps(record["card"]["scope"],sort_keys=True,separators=(",",":")),json.dumps(record,ensure_ascii=False,separators=(",",":"))))
        db.commit(); return {"record_id":record["record_id"],"candidate_id":record["candidate_id"],"revision":record["revision"],"mode":"simulation"}
    except Exception:
        db.rollback(); raise
    finally: db.close()

def read_records(db_path):
    db=sqlite3.connect(Path(db_path).resolve().as_uri()+"?mode=ro", uri=True)
    db.row_factory=sqlite3.Row
    try:
        return _read_from_db(db)
    finally: db.close()

def _read_from_db(db):
    rows=db.execute("SELECT * FROM records ORDER BY created_order").fetchall()
    out=[]
    for row in rows:
        try: r=json.loads(row["payload"], object_pairs_hook=_no_dupes, parse_constant=_bad_constant)
        except (TypeError, ValueError) as ex: raise ValueError("corrupt record JSON") from ex
        e=_record_errors(r)
        if e: raise ValueError("corrupt stored record: "+"; ".join(e))
        for key in ("record_id", "candidate_id", "revision", "task_id"):
            if row[key] != r[key]: raise ValueError("stored columns disagree with record payload")
        if row["scope"] != json.dumps(r["card"]["scope"], sort_keys=True, separators=(",", ":")):
            raise ValueError("stored scope disagrees with record payload")
        out.append(r)
    _check_histories(out)
    return out

def _check_histories(records):
    groups={}
    for r in records:
        errors = _record_errors(r)
        if errors: raise ValueError("invalid history record: "+"; ".join(errors))
        groups.setdefault(r["candidate_id"],[]).append(r)
    ids=set()
    for cid,rs in groups.items():
        rs.sort(key=lambda x:x["revision"])
        for r in rs:
            if r["record_id"] in ids: raise ValueError("duplicate record identity")
            ids.add(r["record_id"])
        for i,r in enumerate(rs,1):
            if r["revision"]!=i: raise ValueError("inconsistent revision history")
            if i==1 and (r["parent_record_id"] is not None): raise ValueError("invalid first parent")
            if i>1 and r["parent_record_id"]!=rs[i-2]["record_id"]: raise ValueError("broken parent chain")
        if len({(r["task_id"],json.dumps(r["card"]["scope"],sort_keys=True)) for r in rs})>1: raise ValueError("scope/task changed in history")

def build_index(records):
    _check_histories(records)
    latest={}
    events={}
    for r in records:
        cid=r["candidate_id"]
        if cid not in latest or r["revision"] > latest[cid]["revision"]: latest[cid]=r
        for ev in r["card"]["evidence"]["source_event_ids"]:
            events.setdefault(ev,{"record_ids":[],"candidate_ids":[]})
            if r["record_id"] not in events[ev]["record_ids"]: events[ev]["record_ids"].append(r["record_id"])
            if cid not in events[ev]["candidate_ids"]: events[ev]["candidate_ids"].append(cid)
    related=set()
    for r in records:
        for x in r["card"]["related_candidates"]:
            if x not in latest: related.add(x)
    return {"records_count":len(records),"candidates":{cid:{"latest_record_id":r["record_id"],"revision":r["revision"],"idea":r["card"]["idea"],"proposed_disposition":r["card"]["proposed_disposition"]} for cid,r in latest.items()},"source_events":events,"unresolved_related_candidates":sorted(related),"semantic_judgment":"not_evaluated","authority":"not_checked","mode":"simulation"}

def _bad_constant(value): raise ValueError("non-finite JSON number: "+value)
def _load_json(path):
    with open(path,encoding="utf-8") as f: return json.load(f,parse_constant=_bad_constant, object_pairs_hook=_no_dupes)
def _no_dupes(pairs):
    d={}
    for k,v in pairs:
        if k in d: raise ValueError("duplicate JSON key: "+k)
        d[k]=v
    return d

def main(argv=None):
    class Parser(argparse.ArgumentParser):
        def error(self, message): raise ValueError(message)
    ap=Parser(); sub=ap.add_subparsers(dest="cmd",required=True)
    c=sub.add_parser("check"); c.add_argument("card")
    r=sub.add_parser("record"); r.add_argument("card"); r.add_argument("--store",required=True); r.add_argument("--task",required=True); r.add_argument("--reporter",required=True); r.add_argument("--candidate"); r.add_argument("--expected-revision",type=int,default=0); r.add_argument("--reason")
    i=sub.add_parser("index"); i.add_argument("--store",required=True)
    try:
        a=ap.parse_args(argv)
        if a.cmd=="check":
            card=_load_json(a.card); errs=validate_card(card); print(json.dumps({"valid":not errs,"errors":errs,"semantic_judgment":"not_evaluated","authority":"not_checked","mode":"simulation"},separators=(",",":"))); return 0 if not errs else 1
        if a.cmd=="index": print(json.dumps(build_index(read_records(a.store)),ensure_ascii=False,separators=(",",":"))); return 0
        if a.expected_revision < 0: raise ValueError("expected revision must be nonnegative")
        if a.expected_revision and not a.candidate: raise ValueError("expected revision requires candidate")
        card=_load_json(a.card); current=read_records(a.store) if os.path.exists(a.store) else []
        heads={r["candidate_id"]:r for r in current}; old=heads.get(a.candidate)
        if (old["revision"] if old else 0)!=a.expected_revision: raise ValueError("expected revision conflict")
        if old is None and a.reason is not None: raise ValueError("first revision cannot have amendment reason")
        cid=a.candidate or _uuid(); rev=(old["revision"]+1 if old else 1)
        rec=make_record(card,a.task,a.reporter,cid,rev,old["record_id"] if old else None,a.reason if old else None)
        print(json.dumps(append_record(a.store,rec),separators=(",",":"))); return 0
    except Exception as ex:
        print(json.dumps({"error":str(ex),"mode":"simulation"},separators=(",",":")),file=sys.stderr); return 1
if __name__=="__main__": sys.exit(main())
