# PHALANX Top-30 Tier 6 - Restart Protocol and Read Contract

**Status:** PREPARED - NO SPEND OR PLATFORM MUTATION AUTHORIZED.

## Command decision

**TEST FIRST.** Restart with one controlled US paid cohort only after the new binary, App Store listing, Item 25 assets, and physical QA gates are complete. Do not scale from clicks, one good day, or blended historical totals.

## Pre-spend release gates

All must be green before a paid restart:

1. New onboarding and paywall binary shipped to the intended App Store version.
2. Five founder-approved Item 25 composites made from fresh physical-device captures and live on the product page.
3. StoreKit trial start, purchase, restore, and entitlement behavior pass on a physical device.
4. Full fresh-install journey passes twice, including the smallest supported iPhone.
5. `prepaywall_rehearsal_confirmed`, `activation_order_saved`, and `activation_reminder_armed` are observed on-device at their actual moments.
6. AppsFlyer -> first open -> RevenueCat customer chain is joined for a real post-activation user without duplicate initial revenue.
7. Advertising remains off until Jesse explicitly authorizes spend.

## Canonical source ownership

| Question | Source of truth | Rule |
|---|---|---|
| Product-page views and App Store downloads | App Store Connect | Use Apple's official store metrics; respect reporting delay. |
| Paid source, campaign, ad, and attributed first open | AppsFlyer | `Organic` means unattributed, not proven organic. |
| Onboarding and in-product behavior | PostHog | Filter to the new release/cohort and exclude founder/App Review/QA traffic. |
| Trial, subscription, proceeds, renewals, refunds, entitlement | RevenueCat | Financial truth; annual and monthly reported separately. |
| Meta delivery and spend | Meta API/CLI only | Browser access is absolutely prohibited. |
| Apple Search Ads delivery and spend | Apple Ads API/CLI/report | Do not merge with Meta rows before source-level economics are calculated. |

## New-cohort identity

- Onboarding activation events carry `release = 1.3.11` and `cohort = top30_v1` in current source.
- Paid acquisition reporting must also pin exact binary identity: app version, Apple build number, EAS build ID, and frozen git commit.
- Use absolute timestamps and state the timezone; operating reports use Asia/Bangkok with UTC retained in raw exports.
- Exclude Jesse's Thailand/Bangkok test traffic, Apple Review launches, TestFlight, simulators, and known internal devices from commercial denominators.

## Product event contract

### Acquisition and onboarding spine

1. `app_first_open`
2. `onboarding_start`
3. `onboarding_screen_viewed`
4. `danger_window_selected`
5. `replacement_move_selected`
6. `activation_plan_viewed` / `custom_plan_revealed`
7. `prepaywall_rehearsal_rendered`
8. `prepaywall_rehearsal_initiated`
9. `prepaywall_rehearsal_confirmed` or `prepaywall_rehearsal_abandoned`
10. `prepaywall_rehearsal_elapsed`
11. `onboarding_complete`
12. `paywall_viewed`

### Commerce and first-paid spine

1. `purchase_started`
2. `trial_started` or `purchase_completed`
3. `first_paid_session_started`
4. `activation_order_saved` - emitted only after durable local order persistence succeeds.
5. `activation_reminder_armed` - emitted only after native weak-window scheduling succeeds.
6. `first_paid_setup_started`
7. `first_paid_fortify_started`
8. `first_rescue_loop_completed`

### Ongoing usefulness spine

- `fortify_started`
- `fortify_completed`
- `fortify_proof_logged`
- `fortify_still_at_risk`
- `post_slip_reset_started`
- `reset_recovery_completed`
- `daily_task_completed`

### Activation composite

The Top-30 source now makes the stated activation definition observable in PostHog:

1. `prepaywall_rehearsal_confirmed`;
2. `activation_order_saved`;
3. `activation_reminder_armed`.

All three carry `release = 1.3.11` and `cohort = top30_v1`. The two first-paid events contain only structural properties (`source`, `step`, campaign day or reminder kind, release, and cohort). They do not send the user's weak-window text, selected action, or exact reminder time.

Count activation only when one unique user records all three events in that order. Automated source tests prove call placement; physical-device PostHog readback remains a hard release gate.

## Denominators and formulas

| Metric | Numerator | Denominator |
|---|---|---|
| Store CVR | App Store downloads | App Store product-page views |
| Click-to-install | Attributed first opens | Valid outbound App Store clicks |
| Onboarding completion | `onboarding_complete` unique users | `onboarding_start` unique users |
| Rehearsal completion | `prepaywall_rehearsal_confirmed` unique users | `prepaywall_rehearsal_rendered` unique users |
| Activation | Unique users with rehearsal confirmed + order saved + reminder armed, in order | New-cohort installs |
| Paywall-to-trial | RevenueCat trials attributed to the cohort | `paywall_viewed` unique eligible users |
| Install-to-paid | New paying RevenueCat customers | New-cohort installs |
| CAC | Source spend | New paying customers attributed to that source |
| Cumulative contribution | Net proceeds minus ad spend | Absolute currency amount, not a percentage |
| Annual share | New annual customers | All new recurring paid customers |

Do not mix trials with paying customers. Do not divide paid spend by paid plus unattributed installs. Do not treat gross revenue as net proceeds. Do not use single-day revenue to declare profitability.

## Minimum readable sample

- At least 100 new-cohort installs before judging install-to-paid.
- At least 100-200 App Store product-page views before judging store CVR.
- At least 10 new paying customers before a commercial verdict.
- Report annual, quarterly, monthly, and lifetime separately; do not let upfront annual cash hide weak monthly retention.

## Authorized restart shape - only after approval

- Meta: one US ad set at US$15-25/day.
- Round 1: one representative from each of the three prepared angles, not all nine variants.
- Apple Search Ads: NoFap-family expansion remains a separate source row and requires explicit authorization.
- No simultaneous audience, listing, onboarding, price, and creative changes after the read begins.

## Daily command table

| Field | Report |
|---|---|
| Data freshness | Last complete date/time per source |
| Spend | Meta and Apple Ads separately |
| Store | Product-page views, downloads, Store CVR |
| Acquisition | Attributed first opens by source/campaign/creative |
| Activation | Rehearsal render/initiate/confirm/abandon, paywall views, first-paid proxy |
| Commerce | Trials, new paid, plan mix, proceeds, refunds |
| Economics | CPI, CAC, cumulative contribution |
| Integrity | Missing joins, duplicate events, QA contamination, delayed sources |
| Decision | HOLD / CONTINUE / PAUSE / SCALE with evidence |

## Day-14 decision

### Continue at maintenance

Continue if the measurement chain is intact and the cohort has not yet crossed all minimum samples. Do not force a verdict from underpowered data.

### Scale

Scale only when the founder's commercial threshold is met: install-to-paid at least 10%, annual share at least 50%, and cumulative contribution supports expansion. Scale in a controlled step; do not multiply budget overnight.

### Pause and repair

Pause if purchase/restore breaks, attribution cannot join, revenue duplicates, App Store conversion materially worsens after a readable sample, refund behavior spikes, or the cohort clears the minimum sample while economics remain below the threshold.

## Stop line

This document authorizes no EAS build, OTA, App Store change, website deployment, email, post, Meta/Apple Ads mutation, or spend.
