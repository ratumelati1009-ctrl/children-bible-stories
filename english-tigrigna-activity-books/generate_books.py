#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate English–Tigrigna Bible Activity Books (42 pages each) as print-ready HTML.
Author of the series: Daniel Tesfamariam.

Each book shares the same 42-page structure as the hand-built Esther pack:
cover, translation note, contents, characters, 5 story pages, memory verse,
comprehension (easy + hard), sequencing, word search, crossword, matching,
Tigrigna word tracing, 4 colouring pages, count & colour, count in Tigrigna,
bravery/lesson scenarios (2), spot-the-difference, maze, dot-to-dot, draw-your-own,
craft + template, bookmarks, secret code, true/false, fill-in-blanks, acrostic,
prayer, reflection, favourite part, verse poster, review, certificate.

Run:  python3 generate_books.py
Output: books/NN-slug/index.html for every book in BOOKS.
"""
import os, html, json

ROOT = os.path.dirname(os.path.abspath(__file__))
AUTHOR_EN = "Daniel Tesfamariam"
AUTHOR_TI = "ብዳንኤል ተስፋማርያም እተጻሕፈ"

def esc(s):
    return html.escape(s, quote=True)

# --------------------------------------------------------------------------
# Small helpers that emit the same HTML idioms used in the Esther book.
# --------------------------------------------------------------------------

def page(book_title, page_label, inner):
    return (f'<section class="page" data-book="{esc(book_title)}" data-page="{esc(str(page_label))}">\n'
            f'{inner}\n</section>\n')

def title_block(en, ti, size=23):
    return (f'  <h2 class="title" style="font-size:{size}pt;">{esc(en)}'
            f'<span class="ti" style="font-size:{size-8}pt;">{esc(ti)}</span></h2>\n')

def subtitle(en, ti):
    return f'  <p class="subtitle">{esc(en)} &nbsp;|&nbsp; <span class="ti">{esc(ti)}</span></p>\n'

def divider():
    return '  <div class="divider"></div>\n'

def instr(en, ti):
    return f'  <div class="instr">{esc(en)}<span class="ti">{esc(ti)}</span></div>\n'

def lines(n=3, tight=False):
    cls = "lines tight" if tight else "lines"
    return f'  <div class="{cls}">' + ''.join('<div class="rule"></div>' for _ in range(n)) + '</div>\n'

def art(el_id, extra_style=""):
    st = f' style="{extra_style}"' if extra_style else ""
    return f'  <div class="art" id="{el_id}"{st}></div>\n'


# --------------------------------------------------------------------------
# The 42-page builder. `b` is a dict describing one book (see BOOKS below).
# It returns the full HTML document string.
# --------------------------------------------------------------------------

def build_book(b):
    T = b["title_en"]           # short running title for footer/header
    parts = []
    A = parts.append

    # ---- HTML head ----
    A(f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{esc(b["title_en"])} — English–Tigrigna Bible Activity Pack</title>
<link rel="stylesheet" href="../../assets/book.css">
</head>
<body>

<div class="toolbar">
  <span style="margin-right:8px;">{esc(b["title_en"])}</span>
  <button onclick="window.print()">🖨️ Print / Save PDF</button>
</div>
''')

    # ---- PAGE 1 — COVER ----
    A(f'''<section class="page" data-book="Bible Activity Pack" data-page="Cover">
  <div class="center" style="margin-top:6mm;">
    <span class="badge">Bible Activity Pack</span>
  </div>
  <h2 class="title" style="margin-top:10mm;">{esc(b["title_en"])}
    <span class="ti">{esc(b["title_ti"])}</span>
  </h2>
  <p class="subtitle">English &ndash; Tigrigna &nbsp;|&nbsp; <span class="ti">እንግሊዝኛ &ndash; ትግርኛ</span></p>
  <p class="center" style="font-size:13pt; color:var(--royal); font-weight:600; margin-top:6px;">
    Written by {esc(AUTHOR_EN)}<br>
    <span class="ti" style="color:var(--rose); font-size:12pt;">{esc(AUTHOR_TI)}</span>
  </p>
  <div class="art" id="cover-art"></div>
  <div class="center mt"><span class="age">For Ages 4&ndash;12</span></div>
  <p class="center small" style="margin-top:14mm;">
    {esc(b["cover_line_en"])}<br>
    <span class="ti">{esc(b["cover_line_ti"])}</span>
  </p>
  <p class="center small" style="position:absolute; bottom:16mm; left:15mm; right:15mm;">
    Memory verse based on the <strong>International Children's Bible (ICB)</strong>.<br>
    <span class="ti">ናይ ኣእምሮ ጥቕሲ ካብ ኣህጉራዊ መጽሓፍ ቅዱስ ቆልዑ (ICB) እተወስደ።</span>
  </p>
</section>
''')

    # ---- PAGE 2 — TRANSLATION NOTE + HOW TO USE ----
    A(page(T, 2, '''  <h3 style="color:var(--royal); font-size:20pt;">A Note About the Tigrigna Translation</h3>
  <p class="ti" style="color:var(--rose); font-size:15pt; margin-top:0;">ሓበሬታ ብዛዕባ ትግርኛ ትርጉም</p>
  <div class="divider"></div>
  <div class="instr"><strong>Please read before printing or publishing.</strong><span class="ti">በጃኹም ቅድሚ ምሕታም ኣንብቡ።</span></div>
  <p class="story">The Tigrigna (ትግርኛ) text in this book was prepared with care, but it has
  <strong>not yet been checked by a professional native-speaker translator</strong>.
  Before this pack is sold, published, or widely distributed, please have the Tigrigna
  proofread by a fluent native speaker to confirm accuracy, spelling, and reverence for the Scriptures.</p>
  <p class="ti" style="font-size:12.5pt; color:#5a3fa0;">እቲ ኣብዚ መጽሓፍ ዘሎ ትግርኛ ጽሑፍ ብጥንቃቐ እተዳለወ እኳ እንተኾነ፡ ገና ብሞያዊ ተወላዲ ተዛራቢ ኣይተረጋገጸን። ቅድሚ ምሽያጡ ወይ ምዝርጋሑ፡ በጃኹም ብተዛራቢ ትግርኛ ኣረጋግጽዎ።</p>
  <div class="divider"></div>
  <h3 style="color:var(--royal); font-size:18pt;">How to Use This Pack &nbsp; <span class="ti" style="font-size:13pt;">ኣጠቓቕማ</span></h3>
  <ul class="bi">
    <li>Print on A4 paper. Each page is one activity.<span class="ti">ኣብ A4 ወረቐት ሕተምዎ። ነፍሲ ወከፍ ገጽ ሓደ ንጥፈት እዩ።</span></li>
    <li>Younger children (4&ndash;7) can colour, trace and match.<span class="ti">ናእሽቱ ቆልዑ ክሕብሩን ከዛምዱን ይኽእሉ።</span></li>
    <li>Older children (8&ndash;12) can do word searches, crosswords and writing.<span class="ti">ዓበይቲ ቆልዑ ቃላት ምድላይን ጽሕፈትን ክገብሩ ይኽእሉ።</span></li>
    <li>Read the Bible story together first, then enjoy the activities.<span class="ti">ቅድም ንታሪኽ ብሓባር ኣንብቡ፡ ደሓር ተዘናግዑ።</span></li>
  </ul>
  <div class="art" id="p2-art" style="margin-top:8mm;"></div>'''))

    # ---- PAGE 3 — CONTENTS ----
    contents = ''.join(
        f'    <li>{esc(en)} <span class="ti">{esc(ti)}</span></li>\n'
        for en, ti in [
            ("The Bible Story (Parts 1–5)", "ታሪኽ መጽሓፍ ቅዱስ"),
            ("Memory Verse & Tracing", "ናይ ኣእምሮ ጥቕሲ"),
            ("Meet the People", "ነቶም ሰባት ፍለጡ"),
            ("Comprehension Questions", "ናይ ምርዳእ ሕቶታት"),
            ("Put the Story in Order", "ብቕደም ተኸተል"),
            ("Word Search", "ቃላት ምድላይ"),
            ("Crossword", "መስቀላዊ ቃላት"),
            ("Match the Words", "ቃላት ኣዛምዱ"),
            ("Colouring Pages", "ገጻት ሕብሪ"),
            ("Count & Colour", "ቁጸርን ሕብርን"),
            ("What Would You Do?", "እንታይ ምገበርካ?"),
            ("Spot the Difference & Maze", "ፍልልይን መንገድን"),
            ("Craft & Bookmarks", "ስራሕን ምልክት መጽሓፍን"),
            ("Prayer & Reflection", "ጸሎትን ምስትንታንን"),
            ("Certificate of Completion", "ምስክር ወረቐት"),
        ])
    A(page(T, 3, title_block("Contents", "  ትሕዝቶ", 24) + divider() +
            f'  <ol class="bi" style="font-size:12.5pt; line-height:1.8;">\n{contents}  </ol>\n' +
            art("p3-art", "margin-top:6mm;")))

    # ---- PAGE 4 — CHARACTERS ----
    char_cards = ''.join(
        f'    <div class="card"><strong>{esc(c[0])}</strong> — {esc(c[1])}<span class="ti">{esc(c[2])}</span></div>\n'
        for c in b["characters"])
    A(page(T, 4, title_block("Meet the People", "  ነቶም ሰባት ፍለጡ", 24) + divider() +
            f'  <div class="grid2">\n{char_cards}  </div>\n' +
            f'  <p class="center mt small">Colour each person in the story.<span class="ti">ንነፍሲ ወከፍ ሰብ ሕብርዎ።</span></p>\n' +
            art("p4-art")))

    # ---- PAGES 5–9 — STORY PARTS ----
    ord_ti = ["ቀዳማይ", "ካልኣይ", "ሳልሳይ", "ራብዓይ", "ሓሙሻይ"]
    for i, sp in enumerate(b["story"]):
        story_html = ""
        for en, ti in sp["paras"]:
            story_html += f'    <p>{esc(en)}</p>\n    <p class="ti">{esc(ti)}</p>\n'
        inner = (title_block(f'The Story &mdash; Part {i+1}', f'  ታሪኽ &mdash; {ord_ti[i]} ክፋል', 23)
                 .replace('&amp;mdash;', '&mdash;') +
                 subtitle(sp["sub_en"], sp["sub_ti"]) + divider() +
                 f'  <div class="story">\n{story_html}  </div>\n' +
                 art(f"p{5+i}-art"))
        A(page(T, 5+i, inner))

    # ---- PAGE 10 — MEMORY VERSE ----
    v = b["verse"]
    A(page(T, 10, title_block("Memory Verse", "  ናይ ኣእምሮ ጥቕሲ", 24) + divider() +
            f'''  <div class="verse">
    &ldquo;{esc(v["en"])}&rdquo;
    <span class="ti">&ldquo;{esc(v["ti"])}&rdquo;</span>
    <span class="ref">{esc(v["ref_en"])} (ICB) &nbsp;·&nbsp; <span class="ti">{esc(v["ref_ti"])}</span></span>
  </div>
''' + instr("Trace the verse, then say it three times out loud!", "ነቲ ጥቕሲ ስዓቦ፡ ሰለስተ ሳዕ ዓው ኢልካ በሎ!") +
            f'  <p style="font-size:20pt; color:#d9d0ec; letter-spacing:2px; line-height:1.8; text-align:center;">{esc(v["en"])}</p>\n' +
            lines(3) +
            '  <p class="center small">Now write it in Tigrigna: <span class="ti">ሕጂ ብትግርኛ ጽሓፎ፦</span></p>\n' +
            lines(2) + art("p10-art")))


    # ---- PAGE 11 — COMPREHENSION (easy) ----
    q_easy = ""
    for i, q in enumerate(b["easy_q"]):
        q_easy += (f'  <div class="qwrap">\n    <p class="q">{i+1}. {esc(q["q_en"])} '
                   f'<span class="ti">{esc(q["q_ti"])}</span></p>\n'
                   f'    <p style="font-size:14pt;">&nbsp;&nbsp; {q["opts"]}</p>\n  </div>\n')
    A(page(T, 11, title_block("Do You Remember?", "", 23).replace('<span class="ti" style="font-size:15pt;"></span>', '') +
            '  <span class="age">Ages 4&ndash;7</span>\n' +
            subtitle("Circle the right answer", "ቅኑዕ መልሲ ኣኽብቡ") + divider() + q_easy + art("p11-art")))

    # ---- PAGE 12 — COMPREHENSION (hard, write) ----
    q_hard = ""
    for i, q in enumerate(b["hard_q"]):
        q_hard += (f'  <div class="qwrap">\n    <p class="q">{i+1}. {esc(q[0])} '
                   f'<span class="ti">{esc(q[1])}</span></p>\n' + lines(2, tight=True) + '  </div>\n')
    A(page(T, 12, title_block("Think &amp; Write", "", 23) +
            '  <span class="age">Ages 8&ndash;12</span>\n' +
            subtitle("Answer in full sentences", "ብምሉእ ሓሳብ መልሱ") + divider() + q_hard))

    # ---- PAGE 13 — SEQUENCING ----
    seq_cards = ''.join(
        f'    <div class="card"><span class="num">&nbsp;</span> {esc(s[0])}<span class="ti">{esc(s[1])}</span></div>\n'
        for s in b["sequence"])
    A(page(T, 13, title_block("Put the Story in Order", "", 23) +
            subtitle("Number the boxes 1 to 6", "ካብ 1 ክሳብ 6 ቁጸሩ") + divider() +
            instr("Write the number in the circle to show the correct order.", "ቅኑዕ ስርዓት ንምርኣይ ቁጽሪ ጽሓፍ።") +
            f'  <div class="grid2" style="gap:14px;">\n{seq_cards}  </div>\n' +
            '  <p class="center small mt">Read the story again to be sure! <span class="ti">እንደገና ኣንብብ!</span></p>\n'))

    # ---- PAGE 14 — WORD SEARCH ----
    ws_words = json.dumps(b["ws_words"])
    A(page(T, 14, title_block("Word Search", "", 23) +
            '  <span class="age">Ages 8&ndash;12</span>\n' +
            subtitle("Find the hidden words", "ተሓቢኦም ዘለዉ ቃላት ርኸብ") + divider() +
            '  <table class="ws" id="ws-table"></table>\n  <div class="bank" id="ws-bank"></div>\n' +
            '  <p class="center small">Words go across &rarr; and down &darr;.<span class="ti"> ንጎድንን ንታሕትን</span></p>\n' +
            f'  <script>window.WS_WORDS={ws_words};</script>\n'))

    # ---- PAGE 15 — CROSSWORD ----
    cw = b["crossword"]
    across_clues = ''.join(f'      <p>{c[0]}. {esc(c[1])} <span class="ti">({esc(c[2])})</span></p>\n' for c in cw["across_clues"])
    down_clues = ''.join(f'      <p>{c[0]}. {esc(c[1])} <span class="ti">({esc(c[2])})</span></p>\n' for c in cw["down_clues"])
    A(page(T, 15, title_block("Crossword Puzzle", "", 23) +
            '  <span class="age">Ages 8&ndash;12</span>\n' +
            subtitle("Use the clues to fill the grid", "ነቲ ፍርግም ምላእ") + divider() +
            '  <table class="cw" id="cw-table"></table>\n' +
            f'  <div class="grid2 mt" style="font-size:11pt;">\n    <div><strong>Down &darr;</strong>\n{down_clues}    </div>\n'
            f'    <div><strong>Across &rarr;</strong>\n{across_clues}    </div>\n  </div>\n' +
            f'  <p class="center small mt">Answers: {esc(cw["answer_line"])}</p>\n' +
            f'  <script>window.CW={json.dumps(cw["words"])};</script>\n'))

    # ---- PAGE 16 — MATCH THE WORDS ----
    left = ''.join(f'      <p style="font-size:16pt; line-height:2.6;">{esc(m[0])} &nbsp; &bull;</p>\n' for m in b["match"])
    # shuffle-ish: reverse order for the Tigrigna column
    right_items = list(b["match"])[::-1]
    right = ''.join(f'      <p style="font-size:16pt; line-height:2.6;">&bull; &nbsp; {esc(m[1])}</p>\n' for m in right_items)
    ans = " · ".join(f'{m[0]}={m[1]}' for m in b["match"])
    A(page(T, 16, title_block("Match the Words", "", 23) +
            subtitle("Draw a line: English &harr; Tigrigna", "መስመር ስኣል") + divider() +
            instr("Match each English word to its Tigrigna meaning.", "ንነፍሲ ወከፍ ቃል ኣዛምዶ።") +
            f'  <div class="grid2" style="gap:0 40px;">\n    <div>\n{left}    </div>\n    <div class="ti">\n{right}    </div>\n  </div>\n' +
            f'  <p class="center small mt">Answers: {esc(ans)}</p>\n'))

    # ---- PAGE 17 — TIGRIGNA TRACING ----
    trace = ""
    for m in b["match"]:
        trace += (f'  <div class="qwrap">\n    <p class="q">{esc(m[0])} &mdash; '
                  f'<span class="ti" style="display:inline; color:#d9d0ec; font-size:20pt;">{esc(m[1])}</span></p>\n'
                  + lines(1, tight=True) + '  </div>\n')
    A(page(T, 17, title_block("Learn Tigrigna Words", "", 23) +
            subtitle("Trace and write", "ስዓብን ጽሓፍን") + divider() + trace + art("p17-art")))

    # ---- PAGES 18–21 — COLOURING ----
    for i, cp in enumerate(b["colouring"]):
        A(page(T, 18+i, title_block(cp["title_en"], "", 23) +
               subtitle(cp["sub_en"], cp["sub_ti"]) + divider() +
               art(f"p{18+i}-art") +
               f'  <p class="color-note">{esc(cp["note_en"])}<span class="ti">{esc(cp["note_ti"])}</span></p>\n'))


    # ---- PAGE 22 — COUNT & COLOUR ----
    A(page(T, 22, title_block("Count &amp; Colour", "", 23) +
            '  <span class="age">Ages 4&ndash;7</span>\n' +
            subtitle(f'Count the {b["count_word_en"]}', f'{b["count_word_ti"]} ቁጸር') + divider() +
            instr(f'Count each set. Write the number and colour them in.', "ቁጸር፡ ቁጽሪ ጽሓፍን ሕብሮምን።") +
            art("p22-art")))

    # ---- PAGE 23 — COUNT IN TIGRIGNA ----
    nums = [("1","One","ሓደ · ፩"),("2","Two","ክልተ · ፪"),("3","Three","ሰለስተ · ፫"),
            ("4","Four","ኣርባዕተ · ፬"),("5","Five","ሓሙሽተ · ፭")]
    ncards = ''.join(f'    <div class="card"><strong style="font-size:20pt;">{n[0]}</strong> &mdash; {n[1]} <span class="ti" style="font-size:18pt;">{n[2]}</span></div>\n' for n in nums)
    A(page(T, 23, title_block("Learn to Count in Tigrigna", "", 22) +
            subtitle("Numbers 1–5", "ቁጽሪ 1–5") + divider() +
            instr("Say each number in English and Tigrigna.", "ንነፍሲ ወከፍ ቁጽሪ በሎ።") +
            f'  <div class="grid2" style="gap:12px;">\n{ncards}'
            f'    <div class="card center" style="border-style:dashed;">{esc(b["count_fact_en"])}<span class="ti">{esc(b["count_fact_ti"])}</span></div>\n  </div>\n'))

    # ---- PAGE 24 — SCENARIOS (circle) ----
    scen = ""
    for i, s in enumerate(b["scenarios"]):
        scen += (f'  <div class="qwrap card">\n    <p class="q">{i+1}. {esc(s["q_en"])}'
                 f'<span class="ti">{esc(s["q_ti"])}</span></p>\n    <p>{s["opts"]}</p>\n  </div>\n')
    A(page(T, 24, title_block("What Would You Do?", "", 23) +
            subtitle(b["lesson_en"], b["lesson_ti"]) + divider() +
            instr("Read each story. Circle the kind and right choice.", "ኣንብቦ። ነቲ ቅኑዕ ምርጫ ኣኽብቦ።") +
            scen + art("p24-art")))

    # ---- PAGE 25 — MY CHOICES (write) ----
    mc = ""
    for i, q in enumerate(b["reflect_write"]):
        mc += (f'  <div class="qwrap">\n    <p class="q">{i+1}. {esc(q[0])}'
               f'<span class="ti">{esc(q[1])}</span></p>\n' + lines(2, tight=True) + '  </div>\n')
    A(page(T, 25, title_block("My Own Answers", "", 23) +
            '  <span class="age">Ages 8&ndash;12</span>\n' +
            subtitle("Write your own answers", "ናትካ መልሲ ጽሓፍ") + divider() + mc))

    # ---- PAGE 26 — SPOT THE DIFFERENCE ----
    A(page(T, 26, title_block("Spot the Difference", "", 23) +
            subtitle("Find 5 differences", "5 ፍልልያት ርኸብ") + divider() +
            instr("Look at the two pictures. Circle 5 things that are different.", "ኣብ ካልአይቲ ስእሊ 5 ፍልልያት ኣኽብብ።") +
            '  <div class="grid2">\n    <div class="art center" id="p26-a"><p class="small center">Picture 1 <span class="ti">ስእሊ 1</span></p></div>\n'
            '    <div class="art center" id="p26-b"><p class="small center">Picture 2 <span class="ti">ስእሊ 2</span></p></div>\n  </div>\n'))

    # ---- PAGE 27 — MAZE ----
    A(page(T, 27, title_block(b["maze_title_en"], "", 22) +
            subtitle("Find the path through the maze", "መንገዲ ርኸብ") + divider() +
            instr(b["maze_instr_en"], b["maze_instr_ti"]) +
            '  <div class="art center" id="p27-art"></div>\n'))

    # ---- PAGE 28 — DOT TO DOT ----
    A(page(T, 28, title_block("Dot to Dot", "", 23) +
            '  <span class="age">Ages 4&ndash;7</span>\n' +
            subtitle("Join the dots 1 to 12", "ካብ 1 ክሳብ 12 ኣራኽብ") + divider() +
            instr("Connect the dots in order, then colour the picture.", "ነጥብታት ኣራኽብ፡ ደሓር ሕብሮ።") +
            '  <div class="art center" id="p28-art"></div>\n'))

    # ---- PAGE 29 — DRAW YOUR OWN ----
    A(page(T, 29, title_block(b["draw_title_en"], "", 23) +
            subtitle(b["draw_sub_en"], b["draw_sub_ti"]) + divider() +
            instr(b["draw_instr_en"], b["draw_instr_ti"]) +
            '  <div style="border:3px dashed var(--royal); border-radius:14px; height:150mm; margin-top:8mm;"></div>\n'))

    # ---- PAGE 30 — CRAFT ----
    craft_steps = ''.join(f'    <li>{esc(s[0])}<span class="ti">{esc(s[1])}</span></li>\n' for s in b["craft_steps"])
    A(page(T, 30, title_block(b["craft_title_en"], "", 22) +
            subtitle(b["craft_sub_en"], b["craft_sub_ti"]) + divider() +
            instr(b["craft_need_en"], b["craft_need_ti"]) +
            f'  <ol class="bi" style="font-size:13pt; line-height:1.7;">\n{craft_steps}  </ol>\n' +
            '  <div class="art center" id="p30-art"></div>\n'))

    # ---- PAGE 31 — CRAFT TEMPLATE ----
    A(page(T, 31, title_block(b["template_title_en"], "", 23) +
            subtitle("Cut along the lines", "ኣብ መስመራት ቆርጽ") + divider() +
            '  <div class="art center" id="p31-art"></div>\n' +
            '  <p class="color-note">Adult help with scissors, please!<span class="ti">ብመቐስ ሓገዝ ዓቢ ሰብ የድሊ!</span></p>\n'))

    # ---- PAGE 32 — BOOKMARKS ----
    bm = b["bookmarks"]
    A(page(T, 32, title_block("Make a Bookmark", "", 23) +
            subtitle("Colour, cut, and use", "ሕብር፡ ቆርጽ፡ ተጠቐም") + divider() +
            f'''  <div class="grid2" style="gap:20px;">
    <div style="border:2px solid var(--royal); border-radius:12px; padding:12px; text-align:center;">
      <p class="ti" style="color:var(--royal); font-size:14pt;">{esc(bm[0][1])}</p>
      <p style="font-size:15pt; color:var(--royal); font-weight:700;">{esc(bm[0][0])}</p>
      <div id="bm-a"></div>
      <p class="small">{esc(b["verse"]["ref_en"])}</p>
    </div>
    <div style="border:2px solid var(--rose); border-radius:12px; padding:12px; text-align:center;">
      <p class="ti" style="color:var(--rose); font-size:14pt;">{esc(bm[1][1])}</p>
      <p style="font-size:15pt; color:var(--rose); font-weight:700;">{esc(bm[1][0])}</p>
      <div id="bm-b"></div>
      <p class="small">{esc(b["verse"]["ref_en"])}</p>
    </div>
  </div>
  <p class="color-note mt">Cut out both bookmarks and give one to a friend.<span class="ti">ሓደ ንፈታዊኻ ሃቦ።</span></p>\n'''))


    # ---- PAGE 33 — SECRET CODE ----
    sc = b["secret_code"]  # dict: key(list of (num,letter)), line1 word, line2 words
    key_spans = ''.join(f'<span>{k[0]}={k[1]}</span>' for k in sc["key"])
    def code_line(word):
        blanks = ' '.join('__' for _ in word)
        nums = ' &nbsp; '.join(sc["letter2num"][ch] for ch in word)
        return blanks, nums
    l1b, l1n = code_line(sc["line1"])
    # line2 may be multiple words
    l2_words = sc["line2"].split()
    l2b = ' &nbsp;&nbsp; '.join(' '.join('__' for _ in w) for w in l2_words)
    l2n = ' &nbsp;&nbsp; '.join(' '.join(sc["letter2num"][ch] for ch in w) for w in l2_words)
    A(page(T, 33, title_block("Crack the Secret Code", "", 23) +
            '  <span class="age">Ages 8&ndash;12</span>\n' +
            subtitle("Use the key to reveal the message", "ነቲ መልእኽቲ ፍታሕ") + divider() +
            instr("Each number stands for a letter. Write the letters!", "ነፍሲ ወከፍ ቁጽሪ ሓደ ፊደል እዩ።") +
            f'  <div class="bank" style="font-size:13pt;">{key_spans}</div>\n' +
            f'  <p class="center" style="font-size:22pt; letter-spacing:8px; margin-top:12mm;">{l1b}<br>'
            f'<span style="font-size:13pt; letter-spacing:4px;">{l1n}</span></p>\n' +
            f'  <p class="center" style="font-size:22pt; letter-spacing:8px; margin-top:12mm;">{l2b}<br>'
            f'<span style="font-size:13pt; letter-spacing:4px;">{l2n}</span></p>\n' +
            f'  <p class="center small mt">Answers: line 1 = <strong>{esc(sc["line1"])}</strong> · line 2 = <strong>{esc(sc["line2"])}</strong>.'
            f'<span class="ti">{esc(sc["hint_ti"])}</span></p>\n'))

    # ---- PAGE 34 — TRUE OR FALSE ----
    tf_rows = ""
    for st in b["true_false"]:
        tf_rows += (f'    <tr><td style="padding:10px; border-bottom:1px solid #ddd;">{esc(st[0])} '
                    f'<span class="ti">{esc(st[1])}</span></td><td style="text-align:center;">☐</td><td style="text-align:center;">☐</td></tr>\n')
    tf_ans = " · ".join("True" if st[2] else "False" for st in b["true_false"])
    A(page(T, 34, title_block("True or False?", "", 23) +
            subtitle("Tick the right box", "ቅኑዕ ሳጹን ምልክት ግበር") + divider() +
            '  <table style="width:100%; border-collapse:collapse; font-size:13pt;">\n'
            '    <tr style="background:var(--soft);"><th style="text-align:left; padding:8px;">Statement <span class="ti">ሓሳብ</span></th>'
            '<th style="padding:8px;">True<br><span class="ti" style="font-size:10pt;">ሓቂ</span></th>'
            '<th style="padding:8px;">False<br><span class="ti" style="font-size:10pt;">ሓሶት</span></th></tr>\n'
            f'{tf_rows}  </table>\n  <p class="center small mt">Answers: {tf_ans}</p>\n'))

    # ---- PAGE 35 — FILL IN THE BLANKS ----
    fb = b["fill_blanks"]
    bank = ''.join(f'<span>{esc(w)}</span>' for w in fb["bank"])
    sentences = ''.join(f'    <p>{esc(s)}</p>\n' for s in fb["sentences"])
    A(page(T, 35, title_block("Fill in the Blanks", "", 23) +
            subtitle("Use the word bank", "ካብ ቃላት ምረጽ") + divider() +
            f'  <div class="bank">{bank}</div>\n' +
            f'  <div class="story" style="font-size:15pt; line-height:2.2;">\n{sentences}  </div>\n' +
            f'  <p class="center small mt">Answers: {esc(fb["answers"])}</p>\n'))

    # ---- PAGE 36 — ACROSTIC ----
    word = b["acrostic"]
    colors = ["var(--royal)","var(--rose)","var(--gold)","var(--sky)","var(--leaf)","var(--royal)","var(--rose)","var(--gold)"]
    ac = ""
    for i, ch in enumerate(word):
        ac += f'    <p><strong style="color:{colors[i%len(colors)]};">{ch}</strong> ______________________________</p>\n'
    A(page(T, 36, title_block(f'{"-".join(word)} Acrostic', "", 22) +
            subtitle("Write a word for each letter", "ንነፍሲ ወከፍ ፊደል ቃል ጽሓፍ") + divider() +
            instr(f"Think of a good word that starts with each letter of {word}.", "ጽቡቕ ቃል ሕሰብ።") +
            f'  <div style="font-size:22pt; line-height:2.4; margin-top:10mm;">\n{ac}  </div>\n'))

    # ---- PAGE 37 — PRAYER ----
    pr = b["prayer"]
    A(page(T, 37, title_block("A Prayer", "", 23) +
            subtitle("Pray together", "ብሓባር ጸልዩ") + divider() +
            f'  <div class="verse" style="font-size:15pt;">{esc(pr["en"])}'
            f'<span class="ti" style="font-size:14pt;">{esc(pr["ti"])}</span></div>\n' +
            instr("Write your own prayer to God below.", "ናትካ ጸሎት ኣብ ታሕቲ ጽሓፍ።") +
            lines(4) + art("p37-art")))

    # ---- PAGE 38 — REFLECTION ----
    A(page(T, 38, title_block("Reflection Time", "", 23) +
            subtitle("Think about the story", "ብዛዕባ እቲ ታሪኽ ሕሰብ") + divider() +
            f'  <div class="qwrap"><p class="q">{esc(b["reflect1_en"])}<span class="ti">{esc(b["reflect1_ti"])}</span></p></div>\n' +
            lines(2, tight=True) +
            f'  <div class="qwrap mt"><p class="q">{esc(b["reflect2_en"])}<span class="ti">{esc(b["reflect2_ti"])}</span></p></div>\n' +
            lines(2, tight=True) +
            '  <div class="qwrap mt"><p class="q">Draw a face for how the story makes you feel.<span class="ti">ገጽ ስኣል።</span></p>\n'
            '    <div class="grid3 mt"><div class="card center" style="height:70px;">😊</div>'
            '<div class="card center" style="height:70px;">😮</div>'
            '<div class="card center" style="height:70px;">🙂</div></div>\n  </div>\n'))

    # ---- PAGE 39 — FAVOURITE PART ----
    A(page(T, 39, title_block("My Favourite Part", "", 23) +
            subtitle("Draw and write", "ስኣልን ጽሓፍን") + divider() +
            f'  <p class="q">Draw your favourite part of the story:<span class="ti">ዝፈተኻዮ ክፋል ስኣል፦</span></p>\n' +
            '  <div style="border:3px solid var(--royal); border-radius:14px; height:130mm; margin:6mm 0;"></div>\n' +
            '  <p class="q">Why is it your favourite? <span class="ti">ስለምንታይ ደስ ኢሉካ?</span></p>\n' +
            lines(2, tight=True)))

    # ---- PAGE 40 — VERSE POSTER ----
    A(page(T, 40, title_block("Memory Verse Poster", "", 23) +
            subtitle("Colour and hang it up", "ሕብሮ ንጥልቆ") + divider() +
            f'''  <div class="cert" style="border-color:var(--royal); padding:16mm 12mm;">
    <div id="poster-art"></div>
    <p style="font-size:19pt; color:var(--royal); font-style:italic; margin-top:6mm;">&ldquo;{esc(v["en"])}&rdquo;</p>
    <p class="ti" style="font-size:15pt; color:var(--rose);">&ldquo;{esc(v["ti"])}&rdquo;</p>
    <p style="color:var(--gold); letter-spacing:2px; margin-top:4mm;">{esc(v["ref_en"].upper())} &nbsp;·&nbsp; <span class="ti">{esc(v["ref_ti"])}</span></p>
  </div>\n'''))

    # ---- PAGE 41 — REVIEW ----
    lessons = b["three_lessons"]
    lcards = ''.join(f'    <div class="card center"><strong style="color:{["var(--royal)","var(--rose)","var(--leaf)"][i]};">{esc(l[0])}</strong><span class="ti">{esc(l[1])}</span></div>\n' for i, l in enumerate(lessons))
    A(page(T, 41, title_block("You Did It!", "  ገበርካዮ!", 23) + divider() +
            f'  <p class="story" style="text-align:center;">{esc(b["review_en"])}<span class="ti" style="text-align:center;">{esc(b["review_ti"])}</span></p>\n' +
            f'  <div class="grid3 mt">\n{lcards}  </div>\n' +
            art("p41-art", "margin-top:6mm;") +
            '  <p class="center mt">Now turn the page for your certificate!<span class="ti">ንምስክር ወረቐትካ ገጽ ግልብጥ!</span></p>\n'))

    # ---- PAGE 42 — CERTIFICATE ----
    A(page(T, 42, f'''  <div class="cert">
    <div id="cert-art"></div>
    <span class="badge" style="background:var(--gold);">Certificate of Completion</span>
    <h1 style="margin-top:6mm;">{esc(b["title_en"])}</h1>
    <p class="ti" style="font-size:16pt; color:var(--rose);">ምስክር ወረቐት &mdash; {esc(b["title_ti"])}</p>
    <p style="font-size:14pt; margin-top:8mm;">This certificate is proudly awarded to:
      <span class="ti" style="display:block; color:var(--royal);">እዚ ምስክር ወረቐት ንዚ ዚስዕብ ይወሃብ፦</span></p>
    <div class="name-line"></div>
    <p style="font-size:13pt;">{esc(b["cert_line_en"])}
      <span class="ti" style="display:block; color:var(--royal);">{esc(b["cert_line_ti"])}</span></p>
    <div class="grid2 mt" style="margin-top:14mm;">
      <div><div style="border-bottom:2px solid var(--ink); margin:0 12%;"></div><p class="small">Date <span class="ti">ዕለት</span></p></div>
      <div><div style="border-bottom:2px solid var(--ink); margin:0 12%;"></div><p class="small">Teacher / Parent <span class="ti">መምህር / ወላዲ</span></p></div>
    </div>
    <p class="small" style="margin-top:10mm;">Written by {esc(AUTHOR_EN)} &nbsp;·&nbsp; <span class="ti">{esc(AUTHOR_TI)}</span></p>
  </div>'''))

    # ---- Closing script: art placement + puzzle generators ----
    A(build_script(b))
    A('</body>\n</html>\n')
    return ''.join(parts)


# --------------------------------------------------------------------------
# Per-book closing <script>: places SVG art and builds word search / crossword
# / count / spot-diff / maze / dot-to-dot. Reuses the verified Esther logic.
# --------------------------------------------------------------------------

def build_script(b):
    icon = b["icon"]          # main Art.* function name, e.g. "lion"
    icon2 = b.get("icon2", icon)  # secondary icon for variety
    counts = b.get("count_sets", [2,3,1,4])
    return f'''
<script src="../../assets/art.js"></script>
<script>
function put(id, svg){{ var el=document.getElementById(id); if(el) el.insertAdjacentHTML('beforeend', svg); }}
function repeat(fn,n,gap){{ var s='<div style="display:flex;justify-content:center;gap:'+(gap||10)+'px;flex-wrap:wrap;">'; for(var i=0;i<n;i++) s+=fn; return s+'</div>'; }}
var ICON='{icon}', ICON2='{icon2}';
function mainArt(sz){{ return Art[ICON](sz); }}
function altArt(sz){{ return Art[ICON2](sz); }}

put('cover-art', mainArt(300));
put('p2-art', Art.scroll(180));
put('p3-art', mainArt(240));
put('p4-art', repeat(mainArt(140),2,40));
put('p5-art', mainArt(200));
put('p6-art', altArt(200));
put('p7-art', mainArt(200));
put('p8-art', altArt(200));
put('p9-art', mainArt(220));
put('p10-art', Art.star(40)+Art.heart(50)+Art.star(40));
put('p11-art', mainArt(150));
put('p17-art', mainArt(180));
put('p18-art', mainArt(360));
put('p19-art', altArt(360));
put('p20-art', mainArt(360));
put('p21-art', altArt(340));
put('p24-art', Art.heart(70));
put('p30-art', mainArt(220));
put('p37-art', Art.heart(70));
put('p41-art', mainArt(200));
put('poster-art', mainArt(160));
put('cert-art', mainArt(150));
put('bm-a', mainArt(120));
put('bm-b', Art.heart(90));

/* Count & colour */
(function(){{
  var rows={json.dumps(counts)};
  var html='';
  rows.forEach(function(n){{
    html+='<div style="display:flex;align-items:center;gap:14px;margin:8px 0;border:2px solid #d4a017;border-radius:12px;padding:8px;">';
    html+= repeat(mainArt(80), n, 8);
    html+='<div style="margin-left:auto;width:56px;height:56px;border:2px solid #4b2e83;border-radius:10px;"></div></div>';
  }});
  put('p22-art', html);
}})();

/* Spot the difference */
put('p26-a', mainArt(220));
put('p26-b', mainArt(220));

/* Craft template — generic wide band */
put('p31-art', (function(){{
  var S='fill="none" stroke="#2b2b2b" stroke-width="3" stroke-linejoin="round"';
  var inner='<path '+S+' d="M20 160 L20 90 L70 140 L120 60 L170 140 L220 60 L270 140 L320 90 L470 90 L470 160 Z"/>';
  inner+='<path stroke-dasharray="6 6" '+S+' d="M20 160 L470 160"/>';
  return '<svg viewBox="0 0 490 180" width="490" height="180" xmlns="http://www.w3.org/2000/svg">'+inner+'</svg>';
}})());

/* Word Search */
(function(){{
  var words=(window.WS_WORDS||[]).map(function(w){{return w.toUpperCase();}});
  var N=12, grid=[]; for(var r=0;r<N;r++){{grid[r]=[];for(var c=0;c<N;c++)grid[r][c]=null;}}
  function place(w){{for(var t=0;t<300;t++){{var dir=Math.random()<0.5?'H':'V';var r=Math.floor(Math.random()*N),c=Math.floor(Math.random()*N);if(dir==='H'&&c+w.length>N)continue;if(dir==='V'&&r+w.length>N)continue;var ok=true;for(var i=0;i<w.length;i++){{var rr=dir==='V'?r+i:r,cc=dir==='H'?c+i:c;if(grid[rr][cc]&&grid[rr][cc]!==w[i]){{ok=false;break;}}}}if(!ok)continue;for(var j=0;j<w.length;j++){{var rr2=dir==='V'?r+j:r,cc2=dir==='H'?c+j:c;grid[rr2][cc2]=w[j];}}return true;}}return false;}}
  words.forEach(place);
  var AL='ABCDEFGHIJKLMNOPQRSTUVWXYZ';
  for(var r2=0;r2<N;r2++)for(var c2=0;c2<N;c2++) if(!grid[r2][c2]) grid[r2][c2]=AL[Math.floor(Math.random()*26)];
  var html='';
  for(var r3=0;r3<N;r3++){{html+='<tr>';for(var c3=0;c3<N;c3++)html+='<td>'+grid[r3][c3]+'</td>';html+='</tr>';}}
  var t=document.getElementById('ws-table'); if(t) t.innerHTML=html;
  var bk=document.getElementById('ws-bank'); if(bk) bk.innerHTML=words.map(function(w){{return '<span>'+w+'</span>';}}).join('');
}})();

/* Crossword — interlocking around a vertical spine word */
(function(){{
  var cw=window.CW; if(!cw) return;
  var N=cw.grid||13;
  var g=[]; for(var r=0;r<N;r++){{g[r]=[];for(var c=0;c<N;c++)g[r][c]={{ch:null,num:0}};}}
  function across(w,r,c){{for(var i=0;i<w.length;i++)g[r][c+i].ch=w[i];}}
  function down(w,r,c){{for(var i=0;i<w.length;i++)g[r+i][c].ch=w[i];}}
  down(cw.spine.word, cw.spine.r, cw.spine.c);
  g[cw.spine.r][cw.spine.c].num=1;
  var n=2;
  cw.cross.forEach(function(x){{ across(x.word, x.r, x.c); g[x.r][x.c].num=x.num||n; n++; }});
  var html='';
  for(var r2=0;r2<N;r2++){{html+='<tr>';for(var c2=0;c2<N;c2++){{var cell=g[r2][c2];
    if(cell.ch===null) html+='<td class="blk"></td>';
    else html+='<td>'+(cell.num?cell.num:'')+'</td>';
  }}html+='</tr>';}}
  var t=document.getElementById('cw-table'); if(t) t.innerHTML=html;
}})();

/* Maze */
put('p27-art',(function(){{
  var s='fill="none" stroke="#2b2b2b" stroke-width="3" stroke-linecap="round"';
  var inner='<rect x="10" y="10" width="380" height="380" '+s+'/>';
  var walls=['M10 90 h300','M390 90 h-300','M90 90 v230','M90 320 h230','M170 10 v230','M170 240 h150','M250 90 v170','M330 170 v220','M250 320 h80','M10 240 h100'];
  walls.forEach(function(w){{inner+='<path '+s+' d="'+w+'"/>';}});
  inner+='<text x="20" y="40" font-size="15" fill="#4b2e83">START</text>';
  inner+='<text x="300" y="382" font-size="15" fill="#c94f7c">END</text>';
  return '<svg viewBox="0 0 400 400" width="400" height="400" xmlns="http://www.w3.org/2000/svg">'+inner+'</svg>';
}})());

/* Dot to dot */
put('p28-art',(function(){{
  var pts=[[60,180],[90,120],[130,150],[150,90],[170,150],[210,120],[240,180],[240,220],[60,220],[60,180]];
  var inner='';
  pts.forEach(function(p,i){{ inner+='<circle cx="'+p[0]+'" cy="'+p[1]+'" r="4" fill="#2b2b2b"/>';
    if(i<7) inner+='<text x="'+(p[0]+6)+'" y="'+(p[1]-6)+'" font-size="14" fill="#4b2e83">'+(i+1)+'</text>'; }});
  var jew=[[90,200,8],[130,200,9],[150,200,10],[170,200,11],[210,200,12]];
  jew.forEach(function(p){{inner+='<circle cx="'+p[0]+'" cy="'+p[1]+'" r="4" fill="#2b2b2b"/><text x="'+(p[0]+6)+'" y="'+(p[1]+16)+'" font-size="14" fill="#c94f7c">'+p[2]+'</text>';}});
  return '<svg viewBox="0 0 300 260" width="300" height="260" xmlns="http://www.w3.org/2000/svg">'+inner+'</svg>';
}})());
</script>
'''


# --------------------------------------------------------------------------
# Crossword auto-layout: given a vertical spine word and a list of crossing
# words, find a valid row + start column for each so it shares one letter with
# the spine. Returns the JS-ready dict. Verified to avoid conflicts.
# --------------------------------------------------------------------------

def make_crossword(spine, crossers, grid=13):
    """
    spine: the vertical word (string).
    crossers: list of horizontal words (strings). Each must share >=1 letter
              with the spine. Placed so its shared letter sits on the spine col.
    """
    spine = spine.upper()
    spine_col = grid // 2
    spine_r = max(1, (grid - len(spine)) // 2)
    crossers = [w.upper() for w in crossers]

    # For each crosser, list all (spine_index, word_index) options where letters match
    # and the word fits horizontally within the grid.
    def options(w):
        opts = []
        for si in range(len(spine)):
            for wi in range(len(w)):
                if w[wi] == spine[si]:
                    start_c = spine_col - wi
                    if 0 <= start_c and start_c + len(w) <= grid:
                        opts.append((si, start_c))
        return opts

    # Backtracking assignment so each crosser sits on a DISTINCT spine row.
    placements = {}  # word -> (row, start_c)
    used_rows = set()

    def solve(idx):
        if idx == len(crossers):
            return True
        w = crossers[idx]
        for (si, start_c) in options(w):
            row = spine_r + si
            if row in used_rows:
                continue
            used_rows.add(row)
            placements[idx] = (row, start_c)
            if solve(idx + 1):
                return True
            used_rows.discard(row)
            del placements[idx]
        return False

    if not solve(0):
        raise ValueError(f"Crossword: could not interlock {crossers} on spine '{spine}'")

    cross = []
    for idx, w in enumerate(crossers):
        row, start_c = placements[idx]
        cross.append({"word": w, "r": row, "c": start_c, "num": idx + 2})
    return {
        "grid": grid,
        "spine": {"word": spine, "r": spine_r, "c": spine_col},
        "cross": cross,
    }


# --------------------------------------------------------------------------
# Runner
# --------------------------------------------------------------------------

def main():
    from book_data import BOOKS  # story data lives in a separate module
    made = []
    for b in BOOKS:
        # auto-build crossword layout from the spine + crossers if provided
        if "crossword" in b and "spine" in b["crossword"]:
            layout = make_crossword(b["crossword"]["spine"],
                                    [c[1] for c in b["crossword"]["down_clues"]] +
                                    [c[1] for c in b["crossword"]["across_clues"]]
                                    if False else b["crossword"]["crossers"],
                                    b["crossword"].get("grid", 13))
            b["crossword"]["words"] = layout
        out_dir = os.path.join(ROOT, "books", b["slug"])
        os.makedirs(out_dir, exist_ok=True)
        html_str = build_book(b)
        with open(os.path.join(out_dir, "index.html"), "w", encoding="utf-8") as f:
            f.write(html_str)
        n_pages = html_str.count('class="page"')
        made.append((b["slug"], n_pages))
        print(f"  ✓ {b['slug']:22s} — {n_pages} pages")
    print(f"\nGenerated {len(made)} book(s).")
    return made


if __name__ == "__main__":
    main()
