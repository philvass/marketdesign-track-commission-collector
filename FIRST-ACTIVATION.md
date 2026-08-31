# First activation checklist

The workflow is deliberately fail-safe: merging it does **not** start production submission until `TRACK_AUTOMATION_ENABLED=true` exists as a repository variable.

1. Manual workflow: `bootstrap`, limit `25`.
2. Confirm the run report says `mode=BOOTSTRAP` and `submitted=0`.
3. Manual workflow: `submit`, limit `25`.
4. Confirm all baseline documents are `duplicate=true`, `submitted=false`.
5. Add repository variable `TRACK_AUTOMATION_ENABLED` = `true`.
6. Wait for the next 6-hour schedule or manually run `submit` once.

If the state cache is ever lost, disable `TRACK_AUTOMATION_ENABLED` before troubleshooting, then rebuild the baseline intentionally.
