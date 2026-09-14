#!/usr/bin/env python3
"""
Generate full-length trilingual (English / ትግርኛ / አማርኛ) children's PICTURE books.
One scene per page: a large illustration + short text in all three languages.
Each book = 1 cover + N scene pages (N >= 44), so every book is 45+ pages.

Embedded Noto Sans Ethiopic font (base64) so Fidel renders correctly in the PDF.

Usage:
    python3 generate_picture_books.py
Reads BOOKS from scenes_data.py. Outputs <nn>_<slug>.html and .pdf here.
"""
import base64
import html as html_module
import os
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
FONT_PATH = os.path.join(HERE, "eth_font.ttf")
CHROME = "/opt/playwright/chromium-1232/chrome-linux64/chrome"

with open(FONT_PATH, "rb") as f:
    FONT_B64 = base64.b64encode(f.read()).decode("ascii")

STYLE = """
@font-face { font-family:"Eth"; src:url(data:font/truetype;base64,__FONT__) format("truetype"); font-weight:normal; }
@font-face { font-family:"Eth"; src:url(data:font/truetype;base64,__FONT__) format("truetype"); font-weight:bold; }
@page { size:8.5in 11in; margin:0; }
* { box-sizing:border-box; margin:0; padding:0; }
body { font-family:"Eth","Noto Sans Ethiopic","Noto Sans",sans-serif; }
.page { width:8.5in; height:11in; page-break-after:always; position:relative; overflow:hidden; }
.border { position:absolute; top:0.3in; bottom:0.3in; left:0.3in; right:0.3in; border:4px double #2E7D32; border-radius:14px; padding:0.4in 0.5in; background:linear-gradient(135deg,#FFFFFB,#EAF7EA); display:flex; flex-direction:column; align-items:center; }
.border::before { content:''; position:absolute; top:8px; bottom:8px; left:8px; right:8px; border:1px solid #66BB6A; border-radius:10px; pointer-events:none; }
.ref { position:absolute; top:14px; right:22px; font-size:11px; color:#2E7D32; font-style:italic; }
.pn { position:absolute; bottom:14px; right:22px; font-size:11px; color:#2E7D32; }
.scene-num { position:absolute; bottom:14px; left:22px; font-size:11px; color:#2E7D32; }
.ill { margin:14px 0 20px; text-align:center; }
.ill svg { width:5.6in; height:auto; border-radius:12px; box-shadow:0 2px 10px rgba(0,0,0,0.12); }
.txt { width:100%; flex:1; display:flex; flex-direction:column; justify-content:flex-start; }
.sen { font-size:22px; color:#1A237E; line-height:1.5; margin-bottom:16px; text-align:center; font-weight:600; }
.sti { font-size:21px; color:#BF360C; line-height:1.7; margin-bottom:14px; text-align:center; }
.sam { font-size:21px; color:#1B5E20; line-height:1.7; text-align:center; }
.cover { display:flex; flex-direction:column; align-items:center; justify-content:center; text-align:center; }
.cover .border { background:linear-gradient(180deg,#1B5E20,#2E7D32,#43A047); border-color:#FFD700; }
.cover .border::before { border-color:#FFD700; }
.ct-en { font-size:34px; color:#FFD700; font-weight:700; margin-bottom:12px; text-shadow:2px 2px 4px rgba(0,0,0,0.35); }
.ct-ti { font-size:24px; color:#FFCC80; font-weight:700; margin-bottom:6px; }
.ct-am { font-size:24px; color:#A5D6A7; font-weight:700; margin-bottom:18px; }
.csub { font-size:14px; color:#E8F5E9; margin-top:8px; }
.cover-ill { margin:20px 0; }
.cover-ill svg { width:4.6in; height:auto; }
.cross { font-size:56px; color:#FFD700; margin:10px 0; }
""".replace("__FONT__", FONT_B64)


def svg_scene(kind):
    sky = '<rect width="300" height="200" fill="#EAF4FF"/>'
    if kind == "scroll":
        return ('<svg viewBox="0 0 300 200">' + sky +
                '<rect x="70" y="45" width="160" height="110" rx="8" fill="#FBE9C7" stroke="#B8860B" stroke-width="3"/>'
                '<rect x="60" y="40" width="20" height="120" rx="10" fill="#8B5A2B"/>'
                '<rect x="220" y="40" width="20" height="120" rx="10" fill="#8B5A2B"/>'
                '<line x1="95" y1="70" x2="205" y2="70" stroke="#B8860B" stroke-width="3"/>'
                '<line x1="95" y1="90" x2="205" y2="90" stroke="#C9A227" stroke-width="2"/>'
                '<line x1="95" y1="108" x2="205" y2="108" stroke="#C9A227" stroke-width="2"/></svg>')
    if kind == "crown":
        return ('<svg viewBox="0 0 300 200">' + sky +
                '<rect y="150" width="300" height="50" fill="#C8A96E"/>'
                '<polygon points="90,130 110,80 130,120 150,70 170,120 190,80 210,130" fill="#FFD700" stroke="#B8860B" stroke-width="3"/>'
                '<rect x="90" y="128" width="120" height="18" fill="#FFD700" stroke="#B8860B" stroke-width="3"/>'
                '<circle cx="110" cy="80" r="5" fill="#E53935"/><circle cx="150" cy="70" r="6" fill="#1E88E5"/><circle cx="190" cy="80" r="5" fill="#43A047"/></svg>')
    if kind == "prophet":
        return ('<svg viewBox="0 0 300 200">' + sky +
                '<rect y="150" width="300" height="50" fill="#D2B48C"/>'
                '<circle cx="150" cy="70" r="22" fill="#F1C27D"/>'
                '<path d="M150 92 L120 160 L180 160 Z" fill="#6D4C41"/>'
                '<rect x="146" y="40" width="8" height="70" fill="#8B5A2B"/>'
                '<circle cx="150" cy="30" r="16" fill="#FFE082" opacity="0.7"/></svg>')
    if kind == "woman":
        return ('<svg viewBox="0 0 300 200">' + sky +
                '<rect y="150" width="300" height="50" fill="#CDE6C5"/>'
                '<circle cx="150" cy="72" r="20" fill="#F1C27D"/>'
                '<path d="M150 92 L118 160 L182 160 Z" fill="#8E44AD"/>'
                '<path d="M130 60 q20 -20 40 0" fill="#4E342E"/></svg>')
    if kind == "heal":
        return ('<svg viewBox="0 0 300 200">' + sky +
                '<circle cx="150" cy="60" r="34" fill="#FFF3B0"/>'
                '<circle cx="150" cy="90" r="18" fill="#F1C27D"/>'
                '<path d="M150 105 L120 165 L180 165 Z" fill="#3F51B5"/>'
                '<line x1="150" y1="30" x2="150" y2="55" stroke="#FFC107" stroke-width="4"/>'
                '<line x1="120" y1="42" x2="135" y2="60" stroke="#FFC107" stroke-width="3"/>'
                '<line x1="180" y1="42" x2="165" y2="60" stroke="#FFC107" stroke-width="3"/></svg>')
    if kind == "boat":
        return ('<svg viewBox="0 0 300 200">' + sky +
                '<path d="M0 150 q75 20 150 0 t150 0 v50 H0 Z" fill="#3B82C4"/>'
                '<path d="M90 120 h120 l-20 35 h-80 Z" fill="#8B5A2B"/>'
                '<rect x="146" y="60" width="6" height="62" fill="#5D4037"/>'
                '<path d="M152 62 l45 45 h-45 Z" fill="#FFFDF7" stroke="#ccc"/></svg>')
    if kind == "ark":
        return ('<svg viewBox="0 0 300 200"><rect width="300" height="200" fill="#CDEBF9"/>'
                '<path d="M0 150 q75 18 150 0 t150 0 v50 H0 Z" fill="#2E86C1"/>'
                '<path d="M55 110 h190 l-24 44 h-142 Z" fill="#8B5A2B" stroke="#5D4037" stroke-width="2"/>'
                '<rect x="95" y="72" width="110" height="42" fill="#A1673B" stroke="#5D4037" stroke-width="2"/>'
                '<rect x="120" y="82" width="18" height="22" fill="#5D4037"/>'
                '<rect x="162" y="82" width="18" height="22" fill="#5D4037"/></svg>')
    if kind == "rainbow":
        return ('<svg viewBox="0 0 300 200"><rect width="300" height="200" fill="#EAF6FF"/>'
                '<path d="M40 180 a110 110 0 0 1 220 0" fill="none" stroke="#E53935" stroke-width="9"/>'
                '<path d="M52 180 a98 98 0 0 1 196 0" fill="none" stroke="#FB8C00" stroke-width="9"/>'
                '<path d="M64 180 a86 86 0 0 1 172 0" fill="none" stroke="#FDD835" stroke-width="9"/>'
                '<path d="M76 180 a74 74 0 0 1 148 0" fill="none" stroke="#43A047" stroke-width="9"/>'
                '<path d="M88 180 a62 62 0 0 1 124 0" fill="none" stroke="#1E88E5" stroke-width="9"/></svg>')
    if kind == "loaves":
        return ('<svg viewBox="0 0 300 200">' + sky +
                '<ellipse cx="150" cy="150" rx="90" ry="28" fill="#C8A96E"/>'
                '<ellipse cx="120" cy="130" rx="34" ry="22" fill="#E3B04B"/>'
                '<ellipse cx="175" cy="128" rx="30" ry="20" fill="#E3B04B"/>'
                '<path d="M95 120 q10 -18 24 0" stroke="#5B8DEF" stroke-width="6" fill="none"/>'
                '<path d="M185 118 q10 -18 24 0" stroke="#5B8DEF" stroke-width="6" fill="none"/></svg>')
    if kind == "sea":
        return ('<svg viewBox="0 0 300 200"><rect width="300" height="200" fill="#FDF3D0"/>'
                '<path d="M0 90 h110 v90 H0 Z" fill="#2E86C1"/>'
                '<path d="M190 90 h110 v90 H190 Z" fill="#2E86C1"/>'
                '<rect x="110" y="90" width="80" height="90" fill="#E0C68A"/>'
                '<circle cx="150" cy="45" r="20" fill="#FFD54F"/></svg>')
    if kind == "fish":
        return ('<svg viewBox="0 0 300 200"><rect width="300" height="200" fill="#1B6CA8"/>'
                '<path d="M70 100 q60 -55 140 0 q-60 55 -140 0 Z" fill="#5DADE2" stroke="#2874A6" stroke-width="3"/>'
                '<polygon points="205,100 245,70 245,130" fill="#5DADE2" stroke="#2874A6" stroke-width="3"/>'
                '<circle cx="110" cy="92" r="7" fill="#fff"/><circle cx="110" cy="92" r="3" fill="#000"/></svg>')
    if kind == "angel":
        return ('<svg viewBox="0 0 300 200"><rect width="300" height="200" fill="#F3ECFF"/>'
                '<circle cx="150" cy="70" r="18" fill="#F1C27D"/>'
                '<path d="M150 90 L124 158 H176 Z" fill="#FFFFFF" stroke="#E0D7F0"/>'
                '<path d="M124 100 q-40 -10 -50 30 q35 -5 50 5 Z" fill="#EDE7F6" stroke="#B39DDB"/>'
                '<path d="M176 100 q40 -10 50 30 q-35 -5 -50 5 Z" fill="#EDE7F6" stroke="#B39DDB"/>'
                '<circle cx="150" cy="44" r="14" fill="none" stroke="#FFD700" stroke-width="3"/></svg>')
    if kind == "temple":
        return ('<svg viewBox="0 0 300 200">' + sky +
                '<rect y="160" width="300" height="40" fill="#C8A96E"/>'
                '<polygon points="150,50 90,95 210,95" fill="#D4AF37"/>'
                '<rect x="95" y="95" width="110" height="65" fill="#F5E6B3"/>'
                '<rect x="112" y="110" width="14" height="50" fill="#8B5A2B"/>'
                '<rect x="143" y="110" width="14" height="50" fill="#8B5A2B"/>'
                '<rect x="174" y="110" width="14" height="50" fill="#8B5A2B"/></svg>')
    if kind == "star":
        return ('<svg viewBox="0 0 300 200"><rect width="300" height="200" fill="#0B1E4D"/>'
                '<polygon points="150,40 160,80 200,80 168,104 180,145 150,120 120,145 132,104 100,80 140,80" fill="#FFD700"/>'
                '<circle cx="60" cy="50" r="2" fill="#fff"/><circle cx="240" cy="60" r="2.5" fill="#fff"/>'
                '<circle cx="210" cy="150" r="2" fill="#fff"/><circle cx="70" cy="150" r="2" fill="#fff"/></svg>')
    if kind == "dove":
        return ('<svg viewBox="0 0 300 200"><rect width="300" height="200" fill="#EAF6FF"/>'
                '<ellipse cx="150" cy="100" rx="34" ry="18" fill="#FFFFFF" stroke="#cfd8dc"/>'
                '<circle cx="185" cy="92" r="12" fill="#FFFFFF" stroke="#cfd8dc"/>'
                '<path d="M120 96 q-30 -30 -55 -5 q30 5 55 20 Z" fill="#F5F5F5" stroke="#cfd8dc"/>'
                '<polygon points="196,90 210,86 200,96" fill="#FFB300"/></svg>')
    if kind == "lion":
        return ('<svg viewBox="0 0 300 200"><rect width="300" height="200" fill="#4E342E"/>'
                '<circle cx="150" cy="105" r="55" fill="#C98A3B"/>'
                '<circle cx="150" cy="105" r="38" fill="#E3B04B"/>'
                '<circle cx="135" cy="98" r="5" fill="#3E2723"/><circle cx="165" cy="98" r="5" fill="#3E2723"/>'
                '<path d="M138 120 q12 12 24 0" fill="none" stroke="#3E2723" stroke-width="3"/>'
                '<polygon points="150,108 143,118 157,118" fill="#3E2723"/></svg>')
    if kind == "coat":
        return ('<svg viewBox="0 0 300 200">' + sky +
                '<rect y="155" width="300" height="45" fill="#D2B48C"/>'
                '<path d="M120 60 h60 l24 24 -18 18 v60 h-96 v-60 l-18 -18 Z" fill="#E53935" stroke="#7B1FA2" stroke-width="3"/>'
                '<rect x="120" y="70" width="60" height="14" fill="#FDD835"/>'
                '<rect x="120" y="98" width="60" height="14" fill="#1E88E5"/>'
                '<rect x="120" y="126" width="60" height="14" fill="#43A047"/></svg>')
    if kind == "basket":
        return ('<svg viewBox="0 0 300 200"><rect width="300" height="200" fill="#CDEBF9"/>'
                '<path d="M0 150 h300 v50 H0 Z" fill="#2E86C1"/>'
                '<path d="M60 140 q10 -60 90 -60 t90 60 Z" fill="#6EB56E"/>'
                '<ellipse cx="150" cy="140" rx="70" ry="20" fill="#C8A96E" stroke="#8B5A2B" stroke-width="3"/>'
                '<path d="M100 130 q50 -22 100 0" fill="#E3B04B"/></svg>')
    if kind == "sheep":
        return ('<svg viewBox="0 0 300 200">' + sky +
                '<path d="M0 150 q75 -40 150 0 t150 0 v50 H0 Z" fill="#8BC34A"/>'
                '<ellipse cx="150" cy="120" rx="44" ry="32" fill="#FFFFFF" stroke="#e0e0e0"/>'
                '<circle cx="150" cy="108" r="18" fill="#5D4037"/>'
                '<circle cx="144" cy="106" r="3" fill="#fff"/><circle cx="156" cy="106" r="3" fill="#fff"/>'
                '<line x1="130" y1="150" x2="130" y2="168" stroke="#5D4037" stroke-width="4"/>'
                '<line x1="170" y1="150" x2="170" y2="168" stroke="#5D4037" stroke-width="4"/></svg>')
    if kind == "tree":
        return ('<svg viewBox="0 0 300 200">' + sky +
                '<rect y="160" width="300" height="40" fill="#C8A96E"/>'
                '<rect x="140" y="90" width="20" height="80" fill="#6D4C41"/>'
                '<circle cx="150" cy="80" r="50" fill="#43A047"/>'
                '<circle cx="115" cy="95" r="30" fill="#66BB6A"/>'
                '<circle cx="185" cy="95" r="30" fill="#66BB6A"/></svg>')
    if kind == "children":
        return ('<svg viewBox="0 0 300 200">' + sky +
                '<rect y="155" width="300" height="45" fill="#CDE6C5"/>'
                '<circle cx="105" cy="95" r="16" fill="#F1C27D"/><path d="M105 112 L88 160 H122 Z" fill="#EF5350"/>'
                '<circle cx="150" cy="88" r="18" fill="#F1C27D"/><path d="M150 108 L128 162 H172 Z" fill="#42A5F5"/>'
                '<circle cx="195" cy="95" r="16" fill="#F1C27D"/><path d="M195 112 L178 160 H212 Z" fill="#AB47BC"/></svg>')
    if kind == "pray":
        return ('<svg viewBox="0 0 300 200">' + sky +
                '<rect y="150" width="300" height="50" fill="#CDE6C5"/>'
                '<circle cx="150" cy="80" r="22" fill="#F1C27D"/>'
                '<path d="M150 102 L122 160 H178 Z" fill="#5C6BC0"/>'
                '<path d="M150 108 l-14 22 M150 108 l14 22" stroke="#F1C27D" stroke-width="6" fill="none"/>'
                '<circle cx="150" cy="40" r="14" fill="#FFE082" opacity="0.7"/></svg>')
    # default: gentle hills
    return ('<svg viewBox="0 0 300 200">' + sky +
            '<path d="M0 150 q75 -50 150 0 t150 0 v50 H0 Z" fill="#8BC34A"/>'
            '<circle cx="240" cy="45" r="22" fill="#FFD54F"/></svg>')


def esc(s):
    return html_module.escape(s, quote=False)


def scene_page(scene, page_num, scene_num, total_scenes, verse):
    ill = svg_scene(scene.get("ill", "hills"))
    return f"""<div class="page"><div class="border">
<div class="ref">{esc(verse)}</div>
<div class="ill">{ill}</div>
<div class="txt">
<div class="sen">{esc(scene['en'])}</div>
<div class="sti">{esc(scene['ti'])}</div>
<div class="sam">{esc(scene['am'])}</div>
</div>
<div class="scene-num">{scene_num} / {total_scenes}</div>
<div class="pn">Page {page_num}</div>
</div></div>"""


def cover_page(book):
    ill = svg_scene(book.get("cover_ill", "hills"))
    return f"""<div class="page cover"><div class="border">
<div class="cross">✝</div>
<div class="ct-en">{esc(book['title_en'])}</div>
<div class="ct-ti">{esc(book['title_ti'])}</div>
<div class="ct-am">{esc(book['title_am'])}</div>
<div class="cover-ill">{ill}</div>
<div class="csub">A Bible Picture Book for Children</div>
<div class="csub">መጽሓፍ ስእሊ ንቈልዑ</div>
<div class="csub">የመጽሐፍ ቅዱስ ሥዕል መጽሐፍ ለልጆች</div>
<div class="csub" style="margin-top:14px;">English • ትግርኛ • አማርኛ &nbsp;|&nbsp; Ages 5-13</div>
</div></div>"""


def build_book(book):
    scenes = book["scenes"]
    total = len(scenes)
    pages = [cover_page(book)]
    for i, sc in enumerate(scenes, start=1):
        pages.append(scene_page(sc, i + 1, i, total, book["verse"]))
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
        check=True, capture_output=True, timeout=300,
    )
    return html_path, pdf_path


def main():
    from scenes_data import BOOKS
    for idx, book in enumerate(BOOKS, start=1):
        slug = f"{idx:02d}_{book['slug']}"
        html = build_book(book)
        h, p = render_pdf(html, slug)
        pages = len(book["scenes"]) + 1
        print(f"[{idx:02d}] {book['title_en']}: {pages} pages -> "
              f"{os.path.basename(p)} ({os.path.getsize(p)//1024} KB)")


if __name__ == "__main__":
    main()
