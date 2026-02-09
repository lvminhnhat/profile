import os
import math
import random
from PIL import Image, ImageDraw, ImageFilter

def create_gradient(width, height, start_color, end_color):
    base = Image.new('RGB', (width, height), start_color)
    top = Image.new('RGB', (width, height), end_color)
    mask = Image.new('L', (width, height))
    mask_data = []
    for y in range(height):
        mask_data.extend([int(255 * (y / height))] * width)
    mask.putdata(mask_data)
    base.paste(top, (0, 0), mask)
    return base

def draw_waves(draw, width, height, color):
    # Draw sine waves
    for i in range(0, height, 40):
        points = []
        phase = random.random() * math.pi * 2
        amplitude = random.randint(20, 50)
        freq = random.uniform(0.01, 0.03)
        for x in range(0, width, 10):
            y = i + math.sin(x * freq + phase) * amplitude
            points.append((x, y))
        
        # Draw line with width
        if len(points) > 1:
            draw.line(points, fill=color, width=3)

def draw_grid(draw, width, height, color):
    # Draw grid of rectangles
    cols = 12
    rows = 6
    cell_w = width // cols
    cell_h = height // rows
    
    for r in range(rows):
        for c in range(cols):
            if random.random() > 0.3:
                margin = 10
                x1 = c * cell_w + margin
                y1 = r * cell_h + margin
                x2 = (c + 1) * cell_w - margin
                y2 = (r + 1) * cell_h - margin
                draw.rectangle([x1, y1, x2, y2], outline=color, width=2)
                if random.random() > 0.7:
                    draw.rectangle([x1, y1, x2, y2], fill=(color[0], color[1], color[2], 50))

def draw_network(draw, width, height, color):
    # Draw nodes and connections
    nodes = []
    for _ in range(30):
        x = random.randint(50, width-50)
        y = random.randint(50, height-50)
        nodes.append((x, y))
    
    # Connect
    for i, n1 in enumerate(nodes):
        for n2 in nodes[i+1:]:
            dist = math.hypot(n1[0]-n2[0], n1[1]-n2[1])
            if dist < 300:
                alpha = int(255 * (1 - dist/300))
                draw.line([n1, n2], fill=(color[0], color[1], color[2], alpha), width=1)
    
    # Draw nodes
    for x, y in nodes:
        r = random.randint(3, 8)
        draw.ellipse([x-r, y-r, x+r, y+r], fill=color)

def draw_terminal(draw, width, height, color):
    # Draw code lines
    font_h = 20
    for y in range(50, height-50, 40):
        indent = random.choice([50, 100, 150])
        line_w = random.randint(100, 600)
        draw.rectangle([indent, y, indent+line_w, y+10], fill=color)
        
        # Add some "cursor" or keywords
        if random.random() > 0.8:
             draw.rectangle([indent-30, y, indent-10, y+10], fill=(255, 255, 255, 100))

def generate_voicetype(path):
    # Purple theme, waves
    width, height = 1200, 630
    img = create_gradient(width, height, (20, 0, 40), (60, 20, 100))
    draw = ImageDraw.Draw(img, 'RGBA')
    
    # Draw multiple layers of waves
    for _ in range(5):
        alpha = random.randint(50, 150)
        draw_waves(draw, width, height, (200, 100, 255, alpha))
    
    # Add a glowing center hint (microphone conceptual)
    # Using a radial gradient simulation by drawing concentric circles
    cx, cy = width//2, height//2
    for r in range(100, 0, -10):
        alpha = int(100 * (1 - r/100))
        draw.ellipse([cx-r, cy-r, cx+r, cy+r], fill=(255, 255, 255, alpha))
        
    img.save(path)
    print(f"Saved {path}")

def generate_filefilter(path):
    # Blue/Teal theme, grid
    width, height = 1200, 630
    img = create_gradient(width, height, (0, 20, 40), (0, 60, 80))
    draw = ImageDraw.Draw(img, 'RGBA')
    
    draw_grid(draw, width, height, (0, 255, 255))
    
    img.save(path)
    print(f"Saved {path}")

def generate_aicontent(path):
    # Green theme, network
    width, height = 1200, 630
    img = create_gradient(width, height, (0, 20, 10), (0, 60, 30))
    draw = ImageDraw.Draw(img, 'RGBA')
    
    draw_network(draw, width, height, (0, 255, 100))
    
    img.save(path)
    print(f"Saved {path}")

def generate_ghcagent(path):
    # Orange theme, terminal
    width, height = 1200, 630
    img = create_gradient(width, height, (30, 10, 0), (60, 30, 0))
    draw = ImageDraw.Draw(img, 'RGBA')
    
    draw_terminal(draw, width, height, (255, 160, 0))
    
    img.save(path)
    print(f"Saved {path}")

if __name__ == "__main__":
    os.makedirs("public/assets", exist_ok=True)
    generate_voicetype("public/assets/voicetype-cover.png")
    generate_filefilter("public/assets/filefilter-cover.png")
    generate_aicontent("public/assets/aicontent-cover.png")
    generate_ghcagent("public/assets/ghcagent-cover.png")
