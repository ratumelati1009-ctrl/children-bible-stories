#!/usr/bin/env python3
"""Build a styled, print-ready HTML ebook from the Markdown source."""
import html
import re
import pathlib

SRC = pathlib.Path(__file__).parent / "Trilingual_Bible_Stories_for_Kids.md"
OUT = pathlib.Path(__file__).parent / "Trilingual_Bible_Stories_for_Kids.html"

CSS = """
  /* Loads the Ethiopic (Fidel) font automatically when online. Safe to keep for offline use too. */
  @import url('https://fonts.googleapis.com/css2?family=Noto+Serif+Ethiopic:wght@400;700&display=swap');
  :root{--ink:#2b2b3a;--gold:#c99a3b;--sky:#4a7fb5;--rose:#b5546f;--cream:#fffdf7;--panel:#f7f2e6;}
  *{box-sizing:border-box;}
  body{font-family:'Noto Serif Ethiopic','Noto Sans Ethiopic','Abyssinica SIL','Nyala','Ebrima',Georgia,serif;background:var(--cream);color:var(--ink);line-height:1.75;margin:0;}
  .page{max-width:780px;margin:0 auto;padding:36px 30px 80px;}
  .cover{text-align:center;padding:90px 24px 70px;background:linear-gradient(160deg,#fef6e0,#f3e7c8);border-bottom:6px solid var(--gold);}
  .cover h1{font-size:2.6rem;margin:0 0 8px;color:var(--rose);}
  .cover h2{font-size:1.25rem;margin:0 0 18px;color:var(--sky);font-weight:normal;}
  .cover .langs{font-size:1.1rem;color:var(--gold);font-weight:bold;}
  .cover .age{margin-top:20px;display:inline-block;background:var(--sky);color:#fff;padding:6px 18px;border-radius:20px;}
  h2.story-title{color:var(--rose);font-size:1.7rem;margin:0;}
  h3.story-sub{color:var(--sky);margin:2px 0 14px;font-weight:normal;}
  .lang-block{margin:16px 0;padding:14px 18px;border-radius:10px;background:var(--panel);}
  .lang-label{font-weight:bold;color:var(--gold);font-size:.9rem;text-transform:uppercase;letter-spacing:1px;margin-bottom:6px;}
  .fidel{font-size:1.12rem;line-height:1.95;}
  .geez{background:#f0ece0;border-left:5px solid var(--gold);padding:14px 18px;font-size:1.25rem;border-radius:6px;}
  .geez .translit{display:block;font-size:.9rem;color:#7a6a45;font-style:italic;margin-top:6px;font-family:Georgia,serif;}
  .lesson{background:#fdf0d5;border-radius:8px;padding:10px 16px;margin:8px 0;}
  .talk{background:#e7f0f8;border-radius:8px;padding:10px 16px;margin:8px 0;}
  .story{border-bottom:2px dashed #e0d5b8;padding-bottom:26px;margin-bottom:36px;}
  .note{background:#fff4f4;border:1px solid #f0c8c8;border-radius:8px;padding:14px 18px;font-size:.92rem;}
  .prayer{background:linear-gradient(160deg,#fef6e0,#f3e7c8);border-radius:12px;padding:22px 26px;text-align:center;}
  footer{text-align:center;color:var(--gold);font-size:1.15rem;margin:30px 0;}
  @media print{.story{page-break-inside:avoid;}.cover{page-break-after:always;}}
"""

def esc(s):
    return html.escape(s.strip())

def main():
    text = SRC.read_text(encoding="utf-8")
    # Split into stories by the "## Story" heading
    stories = re.split(r"\n(?=## Story )", text)
    body = []
    for chunk in stories:
        if not chunk.startswith("## Story"):
            continue
        lines = chunk.splitlines()
        title = lines[0].replace("## ", "").strip()
        sub = ""
        for l in lines[1:4]:
            if l.startswith("### "):
                sub = l.replace("### ", "").strip()
                break
        parts = [f'<div class="story"><h2 class="story-title">{esc(title)}</h2>']
        if sub:
            parts.append(f'<h3 class="story-sub">{esc(sub)}</h3>')

        # Extract each labeled block
        def grab(label):
            m = re.search(r"\*\*" + re.escape(label) + r"\*\*\n+(.+?)(?=\n\*\*|\n> |\n## |\Z)",
                          chunk, re.S)
            return m.group(1).strip() if m else ""

        for label, cls in [("🇬🇧 English", "English"),
                            ("ትግርኛ (Tigrinya)", "ትግርኛ Tigrinya"),
                            ("አማርኛ (Amharic)", "አማርኛ Amharic")]:
            txt = grab(label)
            if txt:
                paras = "".join(f"<p>{esc(p)}</p>" for p in txt.split("\n\n"))
                parts.append(f'<div class="lang-block"><div class="lang-label">{cls}</div>'
                             f'<div class="fidel">{paras}</div></div>')

        # Ge'ez verse (blockquote lines)
        gm = re.search(r"\*\*ግዕዝ \(Ge'ez\)\*\*\n+((?:> .*\n?)+)", chunk)
        if gm:
            qlines = [l[2:] for l in gm.group(1).splitlines() if l.startswith("> ")]
            verse = qlines[0] if qlines else ""
            translit = qlines[1].strip("*") if len(qlines) > 1 else ""
            parts.append(f'<div class="geez">{esc(verse)}'
                         f'<span class="translit">{esc(translit)}</span></div>')

        lm = re.search(r"\*\*💛 Little Lesson:\*\*\s*(.+)", chunk)
        if lm:
            parts.append(f'<div class="lesson">💛 <strong>Little Lesson:</strong> {esc(lm.group(1))}</div>')
        tm = re.search(r"\*\*💬 Talk Together:\*\*\s*(.+)", chunk)
        if tm:
            parts.append(f'<div class="talk">💬 <strong>Talk Together:</strong> {esc(tm.group(1))}</div>')

        parts.append("</div>")
        body.append("\n".join(parts))

    toc_items = [
        "God Makes the World (Creation)", "Noah and the Big Boat (Noah's Ark)",
        "David and the Giant (David &amp; Goliath)", "Daniel and the Lions",
        "Baby Jesus is Born (The First Christmas)", "Jonah and the Big Fish",
        "The Good Shepherd (The Lost Sheep)", "Jesus Feeds the Crowd",
        "Jesus Loves the Children", "Jesus is Alive! (The First Easter)"]
    toc = "".join(f"<li>{t}</li>" for t in toc_items)

    out = f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Bible Stories for Little Hearts</title>
<style>{CSS}</style></head><body>
<div class="cover">
  <h1>🌟 Bible Stories for Little Hearts</h1>
  <h2>A Trilingual Children's Bible Storybook</h2>
  <div class="langs">English &bull; ትግርኛ &bull; አማርኛ &bull; ግዕዝ</div>
  <div class="age">For children ages 5–13</div>
</div>
<div class="page">
<div class="lang-block"><div class="lang-label">📖 Table of Contents</div><ol>{toc}</ol></div>
<p class="note">📝 <strong>Publisher's note:</strong> Have the Tigrinya, Amharic, and Ge'ez text reviewed by a native-speaker / liturgical editor before final publication.</p>
{"".join(body)}
<div class="prayer"><h2 style="color:var(--rose)">🙏 A Closing Prayer</h2>
<p><strong>English:</strong> Thank You, God, for loving me. Help me to be kind, brave, and full of joy. Amen.</p>
<p class="fidel"><strong>ትግርኛ:</strong> የቐንየለይ ኣምላኸይ ስለ ዘፍቀርካኒ። ሕያዋይ፡ ተባዕን ብሓጐስ ዝመላእኩን ክኸውን ሓግዘኒ። ኣሜን።</p>
<p class="fidel"><strong>አማርኛ:</strong> አመሰግንሃለሁ አምላኬ ስለ ወደድከኝ። ደግ፣ ደፋርና በደስታ የተሞላሁ እንድሆን እርዳኝ። አሜን።</p>
<p class="fidel"><strong>ግዕዝ:</strong> ቡሩክ አንተ እግዚአብሔር አምላክነ ለዓለም። አሜን።</p></div>
<footer>The End &bull; መጨረሻ &bull; መወዳእታ</footer>
</div></body></html>"""

    OUT.write_text(out, encoding="utf-8")
    print(f"Wrote {OUT} ({len(out)} bytes, {len(body)} stories)")

if __name__ == "__main__":
    main()
