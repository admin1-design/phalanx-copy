from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont, ImageOps


ROOT = Path(__file__).resolve().parent
BASE_IMAGE = Path(
    r"C:\Users\jesse\.codex\generated_images\019f8630-e032-7670-a07c-f035e58df7e1\exec-d3479af9-48c8-4a36-a898-855b476cd3d9.png"
)
ADS_DIR = ROOT / "ads_1080x1350"
ORGANIC_DIR = ROOT / "organic_1080x1920"
QA_DIR = ROOT / "qa"

FONT_REGULAR = Path(r"C:\Windows\Fonts\arial.ttf")
FONT_BOLD = Path(r"C:\Windows\Fonts\arialbd.ttf")

BG = (14, 15, 18)
OFF_WHITE = (244, 241, 233)
MUTED = (174, 177, 184)
GOLD = (190, 147, 72)
RED = (185, 31, 38)
BURGUNDY = (90, 18, 25)


ADS = [
    {
        "id": "A01",
        "angle": "privacy_no_community",
        "headline": "QUIT PORN.\nPRIVATELY.",
        "subhead": "A 30-day plan. No feed. No community.",
        "cta": "SEE THE PLAN",
    },
    {
        "id": "A02",
        "angle": "privacy_no_community",
        "headline": "NO PUBLIC\nSTREAK.",
        "subhead": "Private progress. One clear next action.",
        "cta": "BUILD TONIGHT'S PLAN",
    },
    {
        "id": "A03",
        "angle": "privacy_no_community",
        "headline": "RECOVERY IS\nNOT CONTENT.",
        "subhead": "No posting. No audience. Just a plan.",
        "cta": "GET PHALANX",
    },
    {
        "id": "B01",
        "angle": "rehearsal_plan_for_tonight",
        "headline": "PLAN FOR\nTONIGHT.",
        "subhead": "Choose one move before the weak window starts.",
        "cta": "BUILD THE PLAN",
    },
    {
        "id": "B02",
        "angle": "rehearsal_plan_for_tonight",
        "headline": "PRACTICE THE\nFIRST MOVE.",
        "subhead": "One rehearsal now. One clear action later.",
        "cta": "SEE HOW IT WORKS",
    },
    {
        "id": "B03",
        "angle": "rehearsal_plan_for_tonight",
        "headline": "ONE ORDER\nA DAY.",
        "subhead": "A concrete action built around the risky hour.",
        "cta": "START THE 30-DAY PLAN",
    },
    {
        "id": "C01",
        "angle": "slip_recovery",
        "headline": "A SLIP DOESN'T\nERASE PROGRESS.",
        "subhead": "Close everything. Reset. Keep moving.",
        "cta": "RETURN TO THE PLAN",
    },
    {
        "id": "C02",
        "angle": "slip_recovery",
        "headline": "STOP THE\nSECOND HIT.",
        "subhead": "One slip does not have to become a lost night.",
        "cta": "SEE THE RESET",
    },
    {
        "id": "C03",
        "angle": "slip_recovery",
        "headline": "RESET. DON'T\nSTART OVER.",
        "subhead": "Record what happened. Adjust the next move.",
        "cta": "KEEP MOVING",
    },
]


ORGANIC = [
    {
        "id": "D01",
        "slug": "pov-weak-window",
        "frames": [
            "POV: IT'S 11:47 PM.",
            "THE LOOP USUALLY STARTS\nBEFORE THE SEARCH.",
            "MOVE THE PHONE.\nLEAVE THE ROOM.",
            "BUILD TONIGHT'S PLAN.\nPHALANX",
        ],
    },
    {
        "id": "D02",
        "slug": "plan-before-willpower",
        "frames": [
            "DON'T WAIT FOR\nWILLPOWER.",
            "CHOOSE ONE MOVE BEFORE\nTHE WEAK WINDOW.",
            "PRACTICE IT ONCE.",
            "THEN USE IT TONIGHT.\nPHALANX",
        ],
    },
    {
        "id": "D03",
        "slug": "one-physical-order",
        "frames": [
            "WHEN THE URGE HITS:",
            "ONE PHYSICAL ORDER.",
            "DO IT BEFORE\nYOU DEBATE IT.",
            "FORTIFY · PHALANX",
        ],
    },
    {
        "id": "D04",
        "slug": "slip-isnt-the-night",
        "frames": [
            "A SLIP ISN'T\nTHE WHOLE NIGHT.",
            "CLOSE EVERYTHING.",
            "PUT THE PHONE AWAY.",
            "RETURN TO COMMAND.\nPHALANX",
        ],
    },
    {
        "id": "D05",
        "slug": "progress-you-can-act-on",
        "frames": [
            "CLEAN TIME ISN'T\nTHE ONLY PROOF.",
            "ORDERS COMPLETED.",
            "RESCUES USED.\nRESETS RECORDED.",
            "PROGRESS YOU CAN ACT ON.\nPHALANX",
        ],
    },
    {
        "id": "D06",
        "slug": "private-by-design",
        "frames": [
            "NO FEED.",
            "NO COMMUNITY.",
            "NO PUBLIC STREAK.",
            "PRIVATE. ON YOUR DEVICE.\nPHALANX",
        ],
    },
    {
        "id": "D07",
        "slug": "one-decision-made-early",
        "frames": [
            "BEFORE:\n\"I'LL JUST RESIST.\"",
            "AFTER:\nTHE PHONE CHARGES OUTSIDE\nTHE BEDROOM.",
            "ONE DECISION\nMADE EARLY.",
            "ONE LESS DECISION\nAT MIDNIGHT.\nPHALANX",
        ],
    },
]


def sha256(path: Path) -> str:
    value = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            value.update(chunk)
    return value.hexdigest()


def base_canvas(size: tuple[int, int]) -> Image.Image:
    source = Image.open(BASE_IMAGE).convert("RGB")
    canvas = ImageOps.fit(source, size, Image.Resampling.LANCZOS)
    overlay = Image.new("RGBA", size, (5, 6, 9, 176))
    canvas = Image.alpha_composite(canvas.convert("RGBA"), overlay)
    draw = ImageDraw.Draw(canvas, "RGBA")
    width, height = size
    for y in range(height):
        alpha = int(72 * y / max(height - 1, 1))
        draw.line((0, y, width, y), fill=(0, 0, 0, alpha))
    return canvas.convert("RGB")


def fit_font(text: str, max_width: int, max_height: int, start: int, minimum: int = 34) -> ImageFont.FreeTypeFont:
    probe = Image.new("RGB", (4, 4))
    draw = ImageDraw.Draw(probe)
    for size in range(start, minimum - 1, -2):
        font = ImageFont.truetype(str(FONT_BOLD), size)
        box = draw.multiline_textbbox((0, 0), text, font=font, spacing=int(size * 0.16), align="left")
        if box[2] - box[0] <= max_width and box[3] - box[1] <= max_height:
            return font
    return ImageFont.truetype(str(FONT_BOLD), minimum)


def accent_for(angle: str) -> tuple[int, int, int]:
    if angle == "privacy_no_community":
        return GOLD
    if angle == "rehearsal_plan_for_tonight":
        return RED
    return (213, 94, 63)


def render_ad(item: dict[str, str]) -> tuple[Path, Path]:
    size = (1080, 1350)
    canvas = base_canvas(size)
    draw = ImageDraw.Draw(canvas, "RGBA")
    accent = accent_for(item["angle"])

    draw.rounded_rectangle((54, 48, 1026, 1302), radius=34, outline=(*accent, 76), width=2)
    draw.text((76, 74), "PHALANX", font=ImageFont.truetype(str(FONT_BOLD), 34), fill=OFF_WHITE)
    draw.text((1004, 80), item["id"], font=ImageFont.truetype(str(FONT_REGULAR), 22), fill=MUTED, anchor="ra")
    draw.line((76, 136, 310, 136), fill=accent, width=5)

    label = item["angle"].replace("_", " ").upper()
    draw.text((76, 218), label, font=ImageFont.truetype(str(FONT_BOLD), 24), fill=accent)

    headline_font = fit_font(item["headline"], 900, 430, 112, 60)
    draw.multiline_text(
        (76, 278),
        item["headline"],
        font=headline_font,
        fill=OFF_WHITE,
        spacing=10,
    )

    sub_font = fit_font(item["subhead"], 880, 190, 52, 36)
    draw.multiline_text((76, 806), item["subhead"], font=sub_font, fill=MUTED, spacing=9)

    cta_font = ImageFont.truetype(str(FONT_BOLD), 29)
    cta_box = draw.textbbox((0, 0), item["cta"], font=cta_font)
    cta_width = min(900, cta_box[2] - cta_box[0] + 78)
    draw.rounded_rectangle((76, 1105, 76 + cta_width, 1198), radius=20, fill=(*accent, 235))
    draw.text((76 + cta_width / 2, 1151), item["cta"], font=cta_font, fill=OFF_WHITE, anchor="mm")
    draw.text((76, 1251), "QUIT PORN: 30-DAY PLAN", font=ImageFont.truetype(str(FONT_REGULAR), 22), fill=(135, 138, 145))

    stem = f"{item['id'].lower()}_{item['angle']}"
    png_path = ADS_DIR / f"{stem}_1080x1350.png"
    jpg_path = ADS_DIR / f"{stem}_1080x1350.jpg"
    canvas.save(png_path, optimize=True)
    canvas.save(jpg_path, quality=93, optimize=True, progressive=False)
    return png_path, jpg_path


def render_organic_frame(item: dict[str, object], index: int, text: str, output: Path) -> None:
    size = (1080, 1920)
    canvas = base_canvas(size)
    draw = ImageDraw.Draw(canvas, "RGBA")
    accent = (GOLD, RED, GOLD, OFF_WHITE)[index]

    draw.text((74, 82), "PHALANX", font=ImageFont.truetype(str(FONT_BOLD), 35), fill=OFF_WHITE)
    draw.text((1006, 88), f"{index + 1}/4", font=ImageFont.truetype(str(FONT_REGULAR), 25), fill=MUTED, anchor="ra")
    draw.line((74, 152, 74 + int(932 * (index + 1) / 4), 152), fill=accent, width=7)
    draw.line((74 + int(932 * (index + 1) / 4), 152, 1006, 152), fill=(75, 78, 84), width=3)

    font = fit_font(text, 900, 850, 108, 52)
    box = draw.multiline_textbbox((0, 0), text, font=font, spacing=18, align="center")
    text_height = box[3] - box[1]
    draw.multiline_text(
        (540, 900 - text_height / 2),
        text,
        font=font,
        fill=OFF_WHITE,
        spacing=18,
        align="center",
        anchor="ma",
    )

    draw.text((540, 1710), "QUIT PORN: 30-DAY PLAN", font=ImageFont.truetype(str(FONT_BOLD), 27), fill=accent, anchor="ma")
    draw.text((540, 1764), "PRIVATE · ONE CLEAR NEXT ACTION", font=ImageFont.truetype(str(FONT_REGULAR), 23), fill=MUTED, anchor="ma")
    canvas.save(output, optimize=True)


def encode_video(frame_paths: list[Path], output: Path) -> None:
    command = ["ffmpeg", "-y"]
    for frame in frame_paths:
        command.extend(["-loop", "1", "-t", "2.25", "-i", str(frame)])
    filter_graph = (
        "[0:v]fps=30,format=yuv420p[v0];"
        "[1:v]fps=30,format=yuv420p[v1];"
        "[2:v]fps=30,format=yuv420p[v2];"
        "[3:v]fps=30,format=yuv420p[v3];"
        "[v0][v1]xfade=transition=fade:duration=0.25:offset=2.0[x1];"
        "[x1][v2]xfade=transition=fade:duration=0.25:offset=4.0[x2];"
        "[x2][v3]xfade=transition=fade:duration=0.25:offset=6.0[outv]"
    )
    command.extend([
        "-filter_complex", filter_graph,
        "-map", "[outv]",
        "-t", "8",
        "-an",
        "-c:v", "libx264",
        "-preset", "medium",
        "-crf", "19",
        "-pix_fmt", "yuv420p",
        "-r", "30",
        "-movflags", "+faststart",
        str(output),
    ])
    result = subprocess.run(command, capture_output=True, text=True, check=False)
    if result.returncode != 0:
        raise RuntimeError(result.stderr[-4000:])


def make_contact_sheet(paths: list[Path], output: Path, columns: int, thumb_size: tuple[int, int]) -> None:
    images = [Image.open(path).convert("RGB") for path in paths]
    rows = (len(images) + columns - 1) // columns
    margin = 24
    label_h = 45
    cell_w, cell_h = thumb_size[0] + margin * 2, thumb_size[1] + margin * 2 + label_h
    sheet = Image.new("RGB", (columns * cell_w, rows * cell_h), BG)
    draw = ImageDraw.Draw(sheet)
    font = ImageFont.truetype(str(FONT_BOLD), 22)
    for idx, (path, source) in enumerate(zip(paths, images)):
        thumb = ImageOps.fit(source, thumb_size, Image.Resampling.LANCZOS)
        x = (idx % columns) * cell_w + margin
        y = (idx // columns) * cell_h + margin + label_h
        sheet.paste(thumb, (x, y))
        draw.text((x, y - 36), path.stem[:32], font=font, fill=OFF_WHITE)
    output.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(output, quality=91, optimize=True)


def main() -> None:
    if not BASE_IMAGE.exists():
        raise FileNotFoundError(BASE_IMAGE)
    ADS_DIR.mkdir(parents=True, exist_ok=True)
    ORGANIC_DIR.mkdir(parents=True, exist_ok=True)
    QA_DIR.mkdir(parents=True, exist_ok=True)

    rendered_ads: list[Path] = []
    for ad in ADS:
        _, jpg = render_ad(ad)
        rendered_ads.append(jpg)

    organic_outputs: list[dict[str, object]] = []
    organic_covers: list[Path] = []
    organic_frames: list[Path] = []
    for post in ORGANIC:
        post_dir = ORGANIC_DIR / str(post["id"]).lower()
        post_dir.mkdir(parents=True, exist_ok=True)
        frames: list[Path] = []
        for index, text in enumerate(post["frames"]):
            path = post_dir / f"frame_{index + 1:02d}.png"
            render_organic_frame(post, index, str(text), path)
            frames.append(path)
            organic_frames.append(path)
        output = ORGANIC_DIR / f"{str(post['id']).lower()}_{post['slug']}_1080x1920.mp4"
        encode_video(frames, output)
        cover = ORGANIC_DIR / f"{str(post['id']).lower()}_{post['slug']}_cover.jpg"
        Image.open(frames[0]).convert("RGB").save(cover, quality=92, optimize=True)
        organic_covers.append(cover)
        organic_outputs.append({
            "id": post["id"],
            "slug": post["slug"],
            "frames": post["frames"],
            "video": str(output),
            "video_bytes": output.stat().st_size,
            "video_sha256": sha256(output),
            "cover": str(cover),
        })

    make_contact_sheet(rendered_ads, QA_DIR / "ads_contact_sheet.jpg", columns=3, thumb_size=(324, 405))
    make_contact_sheet(organic_covers, QA_DIR / "organic_cover_contact_sheet.jpg", columns=4, thumb_size=(216, 384))
    make_contact_sheet(organic_frames, QA_DIR / "organic_all_frames_contact_sheet.jpg", columns=4, thumb_size=(216, 384))

    manifest = {
        "status": "LOCAL ASSETS ONLY — NOT POSTED OR LAUNCHED",
        "background": {
            "path": str(BASE_IMAGE),
            "sha256": sha256(BASE_IMAGE),
            "provenance": "OpenAI ImageGen clean-dark master generated during Top-30 Tier 5",
        },
        "ads": [
            {
                **ad,
                "jpg": str(rendered_ads[index]),
                "jpg_bytes": rendered_ads[index].stat().st_size,
                "jpg_sha256": sha256(rendered_ads[index]),
            }
            for index, ad in enumerate(ADS)
        ],
        "organic": organic_outputs,
    }
    (ROOT / "TIER6_CREATIVE_MANIFEST.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(f"Rendered {len(rendered_ads)} paid-social candidates")
    print(f"Rendered {len(organic_outputs)} organic MP4s")
    print(ROOT / "TIER6_CREATIVE_MANIFEST.json")


if __name__ == "__main__":
    main()
