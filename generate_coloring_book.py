#!/usr/bin/env python3
"""
Generate a 50-page Color By Numbers activity book as HTML (print-ready).
Each page has:
- Colorful block border
- "COLOR BY NUMBERS" title
- SVG outline drawing with numbered regions
- Color legend at the bottom
"""
import random
import math

random.seed(42)

# Color palettes for legends (5 colors each)
PALETTES = [
    ["#FF69B4", "#4B0082", "#FF8C00", "#228B22", "#FFD700"],
    ["#FF0000", "#00AA00", "#FFD700", "#FF69B4", "#4169E1"],
    ["#8B4513", "#FFA500", "#FF69B4", "#DC143C", "#FFD700"],
    ["#87CEEB", "#FFD700", "#333333", "#FF69B4", "#FF8C00"],
    ["#FF6347", "#32CD32", "#4169E1", "#FFD700", "#9932CC"],
    ["#FF1493", "#00CED1", "#FF8C00", "#8B008B", "#3CB371"],
    ["#DC143C", "#4682B4", "#DAA520", "#2E8B57", "#FF4500"],
    ["#6A5ACD", "#FF7F50", "#20B2AA", "#CD853F", "#C71585"],
    ["#1E90FF", "#FF69B4", "#32CD32", "#FF4500", "#9400D3"],
    ["#FF6600", "#0066CC", "#33CC33", "#CC0066", "#FFCC00"],
]

# Border block colors
BORDER_COLORS = [
    "#FF0000", "#00FF00", "#0000FF", "#FFFF00", "#FF00FF",
    "#00FFFF", "#FFA500", "#800080", "#008000", "#FFC0CB",
    "#A52A2A", "#808080", "#000080", "#808000", "#800000",
]


def generate_border_svg():
    """Generate colorful block border as SVG elements."""
    blocks = []
    block_size = 28
    # Top border
    for i in range(22):
        color = random.choice(BORDER_COLORS)
        blocks.append(f'<rect x="{i*block_size}" y="0" width="{block_size}" height="{block_size}" fill="{color}" stroke="#333" stroke-width="1"/>')
        # Small circle inside
        blocks.append(f'<circle cx="{i*block_size + 14}" cy="14" r="6" fill="none" stroke="#fff" stroke-width="1.5"/>')
    # Bottom border
    for i in range(22):
        color = random.choice(BORDER_COLORS)
        blocks.append(f'<rect x="{i*block_size}" y="772" width="{block_size}" height="{block_size}" fill="{color}" stroke="#333" stroke-width="1"/>')
        blocks.append(f'<circle cx="{i*block_size + 14}" cy="786" r="6" fill="none" stroke="#fff" stroke-width="1.5"/>')
    # Left border
    for i in range(28):
        color = random.choice(BORDER_COLORS)
        blocks.append(f'<rect x="0" y="{i*block_size}" width="{block_size}" height="{block_size}" fill="{color}" stroke="#333" stroke-width="1"/>')
        blocks.append(f'<circle cx="14" cy="{i*block_size + 14}" r="6" fill="none" stroke="#fff" stroke-width="1.5"/>')
    # Right border
    for i in range(28):
        color = random.choice(BORDER_COLORS)
        blocks.append(f'<rect x="588" y="{i*block_size}" width="{block_size}" height="{block_size}" fill="{color}" stroke="#333" stroke-width="1"/>')
        blocks.append(f'<circle cx="602" cy="{i*block_size + 14}" r="6" fill="none" stroke="#fff" stroke-width="1.5"/>')
    return "\n".join(blocks)


def draw_cupcake(cx, cy, scale=1.0):
    """Draw a cupcake outline with numbered regions."""
    s = scale
    elements = []
    # Cupcake wrapper (trapezoid shape) - region 3
    wrapper_points = f"{cx-60*s},{cy+50*s} {cx-80*s},{cy-10*s} {cx+80*s},{cy-10*s} {cx+60*s},{cy+50*s}"
    elements.append(f'<polygon points="{wrapper_points}" fill="none" stroke="#000" stroke-width="2.5"/>')
    # Wrapper lines
    for i in range(-2, 3):
        x_off = i * 25 * s
        elements.append(f'<line x1="{cx+x_off-5*s}" y1="{cy-10*s}" x2="{cx+x_off+5*s}" y2="{cy+50*s}" stroke="#000" stroke-width="1.5"/>')
    elements.append(f'<text x="{cx}" y="{cy+25*s}" text-anchor="middle" font-size="18" font-weight="bold">3</text>')
    # Cupcake top (dome) - region 2
    elements.append(f'<ellipse cx="{cx}" cy="{cy-50*s}" rx="{90*s}" ry="{60*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
    elements.append(f'<text x="{cx-40*s}" y="{cy-40*s}" text-anchor="middle" font-size="18" font-weight="bold">2</text>')
    elements.append(f'<text x="{cx+40*s}" y="{cy-40*s}" text-anchor="middle" font-size="18" font-weight="bold">2</text>')
    # Frosting swirl - region 1
    elements.append(f'<path d="M{cx-80*s},{cy-15*s} Q{cx-60*s},{cy-35*s} {cx-40*s},{cy-15*s} Q{cx-20*s},{cy-35*s} {cx},{cy-15*s} Q{cx+20*s},{cy-35*s} {cx+40*s},{cy-15*s} Q{cx+60*s},{cy-35*s} {cx+80*s},{cy-15*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
    elements.append(f'<text x="{cx}" y="{cy-60*s}" text-anchor="middle" font-size="18" font-weight="bold">1</text>')
    # Cherry on top - region 4
    elements.append(f'<circle cx="{cx}" cy="{cy-105*s}" r="{15*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
    elements.append(f'<text x="{cx}" y="{cy-100*s}" text-anchor="middle" font-size="16" font-weight="bold">4</text>')
    # Stem
    elements.append(f'<path d="M{cx},{cy-120*s} Q{cx+10*s},{cy-130*s} {cx+5*s},{cy-140*s}" fill="none" stroke="#000" stroke-width="2"/>')
    return "\n".join(elements)


def draw_star(cx, cy, scale=1.0):
    """Draw a star with numbered regions."""
    s = scale
    elements = []
    # Outer star points
    points = []
    for i in range(10):
        angle = math.radians(i * 36 - 90)
        r = 100*s if i % 2 == 0 else 50*s
        px = cx + r * math.cos(angle)
        py = cy + r * math.sin(angle)
        points.append(f"{px},{py}")
    elements.append(f'<polygon points="{" ".join(points)}" fill="none" stroke="#000" stroke-width="2.5"/>')
    # Inner circle region
    elements.append(f'<circle cx="{cx}" cy="{cy}" r="{35*s}" fill="none" stroke="#000" stroke-width="2"/>')
    # Numbers in regions
    elements.append(f'<text x="{cx}" y="{cy+6}" text-anchor="middle" font-size="20" font-weight="bold">1</text>')
    # Numbers in star points
    for i in range(5):
        angle = math.radians(i * 72 - 90)
        tx = cx + 75*s * math.cos(angle)
        ty = cy + 75*s * math.sin(angle) + 6
        elements.append(f'<text x="{tx}" y="{ty}" text-anchor="middle" font-size="16" font-weight="bold">2</text>')
    return "\n".join(elements)

def draw_butterfly(cx, cy, scale=1.0):
    """Draw a butterfly with numbered regions."""
    s = scale
    elements = []
    # Body - region 1
    elements.append(f'<ellipse cx="{cx}" cy="{cy}" rx="{12*s}" ry="{60*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
    elements.append(f'<text x="{cx}" y="{cy+5}" text-anchor="middle" font-size="16" font-weight="bold">1</text>')
    # Left top wing - region 2
    elements.append(f'<ellipse cx="{cx-60*s}" cy="{cy-30*s}" rx="{55*s}" ry="{45*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
    elements.append(f'<text x="{cx-60*s}" y="{cy-25*s}" text-anchor="middle" font-size="18" font-weight="bold">2</text>')
    # Right top wing - region 2
    elements.append(f'<ellipse cx="{cx+60*s}" cy="{cy-30*s}" rx="{55*s}" ry="{45*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
    elements.append(f'<text x="{cx+60*s}" y="{cy-25*s}" text-anchor="middle" font-size="18" font-weight="bold">2</text>')
    # Left bottom wing - region 3
    elements.append(f'<ellipse cx="{cx-45*s}" cy="{cy+35*s}" rx="{40*s}" ry="{30*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
    elements.append(f'<text x="{cx-45*s}" y="{cy+40*s}" text-anchor="middle" font-size="16" font-weight="bold">3</text>')
    # Right bottom wing - region 3
    elements.append(f'<ellipse cx="{cx+45*s}" cy="{cy+35*s}" rx="{40*s}" ry="{30*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
    elements.append(f'<text x="{cx+45*s}" y="{cy+40*s}" text-anchor="middle" font-size="16" font-weight="bold">3</text>')
    # Wing spots - region 4
    elements.append(f'<circle cx="{cx-60*s}" cy="{cy-35*s}" r="{15*s}" fill="none" stroke="#000" stroke-width="2"/>')
    elements.append(f'<text x="{cx-60*s}" y="{cy-30*s}" text-anchor="middle" font-size="14" font-weight="bold">4</text>')
    elements.append(f'<circle cx="{cx+60*s}" cy="{cy-35*s}" r="{15*s}" fill="none" stroke="#000" stroke-width="2"/>')
    elements.append(f'<text x="{cx+60*s}" y="{cy-30*s}" text-anchor="middle" font-size="14" font-weight="bold">4</text>')
    # Antennae
    elements.append(f'<path d="M{cx-5*s},{cy-60*s} Q{cx-20*s},{cy-90*s} {cx-30*s},{cy-100*s}" fill="none" stroke="#000" stroke-width="2"/>')
    elements.append(f'<path d="M{cx+5*s},{cy-60*s} Q{cx+20*s},{cy-90*s} {cx+30*s},{cy-100*s}" fill="none" stroke="#000" stroke-width="2"/>')
    elements.append(f'<circle cx="{cx-30*s}" cy="{cy-100*s}" r="{5*s}" fill="none" stroke="#000" stroke-width="2"/>')
    elements.append(f'<circle cx="{cx+30*s}" cy="{cy-100*s}" r="{5*s}" fill="none" stroke="#000" stroke-width="2"/>')
    return "\n".join(elements)


def draw_flower(cx, cy, scale=1.0):
    """Draw a flower with numbered regions."""
    s = scale
    elements = []
    # Center circle - region 1
    elements.append(f'<circle cx="{cx}" cy="{cy}" r="{30*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
    elements.append(f'<text x="{cx}" y="{cy+6}" text-anchor="middle" font-size="18" font-weight="bold">1</text>')
    # Petals - region 2
    for i in range(6):
        angle = math.radians(i * 60)
        px = cx + 55*s * math.cos(angle)
        py = cy + 55*s * math.sin(angle)
        elements.append(f'<ellipse cx="{px}" cy="{py}" rx="{30*s}" ry="{20*s}" fill="none" stroke="#000" stroke-width="2.5" transform="rotate({i*60},{px},{py})"/>')
        elements.append(f'<text x="{px}" y="{py+6}" text-anchor="middle" font-size="14" font-weight="bold">2</text>')
    # Stem - region 3
    elements.append(f'<rect x="{cx-6*s}" y="{cy+80*s}" width="{12*s}" height="{100*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
    elements.append(f'<text x="{cx}" y="{cy+135*s}" text-anchor="middle" font-size="16" font-weight="bold">3</text>')
    # Leaves - region 4
    elements.append(f'<ellipse cx="{cx-35*s}" cy="{cy+120*s}" rx="{30*s}" ry="{12*s}" fill="none" stroke="#000" stroke-width="2" transform="rotate(-30,{cx-35*s},{cy+120*s})"/>')
    elements.append(f'<text x="{cx-35*s}" y="{cy+124*s}" text-anchor="middle" font-size="12" font-weight="bold">4</text>')
    elements.append(f'<ellipse cx="{cx+35*s}" cy="{cy+140*s}" rx="{30*s}" ry="{12*s}" fill="none" stroke="#000" stroke-width="2" transform="rotate(30,{cx+35*s},{cy+140*s})"/>')
    elements.append(f'<text x="{cx+35*s}" y="{cy+144*s}" text-anchor="middle" font-size="12" font-weight="bold">4</text>')
    return "\n".join(elements)

def draw_fish(cx, cy, scale=1.0):
    """Draw a fish with numbered regions."""
    s = scale
    elements = []
    # Body ellipse - region 1
    elements.append(f'<ellipse cx="{cx}" cy="{cy}" rx="{90*s}" ry="{55*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
    elements.append(f'<text x="{cx}" y="{cy+6}" text-anchor="middle" font-size="20" font-weight="bold">1</text>')
    # Tail - region 2
    elements.append(f'<polygon points="{cx+80*s},{cy} {cx+130*s},{cy-40*s} {cx+130*s},{cy+40*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
    elements.append(f'<text x="{cx+105*s}" y="{cy+6}" text-anchor="middle" font-size="16" font-weight="bold">2</text>')
    # Dorsal fin - region 3
    elements.append(f'<polygon points="{cx-20*s},{cy-55*s} {cx+20*s},{cy-55*s} {cx},{cy-90*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
    elements.append(f'<text x="{cx}" y="{cy-65*s}" text-anchor="middle" font-size="14" font-weight="bold">3</text>')
    # Eye - region 4
    elements.append(f'<circle cx="{cx-40*s}" cy="{cy-10*s}" r="{15*s}" fill="none" stroke="#000" stroke-width="2"/>')
    elements.append(f'<circle cx="{cx-40*s}" cy="{cy-10*s}" r="{7*s}" fill="#000"/>')
    elements.append(f'<text x="{cx-40*s}" y="{cy+15*s}" text-anchor="middle" font-size="12" font-weight="bold">4</text>')
    # Scales pattern - region 5
    for row in range(2):
        for col in range(3):
            sx = cx - 10*s + col*25*s
            sy = cy + 5*s + row*20*s
            elements.append(f'<path d="M{sx},{sy} A{10*s},{10*s} 0 0 1 {sx+15*s},{sy}" fill="none" stroke="#000" stroke-width="1.5"/>')
    elements.append(f'<text x="{cx+20*s}" y="{cy+20*s}" text-anchor="middle" font-size="12" font-weight="bold">5</text>')
    return "\n".join(elements)


def draw_house(cx, cy, scale=1.0):
    """Draw a house with numbered regions."""
    s = scale
    elements = []
    # Main body - region 1
    elements.append(f'<rect x="{cx-70*s}" y="{cy-30*s}" width="{140*s}" height="{100*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
    elements.append(f'<text x="{cx+30*s}" y="{cy+30*s}" text-anchor="middle" font-size="18" font-weight="bold">1</text>')
    # Roof - region 2
    elements.append(f'<polygon points="{cx-85*s},{cy-30*s} {cx},{cy-100*s} {cx+85*s},{cy-30*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
    elements.append(f'<text x="{cx}" y="{cy-50*s}" text-anchor="middle" font-size="18" font-weight="bold">2</text>')
    # Door - region 3
    elements.append(f'<rect x="{cx-20*s}" y="{cy+20*s}" width="{40*s}" height="{50*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
    elements.append(f'<circle cx="{cx+12*s}" cy="{cy+45*s}" r="{4*s}" fill="#000"/>')
    elements.append(f'<text x="{cx}" y="{cy+40*s}" text-anchor="middle" font-size="14" font-weight="bold">3</text>')
    # Windows - region 4
    elements.append(f'<rect x="{cx-60*s}" y="{cy-15*s}" width="{30*s}" height="{30*s}" fill="none" stroke="#000" stroke-width="2"/>')
    elements.append(f'<line x1="{cx-60*s}" y1="{cy}" x2="{cx-30*s}" y2="{cy}" stroke="#000" stroke-width="1.5"/>')
    elements.append(f'<line x1="{cx-45*s}" y1="{cy-15*s}" x2="{cx-45*s}" y2="{cy+15*s}" stroke="#000" stroke-width="1.5"/>')
    elements.append(f'<text x="{cx-45*s}" y="{cy-18*s}" text-anchor="middle" font-size="12" font-weight="bold">4</text>')
    elements.append(f'<rect x="{cx+30*s}" y="{cy-15*s}" width="{30*s}" height="{30*s}" fill="none" stroke="#000" stroke-width="2"/>')
    elements.append(f'<line x1="{cx+30*s}" y1="{cy}" x2="{cx+60*s}" y2="{cy}" stroke="#000" stroke-width="1.5"/>')
    elements.append(f'<line x1="{cx+45*s}" y1="{cy-15*s}" x2="{cx+45*s}" y2="{cy+15*s}" stroke="#000" stroke-width="1.5"/>')
    elements.append(f'<text x="{cx+45*s}" y="{cy-18*s}" text-anchor="middle" font-size="12" font-weight="bold">4</text>')
    # Chimney - region 5
    elements.append(f'<rect x="{cx+30*s}" y="{cy-95*s}" width="{20*s}" height="{40*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
    elements.append(f'<text x="{cx+40*s}" y="{cy-70*s}" text-anchor="middle" font-size="12" font-weight="bold">5</text>')
    return "\n".join(elements)

def draw_sun(cx, cy, scale=1.0):
    """Draw a sun with numbered regions."""
    s = scale
    elements = []
    # Center circle - region 1
    elements.append(f'<circle cx="{cx}" cy="{cy}" r="{50*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
    elements.append(f'<text x="{cx}" y="{cy+7}" text-anchor="middle" font-size="22" font-weight="bold">1</text>')
    # Rays - region 2
    for i in range(12):
        angle = math.radians(i * 30)
        x1 = cx + 55*s * math.cos(angle)
        y1 = cy + 55*s * math.sin(angle)
        x2 = cx + 90*s * math.cos(angle)
        y2 = cy + 90*s * math.sin(angle)
        # Triangle rays
        a_left = math.radians(i * 30 - 8)
        a_right = math.radians(i * 30 + 8)
        bx1 = cx + 55*s * math.cos(a_left)
        by1 = cy + 55*s * math.sin(a_left)
        bx2 = cx + 55*s * math.cos(a_right)
        by2 = cy + 55*s * math.sin(a_right)
        elements.append(f'<polygon points="{bx1},{by1} {x2},{y2} {bx2},{by2}" fill="none" stroke="#000" stroke-width="2"/>')
        if i % 3 == 0:
            tx = cx + 72*s * math.cos(angle)
            ty = cy + 72*s * math.sin(angle) + 5
            elements.append(f'<text x="{tx}" y="{ty}" text-anchor="middle" font-size="12" font-weight="bold">2</text>')
    # Smile
    elements.append(f'<path d="M{cx-20*s},{cy+10*s} Q{cx},{cy+30*s} {cx+20*s},{cy+10*s}" fill="none" stroke="#000" stroke-width="2"/>')
    # Eyes
    elements.append(f'<circle cx="{cx-15*s}" cy="{cy-10*s}" r="{6*s}" fill="#000"/>')
    elements.append(f'<circle cx="{cx+15*s}" cy="{cy-10*s}" r="{6*s}" fill="#000"/>')
    return "\n".join(elements)


def draw_heart(cx, cy, scale=1.0):
    """Draw a heart with numbered regions."""
    s = scale
    elements = []
    # Outer heart - region 1
    elements.append(f'<path d="M{cx},{cy+70*s} C{cx-120*s},{cy-20*s} {cx-60*s},{cy-90*s} {cx},{cy-40*s} C{cx+60*s},{cy-90*s} {cx+120*s},{cy-20*s} {cx},{cy+70*s}" fill="none" stroke="#000" stroke-width="3"/>')
    elements.append(f'<text x="{cx-50*s}" y="{cy}" text-anchor="middle" font-size="18" font-weight="bold">1</text>')
    elements.append(f'<text x="{cx+50*s}" y="{cy}" text-anchor="middle" font-size="18" font-weight="bold">1</text>')
    # Inner heart - region 2
    inner_s = 0.5 * s
    elements.append(f'<path d="M{cx},{cy+20*inner_s*2} C{cx-80*inner_s*2},{cy-30*inner_s} {cx-40*inner_s*2},{cy-50*inner_s} {cx},{cy-20*inner_s} C{cx+40*inner_s*2},{cy-50*inner_s} {cx+80*inner_s*2},{cy-30*inner_s} {cx},{cy+20*inner_s*2}" fill="none" stroke="#000" stroke-width="2"/>')
    elements.append(f'<text x="{cx}" y="{cy+5}" text-anchor="middle" font-size="16" font-weight="bold">2</text>')
    return "\n".join(elements)

def draw_car(cx, cy, scale=1.0):
    """Draw a car with numbered regions."""
    s = scale
    elements = []
    # Body - region 1
    elements.append(f'<rect x="{cx-90*s}" y="{cy-10*s}" width="{180*s}" height="{50*s}" rx="10" fill="none" stroke="#000" stroke-width="2.5"/>')
    elements.append(f'<text x="{cx}" y="{cy+20*s}" text-anchor="middle" font-size="18" font-weight="bold">1</text>')
    # Top/cabin - region 2
    elements.append(f'<path d="M{cx-50*s},{cy-10*s} L{cx-35*s},{cy-55*s} L{cx+35*s},{cy-55*s} L{cx+50*s},{cy-10*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
    elements.append(f'<text x="{cx}" y="{cy-25*s}" text-anchor="middle" font-size="16" font-weight="bold">2</text>')
    # Windows - region 3
    elements.append(f'<rect x="{cx-30*s}" y="{cy-48*s}" width="{25*s}" height="{30*s}" fill="none" stroke="#000" stroke-width="2"/>')
    elements.append(f'<text x="{cx-18*s}" y="{cy-30*s}" text-anchor="middle" font-size="12" font-weight="bold">3</text>')
    elements.append(f'<rect x="{cx+5*s}" y="{cy-48*s}" width="{25*s}" height="{30*s}" fill="none" stroke="#000" stroke-width="2"/>')
    elements.append(f'<text x="{cx+18*s}" y="{cy-30*s}" text-anchor="middle" font-size="12" font-weight="bold">3</text>')
    # Wheels - region 4
    elements.append(f'<circle cx="{cx-50*s}" cy="{cy+40*s}" r="{22*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
    elements.append(f'<circle cx="{cx-50*s}" cy="{cy+40*s}" r="{10*s}" fill="none" stroke="#000" stroke-width="2"/>')
    elements.append(f'<text x="{cx-50*s}" y="{cy+44*s}" text-anchor="middle" font-size="12" font-weight="bold">4</text>')
    elements.append(f'<circle cx="{cx+50*s}" cy="{cy+40*s}" r="{22*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
    elements.append(f'<circle cx="{cx+50*s}" cy="{cy+40*s}" r="{10*s}" fill="none" stroke="#000" stroke-width="2"/>')
    elements.append(f'<text x="{cx+50*s}" y="{cy+44*s}" text-anchor="middle" font-size="12" font-weight="bold">4</text>')
    # Headlight - region 5
    elements.append(f'<circle cx="{cx+80*s}" cy="{cy+10*s}" r="{10*s}" fill="none" stroke="#000" stroke-width="2"/>')
    elements.append(f'<text x="{cx+80*s}" y="{cy+14*s}" text-anchor="middle" font-size="10" font-weight="bold">5</text>')
    return "\n".join(elements)


def draw_tree(cx, cy, scale=1.0):
    """Draw a tree with numbered regions."""
    s = scale
    elements = []
    # Trunk - region 1
    elements.append(f'<rect x="{cx-15*s}" y="{cy+20*s}" width="{30*s}" height="{80*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
    elements.append(f'<text x="{cx}" y="{cy+65*s}" text-anchor="middle" font-size="16" font-weight="bold">1</text>')
    # Crown layers - region 2, 3
    elements.append(f'<ellipse cx="{cx}" cy="{cy-20*s}" rx="{70*s}" ry="{50*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
    elements.append(f'<text x="{cx-30*s}" y="{cy-10*s}" text-anchor="middle" font-size="18" font-weight="bold">2</text>')
    elements.append(f'<text x="{cx+30*s}" y="{cy-10*s}" text-anchor="middle" font-size="18" font-weight="bold">2</text>')
    elements.append(f'<ellipse cx="{cx}" cy="{cy-60*s}" rx="{50*s}" ry="{35*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
    elements.append(f'<text x="{cx}" y="{cy-55*s}" text-anchor="middle" font-size="16" font-weight="bold">3</text>')
    # Apples - region 4
    for ax, ay in [(cx-40*s, cy-30*s), (cx+35*s, cy-40*s), (cx-10*s, cy-70*s), (cx+20*s, cy-15*s)]:
        elements.append(f'<circle cx="{ax}" cy="{ay}" r="{8*s}" fill="none" stroke="#000" stroke-width="2"/>')
        elements.append(f'<text x="{ax}" y="{ay+4}" text-anchor="middle" font-size="10" font-weight="bold">4</text>')
    return "\n".join(elements)

def draw_mushroom(cx, cy, scale=1.0):
    """Draw a mushroom with numbered regions."""
    s = scale
    elements = []
    # Cap (dome) - region 1
    elements.append(f'<path d="M{cx-70*s},{cy} A{70*s},{60*s} 0 0 1 {cx+70*s},{cy}" fill="none" stroke="#000" stroke-width="2.5"/>')
    elements.append(f'<line x1="{cx-70*s}" y1="{cy}" x2="{cx+70*s}" y2="{cy}" stroke="#000" stroke-width="2.5"/>')
    elements.append(f'<text x="{cx-35*s}" y="{cy-20*s}" text-anchor="middle" font-size="18" font-weight="bold">1</text>')
    elements.append(f'<text x="{cx+35*s}" y="{cy-20*s}" text-anchor="middle" font-size="18" font-weight="bold">1</text>')
    # Spots on cap - region 2
    spots = [(cx-30*s, cy-35*s), (cx+25*s, cy-40*s), (cx, cy-50*s), (cx-50*s, cy-15*s), (cx+45*s, cy-15*s)]
    for sx, sy in spots:
        elements.append(f'<circle cx="{sx}" cy="{sy}" r="{10*s}" fill="none" stroke="#000" stroke-width="2"/>')
        elements.append(f'<text x="{sx}" y="{sy+5}" text-anchor="middle" font-size="10" font-weight="bold">2</text>')
    # Stem - region 3
    elements.append(f'<path d="M{cx-25*s},{cy} L{cx-30*s},{cy+70*s} L{cx+30*s},{cy+70*s} L{cx+25*s},{cy}" fill="none" stroke="#000" stroke-width="2.5"/>')
    elements.append(f'<text x="{cx}" y="{cy+40*s}" text-anchor="middle" font-size="18" font-weight="bold">3</text>')
    # Ground - region 4
    elements.append(f'<ellipse cx="{cx}" cy="{cy+75*s}" rx="{50*s}" ry="{12*s}" fill="none" stroke="#000" stroke-width="2"/>')
    elements.append(f'<text x="{cx}" y="{cy+79*s}" text-anchor="middle" font-size="12" font-weight="bold">4</text>')
    return "\n".join(elements)


def draw_rocket(cx, cy, scale=1.0):
    """Draw a rocket with numbered regions."""
    s = scale
    elements = []
    # Body - region 1
    elements.append(f'<rect x="{cx-25*s}" y="{cy-50*s}" width="{50*s}" height="{120*s}" rx="5" fill="none" stroke="#000" stroke-width="2.5"/>')
    elements.append(f'<text x="{cx}" y="{cy+10*s}" text-anchor="middle" font-size="18" font-weight="bold">1</text>')
    # Nose cone - region 2
    elements.append(f'<polygon points="{cx-25*s},{cy-50*s} {cx},{cy-100*s} {cx+25*s},{cy-50*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
    elements.append(f'<text x="{cx}" y="{cy-60*s}" text-anchor="middle" font-size="14" font-weight="bold">2</text>')
    # Window - region 3
    elements.append(f'<circle cx="{cx}" cy="{cy-20*s}" r="{15*s}" fill="none" stroke="#000" stroke-width="2"/>')
    elements.append(f'<text x="{cx}" y="{cy-15*s}" text-anchor="middle" font-size="12" font-weight="bold">3</text>')
    # Fins - region 4
    elements.append(f'<polygon points="{cx-25*s},{cy+40*s} {cx-55*s},{cy+70*s} {cx-25*s},{cy+70*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
    elements.append(f'<text x="{cx-35*s}" y="{cy+60*s}" text-anchor="middle" font-size="11" font-weight="bold">4</text>')
    elements.append(f'<polygon points="{cx+25*s},{cy+40*s} {cx+55*s},{cy+70*s} {cx+25*s},{cy+70*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
    elements.append(f'<text x="{cx+35*s}" y="{cy+60*s}" text-anchor="middle" font-size="11" font-weight="bold">4</text>')
    # Flames - region 5
    elements.append(f'<polygon points="{cx-15*s},{cy+70*s} {cx},{cy+110*s} {cx+15*s},{cy+70*s}" fill="none" stroke="#000" stroke-width="2"/>')
    elements.append(f'<text x="{cx}" y="{cy+90*s}" text-anchor="middle" font-size="11" font-weight="bold">5</text>')
    return "\n".join(elements)

def draw_balloon(cx, cy, scale=1.0):
    """Draw a balloon with numbered regions."""
    s = scale
    elements = []
    # Balloon body - region 1
    elements.append(f'<ellipse cx="{cx}" cy="{cy-30*s}" rx="{55*s}" ry="{70*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
    elements.append(f'<text x="{cx}" y="{cy-25*s}" text-anchor="middle" font-size="20" font-weight="bold">1</text>')
    # Knot - region 2
    elements.append(f'<polygon points="{cx-8*s},{cy+40*s} {cx},{cy+55*s} {cx+8*s},{cy+40*s}" fill="none" stroke="#000" stroke-width="2"/>')
    elements.append(f'<text x="{cx}" y="{cy+50*s}" text-anchor="middle" font-size="10" font-weight="bold">2</text>')
    # String - region 3
    elements.append(f'<path d="M{cx},{cy+55*s} Q{cx+10*s},{cy+80*s} {cx-5*s},{cy+100*s} Q{cx-15*s},{cy+120*s} {cx},{cy+140*s}" fill="none" stroke="#000" stroke-width="2"/>')
    elements.append(f'<text x="{cx+15*s}" y="{cy+100*s}" text-anchor="middle" font-size="12" font-weight="bold">3</text>')
    # Highlight - region 4
    elements.append(f'<ellipse cx="{cx-20*s}" cy="{cy-50*s}" rx="{12*s}" ry="{20*s}" fill="none" stroke="#000" stroke-width="1.5" transform="rotate(-20,{cx-20*s},{cy-50*s})"/>')
    elements.append(f'<text x="{cx-20*s}" y="{cy-45*s}" text-anchor="middle" font-size="10" font-weight="bold">4</text>')
    return "\n".join(elements)


def draw_ice_cream(cx, cy, scale=1.0):
    """Draw an ice cream cone with numbered regions."""
    s = scale
    elements = []
    # Cone - region 3
    elements.append(f'<polygon points="{cx-40*s},{cy} {cx+40*s},{cy} {cx},{cy+100*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
    # Cone pattern
    for i in range(-1, 2):
        elements.append(f'<line x1="{cx+i*20*s}" y1="{cy}" x2="{cx}" y2="{cy+100*s}" stroke="#000" stroke-width="1"/>')
    for i in range(1, 4):
        y = cy + i*25*s
        w = 40*s - i*10*s
        elements.append(f'<line x1="{cx-w}" y1="{y}" x2="{cx+w}" y2="{y}" stroke="#000" stroke-width="1"/>')
    elements.append(f'<text x="{cx}" y="{cy+55*s}" text-anchor="middle" font-size="16" font-weight="bold">3</text>')
    # Scoop 1 (bottom) - region 1
    elements.append(f'<circle cx="{cx}" cy="{cy-25*s}" r="{40*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
    elements.append(f'<text x="{cx}" y="{cy-20*s}" text-anchor="middle" font-size="18" font-weight="bold">1</text>')
    # Scoop 2 (top) - region 2
    elements.append(f'<circle cx="{cx}" cy="{cy-70*s}" r="{35*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
    elements.append(f'<text x="{cx}" y="{cy-65*s}" text-anchor="middle" font-size="16" font-weight="bold">2</text>')
    # Cherry - region 4
    elements.append(f'<circle cx="{cx}" cy="{cy-105*s}" r="{12*s}" fill="none" stroke="#000" stroke-width="2"/>')
    elements.append(f'<text x="{cx}" y="{cy-101*s}" text-anchor="middle" font-size="11" font-weight="bold">4</text>')
    return "\n".join(elements)

def draw_cat(cx, cy, scale=1.0):
    """Draw a cat face with numbered regions."""
    s = scale
    elements = []
    # Head - region 1
    elements.append(f'<circle cx="{cx}" cy="{cy}" r="{70*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
    elements.append(f'<text x="{cx}" y="{cy+40*s}" text-anchor="middle" font-size="18" font-weight="bold">1</text>')
    # Ears - region 2
    elements.append(f'<polygon points="{cx-55*s},{cy-45*s} {cx-35*s},{cy-90*s} {cx-20*s},{cy-50*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
    elements.append(f'<text x="{cx-38*s}" y="{cy-58*s}" text-anchor="middle" font-size="12" font-weight="bold">2</text>')
    elements.append(f'<polygon points="{cx+55*s},{cy-45*s} {cx+35*s},{cy-90*s} {cx+20*s},{cy-50*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
    elements.append(f'<text x="{cx+38*s}" y="{cy-58*s}" text-anchor="middle" font-size="12" font-weight="bold">2</text>')
    # Inner ears - region 3
    elements.append(f'<polygon points="{cx-48*s},{cy-50*s} {cx-37*s},{cy-78*s} {cx-26*s},{cy-53*s}" fill="none" stroke="#000" stroke-width="1.5"/>')
    elements.append(f'<text x="{cx-37*s}" y="{cy-55*s}" text-anchor="middle" font-size="9" font-weight="bold">3</text>')
    elements.append(f'<polygon points="{cx+48*s},{cy-50*s} {cx+37*s},{cy-78*s} {cx+26*s},{cy-53*s}" fill="none" stroke="#000" stroke-width="1.5"/>')
    elements.append(f'<text x="{cx+37*s}" y="{cy-55*s}" text-anchor="middle" font-size="9" font-weight="bold">3</text>')
    # Eyes
    elements.append(f'<ellipse cx="{cx-25*s}" cy="{cy-10*s}" rx="{15*s}" ry="{18*s}" fill="none" stroke="#000" stroke-width="2"/>')
    elements.append(f'<ellipse cx="{cx+25*s}" cy="{cy-10*s}" rx="{15*s}" ry="{18*s}" fill="none" stroke="#000" stroke-width="2"/>')
    elements.append(f'<circle cx="{cx-25*s}" cy="{cy-8*s}" r="{8*s}" fill="#000"/>')
    elements.append(f'<circle cx="{cx+25*s}" cy="{cy-8*s}" r="{8*s}" fill="#000"/>')
    # Nose - region 4
    elements.append(f'<polygon points="{cx},{cy+5*s} {cx-8*s},{cy+15*s} {cx+8*s},{cy+15*s}" fill="none" stroke="#000" stroke-width="2"/>')
    elements.append(f'<text x="{cx}" y="{cy+30*s}" text-anchor="middle" font-size="10" font-weight="bold">4</text>')
    # Whiskers
    elements.append(f'<line x1="{cx-70*s}" y1="{cy+10*s}" x2="{cx-30*s}" y2="{cy+15*s}" stroke="#000" stroke-width="1.5"/>')
    elements.append(f'<line x1="{cx-65*s}" y1="{cy+20*s}" x2="{cx-30*s}" y2="{cy+20*s}" stroke="#000" stroke-width="1.5"/>')
    elements.append(f'<line x1="{cx+70*s}" y1="{cy+10*s}" x2="{cx+30*s}" y2="{cy+15*s}" stroke="#000" stroke-width="1.5"/>')
    elements.append(f'<line x1="{cx+65*s}" y1="{cy+20*s}" x2="{cx+30*s}" y2="{cy+20*s}" stroke="#000" stroke-width="1.5"/>')
    return "\n".join(elements)


def draw_umbrella(cx, cy, scale=1.0):
    """Draw an umbrella with numbered regions."""
    s = scale
    elements = []
    # Canopy - region 1
    elements.append(f'<path d="M{cx-80*s},{cy} A{80*s},{70*s} 0 0 1 {cx+80*s},{cy}" fill="none" stroke="#000" stroke-width="2.5"/>')
    elements.append(f'<line x1="{cx-80*s}" y1="{cy}" x2="{cx+80*s}" y2="{cy}" stroke="#000" stroke-width="2.5"/>')
    elements.append(f'<text x="{cx}" y="{cy-25*s}" text-anchor="middle" font-size="18" font-weight="bold">1</text>')
    # Scallops
    for i in range(4):
        sx = cx - 60*s + i*40*s
        elements.append(f'<path d="M{sx},{cy} A{20*s},{15*s} 0 0 0 {sx+40*s},{cy}" fill="none" stroke="#000" stroke-width="2"/>')
    # Sections - region 2
    elements.append(f'<line x1="{cx-40*s}" y1="{cy}" x2="{cx-20*s}" y2="{cy-60*s}" stroke="#000" stroke-width="1.5"/>')
    elements.append(f'<line x1="{cx}" y1="{cy}" x2="{cx}" y2="{cy-70*s}" stroke="#000" stroke-width="1.5"/>')
    elements.append(f'<line x1="{cx+40*s}" y1="{cy}" x2="{cx+20*s}" y2="{cy-60*s}" stroke="#000" stroke-width="1.5"/>')
    elements.append(f'<text x="{cx-40*s}" y="{cy-20*s}" text-anchor="middle" font-size="12" font-weight="bold">2</text>')
    elements.append(f'<text x="{cx+40*s}" y="{cy-20*s}" text-anchor="middle" font-size="12" font-weight="bold">2</text>')
    # Handle - region 3
    elements.append(f'<line x1="{cx}" y1="{cy}" x2="{cx}" y2="{cy+80*s}" stroke="#000" stroke-width="3"/>')
    elements.append(f'<path d="M{cx},{cy+80*s} A{12*s},{12*s} 0 0 1 {cx+24*s},{cy+80*s}" fill="none" stroke="#000" stroke-width="3"/>')
    elements.append(f'<text x="{cx+15*s}" y="{cy+50*s}" text-anchor="middle" font-size="14" font-weight="bold">3</text>')
    # Tip - region 4
    elements.append(f'<circle cx="{cx}" cy="{cy-70*s}" r="{6*s}" fill="none" stroke="#000" stroke-width="2"/>')
    elements.append(f'<text x="{cx+12*s}" y="{cy-68*s}" text-anchor="middle" font-size="10" font-weight="bold">4</text>')
    return "\n".join(elements)

def draw_apple(cx, cy, scale=1.0):
    """Draw an apple with numbered regions."""
    s = scale
    elements = []
    # Apple body - region 1
    elements.append(f'<path d="M{cx},{cy+70*s} C{cx-90*s},{cy+70*s} {cx-90*s},{cy-40*s} {cx},{cy-30*s} C{cx+90*s},{cy-40*s} {cx+90*s},{cy+70*s} {cx},{cy+70*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
    elements.append(f'<text x="{cx-30*s}" y="{cy+20*s}" text-anchor="middle" font-size="18" font-weight="bold">1</text>')
    elements.append(f'<text x="{cx+30*s}" y="{cy+20*s}" text-anchor="middle" font-size="18" font-weight="bold">1</text>')
    # Stem - region 2
    elements.append(f'<path d="M{cx},{cy-30*s} Q{cx+5*s},{cy-50*s} {cx+3*s},{cy-60*s}" fill="none" stroke="#000" stroke-width="3"/>')
    elements.append(f'<text x="{cx+15*s}" y="{cy-40*s}" text-anchor="middle" font-size="12" font-weight="bold">2</text>')
    # Leaf - region 3
    elements.append(f'<ellipse cx="{cx+20*s}" cy="{cy-50*s}" rx="{20*s}" ry="{10*s}" fill="none" stroke="#000" stroke-width="2" transform="rotate(-30,{cx+20*s},{cy-50*s})"/>')
    elements.append(f'<text x="{cx+25*s}" y="{cy-47*s}" text-anchor="middle" font-size="10" font-weight="bold">3</text>')
    return "\n".join(elements)


def draw_boat(cx, cy, scale=1.0):
    """Draw a sailboat with numbered regions."""
    s = scale
    elements = []
    # Hull - region 1
    elements.append(f'<polygon points="{cx-70*s},{cy+20*s} {cx-50*s},{cy+60*s} {cx+50*s},{cy+60*s} {cx+70*s},{cy+20*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
    elements.append(f'<text x="{cx}" y="{cy+45*s}" text-anchor="middle" font-size="16" font-weight="bold">1</text>')
    # Mast - region 2
    elements.append(f'<line x1="{cx}" y1="{cy+20*s}" x2="{cx}" y2="{cy-90*s}" stroke="#000" stroke-width="3"/>')
    elements.append(f'<text x="{cx+12*s}" y="{cy-40*s}" text-anchor="middle" font-size="12" font-weight="bold">2</text>')
    # Sail left - region 3
    elements.append(f'<polygon points="{cx},{cy-85*s} {cx},{cy+15*s} {cx-55*s},{cy+15*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
    elements.append(f'<text x="{cx-25*s}" y="{cy}" text-anchor="middle" font-size="16" font-weight="bold">3</text>')
    # Sail right - region 4
    elements.append(f'<polygon points="{cx},{cy-85*s} {cx},{cy+15*s} {cx+45*s},{cy+15*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
    elements.append(f'<text x="{cx+20*s}" y="{cy}" text-anchor="middle" font-size="14" font-weight="bold">4</text>')
    # Flag - region 5
    elements.append(f'<polygon points="{cx},{cy-90*s} {cx+25*s},{cy-80*s} {cx},{cy-70*s}" fill="none" stroke="#000" stroke-width="2"/>')
    elements.append(f'<text x="{cx+10*s}" y="{cy-77*s}" text-anchor="middle" font-size="10" font-weight="bold">5</text>')
    # Waves
    elements.append(f'<path d="M{cx-100*s},{cy+65*s} Q{cx-75*s},{cy+55*s} {cx-50*s},{cy+65*s} Q{cx-25*s},{cy+75*s} {cx},{cy+65*s} Q{cx+25*s},{cy+55*s} {cx+50*s},{cy+65*s} Q{cx+75*s},{cy+75*s} {cx+100*s},{cy+65*s}" fill="none" stroke="#000" stroke-width="1.5"/>')
    return "\n".join(elements)

def draw_rainbow(cx, cy, scale=1.0):
    """Draw a rainbow with numbered regions."""
    s = scale
    elements = []
    colors_num = 5
    for i in range(colors_num):
        r = (90 - i*15) * s
        elements.append(f'<path d="M{cx-r},{cy+20*s} A{r},{r} 0 0 1 {cx+r},{cy+20*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
        # Number in each band
        band_r = (90 - i*15 - 7) * s
        elements.append(f'<text x="{cx}" y="{cy+20*s - band_r}" text-anchor="middle" font-size="14" font-weight="bold">{i+1}</text>')
    # Clouds at ends
    for side in [-1, 1]:
        cloud_cx = cx + side * 85 * s
        cloud_cy = cy + 25 * s
        elements.append(f'<circle cx="{cloud_cx}" cy="{cloud_cy}" r="{20*s}" fill="none" stroke="#000" stroke-width="2"/>')
        elements.append(f'<circle cx="{cloud_cx + side*15*s}" cy="{cloud_cy-5*s}" r="{15*s}" fill="none" stroke="#000" stroke-width="2"/>')
        elements.append(f'<circle cx="{cloud_cx + side*-10*s}" cy="{cloud_cy+5*s}" r="{15*s}" fill="none" stroke="#000" stroke-width="2"/>')
    return "\n".join(elements)


def draw_snail(cx, cy, scale=1.0):
    """Draw a snail with numbered regions."""
    s = scale
    elements = []
    # Shell spiral - region 1
    elements.append(f'<circle cx="{cx+10*s}" cy="{cy-15*s}" r="{50*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
    elements.append(f'<circle cx="{cx+10*s}" cy="{cy-15*s}" r="{35*s}" fill="none" stroke="#000" stroke-width="2"/>')
    elements.append(f'<circle cx="{cx+10*s}" cy="{cy-15*s}" r="{20*s}" fill="none" stroke="#000" stroke-width="1.5"/>')
    elements.append(f'<text x="{cx+10*s}" y="{cy-30*s}" text-anchor="middle" font-size="16" font-weight="bold">1</text>')
    elements.append(f'<text x="{cx+10*s}" y="{cy}" text-anchor="middle" font-size="12" font-weight="bold">2</text>')
    # Body - region 3
    elements.append(f'<ellipse cx="{cx-30*s}" cy="{cy+30*s}" rx="{70*s}" ry="{20*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
    elements.append(f'<text x="{cx-50*s}" y="{cy+35*s}" text-anchor="middle" font-size="16" font-weight="bold">3</text>')
    # Head
    elements.append(f'<circle cx="{cx-80*s}" cy="{cy+10*s}" r="{18*s}" fill="none" stroke="#000" stroke-width="2"/>')
    # Eyes on stalks - region 4
    elements.append(f'<line x1="{cx-85*s}" y1="{cy}" x2="{cx-95*s}" y2="{cy-25*s}" stroke="#000" stroke-width="2"/>')
    elements.append(f'<circle cx="{cx-95*s}" cy="{cy-28*s}" r="{5*s}" fill="none" stroke="#000" stroke-width="2"/>')
    elements.append(f'<line x1="{cx-75*s}" y1="{cy}" x2="{cx-70*s}" y2="{cy-25*s}" stroke="#000" stroke-width="2"/>')
    elements.append(f'<circle cx="{cx-70*s}" cy="{cy-28*s}" r="{5*s}" fill="none" stroke="#000" stroke-width="2"/>')
    elements.append(f'<text x="{cx-80*s}" y="{cy+15*s}" text-anchor="middle" font-size="12" font-weight="bold">4</text>')
    # Smile
    elements.append(f'<path d="M{cx-87*s},{cy+15*s} Q{cx-80*s},{cy+22*s} {cx-73*s},{cy+15*s}" fill="none" stroke="#000" stroke-width="1.5"/>')
    return "\n".join(elements)

def draw_ladybug(cx, cy, scale=1.0):
    """Draw a ladybug with numbered regions."""
    s = scale
    elements = []
    # Body - region 1
    elements.append(f'<ellipse cx="{cx}" cy="{cy}" rx="{70*s}" ry="{55*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
    elements.append(f'<text x="{cx-30*s}" y="{cy+30*s}" text-anchor="middle" font-size="18" font-weight="bold">1</text>')
    elements.append(f'<text x="{cx+30*s}" y="{cy+30*s}" text-anchor="middle" font-size="18" font-weight="bold">1</text>')
    # Center line
    elements.append(f'<line x1="{cx}" y1="{cy-55*s}" x2="{cx}" y2="{cy+55*s}" stroke="#000" stroke-width="2.5"/>')
    # Head - region 2
    elements.append(f'<circle cx="{cx}" cy="{cy-65*s}" r="{25*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
    elements.append(f'<text x="{cx}" y="{cy-60*s}" text-anchor="middle" font-size="14" font-weight="bold">2</text>')
    # Spots - region 3
    spots = [(cx-30*s, cy-15*s), (cx+30*s, cy-15*s), (cx-25*s, cy+20*s), (cx+25*s, cy+20*s), (cx-40*s, cy+5*s), (cx+40*s, cy+5*s)]
    for sx, sy in spots:
        elements.append(f'<circle cx="{sx}" cy="{sy}" r="{12*s}" fill="none" stroke="#000" stroke-width="2"/>')
        elements.append(f'<text x="{sx}" y="{sy+5}" text-anchor="middle" font-size="10" font-weight="bold">3</text>')
    # Antennae
    elements.append(f'<line x1="{cx-10*s}" y1="{cy-85*s}" x2="{cx-25*s}" y2="{cy-100*s}" stroke="#000" stroke-width="2"/>')
    elements.append(f'<circle cx="{cx-25*s}" cy="{cy-103*s}" r="{4*s}" fill="#000"/>')
    elements.append(f'<line x1="{cx+10*s}" y1="{cy-85*s}" x2="{cx+25*s}" y2="{cy-100*s}" stroke="#000" stroke-width="2"/>')
    elements.append(f'<circle cx="{cx+25*s}" cy="{cy-103*s}" r="{4*s}" fill="#000"/>')
    return "\n".join(elements)


def draw_castle(cx, cy, scale=1.0):
    """Draw a castle with numbered regions."""
    s = scale
    elements = []
    # Main wall - region 1
    elements.append(f'<rect x="{cx-60*s}" y="{cy-20*s}" width="{120*s}" height="{80*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
    elements.append(f'<text x="{cx}" y="{cy+20*s}" text-anchor="middle" font-size="18" font-weight="bold">1</text>')
    # Left tower - region 2
    elements.append(f'<rect x="{cx-80*s}" y="{cy-60*s}" width="{30*s}" height="{120*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
    elements.append(f'<text x="{cx-65*s}" y="{cy+10*s}" text-anchor="middle" font-size="12" font-weight="bold">2</text>')
    # Right tower - region 2
    elements.append(f'<rect x="{cx+50*s}" y="{cy-60*s}" width="{30*s}" height="{120*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
    elements.append(f'<text x="{cx+65*s}" y="{cy+10*s}" text-anchor="middle" font-size="12" font-weight="bold">2</text>')
    # Tower tops - region 3
    elements.append(f'<polygon points="{cx-85*s},{cy-60*s} {cx-65*s},{cy-90*s} {cx-45*s},{cy-60*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
    elements.append(f'<text x="{cx-65*s}" y="{cy-63*s}" text-anchor="middle" font-size="10" font-weight="bold">3</text>')
    elements.append(f'<polygon points="{cx+45*s},{cy-60*s} {cx+65*s},{cy-90*s} {cx+85*s},{cy-60*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
    elements.append(f'<text x="{cx+65*s}" y="{cy-63*s}" text-anchor="middle" font-size="10" font-weight="bold">3</text>')
    # Gate - region 4
    elements.append(f'<path d="M{cx-18*s},{cy+60*s} L{cx-18*s},{cy+20*s} A{18*s},{18*s} 0 0 1 {cx+18*s},{cy+20*s} L{cx+18*s},{cy+60*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
    elements.append(f'<text x="{cx}" y="{cy+45*s}" text-anchor="middle" font-size="12" font-weight="bold">4</text>')
    # Windows - region 5
    elements.append(f'<rect x="{cx-55*s}" y="{cy-10*s}" width="{15*s}" height="{20*s}" fill="none" stroke="#000" stroke-width="2"/>')
    elements.append(f'<text x="{cx-48*s}" y="{cy+5*s}" text-anchor="middle" font-size="8" font-weight="bold">5</text>')
    elements.append(f'<rect x="{cx+40*s}" y="{cy-10*s}" width="{15*s}" height="{20*s}" fill="none" stroke="#000" stroke-width="2"/>')
    elements.append(f'<text x="{cx+48*s}" y="{cy+5*s}" text-anchor="middle" font-size="8" font-weight="bold">5</text>')
    # Flags
    elements.append(f'<line x1="{cx-65*s}" y1="{cy-90*s}" x2="{cx-65*s}" y2="{cy-105*s}" stroke="#000" stroke-width="2"/>')
    elements.append(f'<polygon points="{cx-65*s},{cy-105*s} {cx-50*s},{cy-100*s} {cx-65*s},{cy-95*s}" fill="none" stroke="#000" stroke-width="1.5"/>')
    elements.append(f'<line x1="{cx+65*s}" y1="{cy-90*s}" x2="{cx+65*s}" y2="{cy-105*s}" stroke="#000" stroke-width="2"/>')
    elements.append(f'<polygon points="{cx+65*s},{cy-105*s} {cx+80*s},{cy-100*s} {cx+65*s},{cy-95*s}" fill="none" stroke="#000" stroke-width="1.5"/>')
    return "\n".join(elements)

def draw_duck(cx, cy, scale=1.0):
    """Draw a duck with numbered regions."""
    s = scale
    elements = []
    # Body - region 1
    elements.append(f'<ellipse cx="{cx}" cy="{cy+20*s}" rx="{70*s}" ry="{45*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
    elements.append(f'<text x="{cx}" y="{cy+30*s}" text-anchor="middle" font-size="18" font-weight="bold">1</text>')
    # Head - region 2
    elements.append(f'<circle cx="{cx-50*s}" cy="{cy-40*s}" r="{30*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
    elements.append(f'<text x="{cx-50*s}" y="{cy-35*s}" text-anchor="middle" font-size="16" font-weight="bold">2</text>')
    # Neck connecting
    elements.append(f'<path d="M{cx-35*s},{cy-15*s} Q{cx-40*s},{cy} {cx-30*s},{cy-20*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
    # Beak - region 3
    elements.append(f'<ellipse cx="{cx-82*s}" cy="{cy-40*s}" rx="{20*s}" ry="{8*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
    elements.append(f'<text x="{cx-82*s}" y="{cy-37*s}" text-anchor="middle" font-size="10" font-weight="bold">3</text>')
    # Eye
    elements.append(f'<circle cx="{cx-45*s}" cy="{cy-48*s}" r="{6*s}" fill="#000"/>')
    # Wing - region 4
    elements.append(f'<ellipse cx="{cx+10*s}" cy="{cy+15*s}" rx="{35*s}" ry="{25*s}" fill="none" stroke="#000" stroke-width="2" transform="rotate(-10,{cx+10*s},{cy+15*s})"/>')
    elements.append(f'<text x="{cx+10*s}" y="{cy+20*s}" text-anchor="middle" font-size="14" font-weight="bold">4</text>')
    # Water waves - region 5
    elements.append(f'<path d="M{cx-90*s},{cy+65*s} Q{cx-60*s},{cy+55*s} {cx-30*s},{cy+65*s} Q{cx},{cy+75*s} {cx+30*s},{cy+65*s} Q{cx+60*s},{cy+55*s} {cx+90*s},{cy+65*s}" fill="none" stroke="#000" stroke-width="2"/>')
    elements.append(f'<text x="{cx+60*s}" y="{cy+62*s}" text-anchor="middle" font-size="12" font-weight="bold">5</text>')
    return "\n".join(elements)


def draw_kite(cx, cy, scale=1.0):
    """Draw a kite with numbered regions."""
    s = scale
    elements = []
    # Kite body - region 1
    elements.append(f'<polygon points="{cx},{cy-80*s} {cx+50*s},{cy} {cx},{cy+60*s} {cx-50*s},{cy}" fill="none" stroke="#000" stroke-width="2.5"/>')
    # Cross lines
    elements.append(f'<line x1="{cx}" y1="{cy-80*s}" x2="{cx}" y2="{cy+60*s}" stroke="#000" stroke-width="1.5"/>')
    elements.append(f'<line x1="{cx-50*s}" y1="{cy}" x2="{cx+50*s}" y2="{cy}" stroke="#000" stroke-width="1.5"/>')
    # Quadrants numbered
    elements.append(f'<text x="{cx-18*s}" y="{cy-25*s}" text-anchor="middle" font-size="16" font-weight="bold">1</text>')
    elements.append(f'<text x="{cx+18*s}" y="{cy-25*s}" text-anchor="middle" font-size="16" font-weight="bold">2</text>')
    elements.append(f'<text x="{cx-18*s}" y="{cy+25*s}" text-anchor="middle" font-size="16" font-weight="bold">3</text>')
    elements.append(f'<text x="{cx+18*s}" y="{cy+25*s}" text-anchor="middle" font-size="16" font-weight="bold">4</text>')
    # Tail - region 5
    elements.append(f'<path d="M{cx},{cy+60*s} Q{cx+15*s},{cy+80*s} {cx-10*s},{cy+100*s} Q{cx-25*s},{cy+120*s} {cx+5*s},{cy+140*s}" fill="none" stroke="#000" stroke-width="2"/>')
    # Bows on tail
    for i in range(3):
        ty = cy + 80*s + i*30*s
        elements.append(f'<polygon points="{cx-5*s+i*3*s},{ty} {cx-15*s+i*3*s},{ty-5*s} {cx-15*s+i*3*s},{ty+5*s}" fill="none" stroke="#000" stroke-width="1.5"/>')
        elements.append(f'<polygon points="{cx+5*s+i*3*s},{ty} {cx+15*s+i*3*s},{ty-5*s} {cx+15*s+i*3*s},{ty+5*s}" fill="none" stroke="#000" stroke-width="1.5"/>')
    elements.append(f'<text x="{cx+20*s}" y="{cy+95*s}" text-anchor="middle" font-size="12" font-weight="bold">5</text>')
    return "\n".join(elements)

def draw_snowman(cx, cy, scale=1.0):
    """Draw a snowman with numbered regions."""
    s = scale
    elements = []
    # Bottom ball - region 1
    elements.append(f'<circle cx="{cx}" cy="{cy+50*s}" r="{50*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
    elements.append(f'<text x="{cx}" y="{cy+55*s}" text-anchor="middle" font-size="18" font-weight="bold">1</text>')
    # Middle ball - region 2
    elements.append(f'<circle cx="{cx}" cy="{cy-10*s}" r="{38*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
    elements.append(f'<text x="{cx}" y="{cy-5*s}" text-anchor="middle" font-size="16" font-weight="bold">2</text>')
    # Head - region 3
    elements.append(f'<circle cx="{cx}" cy="{cy-62*s}" r="{28*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
    elements.append(f'<text x="{cx}" y="{cy-57*s}" text-anchor="middle" font-size="14" font-weight="bold">3</text>')
    # Hat - region 4
    elements.append(f'<rect x="{cx-20*s}" y="{cy-110*s}" width="{40*s}" height="{30*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
    elements.append(f'<line x1="{cx-30*s}" y1="{cy-80*s}" x2="{cx+30*s}" y2="{cy-80*s}" stroke="#000" stroke-width="3"/>')
    elements.append(f'<text x="{cx}" y="{cy-90*s}" text-anchor="middle" font-size="12" font-weight="bold">4</text>')
    # Buttons - region 5
    for i in range(3):
        by = cy - 20*s + i*15*s
        elements.append(f'<circle cx="{cx}" cy="{by}" r="{5*s}" fill="none" stroke="#000" stroke-width="2"/>')
    elements.append(f'<text x="{cx+15*s}" y="{cy-10*s}" text-anchor="middle" font-size="10" font-weight="bold">5</text>')
    # Eyes and nose
    elements.append(f'<circle cx="{cx-10*s}" cy="{cy-68*s}" r="{4*s}" fill="#000"/>')
    elements.append(f'<circle cx="{cx+10*s}" cy="{cy-68*s}" r="{4*s}" fill="#000"/>')
    elements.append(f'<polygon points="{cx},{cy-60*s} {cx+15*s},{cy-55*s} {cx},{cy-52*s}" fill="none" stroke="#000" stroke-width="2"/>')
    # Arms
    elements.append(f'<line x1="{cx-38*s}" y1="{cy-15*s}" x2="{cx-70*s}" y2="{cy-35*s}" stroke="#000" stroke-width="2.5"/>')
    elements.append(f'<line x1="{cx+38*s}" y1="{cy-15*s}" x2="{cx+70*s}" y2="{cy-35*s}" stroke="#000" stroke-width="2.5"/>')
    return "\n".join(elements)


def draw_bee(cx, cy, scale=1.0):
    """Draw a bee with numbered regions."""
    s = scale
    elements = []
    # Body - region 1
    elements.append(f'<ellipse cx="{cx+20*s}" cy="{cy}" rx="{55*s}" ry="{40*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
    # Stripes - region 2
    for i in range(4):
        sx = cx - 5*s + i*18*s
        elements.append(f'<line x1="{sx}" y1="{cy-35*s}" x2="{sx}" y2="{cy+35*s}" stroke="#000" stroke-width="2"/>')
    elements.append(f'<text x="{cx+5*s}" y="{cy+5}" text-anchor="middle" font-size="14" font-weight="bold">1</text>')
    elements.append(f'<text x="{cx+35*s}" y="{cy+5}" text-anchor="middle" font-size="14" font-weight="bold">2</text>')
    # Head - region 3
    elements.append(f'<circle cx="{cx-40*s}" cy="{cy}" r="{25*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
    elements.append(f'<text x="{cx-40*s}" y="{cy+5}" text-anchor="middle" font-size="14" font-weight="bold">3</text>')
    # Eyes
    elements.append(f'<circle cx="{cx-47*s}" cy="{cy-8*s}" r="{6*s}" fill="#000"/>')
    elements.append(f'<circle cx="{cx-33*s}" cy="{cy-8*s}" r="{6*s}" fill="#000"/>')
    # Smile
    elements.append(f'<path d="M{cx-48*s},{cy+8*s} Q{cx-40*s},{cy+16*s} {cx-32*s},{cy+8*s}" fill="none" stroke="#000" stroke-width="1.5"/>')
    # Wings - region 4
    elements.append(f'<ellipse cx="{cx+10*s}" cy="{cy-45*s}" rx="{30*s}" ry="{18*s}" fill="none" stroke="#000" stroke-width="2" transform="rotate(-15,{cx+10*s},{cy-45*s})"/>')
    elements.append(f'<text x="{cx+10*s}" y="{cy-42*s}" text-anchor="middle" font-size="11" font-weight="bold">4</text>')
    elements.append(f'<ellipse cx="{cx+35*s}" cy="{cy-40*s}" rx="{25*s}" ry="{15*s}" fill="none" stroke="#000" stroke-width="2" transform="rotate(10,{cx+35*s},{cy-40*s})"/>')
    elements.append(f'<text x="{cx+35*s}" y="{cy-37*s}" text-anchor="middle" font-size="11" font-weight="bold">4</text>')
    # Stinger - region 5
    elements.append(f'<polygon points="{cx+75*s},{cy} {cx+90*s},{cy-3*s} {cx+90*s},{cy+3*s}" fill="none" stroke="#000" stroke-width="2"/>')
    elements.append(f'<text x="{cx+80*s}" y="{cy+15*s}" text-anchor="middle" font-size="10" font-weight="bold">5</text>')
    # Antennae
    elements.append(f'<line x1="{cx-50*s}" y1="{cy-25*s}" x2="{cx-60*s}" y2="{cy-45*s}" stroke="#000" stroke-width="2"/>')
    elements.append(f'<circle cx="{cx-60*s}" cy="{cy-48*s}" r="{4*s}" fill="#000"/>')
    elements.append(f'<line x1="{cx-35*s}" y1="{cy-25*s}" x2="{cx-30*s}" y2="{cy-45*s}" stroke="#000" stroke-width="2"/>')
    elements.append(f'<circle cx="{cx-30*s}" cy="{cy-48*s}" r="{4*s}" fill="#000"/>')
    return "\n".join(elements)

def draw_crown(cx, cy, scale=1.0):
    """Draw a crown with numbered regions."""
    s = scale
    elements = []
    # Crown base - region 1
    elements.append(f'<rect x="{cx-70*s}" y="{cy}" width="{140*s}" height="{40*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
    elements.append(f'<text x="{cx}" y="{cy+25}" text-anchor="middle" font-size="16" font-weight="bold">1</text>')
    # Crown points - region 2
    points_str = f"{cx-70*s},{cy} {cx-55*s},{cy-50*s} {cx-35*s},{cy-15*s} {cx-15*s},{cy-60*s} {cx},{cy-20*s} {cx+15*s},{cy-60*s} {cx+35*s},{cy-15*s} {cx+55*s},{cy-50*s} {cx+70*s},{cy}"
    elements.append(f'<polyline points="{points_str}" fill="none" stroke="#000" stroke-width="2.5"/>')
    elements.append(f'<text x="{cx-35*s}" y="{cy-8*s}" text-anchor="middle" font-size="12" font-weight="bold">2</text>')
    elements.append(f'<text x="{cx+35*s}" y="{cy-8*s}" text-anchor="middle" font-size="12" font-weight="bold">2</text>')
    # Jewels on points - region 3
    jewel_positions = [(cx-55*s, cy-45*s), (cx-15*s, cy-55*s), (cx+15*s, cy-55*s), (cx+55*s, cy-45*s)]
    for jx, jy in jewel_positions:
        elements.append(f'<circle cx="{jx}" cy="{jy}" r="{7*s}" fill="none" stroke="#000" stroke-width="2"/>')
        elements.append(f'<text x="{jx}" y="{jy+4}" text-anchor="middle" font-size="9" font-weight="bold">3</text>')
    # Center jewel - region 4
    elements.append(f'<circle cx="{cx}" cy="{cy+20}" r="{12*s}" fill="none" stroke="#000" stroke-width="2"/>')
    elements.append(f'<text x="{cx}" y="{cy+24}" text-anchor="middle" font-size="10" font-weight="bold">4</text>')
    # Band details - region 5
    elements.append(f'<line x1="{cx-70*s}" y1="{cy+13}" x2="{cx+70*s}" y2="{cy+13}" stroke="#000" stroke-width="1.5"/>')
    elements.append(f'<text x="{cx-50*s}" y="{cy+35}" text-anchor="middle" font-size="10" font-weight="bold">5</text>')
    return "\n".join(elements)


def draw_planet(cx, cy, scale=1.0):
    """Draw a planet with ring and numbered regions."""
    s = scale
    elements = []
    # Planet body - region 1
    elements.append(f'<circle cx="{cx}" cy="{cy}" r="{55*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
    elements.append(f'<text x="{cx}" y="{cy+7}" text-anchor="middle" font-size="20" font-weight="bold">1</text>')
    # Ring - region 2
    elements.append(f'<ellipse cx="{cx}" cy="{cy}" rx="{90*s}" ry="{20*s}" fill="none" stroke="#000" stroke-width="2.5" transform="rotate(-20,{cx},{cy})"/>')
    elements.append(f'<text x="{cx+70*s}" y="{cy-15*s}" text-anchor="middle" font-size="14" font-weight="bold">2</text>')
    # Surface features - region 3
    elements.append(f'<circle cx="{cx-20*s}" cy="{cy-15*s}" r="{15*s}" fill="none" stroke="#000" stroke-width="1.5"/>')
    elements.append(f'<text x="{cx-20*s}" y="{cy-11*s}" text-anchor="middle" font-size="10" font-weight="bold">3</text>')
    elements.append(f'<circle cx="{cx+15*s}" cy="{cy+20*s}" r="{10*s}" fill="none" stroke="#000" stroke-width="1.5"/>')
    elements.append(f'<text x="{cx+15*s}" y="{cy+24*s}" text-anchor="middle" font-size="9" font-weight="bold">3</text>')
    # Stars around - region 4
    star_pos = [(cx-80*s, cy-60*s), (cx+75*s, cy-50*s), (cx-70*s, cy+55*s), (cx+80*s, cy+45*s)]
    for sx_pos, sy_pos in star_pos:
        elements.append(f'<polygon points="{sx_pos},{sy_pos-8*s} {sx_pos+3*s},{sy_pos-3*s} {sx_pos+8*s},{sy_pos} {sx_pos+3*s},{sy_pos+3*s} {sx_pos},{sy_pos+8*s} {sx_pos-3*s},{sy_pos+3*s} {sx_pos-8*s},{sy_pos} {sx_pos-3*s},{sy_pos-3*s}" fill="none" stroke="#000" stroke-width="1.5"/>')
    elements.append(f'<text x="{cx-80*s}" y="{cy-47*s}" text-anchor="middle" font-size="10" font-weight="bold">4</text>')
    return "\n".join(elements)

def draw_popsicle(cx, cy, scale=1.0):
    """Draw a popsicle with numbered regions."""
    s = scale
    elements = []
    # Popsicle body - region 1
    elements.append(f'<rect x="{cx-30*s}" y="{cy-70*s}" width="{60*s}" height="{100*s}" rx="20" fill="none" stroke="#000" stroke-width="2.5"/>')
    elements.append(f'<text x="{cx}" y="{cy-15*s}" text-anchor="middle" font-size="20" font-weight="bold">1</text>')
    # Stripe - region 2
    elements.append(f'<rect x="{cx-30*s}" y="{cy-30*s}" width="{60*s}" height="{25*s}" fill="none" stroke="#000" stroke-width="2"/>')
    elements.append(f'<text x="{cx}" y="{cy-12*s}" text-anchor="middle" font-size="14" font-weight="bold">2</text>')
    # Stick - region 3
    elements.append(f'<rect x="{cx-8*s}" y="{cy+30*s}" width="{16*s}" height="{70*s}" rx="5" fill="none" stroke="#000" stroke-width="2.5"/>')
    elements.append(f'<text x="{cx}" y="{cy+70*s}" text-anchor="middle" font-size="14" font-weight="bold">3</text>')
    # Drip - region 4
    elements.append(f'<path d="M{cx+25*s},{cy+20*s} Q{cx+30*s},{cy+35*s} {cx+25*s},{cy+45*s} A{5*s},{5*s} 0 1 1 {cx+20*s},{cy+40*s}" fill="none" stroke="#000" stroke-width="2"/>')
    elements.append(f'<text x="{cx+35*s}" y="{cy+35*s}" text-anchor="middle" font-size="10" font-weight="bold">4</text>')
    return "\n".join(elements)


def draw_diamond(cx, cy, scale=1.0):
    """Draw a diamond/gem with numbered regions."""
    s = scale
    elements = []
    # Top facets
    elements.append(f'<polygon points="{cx},{cy-80*s} {cx-60*s},{cy-30*s} {cx+60*s},{cy-30*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
    elements.append(f'<text x="{cx}" y="{cy-45*s}" text-anchor="middle" font-size="16" font-weight="bold">1</text>')
    # Bottom point
    elements.append(f'<polygon points="{cx-60*s},{cy-30*s} {cx+60*s},{cy-30*s} {cx},{cy+70*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
    # Internal facet lines
    elements.append(f'<line x1="{cx-30*s}" y1="{cy-30*s}" x2="{cx-15*s}" y2="{cy+70*s}" stroke="#000" stroke-width="1.5"/>')
    elements.append(f'<line x1="{cx+30*s}" y1="{cy-30*s}" x2="{cx+15*s}" y2="{cy+70*s}" stroke="#000" stroke-width="1.5"/>')
    elements.append(f'<line x1="{cx}" y1="{cy-30*s}" x2="{cx}" y2="{cy+70*s}" stroke="#000" stroke-width="1.5"/>')
    elements.append(f'<text x="{cx-25*s}" y="{cy+10*s}" text-anchor="middle" font-size="14" font-weight="bold">2</text>')
    elements.append(f'<text x="{cx+25*s}" y="{cy+10*s}" text-anchor="middle" font-size="14" font-weight="bold">3</text>')
    elements.append(f'<text x="{cx}" y="{cy+30*s}" text-anchor="middle" font-size="14" font-weight="bold">4</text>')
    # Top line
    elements.append(f'<line x1="{cx-30*s}" y1="{cy-55*s}" x2="{cx-60*s}" y2="{cy-30*s}" stroke="#000" stroke-width="1.5"/>')
    elements.append(f'<line x1="{cx+30*s}" y1="{cy-55*s}" x2="{cx+60*s}" y2="{cy-30*s}" stroke="#000" stroke-width="1.5"/>')
    elements.append(f'<text x="{cx-35*s}" y="{cy-35*s}" text-anchor="middle" font-size="10" font-weight="bold">5</text>')
    elements.append(f'<text x="{cx+35*s}" y="{cy-35*s}" text-anchor="middle" font-size="10" font-weight="bold">5</text>')
    return "\n".join(elements)

def draw_candy(cx, cy, scale=1.0):
    """Draw a wrapped candy with numbered regions."""
    s = scale
    elements = []
    # Candy body - region 1
    elements.append(f'<ellipse cx="{cx}" cy="{cy}" rx="{50*s}" ry="{35*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
    elements.append(f'<text x="{cx}" y="{cy+6}" text-anchor="middle" font-size="18" font-weight="bold">1</text>')
    # Stripes - region 2
    elements.append(f'<line x1="{cx-20*s}" y1="{cy-33*s}" x2="{cx-20*s}" y2="{cy+33*s}" stroke="#000" stroke-width="2"/>')
    elements.append(f'<line x1="{cx+20*s}" y1="{cy-33*s}" x2="{cx+20*s}" y2="{cy+33*s}" stroke="#000" stroke-width="2"/>')
    elements.append(f'<text x="{cx-35*s}" y="{cy+6}" text-anchor="middle" font-size="12" font-weight="bold">2</text>')
    elements.append(f'<text x="{cx+35*s}" y="{cy+6}" text-anchor="middle" font-size="12" font-weight="bold">2</text>')
    # Left wrapper twist - region 3
    elements.append(f'<polygon points="{cx-50*s},{cy-10*s} {cx-90*s},{cy-25*s} {cx-90*s},{cy+25*s} {cx-50*s},{cy+10*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
    elements.append(f'<text x="{cx-70*s}" y="{cy+6}" text-anchor="middle" font-size="12" font-weight="bold">3</text>')
    # Right wrapper twist - region 4
    elements.append(f'<polygon points="{cx+50*s},{cy-10*s} {cx+90*s},{cy-25*s} {cx+90*s},{cy+25*s} {cx+50*s},{cy+10*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
    elements.append(f'<text x="{cx+70*s}" y="{cy+6}" text-anchor="middle" font-size="12" font-weight="bold">4</text>')
    # Wrapper lines
    elements.append(f'<line x1="{cx-70*s}" y1="{cy-20*s}" x2="{cx-70*s}" y2="{cy+20*s}" stroke="#000" stroke-width="1.5"/>')
    elements.append(f'<line x1="{cx+70*s}" y1="{cy-20*s}" x2="{cx+70*s}" y2="{cy+20*s}" stroke="#000" stroke-width="1.5"/>')
    return "\n".join(elements)


def draw_moon(cx, cy, scale=1.0):
    """Draw a crescent moon with stars."""
    s = scale
    elements = []
    # Moon crescent - region 1
    elements.append(f'<circle cx="{cx}" cy="{cy}" r="{60*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
    elements.append(f'<circle cx="{cx+25*s}" cy="{cy-10*s}" r="{50*s}" fill="white" stroke="#000" stroke-width="2.5"/>')
    elements.append(f'<text x="{cx-25*s}" y="{cy+10*s}" text-anchor="middle" font-size="18" font-weight="bold">1</text>')
    # Stars - region 2
    star_positions = [(cx+50*s, cy-50*s), (cx+70*s, cy+10*s), (cx+40*s, cy+50*s), (cx-60*s, cy-60*s)]
    for sx_pos, sy_pos in star_positions:
        pts = []
        for i in range(10):
            angle = math.radians(i * 36 - 90)
            r = 12*s if i % 2 == 0 else 6*s
            pts.append(f"{sx_pos + r*math.cos(angle)},{sy_pos + r*math.sin(angle)}")
        elements.append(f'<polygon points="{" ".join(pts)}" fill="none" stroke="#000" stroke-width="1.5"/>')
        elements.append(f'<text x="{sx_pos}" y="{sy_pos+4}" text-anchor="middle" font-size="9" font-weight="bold">2</text>')
    # Face on moon
    elements.append(f'<circle cx="{cx-30*s}" cy="{cy-10*s}" r="{4*s}" fill="#000"/>')
    elements.append(f'<path d="M{cx-38*s},{cy+10*s} Q{cx-30*s},{cy+18*s} {cx-22*s},{cy+10*s}" fill="none" stroke="#000" stroke-width="1.5"/>')
    return "\n".join(elements)

def draw_turtle(cx, cy, scale=1.0):
    """Draw a turtle with numbered regions."""
    s = scale
    elements = []
    # Shell (dome) - region 1
    elements.append(f'<ellipse cx="{cx}" cy="{cy}" rx="{65*s}" ry="{50*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
    # Shell pattern - region 2
    elements.append(f'<polygon points="{cx},{cy-30*s} {cx-25*s},{cy} {cx},{cy+25*s} {cx+25*s},{cy}" fill="none" stroke="#000" stroke-width="2"/>')
    elements.append(f'<text x="{cx}" y="{cy+5}" text-anchor="middle" font-size="14" font-weight="bold">2</text>')
    # Shell outer sections
    elements.append(f'<text x="{cx-40*s}" y="{cy+5}" text-anchor="middle" font-size="14" font-weight="bold">1</text>')
    elements.append(f'<text x="{cx+40*s}" y="{cy+5}" text-anchor="middle" font-size="14" font-weight="bold">1</text>')
    elements.append(f'<text x="{cx}" y="{cy-35*s}" text-anchor="middle" font-size="12" font-weight="bold">1</text>')
    # Head - region 3
    elements.append(f'<circle cx="{cx-75*s}" cy="{cy+5*s}" r="{20*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
    elements.append(f'<text x="{cx-75*s}" y="{cy+10*s}" text-anchor="middle" font-size="12" font-weight="bold">3</text>')
    elements.append(f'<circle cx="{cx-80*s}" cy="{cy-2*s}" r="{4*s}" fill="#000"/>')
    # Legs - region 4
    legs = [(cx-35*s, cy+45*s), (cx+35*s, cy+45*s), (cx-40*s, cy+40*s), (cx+40*s, cy+40*s)]
    for i, (lx, ly) in enumerate(legs[:2]):
        elements.append(f'<ellipse cx="{lx}" cy="{ly}" rx="{15*s}" ry="{12*s}" fill="none" stroke="#000" stroke-width="2"/>')
        elements.append(f'<text x="{lx}" y="{ly+4}" text-anchor="middle" font-size="10" font-weight="bold">4</text>')
    # Tail - region 5
    elements.append(f'<polygon points="{cx+60*s},{cy+10*s} {cx+85*s},{cy+5*s} {cx+80*s},{cy+15*s}" fill="none" stroke="#000" stroke-width="2"/>')
    elements.append(f'<text x="{cx+75*s}" y="{cy+25*s}" text-anchor="middle" font-size="10" font-weight="bold">5</text>')
    return "\n".join(elements)


def draw_gift(cx, cy, scale=1.0):
    """Draw a gift box with numbered regions."""
    s = scale
    elements = []
    # Box body - region 1
    elements.append(f'<rect x="{cx-60*s}" y="{cy-20*s}" width="{120*s}" height="{80*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
    elements.append(f'<text x="{cx-30*s}" y="{cy+25*s}" text-anchor="middle" font-size="16" font-weight="bold">1</text>')
    elements.append(f'<text x="{cx+30*s}" y="{cy+25*s}" text-anchor="middle" font-size="16" font-weight="bold">1</text>')
    # Lid - region 2
    elements.append(f'<rect x="{cx-65*s}" y="{cy-40*s}" width="{130*s}" height="{20*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
    elements.append(f'<text x="{cx-30*s}" y="{cy-26*s}" text-anchor="middle" font-size="12" font-weight="bold">2</text>')
    elements.append(f'<text x="{cx+30*s}" y="{cy-26*s}" text-anchor="middle" font-size="12" font-weight="bold">2</text>')
    # Ribbon vertical - region 3
    elements.append(f'<rect x="{cx-10*s}" y="{cy-40*s}" width="{20*s}" height="{100*s}" fill="none" stroke="#000" stroke-width="2"/>')
    elements.append(f'<text x="{cx}" y="{cy+45*s}" text-anchor="middle" font-size="12" font-weight="bold">3</text>')
    # Bow - region 4
    elements.append(f'<ellipse cx="{cx-20*s}" cy="{cy-50*s}" rx="{20*s}" ry="{12*s}" fill="none" stroke="#000" stroke-width="2" transform="rotate(-20,{cx-20*s},{cy-50*s})"/>')
    elements.append(f'<ellipse cx="{cx+20*s}" cy="{cy-50*s}" rx="{20*s}" ry="{12*s}" fill="none" stroke="#000" stroke-width="2" transform="rotate(20,{cx+20*s},{cy-50*s})"/>')
    elements.append(f'<circle cx="{cx}" cy="{cy-45*s}" r="{8*s}" fill="none" stroke="#000" stroke-width="2"/>')
    elements.append(f'<text x="{cx-20*s}" y="{cy-47*s}" text-anchor="middle" font-size="10" font-weight="bold">4</text>')
    elements.append(f'<text x="{cx+20*s}" y="{cy-47*s}" text-anchor="middle" font-size="10" font-weight="bold">4</text>')
    return "\n".join(elements)

def draw_guitar(cx, cy, scale=1.0):
    """Draw a guitar with numbered regions."""
    s = scale
    elements = []
    # Body bottom - region 1
    elements.append(f'<ellipse cx="{cx}" cy="{cy+30*s}" rx="{55*s}" ry="{45*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
    elements.append(f'<text x="{cx}" y="{cy+40*s}" text-anchor="middle" font-size="16" font-weight="bold">1</text>')
    # Body top - region 2
    elements.append(f'<ellipse cx="{cx}" cy="{cy-20*s}" rx="{40*s}" ry="{35*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
    elements.append(f'<text x="{cx}" y="{cy-15*s}" text-anchor="middle" font-size="14" font-weight="bold">2</text>')
    # Sound hole - region 3
    elements.append(f'<circle cx="{cx}" cy="{cy+25*s}" r="{18*s}" fill="none" stroke="#000" stroke-width="2"/>')
    elements.append(f'<text x="{cx}" y="{cy+30*s}" text-anchor="middle" font-size="12" font-weight="bold">3</text>')
    # Neck - region 4
    elements.append(f'<rect x="{cx-10*s}" y="{cy-90*s}" width="{20*s}" height="{60*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
    # Fret lines
    for i in range(4):
        fy = cy - 85*s + i*15*s
        elements.append(f'<line x1="{cx-10*s}" y1="{fy}" x2="{cx+10*s}" y2="{fy}" stroke="#000" stroke-width="1.5"/>')
    elements.append(f'<text x="{cx}" y="{cy-60*s}" text-anchor="middle" font-size="12" font-weight="bold">4</text>')
    # Headstock - region 5
    elements.append(f'<rect x="{cx-12*s}" y="{cy-110*s}" width="{24*s}" height="{22*s}" rx="5" fill="none" stroke="#000" stroke-width="2.5"/>')
    elements.append(f'<text x="{cx}" y="{cy-95*s}" text-anchor="middle" font-size="10" font-weight="bold">5</text>')
    # Tuning pegs
    elements.append(f'<circle cx="{cx-16*s}" cy="{cy-105*s}" r="{4*s}" fill="none" stroke="#000" stroke-width="1.5"/>')
    elements.append(f'<circle cx="{cx-16*s}" cy="{cy-95*s}" r="{4*s}" fill="none" stroke="#000" stroke-width="1.5"/>')
    elements.append(f'<circle cx="{cx+16*s}" cy="{cy-105*s}" r="{4*s}" fill="none" stroke="#000" stroke-width="1.5"/>')
    elements.append(f'<circle cx="{cx+16*s}" cy="{cy-95*s}" r="{4*s}" fill="none" stroke="#000" stroke-width="1.5"/>')
    # Strings
    for i in range(4):
        sx = cx - 6*s + i*4*s
        elements.append(f'<line x1="{sx}" y1="{cy-90*s}" x2="{sx}" y2="{cy+65*s}" stroke="#000" stroke-width="0.8"/>')
    return "\n".join(elements)


def draw_watermelon(cx, cy, scale=1.0):
    """Draw a watermelon slice with numbered regions."""
    s = scale
    elements = []
    # Outer rind - region 1
    elements.append(f'<path d="M{cx-80*s},{cy+20*s} A{80*s},{80*s} 0 0 1 {cx+80*s},{cy+20*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
    elements.append(f'<line x1="{cx-80*s}" y1="{cy+20*s}" x2="{cx+80*s}" y2="{cy+20*s}" stroke="#000" stroke-width="2.5"/>')
    # Inner flesh boundary
    elements.append(f'<path d="M{cx-65*s},{cy+15*s} A{65*s},{65*s} 0 0 1 {cx+65*s},{cy+15*s}" fill="none" stroke="#000" stroke-width="2"/>')
    elements.append(f'<line x1="{cx-65*s}" y1="{cy+15*s}" x2="{cx+65*s}" y2="{cy+15*s}" stroke="#000" stroke-width="2"/>')
    # Rind region label
    elements.append(f'<text x="{cx}" y="{cy+18*s}" text-anchor="middle" font-size="14" font-weight="bold">1</text>')
    # Flesh - region 2
    elements.append(f'<text x="{cx}" y="{cy-20*s}" text-anchor="middle" font-size="20" font-weight="bold">2</text>')
    # Seeds - region 3
    seed_positions = [(cx-35*s, cy-15*s), (cx+35*s, cy-15*s), (cx-15*s, cy-30*s), (cx+15*s, cy-30*s), (cx, cy-5*s)]
    for sx_pos, sy_pos in seed_positions:
        elements.append(f'<ellipse cx="{sx_pos}" cy="{sy_pos}" rx="{5*s}" ry="{8*s}" fill="none" stroke="#000" stroke-width="2"/>')
        elements.append(f'<text x="{sx_pos}" y="{sy_pos+4}" text-anchor="middle" font-size="8" font-weight="bold">3</text>')
    return "\n".join(elements)

def draw_cloud_rain(cx, cy, scale=1.0):
    """Draw a rain cloud with numbered regions."""
    s = scale
    elements = []
    # Cloud body - region 1
    elements.append(f'<circle cx="{cx-25*s}" cy="{cy-20*s}" r="{30*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
    elements.append(f'<circle cx="{cx+20*s}" cy="{cy-25*s}" r="{35*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
    elements.append(f'<circle cx="{cx-50*s}" cy="{cy}" r="{25*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
    elements.append(f'<circle cx="{cx+50*s}" cy="{cy-5*s}" r="{28*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
    elements.append(f'<circle cx="{cx}" cy="{cy}" r="{28*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
    elements.append(f'<text x="{cx}" y="{cy-15*s}" text-anchor="middle" font-size="18" font-weight="bold">1</text>')
    # Rain drops - region 2
    for i in range(5):
        dx = cx - 40*s + i*20*s
        dy = cy + 35*s + (i%2)*15*s
        elements.append(f'<path d="M{dx},{dy} Q{dx-5*s},{dy+12*s} {dx},{dy+18*s} Q{dx+5*s},{dy+12*s} {dx},{dy}" fill="none" stroke="#000" stroke-width="2"/>')
        elements.append(f'<text x="{dx}" y="{dy+12}" text-anchor="middle" font-size="8" font-weight="bold">2</text>')
    return "\n".join(elements)


def draw_lollipop(cx, cy, scale=1.0):
    """Draw a lollipop with numbered regions."""
    s = scale
    elements = []
    # Swirl candy top - region 1
    elements.append(f'<circle cx="{cx}" cy="{cy-30*s}" r="{55*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
    # Spiral inside
    elements.append(f'<circle cx="{cx}" cy="{cy-30*s}" r="{40*s}" fill="none" stroke="#000" stroke-width="1.5"/>')
    elements.append(f'<circle cx="{cx}" cy="{cy-30*s}" r="{25*s}" fill="none" stroke="#000" stroke-width="1.5"/>')
    elements.append(f'<circle cx="{cx}" cy="{cy-30*s}" r="{12*s}" fill="none" stroke="#000" stroke-width="1.5"/>')
    elements.append(f'<text x="{cx}" y="{cy-25*s}" text-anchor="middle" font-size="16" font-weight="bold">1</text>')
    elements.append(f'<text x="{cx-32*s}" y="{cy-25*s}" text-anchor="middle" font-size="12" font-weight="bold">2</text>')
    elements.append(f'<text x="{cx+32*s}" y="{cy-25*s}" text-anchor="middle" font-size="12" font-weight="bold">2</text>')
    # Stick - region 3
    elements.append(f'<rect x="{cx-5*s}" y="{cy+25*s}" width="{10*s}" height="{80*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
    elements.append(f'<text x="{cx}" y="{cy+70*s}" text-anchor="middle" font-size="14" font-weight="bold">3</text>')
    return "\n".join(elements)

def draw_pencil(cx, cy, scale=1.0):
    """Draw a pencil with numbered regions."""
    s = scale
    elements = []
    # Body - region 1
    elements.append(f'<rect x="{cx-70*s}" y="{cy-15*s}" width="{120*s}" height="{30*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
    elements.append(f'<text x="{cx-10*s}" y="{cy+6}" text-anchor="middle" font-size="16" font-weight="bold">1</text>')
    # Tip - region 2
    elements.append(f'<polygon points="{cx+50*s},{cy-15*s} {cx+80*s},{cy} {cx+50*s},{cy+15*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
    elements.append(f'<text x="{cx+58*s}" y="{cy+5}" text-anchor="middle" font-size="12" font-weight="bold">2</text>')
    # Eraser - region 3
    elements.append(f'<rect x="{cx-90*s}" y="{cy-15*s}" width="{20*s}" height="{30*s}" rx="5" fill="none" stroke="#000" stroke-width="2.5"/>')
    elements.append(f'<text x="{cx-80*s}" y="{cy+5}" text-anchor="middle" font-size="10" font-weight="bold">3</text>')
    # Metal band - region 4
    elements.append(f'<rect x="{cx-70*s}" y="{cy-15*s}" width="{10*s}" height="{30*s}" fill="none" stroke="#000" stroke-width="2"/>')
    elements.append(f'<text x="{cx-65*s}" y="{cy+5}" text-anchor="middle" font-size="8" font-weight="bold">4</text>')
    # Lines on body
    elements.append(f'<line x1="{cx-60*s}" y1="{cy-5*s}" x2="{cx+50*s}" y2="{cy-5*s}" stroke="#000" stroke-width="1"/>')
    elements.append(f'<line x1="{cx-60*s}" y1="{cy+5*s}" x2="{cx+50*s}" y2="{cy+5*s}" stroke="#000" stroke-width="1"/>')
    return "\n".join(elements)

def draw_strawberry(cx, cy, scale=1.0):
    """Draw a strawberry with numbered regions."""
    s = scale
    elements = []
    # Berry body - region 1
    elements.append(f'<path d="M{cx},{cy-50*s} C{cx+70*s},{cy-40*s} {cx+60*s},{cy+50*s} {cx},{cy+70*s} C{cx-60*s},{cy+50*s} {cx-70*s},{cy-40*s} {cx},{cy-50*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
    elements.append(f'<text x="{cx}" y="{cy}" text-anchor="middle" font-size="18" font-weight="bold">1</text>')
    # Leaves on top - region 2
    for i in range(-2, 3):
        angle = math.radians(i * 25 - 90)
        lx = cx + 25*s * math.cos(angle)
        ly = cy - 50*s + 25*s * math.sin(angle)
        elements.append(f'<ellipse cx="{lx}" cy="{ly}" rx="{12*s}" ry="{6*s}" fill="none" stroke="#000" stroke-width="2" transform="rotate({i*25},{lx},{ly})"/>')
    elements.append(f'<text x="{cx}" y="{cy-55*s}" text-anchor="middle" font-size="12" font-weight="bold">2</text>')
    # Seeds - region 3
    seed_pos = [(cx-20*s,cy-15*s),(cx+20*s,cy-15*s),(cx-30*s,cy+10*s),(cx+30*s,cy+10*s),(cx-15*s,cy+30*s),(cx+15*s,cy+30*s),(cx,cy+45*s)]
    for sx_pos, sy_pos in seed_pos:
        elements.append(f'<ellipse cx="{sx_pos}" cy="{sy_pos}" rx="{4*s}" ry="{5*s}" fill="none" stroke="#000" stroke-width="1.5"/>')
    elements.append(f'<text x="{cx+40*s}" y="{cy+20*s}" text-anchor="middle" font-size="12" font-weight="bold">3</text>')
    # Face
    elements.append(f'<circle cx="{cx-12*s}" cy="{cy+5*s}" r="{5*s}" fill="#000"/>')
    elements.append(f'<circle cx="{cx+12*s}" cy="{cy+5*s}" r="{5*s}" fill="#000"/>')
    elements.append(f'<path d="M{cx-8*s},{cy+20*s} Q{cx},{cy+28*s} {cx+8*s},{cy+20*s}" fill="none" stroke="#000" stroke-width="2"/>')
    return "\n".join(elements)


# All drawing functions with their titles and number of colors used
DRAWINGS = [
    ("Cupcake", draw_cupcake, 4),
    ("Star", draw_star, 2),
    ("Butterfly", draw_butterfly, 4),
    ("Flower", draw_flower, 4),
    ("Fish", draw_fish, 5),
    ("House", draw_house, 5),
    ("Sun", draw_sun, 2),
    ("Heart", draw_heart, 2),
    ("Car", draw_car, 5),
    ("Tree", draw_tree, 4),
    ("Mushroom", draw_mushroom, 4),
    ("Rocket", draw_rocket, 5),
    ("Balloon", draw_balloon, 4),
    ("Ice Cream", draw_ice_cream, 4),
    ("Cat", draw_cat, 4),
    ("Umbrella", draw_umbrella, 4),
    ("Apple", draw_apple, 3),
    ("Boat", draw_boat, 5),
    ("Rainbow", draw_rainbow, 5),
    ("Snail", draw_snail, 4),
    ("Ladybug", draw_ladybug, 3),
    ("Castle", draw_castle, 5),
    ("Duck", draw_duck, 5),
    ("Kite", draw_kite, 5),
    ("Snowman", draw_snowman, 5),
    ("Bee", draw_bee, 5),
    ("Crown", draw_crown, 5),
    ("Planet", draw_planet, 4),
    ("Popsicle", draw_popsicle, 4),
    ("Diamond", draw_diamond, 5),
    ("Candy", draw_candy, 4),
    ("Moon", draw_moon, 2),
    ("Turtle", draw_turtle, 5),
    ("Gift Box", draw_gift, 4),
    ("Guitar", draw_guitar, 5),
    ("Watermelon", draw_watermelon, 3),
    ("Rain Cloud", draw_cloud_rain, 2),
    ("Lollipop", draw_lollipop, 3),
    ("Pencil", draw_pencil, 4),
    ("Strawberry", draw_strawberry, 3),
]

# We have 40 unique drawings. To get 50 pages, we'll repeat some with different palettes
def get_page_data(page_num):
    """Get drawing data for a given page number (0-indexed)."""
    idx = page_num % len(DRAWINGS)
    title, draw_fn, num_colors = DRAWINGS[idx]
    palette_idx = (page_num // len(DRAWINGS) + page_num) % len(PALETTES)
    palette = PALETTES[palette_idx][:num_colors]
    return title, draw_fn, palette, num_colors


def generate_color_legend(num_colors, palette):
    """Generate the color legend SVG at the bottom of the page."""
    elements = []
    # Layout: up to 3 per row, 2 rows max
    cols = min(3, num_colors)
    rows = math.ceil(num_colors / 3)
    start_y = 650
    for i in range(num_colors):
        row = i // 3
        col = i % 3
        x_base = 80 + col * 175
        y_base = start_y + row * 55
        # Number
        elements.append(f'<text x="{x_base}" y="{y_base + 30}" font-size="28" font-weight="bold" text-anchor="middle">{i+1} -</text>')
        # Color circle
        elements.append(f'<circle cx="{x_base + 45}" cy="{y_base + 22}" r="20" fill="{palette[i]}" stroke="#000" stroke-width="2"/>')
    return "\n".join(elements)

def generate_page(page_num):
    """Generate a single page SVG."""
    title, draw_fn, palette, num_colors = get_page_data(page_num)

    border = generate_border_svg()
    drawing = draw_fn(308, 370, scale=1.0)
    legend = generate_color_legend(num_colors, palette)

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 616 800" width="616" height="800">
  <!-- White background -->
  <rect width="616" height="800" fill="white"/>
  <!-- Colorful border -->
  {border}
  <!-- Title -->
  <rect x="160" y="32" width="296" height="32" fill="white" stroke="#000" stroke-width="1"/>
  <text x="308" y="55" text-anchor="middle" font-family="'Georgia', serif" font-size="20" font-weight="bold" letter-spacing="2">COLOR BY NUMBERS</text>
  <!-- Drawing area -->
  {drawing}
  <!-- Color Legend -->
  {legend}
</svg>'''
    return svg


def generate_html_book():
    """Generate the complete HTML book with 50 pages."""
    pages_html = []
    for i in range(50):
        svg = generate_page(i)
        pages_html.append(f'<div class="page">\n{svg}\n</div>')

    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Color By Numbers - Activity Book (50 Pages)</title>
<style>
  @page {{
    size: 8.5in 11in;
    margin: 0;
  }}
  * {{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
  }}
  html, body {{
    width: 8.5in;
    font-family: Arial, sans-serif;
    background: white;
  }}
  .page {{
    width: 8.5in;
    height: 11in;
    display: flex;
    align-items: center;
    justify-content: center;
    page-break-after: always;
    page-break-inside: avoid;
    overflow: hidden;
    position: relative;
  }}
  .page:last-child {{
    page-break-after: auto;
  }}
  .page svg {{
    width: 8.5in;
    height: 11in;
    display: block;
  }}
</style>
</head>
<body>
{"".join(pages_html)}
</body>
</html>'''
    return html

if __name__ == "__main__":
    print("Generating Color By Numbers book (50 pages)...")
    html_content = generate_html_book()
    with open("/projects/sandbox/color_by_numbers_book.html", "w") as f:
        f.write(html_content)
    print(f"Done! Book saved to: /projects/sandbox/color_by_numbers_book.html")
    print(f"File size: {len(html_content):,} bytes")
    print("To create a PDF: Open the HTML file in a browser and use Print > Save as PDF")
