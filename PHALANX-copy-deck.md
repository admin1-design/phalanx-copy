# PHALANX — COPY DECK (Single Source of Truth) v1.4

> **What this file is:** the authoritative record of what the app says and why — what it currently is, what it's becoming, and every change between. Lives in the repo root. Companion to the visual Screen Change Board.
>
> **Edit protocol (binding on all parties — founder, Kimi, GPT-5.6 agents):**
> 1. Agents implement strings from this deck **exactly**. No interpretation, no "improved" wording in code.
> 2. Proposed changes go in the screen's `LOG` as a proposal — they are not live until marked `APPROVED` by the founder.
> 3. Every edit appends a `LOG` line: date · who · what · why.
> 4. Each string is flagged `[OTA]` (changeable without a new binary) or `[BIN]` (requires submission).
> 5. Copy rules below govern every string. A string that violates them is a defect, whoever wrote it.
>
> **Sync protocol (shared-home architecture — v1.4, 2026-07-22):**
> - This file lives in the founder's **public GitHub repo `phalanx-copy`** (deck only — no code, no finances). **The GitHub copy is the truth.**
> - **GPT-5.6 agents** read it and push edits/proposals directly (rules 1–5). Founder involvement: zero.
> - **Founder** views the Visual Copy Deck page (auto-syncs from GitHub on every open — no refresh requests, ever) and can edit this file on github.com (pencil icon → Commit). Approvals are given to GPT-5.6 in its own chat.
> - **Kimi** reads the GitHub copy anytime; reviews on request.
> - **Conflict rule:** latest commit on GitHub wins; the loser re-proposes in `LOG`.

---

## COPY RULES (global)

- **Claims safety:** literal feature language only. No outcome statistics, no efficacy promises, no testimonials unless verified-real (gate: original message + exact quote + written permission + date). "Quit porn" as category descriptor is allowed.
- **Shame audit:** no perfectionist vows, no failure displays, no uninvited camera, no "enemy" framing of the user, every lapse-adjacent screen leads with stabilization.
- **One decision per screen. Zero required typing.**
- **Recognition before information:** no lectures; the product quotes the user's own answers back.
- **Identity before metrics:** completed actions are named back as identity ("That's one. It counts.").
- **Terminology map (canonical):** repair screen = "Recover After a Slip" · repair message = "Stop the Second Hit" · repair CTA = "Return to Command" · report = "Campaign Report" · blocker-sounding gestures banned ("lock shields") · "clinical" never user-visible.
- **Privacy honesty:** no copy may claim data behavior the code doesn't perform. (Currently binding: analytics-disabled claim must match reality; Centurion context description must name exact fields.)

---

## SCREEN ENTRIES — THE NEW FLOW

### S01 · Welcome — `TARGET`
- **Current:** legion art, "WELCOME TO THE FORMATION / BEGIN TRAINING."
- **Target:** clean dark, one thematic beat, promise-first. Arc: *arrives guarded/ashamed → job: safety + recognition → leaves "this is private and understands me."*
- **Copy:**
  - eyebrow: `Hold the line.` [BIN]
  - headline: `Build tonight's plan.` [BIN]
  - sub: `Get one clear move when the urge hits.` [BIN]
  - CTA: `Build my plan` [BIN]
  - footer: `Private. On your device. No feed, no community.` [BIN]
- **LOG:** 2026-07-22 · Kimi · created (arc spec §1) · APPROVED

### S02 · Weak window — `TARGET`
- **Arc:** *arrives willing/wary → job: effortless first disclosure + first moment of being seen → leaves "it knows my pattern."*
- **Copy:**
  - headline: `When is your weak window?` [OTA]
  - options: `Late night` · `After work` · `Early morning` · `Weekends` · `It varies` [OTA]
  - on-select micro-copy: `That's the most common one. We plan around it.` [OTA]
- **LOG:** 2026-07-22 · Kimi · created · APPROVED

### S03 · Access (merged: device + route + location) — `TARGET`
- **Arc:** *job: map the loop without confession — clinical distance lowers shame.*
- **Copy:**
  - headline: `Where does it usually happen?` [OTA]
  - groups: device (`Phone` / `Computer` / `Tablet`) → route (`Social media` / `Search` / `Direct` / `Messaging`) → place (`Bedroom` / `Bathroom` / `Home office` / `Other`) [OTA]
  - footer: `Three taps. No essays.` [OTA]
- **LOG:** 2026-07-22 · Kimi · created · APPROVED

### S04 · Triggers (max 2) — `TARGET`
- **Arc:** *job: first insight — it's not about porn, it's about the feeling underneath.*
- **Copy:**
  - headline: `What is it usually covering for?` [OTA]
  - chips: `Stress` `Tired` `Alone` `Bored` `Anxious` `Can't sleep` `Other` [OTA]
  - post-select: `Most men pick two. The plan covers both.` [OTA]
- **LOG:** 2026-07-22 · Kimi · created · APPROVED

### S05 · What you're protecting — `TARGET`
- **Arc:** *job: emotional peak — pivot from problem to stakes. Selection feeds plan reveal + Fortify anchors verbatim.*
- **Copy:**
  - headline: `What are you holding the line for?` [OTA]
  - taps: `My relationship` `My energy` `My self-respect` `My faith` `My future` [OTA]
  - optional custom field label: `In your own words (optional)` [OTA]
- **LOG:** 2026-07-22 · Kimi · created · APPROVED

### S06 · Choose first move — `TARGET`
- **Arc:** *job: agency — he chooses; self-endorsed actions survive.*
- **Copy:**
  - headline: `Your first move tonight:` [OTA]
  - 3 tailored options (generated from S02–S04), e.g.: `Phone charges in the kitchen` · `Instagram off the phone after 10` · `Laptop stays out of the bedroom` [OTA]
  - edit link: `Adjust this` (optional) [OTA]
- **LOG:** 2026-07-22 · Kimi · created · APPROVED

### S07 · The Rehearsal — `NEW BUILD`
- **Arc:** *arrives doubting willpower → job: self-efficacy — manufacture one completed action → leaves "tonight is not the first time."*
- **Copy:**
  - headline: `Let's practice — so tonight isn't the first time.` [BIN]
  - body (his data injected): `It's [weak window]. The loop starts. Your move:` [BIN]
  - order card: `[his first move, exact S06 string]` [BIN]
  - CTA: `I did it` [BIN]
  - payoff: `That's one. It counts.` [BIN]
- **Events (not copy, recorded here for completeness):** rehearsal_rendered → initiated → confirmed → elapsed → abandoned. [BIN]
- **LOG:** 2026-07-22 · Kimi · created · APPROVED

### S08 · Plan reveal — `TARGET`
- **Arc:** *job: proof of competence — the plan quotes HIM.*
- **Copy:**
  - headline: `Your 30-day plan is ready.` [OTA]
  - summary: `Built from your answers: [weak window] · [trigger 1 + 2] · protecting [S05 selection].` [OTA]
  - visual: weak-window map + projected milestone dates (Day 7 / 14 / 30) [BIN]
  - insight line (best of cut briefings): `Urges peak and pass in about 90 seconds. Your plan is built for those 90 seconds.` [OTA]
  - CTA: `See it tonight` [OTA]
- **LOG:** 2026-07-22 · Kimi · created · APPROVED

### S09 · Paywall — `TARGET` (full detail in PAYWALL section below)

### S10 · First-paid loop — `TARGET`
- **Arc:** *arrives post-purchase vulnerable → job: money becomes tonight's concrete plan in <60s → leaves "tonight is handled."*
- **Copy:**
  - screen 1: `Tonight's order:` `[his first move]` · CTA `Confirm` [BIN]
  - screen 2: `Reminder set for [weak window − 20 min].` · CTA `Arm it` / `Not now` [BIN]
  - screen 3: `If pressure rises, this is Fortify.` (one screenshot, no tutorial) · CTA `Got it` [BIN]
  - escape (all screens): `Set up later` [BIN]
- **LOG:** 2026-07-22 · Kimi · created · APPROVED

### S11 · Fortify — acute path — `TARGET`
- **Arc:** *arrives fight-or-flight → job: one instruction, zero decisions → leaves agency.*
- **Copy:**
  - order card (large type, above fold): `[generated order — must pass natural-language tests]` [OTA]
  - buttons: `Done` · `Need more help` · `I already slipped` [OTA]
  - escalation sequence (in order): close app → physical distance → visible place → real person → anchor → Counsel [OTA]
  - win confirmation: `Recorded. That's how it's done.` [OTA]
- **LOG:** 2026-07-22 · Kimi · created · APPROVED

### S12 · Post-slip — `TARGET`
- **Arc:** *arrives in shame spiral → job: shame interruption before anything → leaves self-respect + one action.*
- **Copy:**
  - first screen (nothing else): `Close everything. Put the phone away. This can stop here.` [OTA]
  - after confirm: `Log it as a reset — a record, not a verdict.` [OTA]
  - streak line: `A slip resets your current streak. Earned rank remains.` [OTA]
  - next step: `One adjustment for next time:` [trigger-based suggestion] [OTA]
- **LOG:** 2026-07-22 · Kimi · created · APPROVED

### S13 · 24-hour commitment (replaces "Slide to lock shields") — `TARGET`
- **Copy:**
  - title: `Start 24-hour commitment` [OTA]
  - vow: `For the next 24 hours, I will use my plan before the loop takes over. If I slip, I will return immediately.` [OTA]
  - CTA: `Commit` [OTA]
- **LOG:** 2026-07-22 · GPT-5.6 wording, Kimi adopted · APPROVED

---

## PAYWALL (S09 — full detail)

- **Structure:** plan summary (quotes user's S02/S04/S05 data) → Annual → Quarterly → Monthly → Lifetime → trial terms → CTA.
- **Copy:**
  - headline: `Your 30-day plan is waiting.` [OTA]
  - sub: `Start tonight — Fortify included from minute one.` [OTA]
  - Annual card: `Annual — $69.99/year` · badge `BEST VALUE` · per-month note `$5.83/mo` [BIN]
  - Quarterly: `$29.99 / 3 months` [BIN] · Monthly: `$14.99 / month` [BIN]
  - Lifetime: `$149.99 once.` · note: `For men tired of subscriptions.` [BIN]
  - trial line: `3-day free trial, then [plan price]. Cancel anytime in Settings.` [BIN]
  - CTA: `Start my plan` [BIN]
  - footer: `Restore purchase` · `Terms` · `Privacy` [BIN]
  - **BANNED on this screen:** testimonials (until verified), outcome stats, countdown timers, fake discounts.
- **LOG:** 2026-07-22 · Kimi · created · APPROVED

---

## STORE LISTING (lives here too — one source)

- Subtitle: `Quit porn: 30-day plan` · Keyword field: `nofap,porn addiction,reboot,dopamine detox,self control,streak,semen retention,recovery,urge`
- Description: per `PHALANX-store-conversion-package.md` §4 (AI-privacy line only if payload fix shipped)
- Screenshot headlines: `HOLD THE LINE` / `THE MOMENT IT STARTS` / `ONE ORDER A DAY` / `A SLIP DOESN'T ERASE YOU` / `NO FEED. NO COMMUNITY. NO SHAME.`
- Preview video script (15–30s): weak-window card → Fortify opens → one order → "Done" → "Recorded." Captions carry it; no voiceover needed.
- **Current live screenshots (10)** — archived on the Visual Copy Deck (store section). Reshoot notes — founder calls, none blocking [BIN]:
  - Shot 4 carries the `C. Skeggs, 32` testimonial. Authenticity unknown. Only revenue relevance: tiny App Review risk vs one screenshot swap. **Founder decision — default: KEEP. Not raised again.**
  - Shot 5 leads with Mirror Mode selfie. Conversion question only (distinctive visual vs privacy-first message). **Founder decision — default: KEEP.**
  - All 10 use full Roman legion backgrounds — theme reduction decided (clean-dark); reshoot per `PHALANX-store-conversion-package.md`.
- **LOG:** 2026-07-22 · Kimi · created · APPROVED
- **LOG:** 2026-07-22 · Kimi · current 10 live screenshots archived to deck · APPROVED
- **LOG:** 2026-07-22 · Kimi · per founder directive: testimonial + Mirror Mode downgraded from defects to founder calls, default KEEP — revenue-first, not raised again · APPROVED

---

## NOTIFICATIONS

- Weak-window (T-20): `Your weak window starts soon. Tonight's order: [order].` [BIN]
- Discreet Mode variant: `Reminder: tonight's plan.` [BIN]
- Morning (opt-in): `Today's order is set. [order]` [BIN]
- No shame, no streak-guilt, no "you failed to open" copy, ever.
- **LOG:** 2026-07-22 · Kimi · created · APPROVED

---

## CHANGE LOG (global)

- 2026-07-22 · Kimi · v1.0 created: 13 screen entries + paywall + store + notifications; emotional arc integrated per screen; copy rules codified.
- 2026-07-22 · Kimi · v1.1: added sync protocol after GPT-5.6 architecture check — confirmed Kimi has file-transfer access only (no direct repo read/write); repo copy is truth; board formally demoted to visual review layer.
- 2026-07-22 · Kimi · v1.2: 10 current live App Store screenshots archived into the deck (founder-supplied).
- 2026-07-22 · Kimi · v1.3: founder directive — revenue-first. Testimonial + Mirror Mode flags downgraded from defects to founder calls, default KEEP; compliance-style flags not raised again unprompted.
- 2026-07-22 · GPT-5.6 · connected
