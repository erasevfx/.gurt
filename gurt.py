from PIL import Image
import argparse
from gurt_loader import GurtLoader

def png_to_gurt(input_path, output_path):
    image = Image.open(input_path)
    image = image.convert('RGB')
    width, height = image.size

    data = b'GURT' + width.to_bytes(2, 'big') + height.to_bytes(2, 'big')
    
    pixels = image.tobytes()

    data += pixels

    with open(output_path, "wb") as f:
        f.write(data)

def gurt_to_png(input_path, output_path):
    with open(input_path, "rb") as f:
        header = f.read(8)
        magic = header[:4]

        if magic != b'GURT':
            raise ValueError("Not a valid GURT file")
        
        width = int.from_bytes(header[4:6], 'big')
        height = int.from_bytes(header[6:8], 'big')

        pixel_data = f.read(width * height * 3)

        image = Image.frombytes('RGB', (width, height), pixel_data)
        image.save(output_path)

def render(path):
    loader = GurtLoader(path)
    loader.run()

def main():
    parser = argparse.ArgumentParser(description="Convert and render .gurt images")
    parser.add_argument('mode', choices=['ptg', 'gtp', 'render'], help='Mode of operation')
    parser.add_argument('input_path', help='Input file path')
    parser.add_argument('output_path', nargs='?', default=None, help='Output file path (not needed for render mode)')

    args = parser.parse_args()

    if args.mode == 'ptg':
        if not args.output_path:
            parser.error(".png to .gurt mode requires an output_path")
        png_to_gurt(args.input_path, args.output_path)

    elif args.mode == 'gtp':
        if not args.output_path:
            parser.error(".gurt to .png mode requires an output_path")
        gurt_to_png(args.input_path, args.output_path)

    elif args.mode == 'render':
        render(args.input_path)

if __name__ == '__main__':
    main()