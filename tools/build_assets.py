"""Export landing-page assets from the app repo into ./assets.

Usage:  python3 tools/build_assets.py [path/to/day-box-kmm]

Store screenshots are the single source of visual truth for the site — the
landing page never shows a UI that the app does not have.
"""
import sys
from pathlib import Path

from PIL import Image

SITE = Path(__file__).resolve().parent.parent
APP = Path(sys.argv[1] if len(sys.argv) > 1 else SITE.parent.parent / "KMM" / "daybox").resolve()

SHOTS = APP / "aso" / "screenshot" / "raw-ios"
OUT = SITE / "assets"
(OUT / "shots").mkdir(parents=True, exist_ok=True)
(OUT / "fonts").mkdir(parents=True, exist_ok=True)

SHOT_NAMES = [
    "01-board", "02-picker", "03-photo", "04-journey-tasks",
    "05-journey-mood", "06-journey-expense", "07-feed", "08-postcard",
]
SHOT_WIDTH = 660  # half of the 1320 px original; phone frames render ≤ 330 css px


def export_shots() -> None:
    for name in SHOT_NAMES:
        for lang in ("en", "vi"):
            src = SHOTS / f"{name}-{lang}.png"
            im = Image.open(src).convert("RGB")
            h = round(im.height * SHOT_WIDTH / im.width)
            im = im.resize((SHOT_WIDTH, h), Image.LANCZOS)
            im.save(OUT / "shots" / f"{name}-{lang}.webp", "WEBP", quality=82, method=6)


def export_photo_crop() -> None:
    # The coffee tile from the sample day — reused inside the CSS-built board so
    # the "paper collection" section shows a real photo card, not a placeholder.
    im = Image.open(SHOTS / "01-board-en.png").convert("RGB")
    crop = im.crop((63, 1060, 350, 1347))  # left half of the 2×2 photo card
    crop = crop.resize((480, 480), Image.LANCZOS)
    crop.save(OUT / "photo-coffee.webp", "WEBP", quality=85, method=6)


def export_icon() -> None:
    src = Image.open(APP / "aso" / "graphics" / "icon-512.png").convert("RGBA")
    for size in (32, 180, 192, 512):
        src.resize((size, size), Image.LANCZOS).save(OUT / f"icon-{size}.png", optimize=True)


def export_og() -> None:
    for lang in ("en", "vi"):
        im = Image.open(APP / "aso" / "graphics" / f"feature-graphic-{lang}.png").convert("RGB")
        # OG wants 1.91:1 — 1024×500 already is; upscale to 1200×630 for crispness
        im.resize((1200, 586), Image.LANCZOS)
        canvas = Image.new("RGB", (1200, 630), im.getpixel((5, 5)))
        canvas.paste(im.resize((1200, 586), Image.LANCZOS), (0, 22))
        canvas.save(OUT / f"og-{lang}.png", optimize=True)


def export_font() -> None:
    from fontTools.ttLib import TTFont

    src = APP / "core" / "designsystem" / "src" / "commonMain" / "composeResources" / "font" / "plus_jakarta_sans_variable.ttf"
    font = TTFont(src)
    font.flavor = "woff2"
    font.save(OUT / "fonts" / "PlusJakartaSans-Variable.woff2")


if __name__ == "__main__":
    export_shots()
    export_photo_crop()
    export_icon()
    export_og()
    export_font()
    total = sum(p.stat().st_size for p in OUT.rglob("*") if p.is_file())
    print(f"assets: {total/1024:.0f} KB")
