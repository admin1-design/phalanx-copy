# PHALANX App Preview — Build 75 capture and edit specification

Status: **CAPTURE-READY; FINAL MP4 BLOCKED ON FRESH PHYSICAL BUILD 75 FOOTAGE**

## Objective

Show the product mechanism in one continuous, truthful sequence:

`weak-window card → Fortify opens → one order → Done → Recorded`

No voiceover. Captions carry the meaning. Every visible app frame must be captured from the final Build 75 candidate on a physical iPhone; no mock UI, stale Build 74 footage, or reconstructed animation is acceptable.

## Master timeline — 18 seconds

| Time | Physical capture | Caption |
|---|---|---|
| 0.0–3.0s | Command home with the weak-window card and tonight's order visible. Hold long enough to read. | None; the real UI establishes context. |
| 3.0–5.0s | Tap Fortify. Keep the tap and transition in the recording. | `THE MOMENT IT STARTS` |
| 5.0–11.0s | Acute Fortify order visible above the fold. No scrolling. | `One clear move when the urge hits.` |
| 11.0–13.0s | Tap the real `Done` button. | `Done` |
| 13.0–18.0s | Hold on the real win state: `Recorded. That's how it's done.` | `Recorded. That's how it's done.` |

All caption strings above are copied from `PHALANX-copy-deck.md` v1.7.

## Capture state

- Final candidate binary only; receipt must record app version, Apple build number, EAS build ID, and git commit.
- Use a clean QA account with no personal journal text, name, photograph, email, or notification content visible.
- Seed one coherent scenario before capture: `Late night` weak window and a short, natural first move that fits on one line.
- Mirror Check remains off. Do not show the Centurion, rank, Battle Stories, lore, paywall, or settings.
- Start on Command. Capture the actual Fortify tap and actual state transition; do not splice over a failed or loading screen.
- Keep system clock, battery, and status-bar treatment consistent across the take.
- Record at native device resolution with Do Not Disturb enabled. Do not record taps from an assistive overlay.

## Edit and export gate

- Duration: 15–30 seconds; target 18 seconds.
- Portrait delivery: 886×1920 pixels.
- Codec: H.264; maximum 30 fps; maximum file size 500 MB.
- Audio: no voiceover; silence is acceptable. Do not add licensed music.
- Captions: off-white on near-black, large enough to read at product-page thumbnail size; one short caption at a time.
- Use only screen capture of the app itself. No hands, rendered device mockup, external footage, people, or Roman artwork.
- First frame must immediately show the app; no logo bumper or blocking intro.
- Final frame holds on the recorded win state for at least two seconds.

## Acceptance checklist

- [ ] Footage is from the final Build 75 candidate identified by a four-field binary receipt.
- [ ] Weak-window card, Fortify acute order, `Done`, and recorded state match the approved deck copy.
- [ ] First instruction appears within two seconds of the Fortify screen becoming visible.
- [ ] No personal or sensitive test data appears.
- [ ] No text truncation, stale reminder time, grammatical defect, loading flash, or debug UI appears.
- [ ] Export is 15–30 seconds, 886×1920, H.264, and no more than 30 fps.
- [ ] Final MP4 is reviewed on an iPhone before App Store Connect staging.

## Decision rule

**TEST FIRST.** Apple permits app previews, but a preview is not automatically a conversion lift. Stage it as a Product Page Optimization challenger against the clean-dark screenshot-only control. Keep it only if product-page conversion improves at the agreed confidence threshold without increasing low-intent installs.

Official references:

- [Apple — App preview specifications](https://developer.apple.com/help/app-store-connect/reference/app-information/app-preview-specifications/)
- [Apple — Creating app previews](https://developer.apple.com/app-store/app-previews/)
- [Apple — Product Page Optimization](https://developer.apple.com/app-store/product-page-optimization/)

