import os
import glob
from PIL import Image

files = glob.glob(r"c:\Users\Sophia\Desktop\GGJONU\CIENTISTA\*.png")

def is_edge_and_white(x, y, pixels, width, height):
    r, g, b, a = pixels[x, y]
    # Check if the pixel is bright (white/light grey outline)
    border_threshold = 180
    if a > 0 and r > border_threshold and g > border_threshold and b > border_threshold:
        # Check neighboring pixels for transparency = meaning it's an edge
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1), (-1,-1), (1,-1), (-1,1), (1,1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < width and 0 <= ny < height:
                if pixels[nx, ny][3] == 0:
                    return True
            else:
                return True
    return False

for f in files:
    print(f"Processing {f}...")
    img = Image.open(f).convert('RGBA')
    pixels = img.load()
    w, h = img.size
    
    # We run 2 passes to erode the white edge thoroughly
    for _ in range(2):
        to_remove = []
        for y in range(h):
            for x in range(w):
                if is_edge_and_white(x, y, pixels, w, h):
                    to_remove.append((x, y))
                    
        for x, y in to_remove:
            pixels[x, y] = (0, 0, 0, 0)
    
    img.save(f)
    print(f"Successfully cleaned image {f}.")
