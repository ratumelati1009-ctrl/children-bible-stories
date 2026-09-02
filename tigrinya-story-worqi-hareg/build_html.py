#!/usr/bin/env python3
"""Convert the Tigrinya Markdown story into a styled, print-ready HTML file.

The HTML loads the 'Noto Sans Ethiopic' web font so that Ge'ez/Tigrinya
characters render correctly in any browser. Open the HTML in a browser and
choose Print -> Save as PDF to produce a proper 30+ page PDF.
"""
import html
import re
import sys

SRC = "/projects/sandbox/tigrigna-story/ወርቂ-ሓረግ.md"
OUT = "/projects/sandbox/tigrigna-story/ወርቂ-ሓረግ.html"


def inline(text: str) -> str:
    """Escape HTML then apply **bold** and *italic* markdown."""
    text = html.escape(text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)", r"<em>\1</em>", text)
    return text


def convert(md: str) -> str:
    lines = md.splitlines()
    out = []
    in_table = False
    in_list = False
    i = 0
    while i < len(lines):
        line = lines[i].rstrip("\n")
        stripped = line.strip()

        # blank line
        if not stripped:
            if in_list:
                out.append("</ul>")
                in_list = False
            i += 1
            continue

        # horizontal rule
        if re.fullmatch(r"-{3,}", stripped):
            if in_list:
                out.append("</ul>")
                in_list = False
            out.append('<hr class="divider">')
            i += 1
            continue

        # headings
        m = re.match(r"^(#{1,6})\s+(.*)$", stripped)
        if m:
            if in_list:
                out.append("</ul>")
                in_list = False
            level = len(m.group(1))
            content = inline(m.group(2))
            cls = ""
            if level == 1:
                cls = ' class="book-title"'
            elif level == 2:
                cls = ' class="chapter"'
            out.append(f"<h{level}{cls}>{content}</h{level}>")
            i += 1
            continue

        # blockquote
        if stripped.startswith(">"):
            if in_list:
                out.append("</ul>")
                in_list = False
            quote = inline(stripped[1:].strip())
            out.append(f"<blockquote>{quote}</blockquote>")
            i += 1
            continue

        # table (markdown pipe table)
        if stripped.startswith("|") and "|" in stripped[1:]:
            # gather all consecutive table lines
            tbl = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                tbl.append(lines[i].strip())
                i += 1
            out.append(render_table(tbl))
            continue

        # ordered list item -> keep as paragraph with number (simpler, robust)
        mo = re.match(r"^(\d+)\.\s+(.*)$", stripped)
        if mo:
            if in_list:
                out.append("</ul>")
                in_list = False
            out.append(f'<p class="numbered"><span class="num">{mo.group(1)}.</span> {inline(mo.group(2))}</p>')
            i += 1
            continue

        # unordered list
        mu = re.match(r"^[-*]\s+(.*)$", stripped)
        if mu:
            if not in_list:
                out.append("<ul>")
                in_list = True
            out.append(f"<li>{inline(mu.group(1))}</li>")
            i += 1
            continue

        # normal paragraph
        if in_list:
            out.append("</ul>")
            in_list = False
        out.append(f"<p>{inline(stripped)}</p>")
        i += 1

    if in_list:
        out.append("</ul>")
    return "\n".join(out)


def render_table(rows):
    # rows[0] header, rows[1] separator, rest body
    def cells(r):
        parts = [c.strip() for c in r.strip().strip("|").split("|")]
        return parts
    header = cells(rows[0])
    body = [cells(r) for r in rows[2:]] if len(rows) > 2 else []
    thtml = ["<table>", "<thead><tr>"]
    for h in header:
        thtml.append(f"<th>{inline(h)}</th>")
    thtml.append("</tr></thead><tbody>")
    for r in body:
        thtml.append("<tr>")
        for c in r:
            thtml.append(f"<td>{inline(c)}</td>")
        thtml.append("</tr>")
    thtml.append("</tbody></table>")
    return "\n".join(thtml)


def main():
    with open(SRC, encoding="utf-8") as f:
        md = f.read()
    body = convert(md)

    page = f"""<!DOCTYPE html>
<html lang="ti">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>ወርቂ ሓረግ — ዛንታ ብትግርኛ</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+Ethiopic:wght@400;500;700&family=Noto+Serif+Ethiopic:wght@400;600;700&display=swap" rel="stylesheet">
<style>
  :root {{
    --ink: #1f2328;
    --muted: #57606a;
    --accent: #8a5a00;
    --accent-soft: #c99a3a;
    --rule: #e2d8c3;
  }}
  * {{ box-sizing: border-box; }}
  body {{
    font-family: "Noto Serif Ethiopic", "Noto Sans Ethiopic", serif;
    color: var(--ink);
    line-height: 1.9;
    font-size: 12.5pt;
    margin: 0;
    background: #f6f3ec;
  }}
  .sheet {{
    max-width: 760px;
    margin: 0 auto;
    background: #fff;
    padding: 56px 64px;
    box-shadow: 0 2px 24px rgba(0,0,0,.08);
  }}
  h1, h2, h3, h4 {{
    font-family: "Noto Sans Ethiopic", sans-serif;
    line-height: 1.5;
    color: var(--ink);
  }}
  h1.book-title {{
    text-align: center;
    font-size: 30pt;
    color: var(--accent);
    margin: 8px 0 4px;
    letter-spacing: .5px;
  }}
  h2.chapter {{
    color: var(--accent);
    font-size: 18pt;
    margin-top: 2.2em;
    padding-bottom: .25em;
    border-bottom: 2px solid var(--rule);
    page-break-before: always;
  }}
  /* first chapter should not force a blank page after the title page */
  h2.chapter:first-of-type {{ page-break-before: avoid; }}
  h3 {{ font-size: 14pt; color: var(--muted); }}
  h4 {{ font-size: 12.5pt; color: var(--muted); }}
  p {{ margin: 0 0 1em; text-align: justify; }}
  p.numbered {{ text-align: left; }}
  .num {{ color: var(--accent); font-weight: 700; }}
  strong {{ color: #111; }}
  em {{ color: var(--muted); }}
  blockquote {{
    border-right: 4px solid var(--accent-soft);
    background: #faf6ee;
    margin: 1.4em 0;
    padding: .8em 1.2em;
    font-style: italic;
    color: #5b4a28;
    border-radius: 4px;
  }}
  hr.divider {{
    border: none;
    text-align: center;
    margin: 2em 0;
  }}
  hr.divider::before {{
    content: "❦";
    color: var(--accent-soft);
    font-size: 16pt;
  }}
  ul {{ padding-right: 1.2em; padding-left: 0; }}
  li {{ margin-bottom: .5em; }}
  table {{
    width: 100%;
    border-collapse: collapse;
    margin: 1.2em 0;
    font-size: 11.5pt;
  }}
  th, td {{
    border: 1px solid var(--rule);
    padding: 8px 10px;
    text-align: right;
  }}
  th {{ background: #f3ead6; color: #5b4a28; }}
  .print-hint {{
    max-width: 760px;
    margin: 16px auto 0;
    padding: 14px 18px;
    background: #fff8e6;
    border: 1px solid #e6d38a;
    border-radius: 8px;
    font-family: "Noto Sans Ethiopic", sans-serif;
    font-size: 10.5pt;
    color: #6b5620;
  }}
  @media print {{
    body {{ background: #fff; font-size: 12pt; }}
    .sheet {{ box-shadow: none; margin: 0; max-width: none; padding: 0; }}
    .print-hint {{ display: none; }}
    @page {{ margin: 20mm 18mm; }}
  }}
</style>
</head>
<body>
<div class="print-hint">
  📄 ናብ PDF ንምቕያር: ኣብ ብራውዘር <strong>Print</strong> (Ctrl/Cmd+P) ጠውቕ ➜ <strong>Destination: Save as PDF</strong> ምረጽ ➜ <strong>Save</strong>።
  <br>To save as PDF: press <strong>Ctrl/Cmd + P</strong>, choose <strong>“Save as PDF”</strong>, then Save.
</div>
<div class="sheet">
{body}
</div>
</body>
</html>
"""
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(page)
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
