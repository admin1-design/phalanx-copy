# PHALANX — COPY DECK (Single Source of Truth) v2.0

> **What this file is:** the authoritative record of what the app says and why — what it currently is, what it's becoming, and every change between. Lives in the repo root. Companion to the visual Screen Change Board.
>
> **Edit protocol (binding on all parties — founder, Kimi, GPT-5.6 agents):**
> 1. Agents implement strings from this deck **exactly**. No interpretation, no "improved" wording in code.
> 2. Proposed changes go in the screen's `LOG` as a proposal — they are not live until marked `APPROVED` by the founder.
> 3. Every edit appends a `LOG` line: date · who · what · why.
> 4. Each string is flagged `[OTA]` (changeable without a new binary) or `[BIN]` (requires submission).
> 5. Copy rules below govern every string. A string that violates them is a defect, whoever wrote it.
> 6. **Flag rule (founder catch, 2026-07-22):** anything a NEW user can see in their first session (S01–S09 + paywall) is BIN by definition — first launch always runs bundled code; OTA lands on the second launch. OTA is for returning-user surfaces only (S10+).
>
> **Sync protocol (shared-home architecture — v1.5, 2026-07-22):**
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
- **Target:** clean dark, ONE thematic beat (static frame or muted loop only — never a blocking video), promise-first. Arc: *arrives guarded/ashamed → job: safety + recognition → leaves "this is private and understands me."*
- **Copy:**
  - eyebrow: `Hold the line.` [BIN]
  - headline: `Build tonight's plan.` [BIN]
  - sub: `Get one clear move when the urge hits.` [BIN]
  - CTA: `Build my plan` [BIN]
  - footer: `Private. On your device. No feed, no community.` [BIN]
- **LOG:** 2026-07-22 · Kimi · created (arc spec §1) · APPROVED
- **LOG:** 2026-07-22 · founder decision · opening legionary video cut as a gate; wall-builder animation cut mid-flow · APPROVED
- **LOG:** 2026-07-22 · GPT-5.6 · S01 implemented locally at app commit `a18c13f`; automated QA passed; physical QA pending · IMPLEMENTED LOCAL

### S02 · Weak window — `TARGET`
- **Arc:** *arrives willing/wary → job: effortless first disclosure + first moment of being seen → leaves "it knows my pattern."*
- **Copy:**
  - headline: `When is your weak window?` [BIN]
  - options: `Late night` · `After work` · `Early morning` · `Weekends` · `It varies` [BIN]
  - on-select micro-copy: `That's the most common one. We plan around it.` [BIN]
- **LOG:** 2026-07-22 · Kimi · created · APPROVED
- **LOG:** 2026-07-22 · GPT-5.6 · S02 implemented locally at app commit `a18c13f`; physical QA pending · IMPLEMENTED LOCAL

### S03 · Access (merged: device + route + location) — `TARGET`
- **Arc:** *job: map the loop without confession — clinical distance lowers shame.*
- **Copy:**
  - headline: `Where does it usually happen?` [BIN]
  - groups: device (`Phone` / `Computer` / `Tablet`) → route (`Social media` / `Search` / `Direct` / `Messaging`) → place (`Bedroom` / `Bathroom` / `Home office` / `Other`) [BIN]
  - footer: `Three taps. No essays.` [BIN]
- **LOG:** 2026-07-22 · Kimi · created · APPROVED
- **LOG:** 2026-07-22 · GPT-5.6 · S03 implemented locally at app commit `a18c13f`; physical QA pending · IMPLEMENTED LOCAL

### S04 · Triggers (max 2) — `TARGET`
- **Arc:** *job: first insight — it's not about porn, it's about the feeling underneath.*
- **Copy:**
  - headline: `What is it usually covering for?` [BIN]
  - chips: `Stress` `Tired` `Alone` `Bored` `Anxious` `Can't sleep` `Other` [BIN]
  - post-select: `Most men pick two. The plan covers both.` [BIN]
- **LOG:** 2026-07-22 · Kimi · created · APPROVED
- **LOG:** 2026-07-22 · GPT-5.6 · S04 implemented locally at app commit `a18c13f`; physical QA pending · IMPLEMENTED LOCAL

### S05 · What you're protecting — `TARGET`
- **Arc:** *job: emotional peak — pivot from problem to stakes. Selection feeds plan reveal + Fortify anchors verbatim.*
- **Copy:**
  - headline: `What are you holding the line for?` [BIN]
  - taps: `My relationship` `My energy` `My self-respect` `My faith` `My future` [BIN]
  - optional custom field label: `In your own words (optional)` [BIN]
- **LOG:** 2026-07-22 · Kimi · created · APPROVED
- **LOG:** 2026-07-22 · GPT-5.6 · S05 implemented locally at app commit `a18c13f`; downstream propagation tests passed; physical QA pending · IMPLEMENTED LOCAL

### S06 · Choose first move — `TARGET`
- **Arc:** *job: agency — he chooses; self-endorsed actions survive.*
- **Copy:**
  - headline: `Your first move tonight:` [BIN]
  - 3 tailored options (generated from S02–S04), e.g.: `Phone charges in the kitchen` · `Instagram off the phone after 10` · `Laptop stays out of the bedroom` [BIN]
  - edit link: `Adjust this` (optional) [BIN]
- **LOG:** 2026-07-22 · Kimi · created · APPROVED
- **LOG:** 2026-07-22 · GPT-5.6 · S06 implemented locally at app commit `a18c13f`; exact-label propagation tests passed; physical QA pending · IMPLEMENTED LOCAL

### S07 · The Rehearsal — `NEW BUILD`
- **Arc:** *arrives doubting willpower → job: self-efficacy — manufacture one completed action → leaves "tonight is not the first time."*
- **Copy:**
  - headline: `Let's practice Fortify.` [BIN]
  - sub: `This is the drill you'll use when an urge hits — so tonight isn't the first time.` [BIN]
  - body (his data injected): `It's [weak window]. The loop starts. Your move:` [BIN]
  - order card: `[his first move, exact S06 string]` [BIN]
  - instruction: `For practice: one slow breath. Hold here ten seconds.` [BIN]
  - countdown: 10-second ring; CTA remains disabled until zero. [BIN]
  - CTA: `I did it` [BIN]
  - payoff: `That's one. It counts.` [BIN]
- **Events (not copy, recorded here for completeness):** rehearsal_rendered → initiated → confirmed → elapsed → abandoned. [BIN]
- **LOG:** 2026-07-22 · Kimi · created · APPROVED
- **LOG:** 2026-07-22 · GPT-5.6 · S07 implemented locally at app commit `a18c13f`; separated event lifecycle tests passed; device readback pending · IMPLEMENTED LOCAL
- **LOG:** 2026-07-22 · founder directive · Fortify defined on first contact; ten-second breath hold and countdown made mandatory; payoff remains post-tap only · APPROVED
- **LOG:** 2026-07-22 · GPT-5.6 · mandatory hold implemented at app commit `67e765f`; S07 focused tests 16/16 and TypeScript passed · IMPLEMENTED LOCAL

### S08 · Plan reveal — `TARGET`
- **Arc:** *job: proof of competence — the plan quotes HIM.*
- **Copy:**
  - headline: `Your 30-day plan is ready.` [BIN]
  - summary: `Built from your answers: [weak window] · [trigger 1 + 2] · protecting [S05 selection].` [BIN]
  - visual: weak-window map + projected milestone dates (Day 7 / 14 / 30) [BIN]
  - insight line (best of cut briefings): `Urges peak and pass in about 90 seconds. Your plan is built for those 90 seconds.` [BIN]
  - CTA: `See it tonight` [BIN]
- **LOG:** 2026-07-22 · Kimi · created · APPROVED
- **LOG:** 2026-07-22 · GPT-5.6 · S08 implemented locally at app commit `a18c13f`; computed-summary and milestone tests passed; physical QA pending · IMPLEMENTED LOCAL

### S09 · Paywall — `TARGET` (full detail in PAYWALL section below)

### S10 · First-paid loop — `TARGET`
- **Arc:** *arrives post-purchase vulnerable → job: money becomes tonight's concrete plan in <60s → leaves "tonight is handled."*
- **Copy:**
  - screen 1: `Tonight's order:` `[his first move]` · CTA `Confirm` [BIN]
  - screen 2: `Reminder set for [weak window − 20 min].` · CTA `Arm it` / `Not now` [BIN]
  - screen 3: `If pressure rises, this is Fortify.` (one screenshot, no tutorial) · CTA `Got it` [BIN]
  - escape (all screens): `Set up later` [BIN]
- **LOG:** 2026-07-22 · Kimi · created · APPROVED
- **LOG:** 2026-07-22 · GPT-5.6 · S10 implemented locally at app commit `aeb0452`; three-screen sequence and canonical-reminder tests passed; physical QA pending · IMPLEMENTED LOCAL

### S11 · Fortify — acute path — `TARGET`
- **Arc:** *arrives fight-or-flight → job: one instruction, zero decisions → leaves agency.*
- **Copy:**
  - order card (large type, above fold): `[generated order — must pass natural-language tests]` [OTA]
  - buttons: `Done` · `Need more help` · `I already slipped` [OTA]
  - escalation sequence (in order): close app → physical distance → visible place → real person → anchor → Counsel [OTA]
  - win confirmation: `Recorded. That's how it's done.` [OTA]
- **LOG:** 2026-07-22 · Kimi · created · APPROVED
- **LOG:** 2026-07-22 · GPT-5.6 · S11 implemented locally at app commit `aeb0452`; acute hierarchy and escalation-order tests passed; physical QA pending · IMPLEMENTED LOCAL

### S12 · Post-slip — `TARGET`
- **Arc:** *arrives in shame spiral → job: shame interruption before anything → leaves self-respect + one action.*
- **Copy:**
  - first screen (nothing else): `Close everything. Put the phone away. This can stop here.` [OTA]
  - after confirm: `Log it as a reset — a record, not a verdict.` [OTA]
  - streak line: `A slip resets your current streak. Earned rank remains.` [OTA]
  - next step: `One adjustment for next time:` [trigger-based suggestion] [OTA]
- **LOG:** 2026-07-22 · Kimi · created · APPROVED
- **LOG:** 2026-07-22 · GPT-5.6 · S12 implemented locally at app commit `aeb0452`; stabilization-before-logging tests passed; physical QA pending · IMPLEMENTED LOCAL

### S13 · 24-hour commitment (replaces "Slide to lock shields") — `TARGET`
- **Copy:**
  - title: `Start 24-hour commitment` [OTA]
  - vow: `For the next 24 hours, I will use my plan before the loop takes over. If I slip, I will return immediately.` [OTA]
  - CTA: `Commit` [OTA]
- **LOG:** 2026-07-22 · GPT-5.6 wording, Kimi adopted · APPROVED
- **LOG:** 2026-07-22 · GPT-5.6 · S13 implemented locally at app commit `0a56f46`; blocker-like slider and rejected rotating vows removed; automated QA passed; physical QA pending · IMPLEMENTED LOCAL

## APP-WIDE CORRECTNESS LABELS

- Command lifetime counter: `LIFETIME CLEAN DAYS` [OTA]
- Progress counters: `Current Streak` · `Best Streak` [OTA]
- Progress rank explainer: `Rank holds your highest clean-time milestone. DP is earned by completing drills, orders, field notes, and reset reports.` [OTA]
- Arsenal rank explainer: `Rank preserves the highest clean-time milestone you have earned.` [OTA]
- Logic contract: displayed rank = higher of current and historically earned rank; a slip resets the current streak, not earned rank.
- Generated-order contract: known place/device combinations must use natural grammar (for example, `on the computer in the bedroom`), never label concatenation such as `at Bedroom on the computer`.
- **LOG:** 2026-07-22 · GPT-5.6 · Top-30 items 20–24 implemented locally at app commit `0a56f46`; exhaustive grammar and monotonic-progress tests passed; Dynamic Type/smallest-iPhone physical QA pending · IMPLEMENTED LOCAL

---

## PAYWALL (S09 — full detail)

- **Structure:** plan summary (quotes user's S02/S04/S05 data) → Annual → Quarterly → Monthly → Lifetime → trial terms → CTA.
- **Copy:**
  - headline: `Your 30-day plan is waiting.` [BIN]
  - sub: `Start tonight — Fortify included from minute one.` [BIN]
  - Annual card: `Annual — $69.99/year` · badge `BEST VALUE` · per-month note `$5.83/mo` [BIN]
  - Quarterly: `$29.99 / 3 months` [BIN] · Monthly: `$14.99 / month` [BIN]
  - Lifetime: `$149.99 once.` · note: `For men tired of subscriptions.` [BIN]
  - trial line: `3-day free trial, then [plan price]. Cancel anytime in Settings.` [BIN]
  - CTA: `Start my plan` [BIN]
  - footer: `Restore purchase` · `Terms` · `Privacy` [BIN]
  - **BANNED on this screen:** testimonials (until verified), outcome stats, countdown timers, fake discounts.
- **LOG:** 2026-07-22 · Kimi · created · APPROVED
- **LOG:** 2026-07-22 · GPT-5.6 · S09 implemented locally at app commit `a18c13f`; StoreKit fail-closed and trial-eligibility tests passed; physical purchase QA pending · IMPLEMENTED LOCAL

---

## STORE LISTING (lives here too — one source)

- Subtitle: `Quit porn: 30-day plan` · Keyword field: `nofap,porn addiction,reboot,dopamine detox,self control,streak,semen retention,recovery,urge`
- Description: per `PHALANX-store-conversion-package.md` §4 (AI-privacy line only if payload fix shipped)
- Screenshot headlines: `HOLD THE LINE` / `THE MOMENT IT STARTS` / `ONE ORDER A DAY` / `A SLIP DOESN'T ERASE YOU` / `NO FEED. NO COMMUNITY. NO SHAME.`
- Preview video script (15–30s): weak-window card → Fortify opens → one order → "Done" → "Recorded." Captions carry it; no voiceover needed.
- **Screenshot generation prompts (founder runs these in ChatGPT; phone screen left blank → real app screen composited in afterward, then exported at 1290×2796):**
  - Shot 1 (composite: plan-reveal screen): `iOS App Store screenshot background, tall portrait. Solid near-black charcoal background (#0E0F12) with a very subtle vertical gradient. Top: bold condensed uppercase headline "HOLD THE LINE" in off-white, centered. Below it, one small sentence-case subhead in muted gray: "A 30-day system to quit porn and stay in control." Below the text, one short thin gold accent line, centered. Lower two-thirds: a single modern dark iPhone frame, perfectly centered, screen area completely blank dark gray (#111318) — leave it empty, no UI. Nothing else: no people, no Roman or ancient imagery, no textures, no extra text, no logos, no watermark. Minimal, premium, high contrast.`
  - Shot 2 (composite: Fortify order screen): `Same layout and style as shot 1 — near-black charcoal background, bold condensed off-white uppercase headline "THE MOMENT IT STARTS", small gray subhead "One clear move when the urge hits.", thin gold accent line, one centered dark iPhone frame with a blank dark screen. No other elements, no people, no extra text.`
  - Shot 3 (composite: Command home / today's order): `Same layout and style — headline "ONE ORDER A DAY", subhead "One clear action each day.", gold accent line, centered dark iPhone frame, blank dark screen. Near-black background, minimal, premium. No people, no extra text.`
  - Shot 4 (composite: post-slip screen): `Same layout and style — headline "A SLIP DOESN'T ERASE YOU", subhead "Get back to the line without losing your progress.", gold accent line, centered dark iPhone frame, blank dark screen. Near-black background, minimal. No people, no extra text.`
  - Shot 5 (composite: plan or privacy screen): `Same layout and style — headline "NO FEED. NO COMMUNITY. NO SHAME.", subhead "Private. On your device.", gold accent line, centered dark iPhone frame, blank dark screen. Near-black background, minimal. No people, no extra text.`
  - Rule for all 5: generate portrait (2:3 is fine); the blank phone screen gets the REAL app screenshot dropped in during compositing; background extends to 1290×2796 at export.
- **Current live screenshots (10)** — archived on the Visual Copy Deck (store section). Reshoot notes — founder calls, none blocking [BIN]:
  - Shot 4 carries the `C. Skeggs, 32` testimonial. Authenticity unknown. Only revenue relevance: tiny App Review risk vs one screenshot swap. **Founder decision — default: KEEP. Not raised again.**
  - Shot 5 leads with Mirror Mode selfie. Conversion question only (distinctive visual vs privacy-first message). **Founder decision — default: KEEP.**
  - All 10 use full Roman legion backgrounds — theme reduction decided (clean-dark); reshoot per `PHALANX-store-conversion-package.md`.
- **LOG:** 2026-07-22 · Kimi · created · APPROVED
- **LOG:** 2026-07-22 · Kimi · current 10 live screenshots archived to deck · APPROVED
- **LOG:** 2026-07-22 · Kimi · per founder directive: testimonial + Mirror Mode downgraded from defects to founder calls, default KEEP — revenue-first, not raised again · APPROVED
- **LOG:** 2026-07-22 · founder decision · Item 25 reference composite approved as the final layout specification; final assets wait for five physical Build 75 captures at the QA gate; no further screenshot work before then · APPROVED
- **LOG:** 2026-07-22 · GPT-5.6 · Item 26 physical-capture/edit specification prepared; final App Preview MP4 waits for fresh Build 75 device footage and remains a PPO challenger, not an assumed conversion win · PREPARED
- **LOG:** 2026-07-22 · GPT-5.6 · Item 27 metadata entry package prepared verbatim from the deck/store package; Build 75 asset optimization committed at `3c3efe9`; final local iOS export measured 60.97 MiB; signed-IPA size proof remains pending · IMPLEMENTED LOCAL

---

## NOTIFICATIONS

- Weak-window (T-20): `Your weak window starts soon. Tonight's order: [order].` [BIN]
- Discreet Mode variant: `Reminder: tonight's plan.` [BIN]
- Morning (opt-in): `Today's order is set. [order]` [BIN]
- No shame, no streak-guilt, no "you failed to open" copy, ever.
- **LOG:** 2026-07-22 · Kimi · created · APPROVED
- **LOG:** 2026-07-22 · GPT-5.6 · canonical T-20 normal and Discreet Mode reminders implemented locally at app commit `aeb0452`; timing and rollover tests passed; device delivery QA pending · IMPLEMENTED LOCAL

---

## TIER 6 MARKETING COPY CANDIDATES

**Status:** `PROPOSED` — locally prepared for review. None of this copy is founder-approved, live, posted, scheduled, uploaded, or running. The local asset package remains outside this public copy repository.

### Paid social — privacy / no community

- `A01` — headline: `QUIT PORN. PRIVATELY.` · subhead: `A 30-day plan. No feed. No community.` · CTA: `SEE THE PLAN`
- `A02` — headline: `NO PUBLIC STREAK.` · subhead: `Private progress. One clear next action.` · CTA: `BUILD TONIGHT'S PLAN`
- `A03` — headline: `RECOVERY IS NOT CONTENT.` · subhead: `No posting. No audience. Just a plan.` · CTA: `GET PHALANX`

### Paid social — rehearsal / tonight plan

- `B01` — headline: `PLAN FOR TONIGHT.` · subhead: `Choose one move before the weak window starts.` · CTA: `BUILD THE PLAN`
- `B02` — headline: `PRACTICE THE FIRST MOVE.` · subhead: `One rehearsal now. One clear action later.` · CTA: `SEE HOW IT WORKS`
- `B03` — headline: `ONE ORDER A DAY.` · subhead: `A concrete action built around the risky hour.` · CTA: `START THE 30-DAY PLAN`

### Paid social — slip recovery

- `C01` — headline: `A SLIP DOESN'T ERASE PROGRESS.` · subhead: `Close everything. Reset. Keep moving.` · CTA: `RETURN TO THE PLAN`
- `C02` — headline: `STOP THE SECOND HIT.` · subhead: `One slip does not have to become a lost night.` · CTA: `SEE THE RESET`
- `C03` — headline: `RESET. DON'T START OVER.` · subhead: `Record what happened. Adjust the next move.` · CTA: `KEEP MOVING`

### Seven-day faceless organic queue

- `D01` — `POV: IT'S 11:47 PM.` → `THE LOOP USUALLY STARTS BEFORE THE SEARCH.` → `MOVE THE PHONE. LEAVE THE ROOM.` → `BUILD TONIGHT'S PLAN. PHALANX`
- `D02` — `DON'T WAIT FOR WILLPOWER.` → `CHOOSE ONE MOVE BEFORE THE WEAK WINDOW.` → `PRACTICE IT ONCE.` → `USE IT TONIGHT. PHALANX`
- `D03` — `WHEN THE URGE HITS.` → `GIVE YOURSELF ONE PHYSICAL ORDER.` → `DO IT BEFORE THE DEBATE.` → `FORTIFY. PHALANX`
- `D04` — `A SLIP ISN'T THE WHOLE NIGHT.` → `CLOSE EVERYTHING.` → `PUT THE PHONE AWAY.` → `RETURN TO COMMAND. PHALANX`
- `D05` — `CLEAN TIME ISN'T THE ONLY PROOF.` → `ORDERS COMPLETED.` → `RESCUES AND RESETS.` → `PROGRESS YOU CAN ACT ON. PHALANX`
- `D06` — `NO FEED.` → `NO COMMUNITY.` → `NO PUBLIC STREAK.` → `PRIVATE BY DESIGN. PHALANX`
- `D07` — `BEFORE: RESIST AT MIDNIGHT.` → `AFTER: PHONE CHARGES OUTSIDE THE BEDROOM.` → `ONE DECISION MADE EARLY.` → `ONE LESS BATTLE AT MIDNIGHT. PHALANX`

- **LOG:** 2026-07-22 · GPT-5.6 · nine static paid candidates and seven faceless vertical MP4s prepared locally; technical media QA passed; review and all external use pending · PROPOSED
- **LOG:** 2026-07-22 · GPT-5.6 · exact activation composite wired locally at app commit `1f565cc`: rehearsal confirmed → durable order saved → native reminder armed; shared `1.3.11 / top30_v1` tags; no weak-window text, chosen action, or exact reminder time in the two new events; 136/136 suites and 841/841 tests passed; physical event readback pending · IMPLEMENTED LOCAL

---

## CHANGE LOG (global)

- 2026-07-22 · Kimi · v1.0 created: 13 screen entries + paywall + store + notifications; emotional arc integrated per screen; copy rules codified.
- 2026-07-22 · Kimi · v1.1: added sync protocol after GPT-5.6 architecture check — confirmed Kimi has file-transfer access only (no direct repo read/write); repo copy is truth; board formally demoted to visual review layer.
- 2026-07-22 · Kimi · v1.2: 10 current live App Store screenshots archived into the deck (founder-supplied).
- 2026-07-22 · Kimi · v1.3: founder directive — revenue-first. Testimonial + Mirror Mode flags downgraded from defects to founder calls, default KEEP; compliance-style flags not raised again unprompted.
- 2026-07-22 · GPT-5.6 · connected
- 2026-07-22 · founder decision · v1.5: S01 opening legionary video cut as a gate; wall-builder animation cut mid-flow; one thematic beat limited to a static frame or muted loop · APPROVED
- 2026-07-22 · Kimi · v1.6: added 5 screenshot generation prompts to STORE LISTING (founder runs in ChatGPT; blank phone → real screens composited) · APPROVED
- 2026-07-22 · founder catch · v1.7: S01–S09 + paywall reclassified OTA→BIN — first session always runs bundled code; OTA applies from second launch, so onboarding copy can never reach new users via OTA. Flag rule added to edit protocol. No change to current sprint (all onboarding ships in this binary anyway).
- 2026-07-22 · GPT-5.6 · S01–S09 local implementation recorded at app commit `a18c13f`; 132/132 suites and 821/821 tests passed; physical QA remains pending.
- 2026-07-22 · GPT-5.6 · S10–S12, canonical T-20 reminders, and Mirror-default-OFF local implementation recorded at app commit `aeb0452`; 133/133 suites and 828/828 tests passed; physical QA remains pending.
- 2026-07-22 · GPT-5.6 · S13 and Top-30 correctness sweep recorded at app commit `0a56f46`; 134/134 suites and 835/835 tests passed; physical overflow QA remains pending.
- 2026-07-22 · GPT-5.6 · Top-30 Tier 5 local package: founder-approved clean-dark Item 25 layout frozen pending five physical captures; App Preview capture/edit spec prepared; exact metadata package prepared; Build 75 asset pass committed at `3c3efe9`; 135/135 suites and 837/837 tests passed; final local iOS export 60.97 MiB; signed IPA and physical media remain gated.
- 2026-07-22 · GPT-5.6 · v1.8: added Tier 6 paid and organic copy candidates as `PROPOSED`; nine static ads and seven vertical MP4s prepared locally; nothing approved, published, launched, or spent.
- 2026-07-22 · GPT-5.6 · v1.9: recorded the completed three-part activation measurement spine at app commit `1f565cc`; automated QA passed; device/PostHog readback remains a hard gate before spend.
- 2026-07-22 · founder directive · v2.0: S07 made unskippable with exact breath instruction, ten-second countdown ring, disabled CTA until zero, and payoff only after the enabled tap · APPROVED.
