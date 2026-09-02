#!/usr/bin/env python3
"""Build a fully self-contained print HTML (fonts embedded as base64) for PDF generation."""
import base64
import html
import re

SRC = "/projects/sandbox/tigrigna-story/tigrinya-story-worqi-hareg/ወርቂ-ሓረግ.md"
OUT = "/projects/sandbox/tigrigna-story/_print.html"
REG = "/projects/sandbox/tigrigna-story/fonts/NotoSansEthiopic-Regular.ttf"
BOLD = "/projects/sandbox/tigrigna-story/fonts/NotoSansEthiopic-Bold.ttf"


def b64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()


def inline(text):
    text = html.escape(text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)", r"<em>\1</em>", text)
    return text


def convert(md):
    lines = md.splitlines()
    out, in_list = [], False
    i = 0
    while i < len(lines):
        s = lines[i].strip()
        if not s:
            if in_list:
                out.append("</ul>"); in_list = False
            i += 1; continue
        if re.fullmatch(r"-{3,}", s):
            if in_list: out.append("</ul>"); in_list = False
            out.append('<hr class="divider">'); i += 1; continue
        m = re.match(r"^(#{1,6})\s+(.*)$", s)
        if m:
            if in_list: out.append("</ul>"); in_list = False
            lvl = len(m.group(1)); c = inline(m.group(2))
            cls = ' class="book-title"' if lvl == 1 else (' class="chapter"' if lvl == 2 else "")
            out.append(f"<h{lvl}{cls}>{c}</h{lvl}>"); i += 1; continue
        if s.startswith(">"):
            if in_list: out.append("</ul>"); in_list = False
            out.append(f"<blockquote>{inline(s[1:].strip())}</blockquote>"); i += 1; continue
        mo = re.match(r"^(\d+)\.\s+(.*)$", s)
        if mo:
            if in_list: out.append("</ul>"); in_list = False
            out.append(f'<p class="numbered"><span class="num">{mo.group(1)}.</span> {inline(mo.group(2))}</p>'); i += 1; continue
        mu = re.match(r"^[-*]\s+(.*)$", s)
        if mu:
            if not in_list: out.append("<ul>"); in_list = True
            out.append(f"<li>{inline(mu.group(1))}</li>"); i += 1; continue
        if in_list: out.append("</ul>"); in_list = False
        out.append(f"<p>{inline(s)}</p>"); i += 1
    if in_list: out.append("</ul>")
    return "\n".join(out)


with open(SRC, encoding="utf-8") as f:
    body = convert(f.read())

reg_b64 = b64(REG)
bold_b64 = b64(BOLD)

page = f"""<!DOCTYPE html>
<html lang="ti"><head><meta charset="UTF-8">
<style>
@font-face {{ font-family:'NotoEth'; font-weight:400; src:url(data:font/ttf;base64,{reg_b64}) format('truetype'); }}
@font-face {{ font-family:'NotoEth'; font-weight:700; src:url(data:font/ttf;base64,{bold_b64}) format('truetype'); }}
* {{ box-sizing:border-box; }}
html,body {{ font-family:'NotoEth',sans-serif; color:#1f2328; line-height:2.05; font-size:13.5pt; margin:0; }}
.book-title {{ text-align:center; font-size:30pt; font-weight:700; color:#8a5a00; margin:32px 0 6px; }}
h2.chapter {{ color:#8a5a00; font-weight:700; font-size:18pt; margin-top:1.6em; padding-bottom:.2em;
  border-bottom:2px solid #e2d8c3; page-break-before:always; }}
h2.chapter:first-of-type {{ page-break-before:avoid; }}
h3 {{ font-size:14pt; color:#57606a; text-align:center; }}
h4 {{ font-size:12pt; color:#57606a; }}
p {{ margin:0 0 .9em; text-align:justify; }}
p.numbered {{ text-align:left; }}
.num {{ color:#8a5a00; font-weight:700; }}
strong {{ font-weight:700; color:#111; }}
em {{ font-style:italic; color:#57606a; }}
blockquote {{ border-right:4px solid #c99a3a; background:#faf6ee; margin:1.2em 0; padding:.7em 1.1em;
  font-style:italic; color:#5b4a28; border-radius:4px; }}
hr.divider {{ border:none; text-align:center; margin:1.6em 0; }}
hr.divider::before {{ content:"\\2766"; color:#c99a3a; font-size:15pt; }}
ul {{ padding-right:1.2em; padding-left:0; }}
li {{ margin-bottom:.4em; }}
@page {{ size:A4; margin:24mm 20mm; }}
</style></head>
<body>
{body}
</body></html>
"""

with open(OUT, "w", encoding="utf-8") as f:
    f.write(page)
print("Wrote", OUT, "-", len(page), "bytes")
