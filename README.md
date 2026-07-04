# WebP Converter

A lightweight Python utility that converts PNG and JPEG images into optimized WebP files for use on websites.

Designed primarily for the **LowQuality** clothing brand, but works with any image collection.

---

## Features

- Converts **PNG**, **JPG**, and **JPEG** images.
- Compresses images into modern **WebP** format.
- Automatically resizes oversized images while preserving aspect ratio.
- Reports storage savings after every conversion.
- Recursively scans subfolders.
- Keeps original images untouched.

---

## Folder Structure

```text
LQ-WebP-Converter/
│
├── convert.py
├── README.md
│
├── assets/
│   ├── hoodie_bw.png
│   ├── shirt_wb.png
│   ├── socks_w.png
│   └── ...
│
└── converted/
```

---

## Installation

Install Pillow.

```bash
pip install pillow
```

---

## Usage

Place your images inside:

```text
images/
```

Run:

```bash
python convert.py
```

Your optimized images will appear in:

```text
converted/
```

---

## Supported Formats

Input

- PNG
- JPG
- JPEG

Output

- WebP

---

## Default Settings

```python
QUALITY = 85
MAX_SIZE = 1600
```

### QUALITY

Controls image compression.

Higher values

- Better quality
- Larger files

Lower values

- Smaller files
- More compression

Recommended:

```python
QUALITY = 85
```

---

### MAX_SIZE

Maximum width or height.

Images larger than this will automatically be resized while preserving aspect ratio.

Example

```
4096 × 4096
```

↓

```
1600 × 1600
```

---

## Example Output

```
Converted : hoodie_bw.png

Before    : 1245.8 KB
After     : 214.7 KB
Saved      : 1031.1 KB

---------------------------------------------
```

---

## Why WebP?

Compared to PNG, WebP offers:

- Smaller file sizes
- Faster website loading
- Excellent visual quality
- Wide browser support

This makes it ideal for:

- Clothing stores
- Product photography
- Portfolios
- Landing pages
- Ecommerce websites

---

## Future Improvements

- Drag-and-drop support
- Graphical interface (Tkinter)
- Adjustable quality slider
- Batch folder selection
- Automatic image comparison
- Metadata removal
- Progress bar
- PNG deletion after conversion
- JPEG export option
- Command-line arguments

---

## License

Open source.

Use, modify, and improve however you'd like.

---

Made with ❤️ for **LowQuality**.
