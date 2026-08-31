import tempfile
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from collector import Candidate, init_db, record_seen, mark_bootstrapped, is_unchanged

with tempfile.TemporaryDirectory() as td:
    db = init_db(Path(td) / 'state.sqlite3')
    c = Candidate('acer-decision-11-2026', 'ACER Decision No 11-2026', '2026-07-22', 'https://example.test/11.pdf')
    digest = 'abc123'
    assert not is_unchanged(db, c.source_id, digest)
    record_seen(db, c, digest)
    assert not is_unchanged(db, c.source_id, digest)
    mark_bootstrapped(db, c.source_id)
    assert is_unchanged(db, c.source_id, digest)
print('bootstrap state test: PASS')
