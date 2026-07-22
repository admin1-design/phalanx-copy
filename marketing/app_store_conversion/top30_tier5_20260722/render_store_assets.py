from __future__ import annotations

from pathlib import Path
from typing import Iterable

from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageOps


ROOT = Path(__file__).resolve().parent
MASTER = ROOT / "assets" / "generated_clean_dark_master.png"
TEMPLATES = ROOT / "01_capture_ready_templates_1290x2796"
DRAFTS = ROOT / "02_reference_composites_not_final"
QA = ROOT / "qa"

CANVAS = (1290, 2796)
OFF_WHITE = (244, 241, 233)
MUTED = (169, 172, 178)
GOLD = (177, 132, 67)
PHONE = (7, 8, 10)
SCREEN = (17, 19, 24)
WARNING = (213, 60, 54)

HEADLINE_FONT = Path(r"C:\Windows\Fonts\impact.ttf")
BODY_FONT = Path(r"C:\Windows\Fonts\arial.ttf")
BODY_BOLD_FONT = Path(r"C:\Windows\Fonts\arialbd.ttf")

SOURCE_PACK = Path(
    r"C:\Users\jesse\Desktop\1 PHALANX\PHALANX_GPT55_PRO_APP_STORE_SCREENSHOT_PACK_BUILD63_20260711"
)

SHOTS = [
    {
        "number": 1,
        "slug": "hold_the_line",
        "headline": "HOLD THE LINE",
        "subhead": "A 30-day system to quit porn and stay in control.",
        "capture": "Build 75 S08 plan reveal",
        "reference": SOURCE_PACK / "RAW_BUILD63_UI" / "02_RAW_PERSONALIZED_PLAN.jpg",
    },
    {
        "number": 2,
        "slug": "the_moment_it_starts",
        "headline": "THE MOMENT IT STARTS",
        "subhead": "One clear move when the urge hits.",
        "capture": "Build 75 S11 acute Fortify order",
        "reference": SOURCE_PACK / "RAW_BUILD63_UI" / "04_RAW_FORTIFY_RESCUE.jpg",
    },
    {
        "number": 3,
        "slug": "one_order_a_day",
        "headline": "ONE ORDER A DAY",
        "subhead": "One clear action each day.",
        "capture": "Build 75 Command / Today's Order",
        "reference": SOURCE_PACK / "OPTIONAL_RAW_BUILD63_UI" / "ALT_01_SET_TONIGHT_FORM.jpg",
    },
    {
        "number": 4,
        "slug": "a_slip_doesnt_erase_you",
        "headline": "A SLIP DOESN'T ERASE YOU",
        "subhead": "Get back to the line without losing your progress.",
        "capture": "Build 75 S12 post-slip stabilization / preserved progress",
        "reference": SOURCE_PACK / "RAW_BUILD63_UI" / "06_RAW_POST_SLIP_CONTAINMENT.jpg",
    },
    {
        "number": 5,
        "slug": "no_feed_no_community_no_shame",
        "headline": "NO FEED. NO COMMUNITY. NO SHAME.",
        "subhead": "Private. On your device.",
        "capture": "Build 75 private plan / on-device order surface",
        "reference": SOURCE_PACK / "OPTIONAL_RAW_BUILD63_UI" / "ALT_01_SET_TONIGHT_FORM.jpg",
    },
]


def contain_text(
    draw: ImageDraw.ImageDraw,
    text: str,
    font_path: Path,
    max_width: int,
    start_size: int,
    min_size: int,
) -> ImageFont.FreeTypeFont:
    size = start_size
    while size > min_size:
        font = ImageFont.truetype(str(font_path), size)
        if draw.textbbox((0, 0), text, font=font)[2] <= max_width:
            return font
        size -= 2
    return ImageFont.truetype(str(font_path), min_size)


def split_headline(draw: ImageDraw.ImageDraw, text: str, max_width: int) -> tuple[list[str], ImageFont.FreeTypeFont]:
    one_line = contain_text(draw, text, HEADLINE_FONT, max_width, 124, 88)
    if draw.textbbox((0, 0), text, font=one_line)[2] <= max_width and one_line.size >= 96:
        return [text], one_line

    words = text.split()
    best: tuple[list[str], ImageFont.FreeTypeFont] | None = None
    for cut in range(1, len(words)):
        lines = [" ".join(words[:cut]), " ".join(words[cut:])]
        font = contain_text(draw, max(lines, key=len), HEADLINE_FONT, max_width, 116, 82)
        widths = [draw.textbbox((0, 0), line, font=font)[2] for line in lines]
        if max(widths) <= max_width:
            balance = abs(widths[0] - widths[1])
            if best is None or (font.size, -balance) > (best[1].size, -abs(
                draw.textbbox((0, 0), best[0][0], font=best[1])[2]
                - draw.textbbox((0, 0), best[0][1], font=best[1])[2]
            )):
                best = (lines, font)
    if best:
        return best
    return [text], one_line


def wrapped_lines(draw: ImageDraw.ImageDraw, text: str, font: ImageFont.FreeTypeFont, max_width: int) -> list[str]:
    words = text.split()
    lines: list[str] = []
    current = ""
    for word in words:
        candidate = f"{current} {word}".strip()
        if current and draw.textbbox((0, 0), candidate, font=font)[2] > max_width:
            lines.append(current)
            current = word
        else:
            current = candidate
    if current:
        lines.append(current)
    return lines


def center_text(draw: ImageDraw.ImageDraw, text: str, y: int, font: ImageFont.FreeTypeFont, fill: tuple[int, int, int]) -> None:
    box = draw.textbbox((0, 0), text, font=font)
    width = box[2] - box[0]
    draw.text(((CANVAS[0] - width) // 2, y), text, font=font, fill=fill)


def cover(im: Image.Image, size: tuple[int, int]) -> Image.Image:
    return ImageOps.fit(im.convert("RGB"), size, method=Image.Resampling.LANCZOS, centering=(0.5, 0.15))


def phone_layer(screen_image: Image.Image | None) -> Image.Image:
    layer = Image.new("RGBA", CANVAS, (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)

    phone_box = (222, 700, 1068, 2534)
    shadow_box = (204, 686, 1086, 2558)
    shadow = Image.new("RGBA", CANVAS, (0, 0, 0, 0))
    sd = ImageDraw.Draw(shadow)
    sd.rounded_rectangle(shadow_box, radius=112, fill=(0, 0, 0, 165))
    shadow = shadow.filter(ImageFilter.GaussianBlur(34))
    layer.alpha_composite(shadow)

    d.rounded_rectangle(phone_box, radius=100, fill=PHONE, outline=(62, 66, 73, 255), width=4)
    inner = (246, 724, 1044, 2510)
    inner_size = (inner[2] - inner[0], inner[3] - inner[1])
    if screen_image is None:
        screen = Image.new("RGB", inner_size, SCREEN)
    else:
        screen = cover(screen_image, inner_size)
    mask = Image.new("L", inner_size, 0)
    md = ImageDraw.Draw(mask)
    md.rounded_rectangle((0, 0, inner_size[0], inner_size[1]), radius=76, fill=255)
    layer.paste(screen, (inner[0], inner[1]), mask)
    return layer


def render(shot: dict, screen_image: Image.Image | None, warning: bool) -> Image.Image:
    plate = Image.open(MASTER).convert("RGB")
    plate = ImageOps.fit(plate, CANVAS, method=Image.Resampling.LANCZOS)
    draw = ImageDraw.Draw(plate)

    lines, headline_font = split_headline(draw, shot["headline"], 1090)
    line_gap = 12
    line_height = headline_font.size + line_gap
    headline_y = 120 if len(lines) == 2 else 178
    for idx, line in enumerate(lines):
        center_text(draw, line, headline_y + idx * line_height, headline_font, OFF_WHITE)

    sub_font = ImageFont.truetype(str(BODY_FONT), 43)
    sub_lines = wrapped_lines(draw, shot["subhead"], sub_font, 980)
    sub_y = 420 if len(lines) == 1 else 430
    for idx, line in enumerate(sub_lines):
        center_text(draw, line, sub_y + idx * 54, sub_font, MUTED)

    gold_y = sub_y + len(sub_lines) * 54 + 44
    draw.rounded_rectangle((535, gold_y, 755, gold_y + 7), radius=4, fill=GOLD)

    composite = Image.alpha_composite(plate.convert("RGBA"), phone_layer(screen_image)).convert("RGB")
    if warning:
        d = ImageDraw.Draw(composite)
        font = ImageFont.truetype(str(BODY_BOLD_FONT), 27)
        message = "REFERENCE COMPOSITE — NOT FOR APP STORE"
        box = d.textbbox((0, 0), message, font=font)
        x = (CANVAS[0] - (box[2] - box[0])) // 2
        d.rounded_rectangle((x - 24, 2684, x + (box[2] - box[0]) + 24, 2740), radius=14, fill=(46, 8, 8))
        d.text((x, 2696), message, font=font, fill=WARNING)
    return composite


def contact_sheet(paths: Iterable[Path], target: Path) -> None:
    images = [Image.open(path).convert("RGB") for path in paths]
    thumb_w = 300
    thumb_h = round(thumb_w * CANVAS[1] / CANVAS[0])
    margin = 18
    sheet = Image.new("RGB", (len(images) * (thumb_w + margin) + margin, thumb_h + margin * 2), (18, 19, 22))
    for idx, im in enumerate(images):
        thumb = im.resize((thumb_w, thumb_h), Image.Resampling.LANCZOS)
        sheet.paste(thumb, (margin + idx * (thumb_w + margin), margin))
    sheet.save(target, quality=92, optimize=True)


def main() -> None:
    if not MASTER.exists():
        raise FileNotFoundError(MASTER)
    TEMPLATES.mkdir(parents=True, exist_ok=True)
    DRAFTS.mkdir(parents=True, exist_ok=True)
    QA.mkdir(parents=True, exist_ok=True)

    template_paths: list[Path] = []
    draft_paths: list[Path] = []
    for shot in SHOTS:
        stem = f"{shot['number']:02d}_{shot['slug']}_1290x2796"
        template_path = TEMPLATES / f"{stem}.png"
        render(shot, None, warning=False).save(template_path, optimize=True)
        template_paths.append(template_path)

        source = Path(shot["reference"])
        if not source.exists():
            raise FileNotFoundError(source)
        draft_path = DRAFTS / f"{stem}_REFERENCE_ONLY.png"
        render(shot, Image.open(source), warning=True).save(draft_path, optimize=True)
        draft_paths.append(draft_path)

    contact_sheet(template_paths, QA / "store_templates_contact_sheet.jpg")
    contact_sheet(draft_paths, QA / "reference_composites_contact_sheet.jpg")


if __name__ == "__main__":
    main()
