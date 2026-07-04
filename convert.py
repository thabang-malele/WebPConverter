"""
convert.py

Folder setup:

convert.py
converted/
images/

This script converts every image inside the "images" folder
into a .webp file inside the "converted" folder.

The filename stays the same.

Example:
    images/hoodie.png

becomes:
    converted/hoodie.webp
"""

from pathlib import Path
from PIL import Image


# =========================================================
# SETTINGS
# =========================================================

INPUT_FOLDER = Path("images")
OUTPUT_FOLDER = Path("converted")

QUALITY = 85
MAX_SIZE = 1600

VALID_EXTENSIONS = [
    ".png",
    ".jpg",
    ".jpeg"
]


# =========================================================
# HELPER FUNCTIONS
# =========================================================

def format_size(bytes_size):
    """Convert bytes into readable KB."""
    return f"{bytes_size / 1024:.1f} KB"


def resize_image(img):
    """Resize large images while keeping their shape/proportions."""

    width, height = img.size

    if width <= MAX_SIZE and height <= MAX_SIZE:
        return img

    img.thumbnail((MAX_SIZE, MAX_SIZE))
    return img


# =========================================================
# PREPARE OUTPUT FOLDER
# =========================================================

OUTPUT_FOLDER.mkdir(exist_ok=True)


# =========================================================
# CONVERT ALL IMAGES
# =========================================================

for image_path in INPUT_FOLDER.iterdir():

    if image_path.suffix.lower() not in VALID_EXTENSIONS:
        continue

    output_path = OUTPUT_FOLDER / f"{image_path.stem}.webp"

    before_size = image_path.stat().st_size

    with Image.open(image_path) as img:
        img = img.convert("RGB")
        img = resize_image(img)

        img.save(
            output_path,
            "WEBP",
            quality=QUALITY,
            method=6
        )

    after_size = output_path.stat().st_size

    print(f"Converted : {image_path.name} → {output_path.name}")
    print(f"Before    : {format_size(before_size)}")
    print(f"After     : {format_size(after_size)}")
    print(f"Saved     : {format_size(before_size - after_size)}")
    print("-" * 45)


print("Done. All images converted.")