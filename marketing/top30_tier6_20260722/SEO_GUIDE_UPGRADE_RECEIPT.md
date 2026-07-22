# PHALANX Top-30 Tier 6 - SEO / LLM-SEO Guide Upgrade

**Status:** IMPLEMENTED IN LOCAL WEBSITE SOURCE - NOT DEPLOYED.

## Decision

**MODIFY.** The local website already contained three strong, distinct pages matching the requested search intents. Creating three new near-duplicate URLs would split signals and add thin content. The local source was therefore upgraded in place:

1. `phalanx-landing-deploy/30-day-quit-porn-plan/index.html` - broad planning intent.
2. `phalanx-landing-deploy/porn-urge-control/index.html` - acute urge intent.
3. `phalanx-landing-deploy/relapse-reset-protocol/index.html` - post-slip intent.

Exact pre-change files are preserved under `seo_backups/` in this Tier 6 workspace.

## What changed

- Aligned the three pages to the rebuilt product mechanism: weak window, first move, rehearsal, Today's Order, acute Fortify, Return to Command, and Campaign Report.
- Removed stale `Daily Oath` and `Service Record` wording from the acute guide.
- Removed blocker-adjacent positioning from the acute guide.
- Corrected the 30-day guide's duplicated `Fortify, Fortify` sentence.
- Corrected the post-slip order of operations: stabilize first, log second.
- Updated matching metadata and FAQ structured data where the visible answer changed.
- Preserved each page's existing canonical URL; no redirect, DNS, deploy, or production mutation occurred.

## Research boundary

Google's current guidance prioritizes people-first content with original value and warns against search-engine-first mass production. Google also recommends consolidating duplicate URLs through canonicalization or redirects rather than publishing overlapping pages. That supports upgrading these three distinct pages instead of adding three more thin variants:

- [Google Search: Creating helpful, reliable, people-first content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content)
- [Google Search: Consolidate duplicate URLs](https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls)
- [Google Search: Canonicalization overview](https://developers.google.com/search/docs/crawling-indexing/canonicalization)

QUITTR's public guide demonstrates the competitive pattern - a direct answer, clear sections, and a product bridge - but PHALANX copy and mechanism remain original. The inherited `US$1,500/day` claim was not used as verified evidence because the competitor's public guide does not prove that revenue figure:

- [QUITTR: How to stop watching porn](https://quittrapp.com/porn-addiction/how-to-stop)

## Smallest next gate

Run the local site tests and a browser-layout check, then deploy only after Jesse authorizes a website release. Stop deployment if existing SEO-route, legal-product-consistency, or plain-language tests regress.

## Local verification

- All 36 non-visual website tests passed on 2026-07-22.
- All three edited JSON-LD blocks parsed successfully.
- No stale `Daily Oath`, `Service Record`, blocker FAQ, duplicated `Fortify, Fortify`, or pre-stabilization repair instruction remains on these three pages.
- Test log: `qa_logs/website_node_tests.txt`.
- Revised-file hashes: `qa_logs/seo_revised_sha256.txt`.
