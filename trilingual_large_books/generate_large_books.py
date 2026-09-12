#!/usr/bin/env python3
"""
Generate 10 NEW trilingual (English / ትግርኛ / አማርኛ) children's Bible story books.
Matches the format of the existing trilingual_books (books 1-4):
  - 8.5x11in pages, double purple border
  - Per story: English title + Tigrinya + Amharic titles, illustration,
    story text in all 3 languages, LESSON box in 3 languages, verse reference
  - Embedded Noto Sans Ethiopic font (base64) so Fidel renders in the PDF.

Story data has NO duplicates with the existing 4 books or the 20 virtue books.

Usage:
    python3 generate_new_books.py
Outputs <nn>_<slug>.html and .pdf into this folder.
"""
import base64
import html as html_module
import os
import re
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
FONT_PATH = os.path.join(HERE, "eth_font.ttf")
CHROME = "/opt/playwright/chromium-1232/chrome-linux64/chrome"

# ---- Load embedded font once ----
with open(FONT_PATH, "rb") as f:
    FONT_B64 = base64.b64encode(f.read()).decode("ascii")

STYLE = """
@font-face { font-family:"Eth"; src:url(data:font/truetype;base64,__FONT__) format("truetype"); font-weight:normal; }
@font-face { font-family:"Eth"; src:url(data:font/truetype;base64,__FONT__) format("truetype"); font-weight:bold; }
@page { size:8.5in 11in; margin:0; }
* { box-sizing:border-box; margin:0; padding:0; }
body { font-family:"Eth","Noto Sans Ethiopic","Noto Sans",sans-serif; }
.page { width:8.5in; height:11in; page-break-after:always; position:relative; overflow:hidden; }
.border { position:absolute; top:0.25in; bottom:0.25in; left:0.25in; right:0.25in; border:3px double #4A148C; border-radius:10px; padding:0.3in 0.4in; background:linear-gradient(135deg,#FFFFF8,#F3E5F5); display:flex; flex-direction:column; align-items:center; }
.border::before { content:''; position:absolute; top:6px; bottom:6px; left:6px; right:6px; border:1px solid #9C27B0; border-radius:7px; pointer-events:none; }
.ref { position:absolute; top:12px; right:18px; font-size:9px; color:#4A148C; font-style:italic; }
.pn { position:absolute; bottom:12px; right:18px; font-size:9px; color:#4A148C; }
.ten { font-size:18px; color:#1A237E; margin-top:5px; text-align:center; font-weight:700; }
.titles-eth { font-size:14px; color:#4A148C; margin-top:3px; text-align:center; font-weight:600; }
.tti { color:#BF360C; } .tam { color:#1B5E20; }
.ill { margin:6px 0; text-align:center; }
.ill svg { max-width:100%; border-radius:6px; box-shadow:0 1px 4px rgba(0,0,0,0.1); }
.stories { flex:1; overflow:hidden; width:100%; }
.sen { font-size:11px; color:#333; line-height:1.45; margin-bottom:5px; text-align:justify; }
.sti { font-size:11px; color:#BF360C; line-height:1.55; margin-bottom:5px; text-align:justify; }
.sam { font-size:11px; color:#1B5E20; line-height:1.55; margin-bottom:5px; text-align:justify; }
.moral { width:100%; background:linear-gradient(135deg,#EDE7F6,#E8EAF6); border:2px solid #7E57C2; border-radius:8px; padding:7px 12px; margin-top:auto; }
.ml { font-size:9px; font-weight:700; color:#4A148C; margin-bottom:3px; text-transform:uppercase; }
.men { font-size:10px; color:#333; font-style:italic; margin-bottom:2px; }
.mti { font-size:10px; color:#BF360C; margin-bottom:2px; }
.mam { font-size:10px; color:#1B5E20; }
.cover { display:flex; flex-direction:column; align-items:center; justify-content:center; text-align:center; background:linear-gradient(180deg,#1A237E,#283593,#3949AB); }
.cover .border { background:linear-gradient(180deg,#1A237E,#283593,#3949AB); border-color:#FFD700; }
.cover .border::before { border-color:#FFD700; }
.ct-en { font-size:28px; color:#FFD700; font-weight:700; margin-bottom:10px; text-shadow:2px 2px 4px rgba(0,0,0,0.3); }
.ct-ti { font-size:20px; color:#FF8A65; font-weight:700; margin-bottom:5px; }
.ct-am { font-size:20px; color:#81C784; font-weight:700; margin-bottom:20px; }
.csub { font-size:12px; color:#E8EAF6; margin-top:10px; }
.cross { font-size:50px; color:#FFD700; margin:15px 0; }
""".replace("__FONT__", FONT_B64)


# ---- Simple, reusable SVG illustrations keyed by scene name ----
def svg_scene(kind):
    sky = '<rect width="300" height="200" fill="#EAF4FF"/>'
    if kind == "scroll":
        return ('<svg viewBox="0 0 300 200" width="300" height="200">' + sky +
                '<rect x="70" y="45" width="160" height="110" rx="8" fill="#FBE9C7" stroke="#B8860B" stroke-width="3"/>'
                '<rect x="60" y="40" width="20" height="120" rx="10" fill="#8B5A2B"/>'
                '<rect x="220" y="40" width="20" height="120" rx="10" fill="#8B5A2B"/>'
                '<line x1="95" y1="70" x2="205" y2="70" stroke="#B8860B" stroke-width="3"/>'
                '<line x1="95" y1="90" x2="205" y2="90" stroke="#C9A227" stroke-width="2"/>'
                '<line x1="95" y1="108" x2="205" y2="108" stroke="#C9A227" stroke-width="2"/>'
                '<line x1="95" y1="126" x2="180" y2="126" stroke="#C9A227" stroke-width="2"/></svg>')
    if kind == "crown":
        return ('<svg viewBox="0 0 300 200" width="300" height="200">' + sky +
                '<rect y="150" width="300" height="50" fill="#C8A96E"/>'
                '<polygon points="90,130 110,80 130,120 150,70 170,120 190,80 210,130" fill="#FFD700" stroke="#B8860B" stroke-width="3"/>'
                '<rect x="90" y="128" width="120" height="18" fill="#FFD700" stroke="#B8860B" stroke-width="3"/>'
                '<circle cx="110" cy="80" r="5" fill="#E53935"/><circle cx="150" cy="70" r="6" fill="#1E88E5"/><circle cx="190" cy="80" r="5" fill="#43A047"/></svg>')
    if kind == "prophet":
        return ('<svg viewBox="0 0 300 200" width="300" height="200">' + sky +
                '<rect y="150" width="300" height="50" fill="#D2B48C"/>'
                '<circle cx="150" cy="70" r="22" fill="#F1C27D"/>'
                '<path d="M150 92 L120 160 L180 160 Z" fill="#6D4C41"/>'
                '<rect x="146" y="40" width="8" height="70" fill="#8B5A2B"/>'
                '<circle cx="150" cy="30" r="16" fill="#FFE082" opacity="0.7"/></svg>')
    if kind == "woman":
        return ('<svg viewBox="0 0 300 200" width="300" height="200">' + sky +
                '<rect y="150" width="300" height="50" fill="#CDE6C5"/>'
                '<circle cx="150" cy="72" r="20" fill="#F1C27D"/>'
                '<path d="M150 92 L118 160 L182 160 Z" fill="#8E44AD"/>'
                '<path d="M130 60 q20 -20 40 0" fill="#4E342E"/></svg>')
    if kind == "heal":
        return ('<svg viewBox="0 0 300 200" width="300" height="200">' + sky +
                '<circle cx="150" cy="60" r="34" fill="#FFF3B0"/>'
                '<circle cx="150" cy="90" r="18" fill="#F1C27D"/>'
                '<path d="M150 105 L120 165 L180 165 Z" fill="#3F51B5"/>'
                '<line x1="150" y1="30" x2="150" y2="55" stroke="#FFC107" stroke-width="4"/>'
                '<line x1="120" y1="42" x2="135" y2="60" stroke="#FFC107" stroke-width="3"/>'
                '<line x1="180" y1="42" x2="165" y2="60" stroke="#FFC107" stroke-width="3"/></svg>')
    if kind == "boat":
        return ('<svg viewBox="0 0 300 200" width="300" height="200">' + sky +
                '<path d="M0 150 q75 20 150 0 t150 0 v50 H0 Z" fill="#3B82C4"/>'
                '<path d="M90 120 h120 l-20 35 h-80 Z" fill="#8B5A2B"/>'
                '<rect x="146" y="60" width="6" height="62" fill="#5D4037"/>'
                '<path d="M152 62 l45 45 h-45 Z" fill="#FFFDF7" stroke="#ccc"/></svg>')
    if kind == "loaves":
        return ('<svg viewBox="0 0 300 200" width="300" height="200">' + sky +
                '<ellipse cx="150" cy="150" rx="90" ry="28" fill="#C8A96E"/>'
                '<ellipse cx="120" cy="130" rx="34" ry="22" fill="#E3B04B"/>'
                '<ellipse cx="175" cy="128" rx="30" ry="20" fill="#E3B04B"/>'
                '<path d="M95 120 q10 -18 24 0" stroke="#5B8DEF" stroke-width="6" fill="none"/>'
                '<path d="M185 118 q10 -18 24 0" stroke="#5B8DEF" stroke-width="6" fill="none"/></svg>')
    if kind == "sea":
        return ('<svg viewBox="0 0 300 200" width="300" height="200"><rect width="300" height="200" fill="#FDF3D0"/>'
                '<path d="M0 90 h110 v90 H0 Z" fill="#2E86C1"/>'
                '<path d="M190 90 h110 v90 H190 Z" fill="#2E86C1"/>'
                '<rect x="110" y="90" width="80" height="90" fill="#E0C68A"/>'
                '<circle cx="150" cy="45" r="20" fill="#FFD54F"/></svg>')
    if kind == "angel":
        return ('<svg viewBox="0 0 300 200" width="300" height="200"><rect width="300" height="200" fill="#F3ECFF"/>'
                '<circle cx="150" cy="70" r="18" fill="#F1C27D"/>'
                '<path d="M150 90 L124 158 H176 Z" fill="#FFFFFF" stroke="#E0D7F0"/>'
                '<path d="M124 100 q-40 -10 -50 30 q35 -5 50 5 Z" fill="#EDE7F6" stroke="#B39DDB"/>'
                '<path d="M176 100 q40 -10 50 30 q-35 -5 -50 5 Z" fill="#EDE7F6" stroke="#B39DDB"/>'
                '<circle cx="150" cy="44" r="14" fill="none" stroke="#FFD700" stroke-width="3"/></svg>')
    if kind == "temple":
        return ('<svg viewBox="0 0 300 200" width="300" height="200">' + sky +
                '<rect y="160" width="300" height="40" fill="#C8A96E"/>'
                '<polygon points="150,50 90,95 210,95" fill="#D4AF37"/>'
                '<rect x="95" y="95" width="110" height="65" fill="#F5E6B3"/>'
                '<rect x="112" y="110" width="14" height="50" fill="#8B5A2B"/>'
                '<rect x="143" y="110" width="14" height="50" fill="#8B5A2B"/>'
                '<rect x="174" y="110" width="14" height="50" fill="#8B5A2B"/></svg>')
    if kind == "star":
        return ('<svg viewBox="0 0 300 200" width="300" height="200"><rect width="300" height="200" fill="#0B1E4D"/>'
                '<polygon points="150,40 160,80 200,80 168,104 180,145 150,120 120,145 132,104 100,80 140,80" fill="#FFD700"/>'
                '<circle cx="60" cy="50" r="2" fill="#fff"/><circle cx="240" cy="60" r="2.5" fill="#fff"/>'
                '<circle cx="210" cy="150" r="2" fill="#fff"/><circle cx="70" cy="150" r="2" fill="#fff"/></svg>')
    if kind == "dove":
        return ('<svg viewBox="0 0 300 200" width="300" height="200"><rect width="300" height="200" fill="#EAF6FF"/>'
                '<ellipse cx="150" cy="100" rx="34" ry="18" fill="#FFFFFF" stroke="#cfd8dc"/>'
                '<circle cx="185" cy="92" r="12" fill="#FFFFFF" stroke="#cfd8dc"/>'
                '<path d="M120 96 q-30 -30 -55 -5 q30 5 55 20 Z" fill="#F5F5F5" stroke="#cfd8dc"/>'
                '<polygon points="196,90 210,86 200,96" fill="#FFB300"/></svg>')
    # default: gentle hills
    return ('<svg viewBox="0 0 300 200" width="300" height="200">' + sky +
            '<path d="M0 150 q75 -50 150 0 t150 0 v50 H0 Z" fill="#8BC34A"/>'
            '<circle cx="240" cy="45" r="22" fill="#FFD54F"/></svg>')


def esc(s):
    return html_module.escape(s, quote=False)


def story_page(story, page_num):
    ill = svg_scene(story.get("illustration", "hills"))
    sen = "".join(f'<p class="sen">{esc(p)}</p>' for p in story["story_en"].split("\n"))
    sti = "".join(f'<p class="sti">{esc(p)}</p>' for p in story["story_ti"].split("\n"))
    sam = "".join(f'<p class="sam">{esc(p)}</p>' for p in story["story_am"].split("\n"))
    return f"""<div class="page"><div class="border">
<div class="ref">{esc(story['verse'])}</div>
<div class="ten">{esc(story['title_en'])}</div>
<div class="titles-eth"><span class="tti">{esc(story['title_ti'])}</span> &nbsp;•&nbsp; <span class="tam">{esc(story['title_am'])}</span></div>
<div class="ill">{ill}</div>
<div class="stories">{sen}{sti}{sam}</div>
<div class="moral">
<div class="ml">LESSON / ትምህርቲ / ትምህርት</div>
<div class="men">{esc(story['moral_en'])}</div>
<div class="mti">{esc(story['moral_ti'])}</div>
<div class="mam">{esc(story['moral_am'])}</div>
</div>
<div class="pn">Page {page_num}</div>
</div></div>"""


def cover_page(title_en, title_ti, title_am):
    return f"""<div class="page cover"><div class="border">
<div class="cross">✝</div>
<div class="ct-en">{esc(title_en)}</div>
<div class="ct-ti">{esc(title_ti)}</div>
<div class="ct-am">{esc(title_am)}</div>
<div class="csub">Bible Stories for Children</div>
<div class="csub">ዛንታታት መጽሓፍ ቅዱስ ንቈልዑ</div>
<div class="csub">የመጽሐፍ ቅዱስ ታሪኮች ለልጆች</div>
<div class="csub" style="margin-top:16px;">Trilingual: English • ትግርኛ • አማርኛ</div>
<div class="csub">Ages / ዕድመ / ዕድሜ: 6-13</div>
</div></div>"""


def build_book(book):
    pages = [cover_page(book["title_en"], book["title_ti"], book["title_am"])]
    for i, s in enumerate(book["stories"], start=1):
        pages.append(story_page(s, i))
    html = ('<!DOCTYPE html><html><head><meta charset="UTF-8"/>'
            f'<title>{esc(book["title_en"])}</title><style>{STYLE}</style></head>'
            f'<body>{"".join(pages)}</body></html>')
    return html


def render_pdf(html, slug):
    html_path = os.path.join(HERE, slug + ".html")
    pdf_path = os.path.join(HERE, slug + ".pdf")
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html)
    subprocess.run(
        [CHROME, "--headless=new", "--no-sandbox", "--disable-gpu",
         "--no-pdf-header-footer", f"--print-to-pdf={pdf_path}",
         "file://" + html_path],
        check=True, capture_output=True, timeout=180,
    )
    return html_path, pdf_path


def main():
    from books_data_large import BOOKS
    for idx, book in enumerate(BOOKS, start=1):
        slug = f"{idx:02d}_{book['slug']}"
        html = build_book(book)
        h, p = render_pdf(html, slug)
        n = len(book["stories"])
        print(f"[{idx:02d}] {book['title_en']}: {n} stories -> {os.path.basename(p)} "
              f"({os.path.getsize(p)//1024} KB)")


if __name__ == "__main__":
    main()
