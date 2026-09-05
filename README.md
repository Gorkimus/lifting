# Hypertrophy & Hinge Re-entry Tracker v4.2

A single-file, build-free workout tracker. Upper/Lower split with antagonist
supersets, designed around spine-sparing (no standing axial loading) on a home
setup: Freak Athlete Hyper Pro, dumbbells to 45 lb, full barbell set, rings,
bands, and a weight vest.

## Using it on your phone

1. Open the GitHub Pages URL in Chrome (published after enabling Pages on this
   repo — see Publishing below).
2. Chrome menu (⋮) → **Add to Home screen** → install. You get an app icon;
   it launches full-screen like an app.
3. All data lives in the browser storage tied to that URL. Updating the code
   (git push) never touches your data.

## Logging flow

- **Session tab** → it knows your next day from the 2-on/1-off rotation
  (D1 → D2 → off → D3 → D4 → off). Override if life happened.
- Tap an exercise → weight is prefilled from last time, big ± steppers,
  set dots show progress. A set is 2–3 taps.
- 🎙 mic on each exercise: speak "45, eight reps, 2 RIR" — parsed and filled
  into the form for review before saving. Uses the phone's built-in speech
  recognition (free). Optionally add an OpenAI-compatible LLM endpoint in
  Settings for smarter parsing; the key is stored on-device only, never in
  the code.
- Progression nudges: hit the top of every rep range → it suggests the next
  jump (+2.5 barbell, +5 DB, vest at the 45 lb DB cap). Missed reps → it says
  hold the weight and skip the finisher.
- Mistakes: every set logged this session appears in the exercise's card with
  **Edit** and **×** controls — Edit loads it back into the form, saving
  updates it in place. Past sessions: tap **edit** on any set line in History
  for an inline number fix.
- Progress: filter History by exercise for a top-set est. 1RM sparkline
  (green dots = PR sessions), best-ever set, and trend. Stall detection
  compares your last 3 sessions of a lift against the prior 3 (~5 weeks):
  flat or regressing lifts get flagged when you open them and in the session
  recap. Top-of-range nudges get an **Apply** button that pre-sets the next
  weight in one tap.
- Bodyweight lifts (pull-ups, dips) use a bodyweight estimate in Settings
  (default 180 lb) for progress math.
- **History tab** → everything grouped by session, filterable, JSON
  export/import for backups. Export regularly.

## Editing the program

Everything (days, exercises, prescriptions, notes, logging types) lives in the
`PROGRAM` block at the top of `index.html`. Logs reference exercises by stable
`id`, so renaming or reordering never orphans history. You can edit this file
on your phone in GitHub's web editor — the change is live after refresh.

## Publishing (GitHub Pages)

    git init -b main
    git add -A
    git commit -m "feat: v4.0 session-first tracker"
    # create the repo on github.com (public), then:
    git remote add origin https://github.com/<you>/lifting.git
    git push -u origin main
    # Repo → Settings → Pages → Deploy from branch → main / (root)

## Files

- `index.html` — the entire app (no build step, no dependencies).
- `manifest.json` + `icons/` — makes it installable as a home-screen app.
- `tools/make_icons.py` — regenerates the icons (stdlib only).
- `legacy/` — the original v3.4 single-file tracker, kept for reference.
