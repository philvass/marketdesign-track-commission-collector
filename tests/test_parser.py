from collector import parse_candidates, source_id_from_title, normalise_date

FIXTURE = """
<html><body>
<div class='card'>
  <div>22.07.2026</div>
  <a href='/files/decision-11.pdf'>ACER Decision No 11-2026 on the methodology for cost sharing</a>
  <a href='/files/annex-11.pdf'>ACER Decision 11-2026 - Methodology - Annex I</a>
</div>
<div class='card'>
  <div>17.07.2026</div>
  <a href='/files/decision-10.pdf'>ACER Decision No 10-2026 on the fourth amendment</a>
</div>
</body></html>
"""


def test_parse_candidates():
    rows = parse_candidates(FIXTURE, 'https://www.acer.europa.eu/documents/search')
    assert len(rows) == 2
    assert rows[0].source_id == 'acer-decision-11-2026'
    assert rows[0].publication_date == '2026-07-22'
    assert rows[0].url == 'https://www.acer.europa.eu/files/decision-11.pdf'
    assert rows[1].source_id == 'acer-decision-10-2026'


def test_helpers():
    assert source_id_from_title('ACER Decision No 09-2026 on x') == 'acer-decision-09-2026'
    assert normalise_date('17.07.2026') == '2026-07-17'
