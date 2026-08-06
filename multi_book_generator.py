#!/usr/bin/env python3
"""
Generate 20 Color By Numbers PDF books, each with 50+ pages.
All drawings use 5-8 colors for more complex and engaging coloring.
Each book has a unique theme.
"""
import math
import random
import os
import subprocess
import sys

# 20 Book Themes
BOOK_THEMES = [
    "Ocean Animals",
    "Farm Animals",
    "Space Adventure",
    "Dinosaurs",
    "Garden & Flowers",
    "Food & Treats",
    "Vehicles & Transport",
    "Insects & Bugs",
    "Birds & Sky",
    "Jungle Animals",
    "Under the Sea",
    "Fantasy & Magic",
    "Sports & Games",
    "Musical Instruments",
    "Weather & Seasons",
    "Fruits & Vegetables",
    "Buildings & Houses",
    "Christmas & Winter",
    "Easter & Spring",
    "Pets & Home Animals",
]

# Extended color palettes (6-8 colors each)
PALETTES_6 = [
    ["#FF0000", "#0066CC", "#33CC33", "#FFD700", "#FF69B4", "#8B4513"],
    ["#DC143C", "#4169E1", "#228B22", "#FF8C00", "#9932CC", "#FFD700"],
    ["#FF6347", "#1E90FF", "#32CD32", "#FFA500", "#BA55D3", "#00CED1"],
    ["#CC0000", "#003399", "#009900", "#FF9900", "#660099", "#FF3399"],
    ["#E74C3C", "#2980B9", "#27AE60", "#F39C12", "#8E44AD", "#16A085"],
    ["#FF4444", "#4488FF", "#44CC44", "#FFAA00", "#AA44FF", "#FF44AA"],
]

PALETTES_7 = [
    ["#FF0000", "#0066CC", "#33CC33", "#FFD700", "#FF69B4", "#8B4513", "#00CED1"],
    ["#DC143C", "#4169E1", "#228B22", "#FF8C00", "#9932CC", "#20B2AA", "#FF6347"],
    ["#E74C3C", "#2980B9", "#27AE60", "#F39C12", "#8E44AD", "#16A085", "#D35400"],
    ["#CC0000", "#003399", "#009900", "#FF9900", "#660099", "#FF3399", "#006666"],
    ["#FF4444", "#4488FF", "#44CC44", "#FFAA00", "#AA44FF", "#FF44AA", "#448888"],
]

PALETTES_8 = [
    ["#FF0000", "#0066CC", "#33CC33", "#FFD700", "#FF69B4", "#8B4513", "#00CED1", "#808080"],
    ["#DC143C", "#4169E1", "#228B22", "#FF8C00", "#9932CC", "#20B2AA", "#FF6347", "#4B0082"],
    ["#E74C3C", "#2980B9", "#27AE60", "#F39C12", "#8E44AD", "#16A085", "#D35400", "#2C3E50"],
    ["#CC0000", "#003399", "#009900", "#FF9900", "#660099", "#FF3399", "#006666", "#333333"],
]

BORDER_COLORS = [
    "#FF0000", "#00FF00", "#0000FF", "#FFFF00", "#FF00FF",
    "#00FFFF", "#FFA500", "#800080", "#008000", "#FFC0CB",
    "#A52A2A", "#808080", "#000080", "#808000", "#800000",
]

def get_palette(num_colors, seed_val):
    """Get a color palette with the specified number of colors."""
    random.seed(seed_val)
    if num_colors <= 6:
        p = random.choice(PALETTES_6)
        return p[:num_colors]
    elif num_colors == 7:
        p = random.choice(PALETTES_7)
        return p[:7]
    else:
        p = random.choice(PALETTES_8)
        return p[:num_colors]


def generate_border_svg(seed_val):
    """Generate colorful block border."""
    random.seed(seed_val)
    blocks = []
    block_size = 28
    for i in range(22):
        color = random.choice(BORDER_COLORS)
        blocks.append(f'<rect x="{i*block_size}" y="0" width="{block_size}" height="{block_size}" fill="{color}" stroke="#333" stroke-width="1"/>')
        blocks.append(f'<circle cx="{i*block_size+14}" cy="14" r="6" fill="none" stroke="#fff" stroke-width="1.5"/>')
    for i in range(22):
        color = random.choice(BORDER_COLORS)
        blocks.append(f'<rect x="{i*block_size}" y="772" width="{block_size}" height="{block_size}" fill="{color}" stroke="#333" stroke-width="1"/>')
        blocks.append(f'<circle cx="{i*block_size+14}" cy="786" r="6" fill="none" stroke="#fff" stroke-width="1.5"/>')
    for i in range(28):
        color = random.choice(BORDER_COLORS)
        blocks.append(f'<rect x="0" y="{i*block_size}" width="{block_size}" height="{block_size}" fill="{color}" stroke="#333" stroke-width="1"/>')
        blocks.append(f'<circle cx="14" cy="{i*block_size+14}" r="6" fill="none" stroke="#fff" stroke-width="1.5"/>')
    for i in range(28):
        color = random.choice(BORDER_COLORS)
        blocks.append(f'<rect x="588" y="{i*block_size}" width="{block_size}" height="{block_size}" fill="{color}" stroke="#333" stroke-width="1"/>')
        blocks.append(f'<circle cx="602" cy="{i*block_size+14}" r="6" fill="none" stroke="#fff" stroke-width="1.5"/>')
    return "\n".join(blocks)

def generate_color_legend(num_colors, palette):
    """Generate color legend at bottom of page."""
    elements = []
    start_y = 640
    if num_colors <= 4:
        cols = 2
    elif num_colors <= 6:
        cols = 3
    else:
        cols = 4
    for i in range(num_colors):
        row = i // cols
        col = i % cols
        col_width = 500 // cols
        x_base = 58 + col * col_width
        y_base = start_y + row * 50
        elements.append(f'<text x="{x_base}" y="{y_base+28}" font-size="24" font-weight="bold" text-anchor="middle">{i+1} -</text>')
        elements.append(f'<circle cx="{x_base+35}" cy="{y_base+20}" r="18" fill="{palette[i]}" stroke="#000" stroke-width="2"/>')
    return "\n".join(elements)


# ============================================================
# THEME 1: OCEAN ANIMALS (6-7 colors each)
# ============================================================
def draw_whale(cx, cy, s=1.0):
    e = []
    # Body - 1
    e.append(f'<ellipse cx="{cx}" cy="{cy}" rx="{90*s}" ry="{55*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
    e.append(f'<text x="{cx+10*s}" y="{cy+10}" text-anchor="middle" font-size="20" font-weight="bold">1</text>')
    # Belly - 2
    e.append(f'<path d="M{cx-60*s},{cy+15*s} Q{cx},{cy+45*s} {cx+60*s},{cy+15*s}" fill="none" stroke="#000" stroke-width="2"/>')
    e.append(f'<text x="{cx}" y="{cy+35*s}" text-anchor="middle" font-size="14" font-weight="bold">2</text>')
    # Tail - 3
    e.append(f'<path d="M{cx+85*s},{cy} Q{cx+110*s},{cy-30*s} {cx+130*s},{cy-40*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
    e.append(f'<path d="M{cx+85*s},{cy} Q{cx+110*s},{cy+30*s} {cx+130*s},{cy+40*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
    e.append(f'<path d="M{cx+130*s},{cy-40*s} Q{cx+115*s},{cy} {cx+130*s},{cy+40*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
    e.append(f'<text x="{cx+115*s}" y="{cy+5}" text-anchor="middle" font-size="12" font-weight="bold">3</text>')
    # Fin on top - 4
    e.append(f'<polygon points="{cx-10*s},{cy-55*s} {cx+10*s},{cy-55*s} {cx+20*s},{cy-80*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
    e.append(f'<text x="{cx+8*s}" y="{cy-62*s}" text-anchor="middle" font-size="10" font-weight="bold">4</text>')
    # Eye - 5
    e.append(f'<circle cx="{cx-50*s}" cy="{cy-10*s}" r="{12*s}" fill="none" stroke="#000" stroke-width="2"/>')
    e.append(f'<circle cx="{cx-50*s}" cy="{cy-10*s}" r="{5*s}" fill="#000"/>')
    e.append(f'<text x="{cx-50*s}" y="{cy+10*s}" text-anchor="middle" font-size="10" font-weight="bold">5</text>')
    # Water spout - 6
    e.append(f'<path d="M{cx-20*s},{cy-55*s} Q{cx-25*s},{cy-80*s} {cx-35*s},{cy-95*s}" fill="none" stroke="#000" stroke-width="2"/>')
    e.append(f'<path d="M{cx-20*s},{cy-55*s} Q{cx-15*s},{cy-80*s} {cx-5*s},{cy-95*s}" fill="none" stroke="#000" stroke-width="2"/>')
    e.append(f'<path d="M{cx-35*s},{cy-95*s} Q{cx-20*s},{cy-100*s} {cx-5*s},{cy-95*s}" fill="none" stroke="#000" stroke-width="2"/>')
    e.append(f'<text x="{cx-20*s}" y="{cy-85*s}" text-anchor="middle" font-size="10" font-weight="bold">6</text>')
    return "\n".join(e)

def draw_jellyfish(cx, cy, s=1.0):
    e = []
    # Bell/dome - 1
    e.append(f'<path d="M{cx-60*s},{cy} A{60*s},{55*s} 0 0 1 {cx+60*s},{cy}" fill="none" stroke="#000" stroke-width="2.5"/>')
    e.append(f'<line x1="{cx-60*s}" y1="{cy}" x2="{cx+60*s}" y2="{cy}" stroke="#000" stroke-width="2.5"/>')
    e.append(f'<text x="{cx}" y="{cy-20*s}" text-anchor="middle" font-size="18" font-weight="bold">1</text>')
    # Inner pattern - 2
    e.append(f'<path d="M{cx-40*s},{cy-5*s} A{40*s},{35*s} 0 0 1 {cx+40*s},{cy-5*s}" fill="none" stroke="#000" stroke-width="1.5"/>')
    e.append(f'<text x="{cx}" y="{cy-40*s}" text-anchor="middle" font-size="12" font-weight="bold">2</text>')
    # Tentacles - 3,4,5
    for i in range(5):
        tx = cx - 40*s + i*20*s
        e.append(f'<path d="M{tx},{cy} Q{tx+10*s},{cy+30*s} {tx-5*s},{cy+55*s} Q{tx+8*s},{cy+80*s} {tx},{cy+100*s}" fill="none" stroke="#000" stroke-width="2"/>')
        num = 3 + (i % 3)
        e.append(f'<text x="{tx+5*s}" y="{cy+50*s+i*5*s}" text-anchor="middle" font-size="10" font-weight="bold">{num}</text>')
    # Frilly edge - 6
    for i in range(6):
        fx = cx - 55*s + i*22*s
        e.append(f'<path d="M{fx},{cy} Q{fx+5*s},{cy+12*s} {fx+11*s},{cy}" fill="none" stroke="#000" stroke-width="1.5"/>')
    e.append(f'<text x="{cx+50*s}" y="{cy+12*s}" text-anchor="middle" font-size="10" font-weight="bold">6</text>')
    # Eyes
    e.append(f'<circle cx="{cx-15*s}" cy="{cy-15*s}" r="{5*s}" fill="#000"/>')
    e.append(f'<circle cx="{cx+15*s}" cy="{cy-15*s}" r="{5*s}" fill="#000"/>')
    return "\n".join(e)

def draw_seahorse(cx, cy, s=1.0):
    e = []
    # Head - 1
    e.append(f'<circle cx="{cx}" cy="{cy-60*s}" r="{25*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
    e.append(f'<text x="{cx}" y="{cy-55*s}" text-anchor="middle" font-size="14" font-weight="bold">1</text>')
    # Snout - 2
    e.append(f'<ellipse cx="{cx-30*s}" cy="{cy-60*s}" rx="{18*s}" ry="{8*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
    e.append(f'<text x="{cx-30*s}" y="{cy-57*s}" text-anchor="middle" font-size="9" font-weight="bold">2</text>')
    # Body curve - 3
    e.append(f'<path d="M{cx+10*s},{cy-38*s} Q{cx+30*s},{cy} {cx+15*s},{cy+30*s} Q{cx},{cy+60*s} {cx-15*s},{cy+40*s} Q{cx-25*s},{cy+20*s} {cx-10*s},{cy}" fill="none" stroke="#000" stroke-width="2.5"/>')
    e.append(f'<text x="{cx+15*s}" y="{cy+5}" text-anchor="middle" font-size="14" font-weight="bold">3</text>')
    # Tail curl - 4
    e.append(f'<path d="M{cx-15*s},{cy+40*s} Q{cx-30*s},{cy+60*s} {cx-20*s},{cy+75*s} Q{cx-5*s},{cy+85*s} {cx},{cy+70*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
    e.append(f'<text x="{cx-18*s}" y="{cy+65*s}" text-anchor="middle" font-size="11" font-weight="bold">4</text>')
    # Dorsal fin - 5
    e.append(f'<path d="M{cx+20*s},{cy-20*s} Q{cx+45*s},{cy-10*s} {cx+40*s},{cy+10*s} Q{cx+30*s},{cy+20*s} {cx+20*s},{cy+15*s}" fill="none" stroke="#000" stroke-width="2"/>')
    e.append(f'<text x="{cx+35*s}" y="{cy}" text-anchor="middle" font-size="10" font-weight="bold">5</text>')
    # Belly segments - 6
    for i in range(4):
        by = cy - 25*s + i*18*s
        e.append(f'<line x1="{cx-5*s}" y1="{by}" x2="{cx+10*s}" y2="{by}" stroke="#000" stroke-width="1.5"/>')
    e.append(f'<text x="{cx+5*s}" y="{cy+25*s}" text-anchor="middle" font-size="10" font-weight="bold">6</text>')
    # Crown - 7
    e.append(f'<path d="M{cx-5*s},{cy-85*s} L{cx},{cy-100*s} L{cx+5*s},{cy-85*s}" fill="none" stroke="#000" stroke-width="2"/>')
    e.append(f'<path d="M{cx+5*s},{cy-85*s} L{cx+12*s},{cy-95*s} L{cx+15*s},{cy-82*s}" fill="none" stroke="#000" stroke-width="2"/>')
    e.append(f'<text x="{cx+5*s}" y="{cy-88*s}" text-anchor="middle" font-size="9" font-weight="bold">7</text>')
    # Eye
    e.append(f'<circle cx="{cx-5*s}" cy="{cy-65*s}" r="{5*s}" fill="#000"/>')
    return "\n".join(e)


def draw_octopus(cx, cy, s=1.0):
    e = []
    # Head - 1
    e.append(f'<ellipse cx="{cx}" cy="{cy-30*s}" rx="{50*s}" ry="{45*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
    e.append(f'<text x="{cx}" y="{cy-25*s}" text-anchor="middle" font-size="18" font-weight="bold">1</text>')
    # Eyes
    e.append(f'<circle cx="{cx-18*s}" cy="{cy-40*s}" r="{10*s}" fill="none" stroke="#000" stroke-width="2"/>')
    e.append(f'<circle cx="{cx-18*s}" cy="{cy-40*s}" r="{5*s}" fill="#000"/>')
    e.append(f'<circle cx="{cx+18*s}" cy="{cy-40*s}" r="{10*s}" fill="none" stroke="#000" stroke-width="2"/>')
    e.append(f'<circle cx="{cx+18*s}" cy="{cy-40*s}" r="{5*s}" fill="#000"/>')
    # Tentacles (8) with alternating colors 2-5
    angles = [-70, -50, -30, -10, 10, 30, 50, 70]
    for i, ang in enumerate(angles):
        rad = math.radians(ang)
        x1 = cx + 45*s * math.sin(rad)
        y1 = cy + 10*s
        x2 = x1 + 20*s * math.sin(rad + 0.3)
        y2 = y1 + 50*s
        x3 = x2 - 10*s * math.sin(rad)
        y3 = y2 + 40*s
        e.append(f'<path d="M{x1},{y1} Q{x2},{y2} {x3},{y3}" fill="none" stroke="#000" stroke-width="2.5"/>')
        num = 2 + (i % 4)
        e.append(f'<text x="{x2}" y="{y2}" text-anchor="middle" font-size="10" font-weight="bold">{num}</text>')
    # Suction cups detail - 6
    e.append(f'<text x="{cx-45*s}" y="{cy+80*s}" text-anchor="middle" font-size="10" font-weight="bold">6</text>')
    # Smile
    e.append(f'<path d="M{cx-15*s},{cy-20*s} Q{cx},{cy-10*s} {cx+15*s},{cy-20*s}" fill="none" stroke="#000" stroke-width="2"/>')
    return "\n".join(e)

def draw_crab(cx, cy, s=1.0):
    e = []
    # Body - 1
    e.append(f'<ellipse cx="{cx}" cy="{cy}" rx="{60*s}" ry="{40*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
    e.append(f'<text x="{cx}" y="{cy+5}" text-anchor="middle" font-size="18" font-weight="bold">1</text>')
    # Eyes on stalks - 2
    e.append(f'<line x1="{cx-20*s}" y1="{cy-40*s}" x2="{cx-25*s}" y2="{cy-60*s}" stroke="#000" stroke-width="2.5"/>')
    e.append(f'<circle cx="{cx-25*s}" cy="{cy-65*s}" r="{8*s}" fill="none" stroke="#000" stroke-width="2"/>')
    e.append(f'<circle cx="{cx-25*s}" cy="{cy-65*s}" r="{3*s}" fill="#000"/>')
    e.append(f'<line x1="{cx+20*s}" y1="{cy-40*s}" x2="{cx+25*s}" y2="{cy-60*s}" stroke="#000" stroke-width="2.5"/>')
    e.append(f'<circle cx="{cx+25*s}" cy="{cy-65*s}" r="{8*s}" fill="none" stroke="#000" stroke-width="2"/>')
    e.append(f'<circle cx="{cx+25*s}" cy="{cy-65*s}" r="{3*s}" fill="#000"/>')
    e.append(f'<text x="{cx}" y="{cy-55*s}" text-anchor="middle" font-size="10" font-weight="bold">2</text>')
    # Claws - 3
    e.append(f'<ellipse cx="{cx-90*s}" cy="{cy-15*s}" rx="{25*s}" ry="{18*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
    e.append(f'<path d="M{cx-80*s},{cy-30*s} L{cx-70*s},{cy-15*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
    e.append(f'<text x="{cx-90*s}" y="{cy-10*s}" text-anchor="middle" font-size="12" font-weight="bold">3</text>')
    e.append(f'<ellipse cx="{cx+90*s}" cy="{cy-15*s}" rx="{25*s}" ry="{18*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
    e.append(f'<path d="M{cx+80*s},{cy-30*s} L{cx+70*s},{cy-15*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
    e.append(f'<text x="{cx+90*s}" y="{cy-10*s}" text-anchor="middle" font-size="12" font-weight="bold">3</text>')
    # Legs - 4,5,6
    for i in range(3):
        lx = cx - 50*s + i*10*s
        e.append(f'<line x1="{lx}" y1="{cy+35*s}" x2="{lx-15*s}" y2="{cy+65*s}" stroke="#000" stroke-width="2"/>')
        e.append(f'<text x="{lx-15*s}" y="{cy+60*s}" text-anchor="middle" font-size="9" font-weight="bold">{4+i%3}</text>')
        rx = cx + 30*s + i*10*s
        e.append(f'<line x1="{rx}" y1="{cy+35*s}" x2="{rx+15*s}" y2="{cy+65*s}" stroke="#000" stroke-width="2"/>')
        e.append(f'<text x="{rx+15*s}" y="{cy+60*s}" text-anchor="middle" font-size="9" font-weight="bold">{4+i%3}</text>')
    return "\n".join(e)

def draw_starfish(cx, cy, s=1.0):
    e = []
    # 5-pointed star body
    points_outer = []
    points_inner = []
    for i in range(10):
        angle = math.radians(i * 36 - 90)
        r = 80*s if i % 2 == 0 else 40*s
        px = cx + r * math.cos(angle)
        py = cy + r * math.sin(angle)
        points_outer.append(f"{px},{py}")
    e.append(f'<polygon points="{" ".join(points_outer)}" fill="none" stroke="#000" stroke-width="2.5"/>')
    # Number each arm 1-5
    for i in range(5):
        angle = math.radians(i * 72 - 90)
        tx = cx + 55*s * math.cos(angle)
        ty = cy + 55*s * math.sin(angle) + 5
        e.append(f'<text x="{tx}" y="{ty}" text-anchor="middle" font-size="14" font-weight="bold">{i+1}</text>')
    # Center - 6
    e.append(f'<circle cx="{cx}" cy="{cy}" r="{20*s}" fill="none" stroke="#000" stroke-width="2"/>')
    e.append(f'<text x="{cx}" y="{cy+6}" text-anchor="middle" font-size="14" font-weight="bold">6</text>')
    # Dots on arms
    for i in range(5):
        angle = math.radians(i * 72 - 90)
        for d in [30, 50]:
            dx = cx + d*s * math.cos(angle)
            dy = cy + d*s * math.sin(angle)
            e.append(f'<circle cx="{dx}" cy="{dy}" r="{4*s}" fill="none" stroke="#000" stroke-width="1.5"/>')
    # Eyes
    e.append(f'<circle cx="{cx-8*s}" cy="{cy-5*s}" r="{4*s}" fill="#000"/>')
    e.append(f'<circle cx="{cx+8*s}" cy="{cy-5*s}" r="{4*s}" fill="#000"/>')
    return "\n".join(e)


def draw_turtle_ocean(cx, cy, s=1.0):
    e = []
    # Shell - 1
    e.append(f'<ellipse cx="{cx}" cy="{cy-10*s}" rx="{65*s}" ry="{50*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
    e.append(f'<text x="{cx}" y="{cy-5*s}" text-anchor="middle" font-size="16" font-weight="bold">1</text>')
    # Shell pattern hexagons - 2
    for dx, dy in [(-25*s,-25*s),(25*s,-25*s),(0,5*s),(-30*s,10*s),(30*s,10*s)]:
        e.append(f'<circle cx="{cx+dx}" cy="{cy+dy}" r="{15*s}" fill="none" stroke="#000" stroke-width="1.5"/>')
    e.append(f'<text x="{cx-25*s}" y="{cy-20*s}" text-anchor="middle" font-size="10" font-weight="bold">2</text>')
    # Head - 3
    e.append(f'<circle cx="{cx-75*s}" cy="{cy}" r="{18*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
    e.append(f'<text x="{cx-75*s}" y="{cy+5}" text-anchor="middle" font-size="12" font-weight="bold">3</text>')
    e.append(f'<circle cx="{cx-80*s}" cy="{cy-5*s}" r="{4*s}" fill="#000"/>')
    # Flippers - 4
    e.append(f'<ellipse cx="{cx-40*s}" cy="{cy+45*s}" rx="{25*s}" ry="{12*s}" fill="none" stroke="#000" stroke-width="2" transform="rotate(-20,{cx-40*s},{cy+45*s})"/>')
    e.append(f'<ellipse cx="{cx+40*s}" cy="{cy+45*s}" rx="{25*s}" ry="{12*s}" fill="none" stroke="#000" stroke-width="2" transform="rotate(20,{cx+40*s},{cy+45*s})"/>')
    e.append(f'<text x="{cx-40*s}" y="{cy+50*s}" text-anchor="middle" font-size="10" font-weight="bold">4</text>')
    e.append(f'<text x="{cx+40*s}" y="{cy+50*s}" text-anchor="middle" font-size="10" font-weight="bold">4</text>')
    # Back flippers - 5
    e.append(f'<ellipse cx="{cx+60*s}" cy="{cy+20*s}" rx="{18*s}" ry="{8*s}" fill="none" stroke="#000" stroke-width="2"/>')
    e.append(f'<text x="{cx+60*s}" y="{cy+24*s}" text-anchor="middle" font-size="9" font-weight="bold">5</text>')
    # Tail - 6
    e.append(f'<polygon points="{cx+65*s},{cy} {cx+85*s},{cy-5*s} {cx+80*s},{cy+5*s}" fill="none" stroke="#000" stroke-width="2"/>')
    e.append(f'<text x="{cx+80*s}" y="{cy-8*s}" text-anchor="middle" font-size="9" font-weight="bold">6</text>')
    return "\n".join(e)

def draw_dolphin(cx, cy, s=1.0):
    e = []
    # Body - 1
    e.append(f'<path d="M{cx-80*s},{cy} Q{cx-40*s},{cy-50*s} {cx+20*s},{cy-30*s} Q{cx+60*s},{cy-15*s} {cx+90*s},{cy+10*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
    e.append(f'<path d="M{cx-80*s},{cy} Q{cx-30*s},{cy+30*s} {cx+30*s},{cy+20*s} Q{cx+60*s},{cy+15*s} {cx+90*s},{cy+10*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
    e.append(f'<text x="{cx}" y="{cy+5}" text-anchor="middle" font-size="18" font-weight="bold">1</text>')
    # Belly - 2
    e.append(f'<path d="M{cx-50*s},{cy+10*s} Q{cx},{cy+25*s} {cx+50*s},{cy+12*s}" fill="none" stroke="#000" stroke-width="1.5"/>')
    e.append(f'<text x="{cx}" y="{cy+20*s}" text-anchor="middle" font-size="12" font-weight="bold">2</text>')
    # Dorsal fin - 3
    e.append(f'<polygon points="{cx-10*s},{cy-30*s} {cx+10*s},{cy-30*s} {cx},{cy-60*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
    e.append(f'<text x="{cx}" y="{cy-38*s}" text-anchor="middle" font-size="10" font-weight="bold">3</text>')
    # Tail fluke - 4
    e.append(f'<path d="M{cx+85*s},{cy+10*s} Q{cx+100*s},{cy-10*s} {cx+120*s},{cy-20*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
    e.append(f'<path d="M{cx+85*s},{cy+10*s} Q{cx+100*s},{cy+30*s} {cx+120*s},{cy+35*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
    e.append(f'<path d="M{cx+120*s},{cy-20*s} Q{cx+110*s},{cy+5*s} {cx+120*s},{cy+35*s}" fill="none" stroke="#000" stroke-width="2"/>')
    e.append(f'<text x="{cx+108*s}" y="{cy+10*s}" text-anchor="middle" font-size="10" font-weight="bold">4</text>')
    # Flipper - 5
    e.append(f'<ellipse cx="{cx-30*s}" cy="{cy+20*s}" rx="{20*s}" ry="{10*s}" fill="none" stroke="#000" stroke-width="2" transform="rotate(-20,{cx-30*s},{cy+20*s})"/>')
    e.append(f'<text x="{cx-30*s}" y="{cy+24*s}" text-anchor="middle" font-size="10" font-weight="bold">5</text>')
    # Snout/beak - 6
    e.append(f'<path d="M{cx-80*s},{cy} L{cx-105*s},{cy-5*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
    e.append(f'<text x="{cx-95*s}" y="{cy-8*s}" text-anchor="middle" font-size="10" font-weight="bold">6</text>')
    # Eye
    e.append(f'<circle cx="{cx-60*s}" cy="{cy-10*s}" r="{6*s}" fill="#000"/>')
    return "\n".join(e)

# ============================================================
# THEME 2: FARM ANIMALS (6 colors each)
# ============================================================
def draw_cow(cx, cy, s=1.0):
    e = []
    # Body - 1
    e.append(f'<ellipse cx="{cx}" cy="{cy+10*s}" rx="{80*s}" ry="{50*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
    e.append(f'<text x="{cx+20*s}" y="{cy+20*s}" text-anchor="middle" font-size="18" font-weight="bold">1</text>')
    # Spots - 2
    spots = [(cx-30*s,cy-10*s,18*s),(cx+25*s,cy+25*s,15*s),(cx-10*s,cy+30*s,12*s)]
    for sx,sy,sr in spots:
        e.append(f'<circle cx="{sx}" cy="{sy}" r="{sr}" fill="none" stroke="#000" stroke-width="2"/>')
        e.append(f'<text x="{sx}" y="{sy+5}" text-anchor="middle" font-size="10" font-weight="bold">2</text>')
    # Head - 3
    e.append(f'<circle cx="{cx-85*s}" cy="{cy-20*s}" r="{30*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
    e.append(f'<text x="{cx-85*s}" y="{cy-15*s}" text-anchor="middle" font-size="14" font-weight="bold">3</text>')
    # Horns - 4
    e.append(f'<path d="M{cx-95*s},{cy-48*s} Q{cx-105*s},{cy-70*s} {cx-100*s},{cy-75*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
    e.append(f'<path d="M{cx-75*s},{cy-48*s} Q{cx-65*s},{cy-70*s} {cx-70*s},{cy-75*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
    e.append(f'<text x="{cx-85*s}" y="{cy-60*s}" text-anchor="middle" font-size="10" font-weight="bold">4</text>')
    # Legs - 5
    for lx in [cx-40*s, cx-20*s, cx+20*s, cx+40*s]:
        e.append(f'<rect x="{lx-6*s}" y="{cy+55*s}" width="{12*s}" height="{40*s}" fill="none" stroke="#000" stroke-width="2"/>')
    e.append(f'<text x="{cx-40*s}" y="{cy+80*s}" text-anchor="middle" font-size="10" font-weight="bold">5</text>')
    # Udder/Tail - 6
    e.append(f'<path d="M{cx+75*s},{cy} Q{cx+95*s},{cy-20*s} {cx+100*s},{cy-35*s}" fill="none" stroke="#000" stroke-width="2"/>')
    e.append(f'<text x="{cx+95*s}" y="{cy-20*s}" text-anchor="middle" font-size="10" font-weight="bold">6</text>')
    # Face details
    e.append(f'<circle cx="{cx-92*s}" cy="{cy-25*s}" r="{4*s}" fill="#000"/>')
    e.append(f'<circle cx="{cx-78*s}" cy="{cy-25*s}" r="{4*s}" fill="#000"/>')
    e.append(f'<ellipse cx="{cx-85*s}" cy="{cy-8*s}" rx="{12*s}" ry="{8*s}" fill="none" stroke="#000" stroke-width="1.5"/>')
    return "\n".join(e)


def draw_pig(cx, cy, s=1.0):
    e = []
    # Body - 1
    e.append(f'<ellipse cx="{cx}" cy="{cy+10*s}" rx="{75*s}" ry="{50*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
    e.append(f'<text x="{cx+20*s}" y="{cy+20*s}" text-anchor="middle" font-size="18" font-weight="bold">1</text>')
    # Head - 2
    e.append(f'<circle cx="{cx-70*s}" cy="{cy-20*s}" r="{35*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
    e.append(f'<text x="{cx-70*s}" y="{cy-15*s}" text-anchor="middle" font-size="14" font-weight="bold">2</text>')
    # Snout - 3
    e.append(f'<ellipse cx="{cx-95*s}" cy="{cy-15*s}" rx="{15*s}" ry="{12*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
    e.append(f'<circle cx="{cx-99*s}" cy="{cy-15*s}" r="{3*s}" fill="#000"/>')
    e.append(f'<circle cx="{cx-91*s}" cy="{cy-15*s}" r="{3*s}" fill="#000"/>')
    e.append(f'<text x="{cx-95*s}" y="{cy-5*s}" text-anchor="middle" font-size="10" font-weight="bold">3</text>')
    # Ears - 4
    e.append(f'<polygon points="{cx-80*s},{cy-50*s} {cx-95*s},{cy-75*s} {cx-65*s},{cy-65*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
    e.append(f'<polygon points="{cx-55*s},{cy-50*s} {cx-70*s},{cy-75*s} {cx-45*s},{cy-65*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
    e.append(f'<text x="{cx-75*s}" y="{cy-60*s}" text-anchor="middle" font-size="9" font-weight="bold">4</text>')
    # Legs - 5
    for lx in [cx-35*s, cx-15*s, cx+25*s, cx+45*s]:
        e.append(f'<rect x="{lx-7*s}" y="{cy+55*s}" width="{14*s}" height="{35*s}" fill="none" stroke="#000" stroke-width="2"/>')
    e.append(f'<text x="{cx-35*s}" y="{cy+75*s}" text-anchor="middle" font-size="10" font-weight="bold">5</text>')
    # Tail curl - 6
    e.append(f'<path d="M{cx+72*s},{cy} Q{cx+90*s},{cy-10*s} {cx+85*s},{cy-25*s} Q{cx+80*s},{cy-35*s} {cx+90*s},{cy-40*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
    e.append(f'<text x="{cx+90*s}" y="{cy-25*s}" text-anchor="middle" font-size="10" font-weight="bold">6</text>')
    # Eyes
    e.append(f'<circle cx="{cx-78*s}" cy="{cy-28*s}" r="{5*s}" fill="#000"/>')
    e.append(f'<circle cx="{cx-62*s}" cy="{cy-28*s}" r="{5*s}" fill="#000"/>')
    return "\n".join(e)

def draw_chicken(cx, cy, s=1.0):
    e = []
    # Body - 1
    e.append(f'<ellipse cx="{cx}" cy="{cy+15*s}" rx="{65*s}" ry="{50*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
    e.append(f'<text x="{cx}" y="{cy+25*s}" text-anchor="middle" font-size="18" font-weight="bold">1</text>')
    # Head - 2
    e.append(f'<circle cx="{cx-60*s}" cy="{cy-40*s}" r="{28*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
    e.append(f'<text x="{cx-60*s}" y="{cy-35*s}" text-anchor="middle" font-size="14" font-weight="bold">2</text>')
    # Comb - 3
    e.append(f'<path d="M{cx-70*s},{cy-68*s} Q{cx-65*s},{cy-85*s} {cx-60*s},{cy-68*s} Q{cx-55*s},{cy-85*s} {cx-50*s},{cy-68*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
    e.append(f'<text x="{cx-60*s}" y="{cy-75*s}" text-anchor="middle" font-size="10" font-weight="bold">3</text>')
    # Beak - 4
    e.append(f'<polygon points="{cx-85*s},{cy-40*s} {cx-105*s},{cy-35*s} {cx-85*s},{cy-30*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
    e.append(f'<text x="{cx-95*s}" y="{cy-33*s}" text-anchor="middle" font-size="9" font-weight="bold">4</text>')
    # Wing - 5
    e.append(f'<ellipse cx="{cx+15*s}" cy="{cy+10*s}" rx="{35*s}" ry="{25*s}" fill="none" stroke="#000" stroke-width="2" transform="rotate(-10,{cx+15*s},{cy+10*s})"/>')
    e.append(f'<text x="{cx+15*s}" y="{cy+15*s}" text-anchor="middle" font-size="14" font-weight="bold">5</text>')
    # Tail feathers - 6
    e.append(f'<path d="M{cx+60*s},{cy} Q{cx+90*s},{cy-20*s} {cx+95*s},{cy-40*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
    e.append(f'<path d="M{cx+60*s},{cy+5*s} Q{cx+85*s},{cy-10*s} {cx+90*s},{cy-30*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
    e.append(f'<path d="M{cx+55*s},{cy+10*s} Q{cx+80*s},{cy} {cx+85*s},{cy-20*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
    e.append(f'<text x="{cx+80*s}" y="{cy-15*s}" text-anchor="middle" font-size="10" font-weight="bold">6</text>')
    # Legs - 7
    e.append(f'<line x1="{cx-15*s}" y1="{cy+60*s}" x2="{cx-15*s}" y2="{cy+90*s}" stroke="#000" stroke-width="2.5"/>')
    e.append(f'<line x1="{cx+15*s}" y1="{cy+60*s}" x2="{cx+15*s}" y2="{cy+90*s}" stroke="#000" stroke-width="2.5"/>')
    e.append(f'<text x="{cx}" y="{cy+85*s}" text-anchor="middle" font-size="10" font-weight="bold">7</text>')
    # Eye, wattle
    e.append(f'<circle cx="{cx-65*s}" cy="{cy-45*s}" r="{5*s}" fill="#000"/>')
    e.append(f'<ellipse cx="{cx-72*s}" cy="{cy-25*s}" rx="{6*s}" ry="{10*s}" fill="none" stroke="#000" stroke-width="1.5"/>')
    return "\n".join(e)

def draw_horse(cx, cy, s=1.0):
    e = []
    # Body - 1
    e.append(f'<ellipse cx="{cx+10*s}" cy="{cy+10*s}" rx="{80*s}" ry="{45*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
    e.append(f'<text x="{cx+20*s}" y="{cy+15*s}" text-anchor="middle" font-size="18" font-weight="bold">1</text>')
    # Neck - 2
    e.append(f'<path d="M{cx-55*s},{cy-20*s} Q{cx-70*s},{cy-50*s} {cx-75*s},{cy-70*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
    e.append(f'<path d="M{cx-35*s},{cy-20*s} Q{cx-50*s},{cy-50*s} {cx-55*s},{cy-70*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
    e.append(f'<text x="{cx-55*s}" y="{cy-40*s}" text-anchor="middle" font-size="12" font-weight="bold">2</text>')
    # Head - 3
    e.append(f'<ellipse cx="{cx-75*s}" cy="{cy-85*s}" rx="{22*s}" ry="{18*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
    e.append(f'<text x="{cx-75*s}" y="{cy-80*s}" text-anchor="middle" font-size="12" font-weight="bold">3</text>')
    e.append(f'<circle cx="{cx-80*s}" cy="{cy-90*s}" r="{4*s}" fill="#000"/>')
    # Mane - 4
    e.append(f'<path d="M{cx-65*s},{cy-70*s} Q{cx-55*s},{cy-60*s} {cx-60*s},{cy-50*s} Q{cx-50*s},{cy-40*s} {cx-55*s},{cy-30*s}" fill="none" stroke="#000" stroke-width="3"/>')
    e.append(f'<text x="{cx-48*s}" y="{cy-55*s}" text-anchor="middle" font-size="10" font-weight="bold">4</text>')
    # Legs - 5
    for lx in [cx-30*s, cx-10*s, cx+40*s, cx+60*s]:
        e.append(f'<rect x="{lx-5*s}" y="{cy+50*s}" width="{10*s}" height="{45*s}" fill="none" stroke="#000" stroke-width="2"/>')
    e.append(f'<text x="{cx-30*s}" y="{cy+75*s}" text-anchor="middle" font-size="10" font-weight="bold">5</text>')
    # Hooves - 6
    for lx in [cx-30*s, cx-10*s, cx+40*s, cx+60*s]:
        e.append(f'<rect x="{lx-6*s}" y="{cy+92*s}" width="{12*s}" height="{8*s}" fill="none" stroke="#000" stroke-width="2"/>')
    e.append(f'<text x="{cx+60*s}" y="{cy+99*s}" text-anchor="middle" font-size="9" font-weight="bold">6</text>')
    # Tail - 7
    e.append(f'<path d="M{cx+85*s},{cy} Q{cx+100*s},{cy+20*s} {cx+95*s},{cy+45*s} Q{cx+90*s},{cy+60*s} {cx+100*s},{cy+70*s}" fill="none" stroke="#000" stroke-width="3"/>')
    e.append(f'<text x="{cx+100*s}" y="{cy+50*s}" text-anchor="middle" font-size="10" font-weight="bold">7</text>')
    return "\n".join(e)


def draw_sheep(cx, cy, s=1.0):
    e = []
    # Wool body - 1
    for dx, dy in [(0,0),(-30*s,-15*s),(30*s,-15*s),(-25*s,20*s),(25*s,20*s)]:
        e.append(f'<circle cx="{cx+dx}" cy="{cy+dy}" r="{30*s}" fill="none" stroke="#000" stroke-width="2"/>')
    e.append(f'<text x="{cx}" y="{cy+5}" text-anchor="middle" font-size="18" font-weight="bold">1</text>')
    # Face - 2
    e.append(f'<ellipse cx="{cx-65*s}" cy="{cy}" rx="{20*s}" ry="{25*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
    e.append(f'<text x="{cx-65*s}" y="{cy+5}" text-anchor="middle" font-size="12" font-weight="bold">2</text>')
    # Ears - 3
    e.append(f'<ellipse cx="{cx-75*s}" cy="{cy-20*s}" rx="{12*s}" ry="{8*s}" fill="none" stroke="#000" stroke-width="2" transform="rotate(-30,{cx-75*s},{cy-20*s})"/>')
    e.append(f'<ellipse cx="{cx-55*s}" cy="{cy-20*s}" rx="{12*s}" ry="{8*s}" fill="none" stroke="#000" stroke-width="2" transform="rotate(30,{cx-55*s},{cy-20*s})"/>')
    e.append(f'<text x="{cx-65*s}" y="{cy-20*s}" text-anchor="middle" font-size="9" font-weight="bold">3</text>')
    # Legs - 4
    for lx in [cx-25*s, cx-10*s, cx+15*s, cx+30*s]:
        e.append(f'<rect x="{lx-5*s}" y="{cy+40*s}" width="{10*s}" height="{35*s}" fill="none" stroke="#000" stroke-width="2"/>')
    e.append(f'<text x="{cx-25*s}" y="{cy+60*s}" text-anchor="middle" font-size="10" font-weight="bold">4</text>')
    # Hooves - 5
    for lx in [cx-25*s, cx-10*s, cx+15*s, cx+30*s]:
        e.append(f'<rect x="{lx-6*s}" y="{cy+73*s}" width="{12*s}" height="{6*s}" fill="none" stroke="#000" stroke-width="2"/>')
    e.append(f'<text x="{cx+30*s}" y="{cy+78*s}" text-anchor="middle" font-size="9" font-weight="bold">5</text>')
    # Tail - 6
    e.append(f'<circle cx="{cx+55*s}" cy="{cy+5*s}" r="{12*s}" fill="none" stroke="#000" stroke-width="2"/>')
    e.append(f'<text x="{cx+55*s}" y="{cy+9*s}" text-anchor="middle" font-size="10" font-weight="bold">6</text>')
    # Eyes
    e.append(f'<circle cx="{cx-70*s}" cy="{cy-5*s}" r="{4*s}" fill="#000"/>')
    e.append(f'<circle cx="{cx-60*s}" cy="{cy-5*s}" r="{4*s}" fill="#000"/>')
    return "\n".join(e)

# ============================================================
# GENERIC PARAMETRIC DRAWINGS (for filling 50 pages per theme)
# ============================================================
def draw_generic_animal(cx, cy, s, params):
    """Generic animal with numbered parts: body, head, limbs, features."""
    e = []
    body_shape = params.get("body", "ellipse")
    # Body - 1
    if body_shape == "circle":
        e.append(f'<circle cx="{cx}" cy="{cy}" r="{65*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
    else:
        bw = params.get("bw", 80)
        bh = params.get("bh", 50)
        e.append(f'<ellipse cx="{cx}" cy="{cy+10*s}" rx="{bw*s}" ry="{bh*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
    e.append(f'<text x="{cx+15*s}" y="{cy+15*s}" text-anchor="middle" font-size="18" font-weight="bold">1</text>')
    # Head - 2
    hx = params.get("hx", -70)
    hy = params.get("hy", -30)
    hr = params.get("hr", 30)
    e.append(f'<circle cx="{cx+hx*s}" cy="{cy+hy*s}" r="{hr*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
    e.append(f'<text x="{cx+hx*s}" y="{cy+hy*s+5}" text-anchor="middle" font-size="14" font-weight="bold">2</text>')
    # Eyes
    e.append(f'<circle cx="{cx+(hx-8)*s}" cy="{cy+(hy-8)*s}" r="{4*s}" fill="#000"/>')
    e.append(f'<circle cx="{cx+(hx+8)*s}" cy="{cy+(hy-8)*s}" r="{4*s}" fill="#000"/>')
    # Ears/horns - 3
    ear_type = params.get("ears", "pointed")
    if ear_type == "pointed":
        e.append(f'<polygon points="{cx+(hx-15)*s},{cy+(hy-hr)*s} {cx+(hx-5)*s},{cy+(hy-hr-25)*s} {cx+(hx+5)*s},{cy+(hy-hr)*s}" fill="none" stroke="#000" stroke-width="2"/>')
        e.append(f'<polygon points="{cx+(hx+5)*s},{cy+(hy-hr)*s} {cx+(hx+15)*s},{cy+(hy-hr-25)*s} {cx+(hx+25)*s},{cy+(hy-hr)*s}" fill="none" stroke="#000" stroke-width="2"/>')
    else:
        e.append(f'<ellipse cx="{cx+(hx-15)*s}" cy="{cy+(hy-hr+5)*s}" rx="{12*s}" ry="{8*s}" fill="none" stroke="#000" stroke-width="2" transform="rotate(-20,{cx+(hx-15)*s},{cy+(hy-hr+5)*s})"/>')
        e.append(f'<ellipse cx="{cx+(hx+15)*s}" cy="{cy+(hy-hr+5)*s}" rx="{12*s}" ry="{8*s}" fill="none" stroke="#000" stroke-width="2" transform="rotate(20,{cx+(hx+15)*s},{cy+(hy-hr+5)*s})"/>')
    e.append(f'<text x="{cx+(hx)*s}" y="{cy+(hy-hr-5)*s}" text-anchor="middle" font-size="10" font-weight="bold">3</text>')
    # Legs - 4
    num_legs = params.get("legs", 4)
    leg_y = cy + params.get("bh", 50)*s + 5*s
    leg_spread = params.get("bw", 80) * 0.6
    for i in range(num_legs):
        lx = cx - leg_spread*s/2 + i * (leg_spread*s / (num_legs-1)) if num_legs > 1 else cx
        e.append(f'<rect x="{lx-5*s}" y="{leg_y}" width="{10*s}" height="{35*s}" fill="none" stroke="#000" stroke-width="2"/>')
    e.append(f'<text x="{cx}" y="{leg_y+25*s}" text-anchor="middle" font-size="10" font-weight="bold">4</text>')
    # Tail - 5
    tail_type = params.get("tail", "curve")
    tx = cx + params.get("bw", 80)*s * 0.9
    if tail_type == "curl":
        e.append(f'<path d="M{tx},{cy} Q{tx+20*s},{cy-15*s} {tx+15*s},{cy-30*s} Q{tx+10*s},{cy-40*s} {tx+20*s},{cy-45*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
    else:
        e.append(f'<path d="M{tx},{cy} Q{tx+25*s},{cy+15*s} {tx+20*s},{cy+35*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
    e.append(f'<text x="{tx+15*s}" y="{cy-20*s}" text-anchor="middle" font-size="10" font-weight="bold">5</text>')
    # Markings/spot - 6
    e.append(f'<ellipse cx="{cx+20*s}" cy="{cy-10*s}" rx="{20*s}" ry="{15*s}" fill="none" stroke="#000" stroke-width="1.5"/>')
    e.append(f'<text x="{cx+20*s}" y="{cy-5*s}" text-anchor="middle" font-size="10" font-weight="bold">6</text>')
    return "\n".join(e)

def draw_generic_object(cx, cy, s, params):
    """Generic object with numbered parts."""
    e = []
    shape = params.get("main_shape", "rect")
    # Main body - 1
    if shape == "rect":
        w = params.get("w", 100)
        h = params.get("h", 80)
        e.append(f'<rect x="{cx-w*s/2}" y="{cy-h*s/2}" width="{w*s}" height="{h*s}" rx="5" fill="none" stroke="#000" stroke-width="2.5"/>')
    elif shape == "circle":
        r = params.get("r", 60)
        e.append(f'<circle cx="{cx}" cy="{cy}" r="{r*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
    elif shape == "diamond":
        w = params.get("w", 80)
        h = params.get("h", 100)
        e.append(f'<polygon points="{cx},{cy-h*s/2} {cx+w*s/2},{cy} {cx},{cy+h*s/2} {cx-w*s/2},{cy}" fill="none" stroke="#000" stroke-width="2.5"/>')
    else:
        e.append(f'<ellipse cx="{cx}" cy="{cy}" rx="{params.get("w",80)*s/2}" ry="{params.get("h",60)*s/2}" fill="none" stroke="#000" stroke-width="2.5"/>')
    e.append(f'<text x="{cx}" y="{cy+5}" text-anchor="middle" font-size="18" font-weight="bold">1</text>')
    # Detail regions 2-6
    details = params.get("details", [])
    for i, detail in enumerate(details):
        d_type = detail.get("type", "circle")
        dx = detail.get("x", 0)
        dy = detail.get("y", 0)
        num = i + 2
        if d_type == "circle":
            dr = detail.get("r", 15)
            e.append(f'<circle cx="{cx+dx*s}" cy="{cy+dy*s}" r="{dr*s}" fill="none" stroke="#000" stroke-width="2"/>')
        elif d_type == "rect":
            dw = detail.get("w", 30)
            dh = detail.get("h", 20)
            e.append(f'<rect x="{cx+dx*s-dw*s/2}" y="{cy+dy*s-dh*s/2}" width="{dw*s}" height="{dh*s}" fill="none" stroke="#000" stroke-width="2"/>')
        elif d_type == "triangle":
            ds = detail.get("size", 20)
            e.append(f'<polygon points="{cx+dx*s},{cy+dy*s-ds*s} {cx+dx*s-ds*s},{cy+dy*s+ds*s/2} {cx+dx*s+ds*s},{cy+dy*s+ds*s/2}" fill="none" stroke="#000" stroke-width="2"/>')
        elif d_type == "ellipse":
            dw = detail.get("w", 30)
            dh = detail.get("h", 20)
            e.append(f'<ellipse cx="{cx+dx*s}" cy="{cy+dy*s}" rx="{dw*s/2}" ry="{dh*s/2}" fill="none" stroke="#000" stroke-width="2"/>')
        e.append(f'<text x="{cx+dx*s}" y="{cy+dy*s+5}" text-anchor="middle" font-size="12" font-weight="bold">{num}</text>')
    return "\n".join(e)


# ============================================================
# MORE SPECIFIC DRAWINGS FOR VARIOUS THEMES
# ============================================================
def draw_dinosaur(cx, cy, s=1.0):
    e = []
    # Body - 1
    e.append(f'<ellipse cx="{cx}" cy="{cy}" rx="{75*s}" ry="{45*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
    e.append(f'<text x="{cx+10*s}" y="{cy+10*s}" text-anchor="middle" font-size="18" font-weight="bold">1</text>')
    # Head - 2
    e.append(f'<ellipse cx="{cx-85*s}" cy="{cy-30*s}" rx="{30*s}" ry="{22*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
    e.append(f'<text x="{cx-85*s}" y="{cy-25*s}" text-anchor="middle" font-size="14" font-weight="bold">2</text>')
    e.append(f'<circle cx="{cx-90*s}" cy="{cy-38*s}" r="{5*s}" fill="#000"/>')
    # Neck - 3
    e.append(f'<path d="M{cx-60*s},{cy-15*s} Q{cx-70*s},{cy-30*s} {cx-60*s},{cy-35*s}" fill="none" stroke="#000" stroke-width="8"/>')
    e.append(f'<text x="{cx-65*s}" y="{cy-15*s}" text-anchor="middle" font-size="10" font-weight="bold">3</text>')
    # Back plates/spikes - 4
    for i in range(5):
        px = cx - 30*s + i*20*s
        e.append(f'<polygon points="{px-5*s},{cy-45*s} {px},{cy-70*s} {px+5*s},{cy-45*s}" fill="none" stroke="#000" stroke-width="2"/>')
    e.append(f'<text x="{cx}" y="{cy-55*s}" text-anchor="middle" font-size="10" font-weight="bold">4</text>')
    # Legs - 5
    for lx in [cx-30*s, cx-10*s, cx+25*s, cx+45*s]:
        e.append(f'<rect x="{lx-7*s}" y="{cy+40*s}" width="{14*s}" height="{40*s}" rx="3" fill="none" stroke="#000" stroke-width="2"/>')
    e.append(f'<text x="{cx-30*s}" y="{cy+65*s}" text-anchor="middle" font-size="10" font-weight="bold">5</text>')
    # Tail - 6
    e.append(f'<path d="M{cx+70*s},{cy} Q{cx+100*s},{cy+10*s} {cx+120*s},{cy-5*s} Q{cx+130*s},{cy-15*s} {cx+125*s},{cy-25*s}" fill="none" stroke="#000" stroke-width="3"/>')
    e.append(f'<text x="{cx+110*s}" y="{cy-10*s}" text-anchor="middle" font-size="10" font-weight="bold">6</text>')
    # Belly marking - 7
    e.append(f'<ellipse cx="{cx}" cy="{cy+15*s}" rx="{40*s}" ry="{20*s}" fill="none" stroke="#000" stroke-width="1.5"/>')
    e.append(f'<text x="{cx}" y="{cy+20*s}" text-anchor="middle" font-size="12" font-weight="bold">7</text>')
    return "\n".join(e)

def draw_trex(cx, cy, s=1.0):
    e = []
    # Body - 1
    e.append(f'<ellipse cx="{cx}" cy="{cy}" rx="{60*s}" ry="{50*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
    e.append(f'<text x="{cx}" y="{cy+5}" text-anchor="middle" font-size="18" font-weight="bold">1</text>')
    # Head - 2 (big jaw)
    e.append(f'<ellipse cx="{cx-70*s}" cy="{cy-40*s}" rx="{35*s}" ry="{25*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
    e.append(f'<text x="{cx-70*s}" y="{cy-35*s}" text-anchor="middle" font-size="14" font-weight="bold">2</text>')
    # Teeth
    for i in range(5):
        tx = cx - 90*s + i*10*s
        e.append(f'<polygon points="{tx},{cy-20*s} {tx+3*s},{cy-12*s} {tx+6*s},{cy-20*s}" fill="none" stroke="#000" stroke-width="1.5"/>')
    # Tiny arms - 3
    e.append(f'<path d="M{cx-30*s},{cy-20*s} L{cx-45*s},{cy-10*s} L{cx-50*s},{cy-15*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
    e.append(f'<path d="M{cx-25*s},{cy-15*s} L{cx-40*s},{cy-5*s} L{cx-45*s},{cy-10*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
    e.append(f'<text x="{cx-42*s}" y="{cy-3*s}" text-anchor="middle" font-size="10" font-weight="bold">3</text>')
    # Big legs - 4
    e.append(f'<path d="M{cx-15*s},{cy+45*s} L{cx-20*s},{cy+80*s} L{cx-35*s},{cy+85*s}" fill="none" stroke="#000" stroke-width="3"/>')
    e.append(f'<path d="M{cx+20*s},{cy+45*s} L{cx+25*s},{cy+80*s} L{cx+10*s},{cy+85*s}" fill="none" stroke="#000" stroke-width="3"/>')
    e.append(f'<text x="{cx}" y="{cy+75*s}" text-anchor="middle" font-size="10" font-weight="bold">4</text>')
    # Tail - 5
    e.append(f'<path d="M{cx+55*s},{cy} Q{cx+90*s},{cy+10*s} {cx+110*s},{cy-10*s} Q{cx+125*s},{cy-20*s} {cx+130*s},{cy-15*s}" fill="none" stroke="#000" stroke-width="3"/>')
    e.append(f'<text x="{cx+100*s}" y="{cy-5*s}" text-anchor="middle" font-size="10" font-weight="bold">5</text>')
    # Eye - 6
    e.append(f'<circle cx="{cx-75*s}" cy="{cy-50*s}" r="{10*s}" fill="none" stroke="#000" stroke-width="2"/>')
    e.append(f'<circle cx="{cx-75*s}" cy="{cy-50*s}" r="{5*s}" fill="#000"/>')
    e.append(f'<text x="{cx-60*s}" y="{cy-55*s}" text-anchor="middle" font-size="9" font-weight="bold">6</text>')
    return "\n".join(e)

def draw_rocket_detailed(cx, cy, s=1.0):
    e = []
    # Body - 1
    e.append(f'<rect x="{cx-28*s}" y="{cy-50*s}" width="{56*s}" height="{120*s}" rx="8" fill="none" stroke="#000" stroke-width="2.5"/>')
    e.append(f'<text x="{cx}" y="{cy+20*s}" text-anchor="middle" font-size="18" font-weight="bold">1</text>')
    # Nose cone - 2
    e.append(f'<polygon points="{cx-28*s},{cy-50*s} {cx},{cy-100*s} {cx+28*s},{cy-50*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
    e.append(f'<text x="{cx}" y="{cy-60*s}" text-anchor="middle" font-size="14" font-weight="bold">2</text>')
    # Window - 3
    e.append(f'<circle cx="{cx}" cy="{cy-20*s}" r="{16*s}" fill="none" stroke="#000" stroke-width="2"/>')
    e.append(f'<circle cx="{cx}" cy="{cy-20*s}" r="{10*s}" fill="none" stroke="#000" stroke-width="1.5"/>')
    e.append(f'<text x="{cx}" y="{cy-16*s}" text-anchor="middle" font-size="12" font-weight="bold">3</text>')
    # Left fin - 4
    e.append(f'<polygon points="{cx-28*s},{cy+40*s} {cx-60*s},{cy+70*s} {cx-28*s},{cy+70*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
    e.append(f'<text x="{cx-38*s}" y="{cy+60*s}" text-anchor="middle" font-size="11" font-weight="bold">4</text>')
    # Right fin - 5
    e.append(f'<polygon points="{cx+28*s},{cy+40*s} {cx+60*s},{cy+70*s} {cx+28*s},{cy+70*s}" fill="none" stroke="#000" stroke-width="2.5"/>')
    e.append(f'<text x="{cx+38*s}" y="{cy+60*s}" text-anchor="middle" font-size="11" font-weight="bold">5</text>')
    # Flames - 6
    e.append(f'<polygon points="{cx-20*s},{cy+70*s} {cx},{cy+115*s} {cx+20*s},{cy+70*s}" fill="none" stroke="#000" stroke-width="2"/>')
    e.append(f'<text x="{cx}" y="{cy+95*s}" text-anchor="middle" font-size="11" font-weight="bold">6</text>')
    # Stripe detail - 7
    e.append(f'<rect x="{cx-28*s}" y="{cy+10*s}" width="{56*s}" height="{15*s}" fill="none" stroke="#000" stroke-width="2"/>')
    e.append(f'<text x="{cx}" y="{cy+22*s}" text-anchor="middle" font-size="10" font-weight="bold">7</text>')
    return "\n".join(e)


# ============================================================
# MASTER DRAWING REGISTRY - Organized by theme
# Each entry: (title, draw_function, num_colors)
# ============================================================

# Helper to create parametric animal variants
def make_animal(name, body="ellipse", bw=80, bh=50, hx=-70, hy=-30, hr=30, ears="pointed", legs=4, tail="curve"):
    def drawer(cx, cy, s=1.0):
        return draw_generic_animal(cx, cy, s, {"body":body,"bw":bw,"bh":bh,"hx":hx,"hy":hy,"hr":hr,"ears":ears,"legs":legs,"tail":tail})
    return (name, drawer, 6)

def make_object(name, main_shape="rect", w=100, h=80, details=None):
    if details is None:
        details = [{"type":"circle","x":0,"y":-20,"r":15},{"type":"rect","x":-30,"y":20,"w":25,"h":20},
                   {"type":"circle","x":30,"y":20,"r":12},{"type":"triangle","x":0,"y":45,"size":15},
                   {"type":"ellipse","x":35,"y":-25,"w":20,"h":15}]
    def drawer(cx, cy, s=1.0):
        return draw_generic_object(cx, cy, s, {"main_shape":main_shape,"w":w,"h":h,"details":details})
    return (name, drawer, min(len(details)+1, 7))

# Theme-based drawing collections
THEME_DRAWINGS = {
    "Ocean Animals": [
        ("Whale", draw_whale, 6),
        ("Jellyfish", draw_jellyfish, 6),
        ("Seahorse", draw_seahorse, 7),
        ("Octopus", draw_octopus, 6),
        ("Crab", draw_crab, 6),
        ("Starfish", draw_starfish, 6),
        ("Sea Turtle", draw_turtle_ocean, 6),
        ("Dolphin", draw_dolphin, 6),
        make_animal("Seal", bw=75, bh=40, hx=-65, hy=-25, hr=25, ears="round", legs=4, tail="curve"),
        make_animal("Shark", bw=90, bh=35, hx=-80, hy=-10, hr=20, ears="pointed", legs=2, tail="curve"),
    ],
    "Farm Animals": [
        ("Cow", draw_cow, 6),
        ("Pig", draw_pig, 6),
        ("Chicken", draw_chicken, 7),
        ("Horse", draw_horse, 7),
        ("Sheep", draw_sheep, 6),
        make_animal("Goat", bw=70, bh=45, hx=-65, hy=-30, hr=25, ears="round", legs=4, tail="curl"),
        make_animal("Donkey", bw=75, bh=45, hx=-70, hy=-35, hr=28, ears="pointed", legs=4, tail="curve"),
        make_animal("Duck", bw=60, bh=40, hx=-55, hy=-30, hr=22, ears="round", legs=2, tail="curve"),
        make_animal("Rabbit", bw=55, bh=45, hx=-50, hy=-40, hr=25, ears="pointed", legs=4, tail="curl"),
        make_animal("Turkey", bw=65, bh=50, hx=-60, hy=-35, hr=28, ears="round", legs=2, tail="curve"),
    ],
    "Space Adventure": [
        ("Rocket Ship", draw_rocket_detailed, 7),
        make_object("Planet", "circle", w=120, h=120, details=[
            {"type":"circle","x":-20,"y":-15,"r":18},{"type":"circle","x":20,"y":15,"r":12},
            {"type":"ellipse","x":0,"y":0,"w":140,"h":30},{"type":"circle","x":-35,"y":25,"r":10},
            {"type":"triangle","x":30,"y":-30,"size":12}]),
        make_object("UFO", "ellipse", w=140, h=50, details=[
            {"type":"circle","x":0,"y":-25,"r":25},{"type":"circle","x":-35,"y":0,"r":8},
            {"type":"circle","x":0,"y":0,"r":8},{"type":"circle","x":35,"y":0,"r":8},
            {"type":"triangle","x":0,"y":30,"size":15}]),
        make_object("Astronaut", "rect", w=60, h=100, details=[
            {"type":"circle","x":0,"y":-40,"r":22},{"type":"rect","x":-25,"y":10,"w":15,"h":40},
            {"type":"rect","x":25,"y":10,"w":15,"h":40},{"type":"rect","x":-12,"y":50,"w":12,"h":35},
            {"type":"rect","x":12,"y":50,"w":12,"h":35}]),
        make_object("Satellite", "rect", w=40, h=50, details=[
            {"type":"rect","x":-50,"y":0,"w":40,"h":25},{"type":"rect","x":50,"y":0,"w":40,"h":25},
            {"type":"circle","x":0,"y":-15,"r":10},{"type":"triangle","x":0,"y":30,"size":12},
            {"type":"circle","x":0,"y":15,"r":8}]),
        make_object("Moon", "circle", w=100, h=100, details=[
            {"type":"circle","x":-20,"y":-15,"r":15},{"type":"circle","x":15,"y":20,"r":12},
            {"type":"circle","x":-30,"y":20,"r":8},{"type":"circle","x":25,"y":-25,"r":10},
            {"type":"circle","x":5,"y":-5,"r":18}]),
        make_object("Star", "diamond", w=80, h=100, details=[
            {"type":"triangle","x":0,"y":-30,"size":15},{"type":"triangle","x":-30,"y":0,"size":12},
            {"type":"triangle","x":30,"y":0,"size":12},{"type":"circle","x":0,"y":0,"r":15},
            {"type":"triangle","x":0,"y":30,"size":15}]),
        make_object("Comet", "ellipse", w=60, h=40, details=[
            {"type":"ellipse","x":50,"y":0,"w":60,"h":15},{"type":"ellipse","x":80,"y":-8,"w":40,"h":8},
            {"type":"ellipse","x":80,"y":8,"w":40,"h":8},{"type":"circle","x":-10,"y":0,"r":12},
            {"type":"circle","x":10,"y":5,"r":8}]),
        make_object("Space Station", "rect", w=120, h=40, details=[
            {"type":"rect","x":-60,"y":-30,"w":30,"h":20},{"type":"rect","x":60,"y":-30,"w":30,"h":20},
            {"type":"circle","x":0,"y":0,"r":12},{"type":"rect","x":-40,"y":20,"w":20,"h":15},
            {"type":"rect","x":40,"y":20,"w":20,"h":15}]),
        make_object("Alien", "circle", w=80, h=80, details=[
            {"type":"ellipse","x":-15,"y":-10,"w":20,"h":25},{"type":"ellipse","x":15,"y":-10,"w":20,"h":25},
            {"type":"ellipse","x":0,"y":20,"w":15,"h":10},{"type":"rect","x":-25,"y":40,"w":10,"h":30},
            {"type":"rect","x":25,"y":40,"w":10,"h":30}]),
    ],
    "Dinosaurs": [
        ("Stegosaurus", draw_dinosaur, 7),
        ("T-Rex", draw_trex, 6),
        make_animal("Triceratops", bw=80, bh=50, hx=-75, hy=-20, hr=35, ears="pointed", legs=4, tail="curve"),
        make_animal("Brontosaurus", bw=85, bh=40, hx=-90, hy=-50, hr=22, ears="round", legs=4, tail="curve"),
        make_animal("Pterodactyl", bw=60, bh=30, hx=-55, hy=-25, hr=20, ears="pointed", legs=2, tail="curve"),
        make_animal("Velociraptor", bw=55, bh=40, hx=-55, hy=-35, hr=22, ears="pointed", legs=2, tail="curve"),
        make_animal("Ankylosaurus", bw=85, bh=45, hx=-70, hy=-15, hr=25, ears="round", legs=4, tail="curve"),
        make_animal("Diplodocus", bw=90, bh=35, hx=-95, hy=-55, hr=20, ears="round", legs=4, tail="curve"),
        make_animal("Spinosaurus", bw=75, bh=45, hx=-70, hy=-30, hr=28, ears="pointed", legs=2, tail="curve"),
        make_animal("Baby Dino Egg", body="circle", bw=65, bh=65, hx=0, hy=-50, hr=20, ears="round", legs=2, tail="curl"),
    ],
}

# Generate remaining themes using parametric approach
def generate_theme_drawings(theme_name, seed):
    """Generate 10 drawings for a theme using parametric variations."""
    random.seed(seed)
    drawings = []
    
    # Theme-specific naming and shape configs
    theme_configs = {
        "Garden & Flowers": [
            ("Sunflower", "circle", 100, 100), ("Rose", "circle", 90, 90),
            ("Tulip", "ellipse", 50, 80), ("Daisy", "circle", 80, 80),
            ("Cactus", "rect", 40, 100), ("Watering Can", "rect", 80, 60),
            ("Butterfly", "ellipse", 100, 60), ("Snail", "circle", 70, 70),
            ("Ladybug", "ellipse", 90, 70), ("Garden Pot", "rect", 70, 60),
        ],
        "Food & Treats": [
            ("Birthday Cake", "rect", 100, 80), ("Pizza Slice", "diamond", 80, 120),
            ("Donut", "circle", 90, 90), ("Cupcake", "ellipse", 80, 70),
            ("Ice Cream Cone", "diamond", 60, 120), ("Lollipop", "circle", 80, 80),
            ("Cookie", "circle", 85, 85), ("Hamburger", "ellipse", 100, 70),
            ("Hot Dog", "ellipse", 120, 40), ("Candy Bar", "rect", 100, 50),
        ],
        "Vehicles & Transport": [
            ("Fire Truck", "rect", 140, 60), ("Airplane", "ellipse", 130, 40),
            ("Train", "rect", 120, 50), ("Submarine", "ellipse", 120, 50),
            ("Helicopter", "ellipse", 90, 50), ("School Bus", "rect", 130, 55),
            ("Sailboat", "diamond", 80, 100), ("Hot Air Balloon", "circle", 90, 90),
            ("Bicycle", "rect", 110, 60), ("Tractor", "rect", 100, 65),
        ],
        "Insects & Bugs": [
            ("Butterfly", "ellipse", 120, 60), ("Ladybug", "ellipse", 80, 65),
            ("Dragonfly", "ellipse", 30, 80), ("Caterpillar", "ellipse", 120, 35),
            ("Bee", "ellipse", 70, 50), ("Spider", "circle", 60, 60),
            ("Ant", "ellipse", 90, 30), ("Grasshopper", "ellipse", 100, 40),
            ("Firefly", "ellipse", 50, 60), ("Beetle", "ellipse", 70, 55),
        ],
        "Birds & Sky": [
            ("Parrot", "ellipse", 60, 80), ("Owl", "ellipse", 65, 80),
            ("Eagle", "ellipse", 80, 50), ("Penguin", "ellipse", 55, 85),
            ("Flamingo", "circle", 50, 50), ("Toucan", "ellipse", 60, 70),
            ("Robin", "ellipse", 55, 60), ("Peacock", "circle", 70, 70),
            ("Hummingbird", "ellipse", 45, 50), ("Cloud & Sun", "ellipse", 100, 50),
        ],
        "Jungle Animals": [
            ("Lion", "ellipse", 80, 55), ("Elephant", "ellipse", 90, 65),
            ("Giraffe", "ellipse", 60, 50), ("Monkey", "circle", 55, 55),
            ("Tiger", "ellipse", 85, 50), ("Snake", "ellipse", 120, 25),
            ("Parrot", "ellipse", 50, 65), ("Zebra", "ellipse", 80, 50),
            ("Hippo", "ellipse", 85, 60), ("Crocodile", "ellipse", 120, 35),
        ],
        "Under the Sea": [
            ("Clownfish", "ellipse", 70, 45), ("Pufferfish", "circle", 70, 70),
            ("Anglerfish", "circle", 65, 65), ("Manta Ray", "ellipse", 110, 50),
            ("Coral", "rect", 80, 90), ("Seaweed", "rect", 30, 110),
            ("Lobster", "ellipse", 70, 45), ("Treasure Chest", "rect", 90, 60),
            ("Submarine", "ellipse", 110, 45), ("Anchor", "rect", 50, 100),
        ],
        "Fantasy & Magic": [
            ("Dragon", "ellipse", 90, 55), ("Unicorn", "ellipse", 80, 55),
            ("Castle", "rect", 100, 100), ("Wizard Hat", "diamond", 80, 100),
            ("Magic Wand", "rect", 20, 100), ("Fairy", "circle", 50, 50),
            ("Crystal Ball", "circle", 80, 80), ("Shield", "diamond", 70, 90),
            ("Potion Bottle", "rect", 50, 80), ("Crown", "rect", 90, 40),
        ],
        "Sports & Games": [
            ("Soccer Ball", "circle", 85, 85), ("Basketball", "circle", 80, 80),
            ("Baseball Bat", "rect", 25, 110), ("Tennis Racket", "ellipse", 55, 80),
            ("Football", "ellipse", 90, 55), ("Trophy", "rect", 60, 90),
            ("Skateboard", "rect", 120, 25), ("Jump Rope", "ellipse", 100, 80),
            ("Medal", "circle", 60, 60), ("Bowling Pin", "rect", 35, 90),
        ],
        "Musical Instruments": [
            ("Guitar", "ellipse", 60, 80), ("Piano Keys", "rect", 130, 50),
            ("Drum", "rect", 80, 70), ("Trumpet", "ellipse", 110, 40),
            ("Violin", "ellipse", 50, 85), ("Xylophone", "rect", 110, 70),
            ("Tambourine", "circle", 75, 75), ("Harp", "rect", 70, 100),
            ("Maracas", "ellipse", 30, 70), ("Flute", "rect", 120, 20),
        ],
        "Weather & Seasons": [
            ("Sun", "circle", 90, 90), ("Rain Cloud", "ellipse", 100, 60),
            ("Snowflake", "diamond", 90, 90), ("Rainbow", "ellipse", 120, 60),
            ("Tornado", "diamond", 50, 100), ("Lightning", "diamond", 60, 100),
            ("Umbrella", "ellipse", 100, 60), ("Leaf", "ellipse", 70, 90),
            ("Snowman", "circle", 60, 60), ("Thermometer", "rect", 25, 110),
        ],
        "Fruits & Vegetables": [
            ("Apple", "circle", 75, 75), ("Banana", "ellipse", 100, 40),
            ("Strawberry", "ellipse", 60, 80), ("Pineapple", "ellipse", 55, 90),
            ("Watermelon", "ellipse", 90, 70), ("Grapes", "circle", 70, 70),
            ("Carrot", "diamond", 40, 110), ("Broccoli", "circle", 70, 70),
            ("Pumpkin", "ellipse", 80, 70), ("Corn", "rect", 40, 100),
        ],
        "Buildings & Houses": [
            ("House", "rect", 100, 80), ("Skyscraper", "rect", 50, 130),
            ("Church", "rect", 80, 90), ("Lighthouse", "rect", 40, 110),
            ("Windmill", "rect", 60, 90), ("Barn", "rect", 100, 80),
            ("Castle", "rect", 110, 100), ("Igloo", "ellipse", 90, 60),
            ("Tent", "diamond", 90, 80), ("Tree House", "rect", 70, 90),
        ],
        "Christmas & Winter": [
            ("Christmas Tree", "diamond", 80, 110), ("Snowman", "circle", 60, 60),
            ("Present Box", "rect", 80, 70), ("Candy Cane", "rect", 30, 100),
            ("Stocking", "rect", 50, 90), ("Gingerbread Man", "rect", 60, 90),
            ("Ornament", "circle", 70, 70), ("Bell", "ellipse", 60, 80),
            ("Wreath", "circle", 85, 85), ("Reindeer", "ellipse", 80, 55),
        ],
        "Easter & Spring": [
            ("Easter Egg", "ellipse", 60, 85), ("Bunny", "ellipse", 55, 75),
            ("Chick", "circle", 55, 55), ("Basket", "rect", 80, 60),
            ("Flower", "circle", 70, 70), ("Butterfly", "ellipse", 100, 55),
            ("Lamb", "ellipse", 65, 55), ("Bird Nest", "ellipse", 80, 45),
            ("Rain Boot", "rect", 50, 80), ("Watering Can", "rect", 70, 60),
        ],
        "Pets & Home Animals": [
            ("Puppy", "ellipse", 70, 50), ("Kitten", "ellipse", 60, 50),
            ("Hamster", "circle", 55, 55), ("Goldfish", "ellipse", 70, 45),
            ("Parrot", "ellipse", 45, 65), ("Turtle", "ellipse", 70, 50),
            ("Guinea Pig", "ellipse", 65, 40), ("Ferret", "ellipse", 80, 30),
            ("Dog House", "rect", 80, 70), ("Cat Bed", "ellipse", 90, 45),
        ],
    }
    
    config = theme_configs.get(theme_name, None)
    if config is None:
        # Fallback generic
        config = [(f"Drawing {i+1}", random.choice(["circle","rect","ellipse","diamond"]), 
                   random.randint(60,120), random.randint(50,100)) for i in range(10)]
    
    for name, shape, w, h in config:
        num_colors = random.choice([5, 6, 6, 7, 7, 7, 8])
        # Generate varied detail placements
        details = []
        for j in range(num_colors - 1):
            d_type = random.choice(["circle", "rect", "triangle", "ellipse"])
            dx = random.randint(-40, 40)
            dy = random.randint(-35, 45)
            details.append({"type": d_type, "x": dx, "y": dy, 
                           "r": random.randint(10, 20),
                           "w": random.randint(20, 35), "h": random.randint(15, 30),
                           "size": random.randint(10, 18)})
        drawings.append(make_object(name, shape, w, h, details))
    
    return drawings


# ============================================================
# MAIN BOOK GENERATION
# ============================================================

def get_drawings_for_theme(theme_name, book_idx):
    """Get 10+ drawings for a given theme."""
    if theme_name in THEME_DRAWINGS:
        return THEME_DRAWINGS[theme_name]
    else:
        return generate_theme_drawings(theme_name, seed=book_idx * 100)

def generate_page_svg(page_num, drawing_entry, palette, book_seed):
    """Generate SVG for a single page."""
    title, draw_fn, num_colors = drawing_entry
    border = generate_border_svg(book_seed + page_num)
    drawing_svg = draw_fn(308, 360, s=1.0)
    legend_svg = generate_color_legend(num_colors, palette)
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 616 800" width="616" height="800">
  <rect width="616" height="800" fill="white"/>
  {border}
  <rect x="160" y="32" width="296" height="32" fill="white" stroke="#000" stroke-width="1"/>
  <text x="308" y="55" text-anchor="middle" font-family="Georgia,serif" font-size="20" font-weight="bold" letter-spacing="2">COLOR BY NUMBERS</text>
  {drawing_svg}
  {legend_svg}
</svg>'''
    return svg

def generate_book_html(theme_name, book_idx):
    """Generate complete HTML for a single book."""
    drawings = get_drawings_for_theme(theme_name, book_idx)
    num_drawings = len(drawings)
    
    pages_html = []
    for page in range(50):
        drawing_idx = page % num_drawings
        drawing_entry = drawings[drawing_idx]
        _, _, num_colors = drawing_entry
        palette = get_palette(num_colors, book_idx * 1000 + page)
        svg = generate_page_svg(page, drawing_entry, palette, book_idx * 500)
        pages_html.append(f'<div class="page">\n{svg}\n</div>')
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Color By Numbers - {theme_name}</title>
<style>
  @page {{ size: 8.5in 11in; margin: 0; }}
  * {{ margin: 0; padding: 0; box-sizing: border-box; }}
  html, body {{ width: 8.5in; font-family: Arial, sans-serif; background: white; }}
  .page {{
    width: 8.5in; height: 11in;
    display: flex; align-items: center; justify-content: center;
    page-break-after: always; page-break-inside: avoid;
    overflow: hidden; position: relative;
  }}
  .page:last-child {{ page-break-after: auto; }}
  .page svg {{ width: 8.5in; height: 11in; display: block; }}
</style>
</head>
<body>
{"".join(pages_html)}
</body>
</html>'''
    return html

def generate_all_books():
    """Generate all 20 books as HTML files, then convert to PDF."""
    os.makedirs("/projects/sandbox/coloring_books", exist_ok=True)
    
    for idx, theme in enumerate(BOOK_THEMES):
        safe_name = theme.lower().replace(" ", "_").replace("&", "and").replace("'", "")
        html_path = f"/projects/sandbox/coloring_books/{idx+1:02d}_{safe_name}.html"
        pdf_path = f"/projects/sandbox/coloring_books/{idx+1:02d}_{safe_name}.pdf"
        
        print(f"[{idx+1}/20] Generating: {theme}...", end=" ", flush=True)
        
        html_content = generate_book_html(theme, idx)
        with open(html_path, "w") as f:
            f.write(html_content)
        
        # Convert to PDF using Chrome
        result = subprocess.run([
            "/opt/playwright/chromium-1232/chrome-linux64/chrome",
            "--headless", "--no-sandbox", "--disable-gpu",
            f"--print-to-pdf={pdf_path}",
            "--print-to-pdf-no-header",
            f"file://{html_path}"
        ], capture_output=True, text=True, timeout=120)
        
        if os.path.exists(pdf_path):
            size_mb = os.path.getsize(pdf_path) / (1024*1024)
            print(f"OK ({size_mb:.1f} MB)")
        else:
            print(f"FAILED - {result.stderr[:100]}")
    
    print("\n=== ALL DONE ===")
    print(f"Books saved in: /projects/sandbox/coloring_books/")

if __name__ == "__main__":
    generate_all_books()
