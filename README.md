# GURT Image Format

**GURT** custom binary image format called .gurt. Includes png to gurt/gurt to png conversions and a pygame-based renderer.

---

## Features

- Convert any PNG to a `.gurt` image
- Convert `.gurt` images back to PNG
- Render `.gurt` images using a pygame-based renderer
- CLI interface with `ptg`, `gtp`, and `render` modes

---

## Usage

```bash
python gurt.py ptg <input.png> <output.gurt>
# Converts a PNG file to a .gurt file

python gurt.py gtp <input.gurt> <output.png>
# Converts a .gurt file to a PNG file

python gurt.py render <input.gurt>
# Opens a window and renders the .gurt image using Pygame
