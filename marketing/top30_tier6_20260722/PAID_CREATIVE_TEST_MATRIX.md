# PHALANX Top-30 Tier 6 - Paid Creative Test Matrix

**Status:** PREPARED LOCALLY - HOLD. No campaign, ad, spend, upload, or platform mutation is authorized.

**Standing gate:** Nothing in this package may run until Top-30 items 5-14 and Item 25 have shipped, the physical QA gates have passed, and Jesse explicitly authorizes the restart. PHALANX Meta advertising is API/CLI only. Browser access is prohibited.

## Decision

**TEST FIRST.** Nine assets are ready, but a US$15-25/day restart cannot discriminate among nine simultaneous ads quickly. Start with one representative from each angle. Advance only the winning angle to its two sibling variants. This preserves the requested creative range without fragmenting the first read.

## Asset matrix

| ID | Angle | Headline | Supporting line | JPG |
|---|---|---|---|---|
| A01 | Privacy / no community | QUIT PORN. PRIVATELY. | A 30-day plan. No feed. No community. | `ads_1080x1350/a01_privacy_no_community_1080x1350.jpg` |
| A02 | Privacy / no community | NO PUBLIC STREAK. | Private progress. One clear next action. | `ads_1080x1350/a02_privacy_no_community_1080x1350.jpg` |
| A03 | Privacy / no community | RECOVERY IS NOT CONTENT. | No posting. No audience. Just a plan. | `ads_1080x1350/a03_privacy_no_community_1080x1350.jpg` |
| B01 | Rehearsal / tonight plan | PLAN FOR TONIGHT. | Choose one move before the weak window starts. | `ads_1080x1350/b01_rehearsal_plan_for_tonight_1080x1350.jpg` |
| B02 | Rehearsal / tonight plan | PRACTICE THE FIRST MOVE. | One rehearsal now. One clear action later. | `ads_1080x1350/b02_rehearsal_plan_for_tonight_1080x1350.jpg` |
| B03 | Rehearsal / tonight plan | ONE ORDER A DAY. | A concrete action built around the risky hour. | `ads_1080x1350/b03_rehearsal_plan_for_tonight_1080x1350.jpg` |
| C01 | Slip recovery | A SLIP DOESN'T ERASE PROGRESS. | Close everything. Reset. Keep moving. | `ads_1080x1350/c01_slip_recovery_1080x1350.jpg` |
| C02 | Slip recovery | STOP THE SECOND HIT. | One slip does not have to become a lost night. | `ads_1080x1350/c02_slip_recovery_1080x1350.jpg` |
| C03 | Slip recovery | RESET. DON'T START OVER. | Record what happened. Adjust the next move. | `ads_1080x1350/c03_slip_recovery_1080x1350.jpg` |

PNG masters sit beside each JPG. The exact inventory and file hashes are in `TIER6_CREATIVE_MANIFEST.json`.

## Recommended launch sequence after authorization

### Round 1 - angle discrimination

- One US ad set.
- Three ads only: A01, B01, C01.
- Same audience, optimization, placement policy, destination, and measurement window.
- Do not change creative, audience, bid, or destination during the first readable window.
- Treat Meta delivery as directional until the AppsFlyer -> install -> RevenueCat chain is joined without duplicate revenue.

### Round 2 - execution discrimination

- Keep the winning Round-1 angle.
- Test its three variants against each other.
- Retire the other two angles unless their lower-funnel economics materially beat the click winner.

## Required naming

`PHX_TOP30_US_<ANGLE>_<ASSET_ID>_20260722`

Recommended URL tags:

`source=meta&medium=paid_social&campaign=top30_restart&content=<asset_id>`

## Read order

1. Delivery integrity: impressions and spend populated.
2. Creative signal: outbound CTR and CPC.
3. Store signal: App Store product-page views and downloads, using App Store Connect as official store truth.
4. Acquisition signal: AppsFlyer attributed first opens.
5. Commercial signal: RevenueCat new trials, paid customers, proceeds, refunds, and plan mix.
6. Business decision: cumulative contribution = net proceeds minus ad spend, with annual and monthly reported separately.

## Kill and escalation rules

- Stop immediately if StoreKit, attribution, or revenue-event duplication is broken.
- Do not call an angle a loser from a handful of clicks or one sale.
- Do not judge install-to-paid before at least 100 new-cohort installs and 10 new paying customers.
- Do not judge store conversion before 100-200 product-page views.
- Do not scale until the founder's threshold is met: new-cohort install-to-paid at least 10%, annual share at least 50%, and economics support expansion.

## Provenance

The visual master was generated with OpenAI ImageGen. Exact text, brand lines, cropping, and exports were applied deterministically by `render_tier6_creatives.py`. QA contact sheet: `qa/ads_contact_sheet.jpg`.
