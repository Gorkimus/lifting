Build v4.2 of the tracker in C:\Users\pablo\Projects\Lifting\index.html (single file, no dependencies, as before), then test in the browser, commit, and push to GitHub Pages (live on refresh).

## Scope (per your selection — plate math excluded)

### 1. Exercise progress view + PR detection
- New helpers: `e1RM(weight, reps)` = weight × (1 + min(reps,15)/30); `progressData(exId)` = chronological per-session best score + best set label; `stallInfo(exId)` (see #4).
- History tab, when filtering by a specific exercise: header block above the existing set list showing — best-ever set, current est. 1RM vs ~5 weeks ago (+/- %), stall status line, and an SVG sparkline (last 12 sessions, dark-theme blue line, first/last values labeled). Hand-rolled SVG, no chart library.
- PR detection: when logging a set that beats the best prior est. 1RM for that exercise, the set is stored with `pr: true`, you get a "🏆 PR" toast immediately, the set row in the session card shows 🏆, and PRs appear in the finish recap.

### 2. One-tap progression
- Refactor `suggestion()` to return text + an optional concrete weight. When the "top of range" condition is met, the log card shows an "Apply 47.5 lb" button that pre-sets the draft weight (for pull-ups/dips: "Apply +2.5 lb vest"). Capped-DB and carries cases stay text-only, as they have no single number to apply.

### 3. Backup reminder + finish recap
- `exportData()` records `lastExportAt` in settings. If ≥20 sets stored and no export in 30+ days (or never exported), History shows a dismissible banner ("Last backup 34 days ago — Export JSON now"); dismissing re-prompts after another 30 days.
- Fix a real latent bug while touching settings: `readSettingsForm` currently rebuilds the settings object from scratch, so saving LLM settings would erase `lastExportAt`/dismissal flags — switch to merging into the stored settings.
- `finishSession()` now renders a recap card instead of just a toast: duration, sets logged, exercises completed, PRs hit this session, any lifts currently flagged as stalled, and a "Next up: Day X" line with a start shortcut.

### 4. Stall detection
- Score per session per exercise: est. 1RM of the best working set (rep lifts); added-weight progression for bodyweight lifts when no added weight has ever been logged (so pull-ups progress via reps, not fake 0-kg stalls); weight × distance for carries; excluded for "done"-type recovery work.
- Rule: with at least 6 sessions of history, compare the best score across the last 3 sessions vs the prior 3 sessions (~5 weeks per lift on the 6-day cycle). Flat: current ≤ prior. Regressing: current < 95% of prior. Otherwise progressing, with % shown.
- Surfaced three places: the progress view status line; an amber suggestion in the log card when you open a stalled exercise ("Flat ~5 wks at 47.5×8 — rotate overload method (vest/tempo/partials) or take a lighter week"); and the finish recap.

## Also
- Version bump to v4.2 everywhere (title, header chip, footer, About), README updated.
- Everything stays in the PROGRAM/storage patterns already in the file; no schema migration needed (`pr` is a new optional field on sets; settings gains optional timestamps).

## Verification
- node syntax check on the extracted script.
- Browser tests on localhost: seed fabricated multi-session history via localStorage to force each stall state (progressing / flat / regressing / too-few), verify sparkline, status lines, PR toast + flag, Apply button prefill, recap card contents, and the backup banner (fresh, old, dismissed). Wipe test data afterward.
- Commit and push; poll the live URL until v4.2 is served (same as v4.1 rollout).

## Deferred (not now)
Plate math (you deselected it — trivial to add later), offline/service-worker mode, weekly volume dashboards (want 4+ weeks of real data first).