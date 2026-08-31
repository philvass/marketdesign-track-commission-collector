# MarketDesign.ai TRACK V20.3 — ACER automation

This package automates the frozen V20.1 ACER acquisition behavior against the frozen V20.2 TRACK milestone-policy backend.

## Production behavior

- GitHub Actions checks ACER every 6 hours at minute 17.
- The scheduled job only runs when repository variable `TRACK_AUTOMATION_ENABLED` equals `true`.
- The collector persists its SQLite deduplication state through a GitHub Actions cache.
- Each successful run saves a new state cache key; the next run restores the most recent matching cache.
- New or changed ACER decisions are posted to TRACK; unchanged decisions are skipped.
- `concurrency` prevents overlapping collector runs.
- A JSON run report is retained as a GitHub Actions artifact for 14 days.
- Secrets are never written to the SQLite state or cache.

## Safe first activation

1. Put this package in a GitHub repository.
2. Leave `TRACK_AUTOMATION_ENABLED` unset/false. Scheduled jobs will be skipped.
3. Run **Actions → MarketDesign.ai ACER monitor → Run workflow** with `mode=bootstrap`, `limit=25`.
   This records the current catalogue as the baseline and sends nothing to TRACK.
4. Run the workflow manually once with `mode=submit`. Expected: existing baseline documents are duplicates and nothing is submitted.
5. Set repository variable `TRACK_AUTOMATION_ENABLED=true`.
6. The 6-hour schedule is now live.

Do not bootstrap after production monitoring is live: bootstrap intentionally marks currently discovered documents as already handled.

## Optional configuration

Repository variable:
- `TRACK_INGEST_URL` — optional. If blank, `collector.py` uses the existing MarketDesign.ai TRACK endpoint.
- `TRACK_AUTOMATION_ENABLED` — must be exactly `true` for scheduled runs.

Repository secret:
- `TRACK_INGEST_TOKEN` — optional today; use it if/when TRACK ingestion is protected by bearer authentication.

## Local commands

Dry run:

```bash
python3 collector.py --dry-run --limit 25 --json
```

One-time baseline bootstrap:

```bash
python3 collector.py --bootstrap-state --limit 25 --json
```

Production submit:

```bash
python3 collector.py --submit --limit 25 --json
```
