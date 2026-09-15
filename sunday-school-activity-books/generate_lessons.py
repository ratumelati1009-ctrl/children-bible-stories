#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate the Christian Sunday-School Activity Books (42 pages each), print-ready HTML.
Series author: Daniel Tesfamariam.

Sunday-school LESSON-PACK format (teacher/leader oriented, English):
cover, welcome, contents, lesson aim + teacher prep, opening prayer,
Bible story (4 pages), memory verse + trace, discussion, comprehension (easy/hard),
true-false, sequencing, word search, crossword, matching, fill-in-the-blanks,
acrostic, secret code, 4 colouring pages, count & colour, spot-the-difference,
maze, dot-to-dot, "living it out" scenarios, drama/role-play, group game,
craft + template, snack idea, verse poster, take-home note, review, response
prayer, certificate.

Run:  python3 generate_lessons.py
Output: books/<slug>/index.html
"""
import os, html, json

ROOT = os.path.dirname(os.path.abspath(__file__))
AUTHOR = "Daniel Tesfamariam"


def esc(s):
    return html.escape(str(s), quote=True)

def page(book, label, inner):
    return f'<section class="page" data-book="{esc(book)}" data-page="{esc(label)}">\n{inner}\n</section>\n'

def title(en, size=26):
    return f'  <h2 class="title" style="font-size:{size}pt;">{esc(en)}</h2>\n'

def sub(s):
    return f'  <p class="subtitle">{esc(s)}</p>\n'

def divider():
    return '  <div class="divider"></div>\n'

def instr(s):
    return f'  <div class="instr">{esc(s)}</div>\n'

def teacher(s):
    return f'  <div class="teacher"><b>Teacher tip:</b> {esc(s)}</div>\n'

def lines(n=3, tight=False):
    c = "lines tight" if tight else "lines"
    return f'  <div class="{c}">' + ''.join('<div class="rule"></div>' for _ in range(n)) + '</div>\n'

def art(el_id, style=""):
    st = f' style="{style}"' if style else ""
    return f'  <div class="art" id="{el_id}"{st}></div>\n'



def build_book(b):
    T = b["short"]
    P = []
    A = P.append

    A(f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{esc(b["title"])} — Sunday-School Activity Pack</title>
<link rel="stylesheet" href="../../assets/lesson.css">
</head>
<body>
<div class="toolbar"><span style="margin-right:8px;">{esc(b["short"])}</span>
  <button onclick="window.print()">🖨️ Print / Save PDF</button></div>
''')

    # 1 — COVER
    A(f'''<section class="page" data-book="Sunday-School Activity Pack" data-page="Cover">
  <div class="center" style="margin-top:6mm;"><span class="badge">Sunday-School Activity Pack</span></div>
  <h2 class="title" style="margin-top:12mm; font-size:30pt;">{esc(b["title"])}</h2>
  <p class="subtitle">{esc(b["theme"])}</p>
  <p class="center" style="font-size:13pt; color:var(--deep); font-weight:700; margin-top:6px;">Written by {esc(AUTHOR)}</p>
  <div class="art" id="cover-art"></div>
  <div class="center mt"><span class="age">For Ages 4&ndash;12</span></div>
  <p class="center small" style="margin-top:12mm;">{esc(b["cover_line"])}</p>
  <p class="center small" style="position:absolute; bottom:16mm; left:16mm; right:16mm;">
    A complete lesson pack for teachers and families — story, memory verse, discussion,
    games, crafts and activities. Memory verse based on the International Children's Bible (ICB).</p>
</section>
''')

    # 2 — WELCOME / HOW TO USE
    hints = ''.join(f'    <li>{esc(x)}</li>\n' for x in b["how_to_use"])
    A(page(T, 2, title("Welcome, Teacher!", 24) + divider() +
      f'  <p class="story">{esc(b["welcome"])}</p>\n' +
      '  <h3 style="color:var(--primary); font-size:17pt;">How to Use This Pack</h3>\n' +
      f'  <ul class="list">\n{hints}  </ul>\n' +
      teacher(b["welcome_tip"]) + art("p2-art", "margin-top:6mm;")))

    # 3 — CONTENTS
    items = [
        "Lesson Aim & Teacher Preparation", "Opening Prayer & Gathering",
        "The Bible Story (Parts 1–4)", "Memory Verse & Tracing",
        "Talk About It — Discussion", "Comprehension Questions",
        "True or False & Sequencing", "Word Search & Crossword",
        "Match & Fill in the Blanks", "Acrostic & Secret Code",
        "Colouring Pages", "Count, Spot the Difference & Maze",
        "Living It Out — Scenarios", "Act It Out — Drama",
        "Group Game", "Craft & Template", "Snack Idea & Memory Poster",
        "Take-Home Note", "Review & Response Prayer", "Certificate of Completion",
    ]
    ol = ''.join(f'    <li>{esc(x)}</li>\n' for x in items)
    A(page(T, 3, title("Contents", 24) + divider() +
      f'  <ol class="list" style="font-size:12.5pt; line-height:1.9;">\n{ol}  </ol>\n' +
      art("p3-art", "margin-top:6mm;")))

    # 4 — LESSON AIM & PREP
    obj = ''.join(f'    <li>{esc(x)}</li>\n' for x in b["objectives"])
    prep = ''.join(f'    <li>{esc(x)}</li>\n' for x in b["prep"])
    A(page(T, 4, title("Lesson Aim & Teacher Preparation", 22) + divider() +
      f'  <div class="aim"><b>Lesson aim:</b> {esc(b["aim"])}</div>\n' +
      '  <h3 style="color:var(--primary); font-size:16pt;">Learning objectives</h3>\n' +
      f'  <ul class="list">\n{obj}  </ul>\n' +
      '  <h3 style="color:var(--primary); font-size:16pt;">You will need</h3>\n' +
      f'  <ul class="list">\n{prep}  </ul>\n' +
      teacher(b["prep_tip"])))

    # 5 — OPENING PRAYER & GATHERING
    A(page(T, 5, title("Opening Prayer & Gathering", 22) + divider() +
      '  <h3 style="color:var(--primary); font-size:16pt;">Welcome circle</h3>\n' +
      f'  <p class="story">{esc(b["gathering"])}</p>\n' +
      f'  <div class="verse" style="font-size:15pt;">{esc(b["opening_prayer"])}</div>\n' +
      '  <h3 style="color:var(--primary); font-size:16pt;">Icebreaker question</h3>\n' +
      f'  <div class="card q">{esc(b["icebreaker"])}</div>\n' +
      art("p5-art")))

    # 6–9 — STORY (4 parts)
    for i, sp in enumerate(b["story"]):
        paras = ''.join(f'    <p>{esc(x)}</p>\n' for x in sp["paras"])
        A(page(T, 6 + i, title(f'The Bible Story — Part {i+1}', 22) +
          sub(sp["sub"]) + divider() +
          f'  <div class="story">\n{paras}  </div>\n' + art(f"p{6+i}-art")))

    # 10 — MEMORY VERSE
    v = b["verse"]
    A(page(T, 10, title("Memory Verse", 24) + divider() +
      f'  <div class="verse">&ldquo;{esc(v["text"])}&rdquo;<span class="ref">{esc(v["ref"])} (ICB)</span></div>\n' +
      instr("Read the verse together three times. Then trace it and say it from memory!") +
      f'  <p style="font-size:20pt; color:#cfe0d6; letter-spacing:1px; line-height:1.8; text-align:center;">{esc(v["text"])}</p>\n' +
      lines(3) + teacher(b["verse_tip"]) + art("p10-art")))

    # 11 — DISCUSSION
    disc = ''.join(f'  <div class="qwrap card q"><p class="q">{i+1}. {esc(q)}</p></div>\n' for i, q in enumerate(b["discussion"]))
    A(page(T, 11, title("Talk About It", 23) + sub("Discussion questions for the group") + divider() +
      instr("Sit in a circle. Let everyone share. There are no wrong answers when we talk about God's Word!") +
      disc))

    # 12 — COMPREHENSION EASY
    qe = ''
    for i, q in enumerate(b["easy_q"]):
        qe += f'  <div class="qwrap"><p class="q">{i+1}. {esc(q["q"])}</p><p style="font-size:14pt;">&nbsp;&nbsp; {q["opts"]}</p></div>\n'
    A(page(T, 12, title("What Did You Learn?", 22) + '  <span class="age">Ages 4&ndash;7</span>\n' +
      sub("Circle the right answer") + divider() + qe + art("p12-art")))

    # 13 — COMPREHENSION HARD
    qh = ''.join(f'  <div class="qwrap"><p class="q">{i+1}. {esc(q)}</p>{lines(2, True)}</div>\n' for i, q in enumerate(b["hard_q"]))
    A(page(T, 13, title("Think & Write", 22) + '  <span class="age">Ages 8&ndash;12</span>\n' +
      sub("Answer in full sentences") + divider() + qh))

    # 14 — TRUE/FALSE + SEQUENCING
    tf = ''
    for st in b["true_false"]:
        tf += f'    <tr><td style="padding:8px; border-bottom:1px solid #ddd;">{esc(st[0])}</td><td style="text-align:center;">☐</td><td style="text-align:center;">☐</td></tr>\n'
    tf_ans = " · ".join("T" if s[1] else "F" for s in b["true_false"])
    seq = ''.join(f'    <div class="card"><span class="num">&nbsp;</span> {esc(s)}</div>\n' for s in b["sequence"])
    A(page(T, 14, title("True or False?", 22) + divider() +
      '  <table style="width:100%; border-collapse:collapse; font-size:12.5pt;">\n'
      '    <tr style="background:var(--soft);"><th style="text-align:left; padding:8px;">Statement</th><th style="padding:8px;">True</th><th style="padding:8px;">False</th></tr>\n'
      f'{tf}  </table>\n  <p class="center small">Answers: {tf_ans}</p>\n' + divider() +
      '  <h3 style="color:var(--primary); font-size:15pt;">Put the story in order (1–4)</h3>\n' +
      f'  <div class="grid2" style="gap:10px;">\n{seq}  </div>\n'))

    # 15 — WORD SEARCH
    A(page(T, 15, title("Word Search", 22) + '  <span class="age">Ages 8&ndash;12</span>\n' +
      sub("Find the hidden words") + divider() +
      '  <table class="ws" id="ws-table"></table>\n  <div class="bank" id="ws-bank"></div>\n' +
      f'  <script>window.WS_WORDS={json.dumps(b["ws_words"])};</script>\n'))

    # 16 — CROSSWORD
    cw = b["crossword"]
    ac = ''.join(f'      <p>{c[0]}. {esc(c[1])}</p>\n' for c in cw["across_clues"])
    dn = ''.join(f'      <p>{c[0]}. {esc(c[1])}</p>\n' for c in cw["down_clues"])
    A(page(T, 16, title("Crossword", 22) + sub("Use the clues to fill the grid") + divider() +
      '  <table class="cw" id="cw-table"></table>\n' +
      f'  <div class="grid2 mt" style="font-size:11pt;">\n    <div><strong>Down</strong>\n{dn}    </div>\n    <div><strong>Across</strong>\n{ac}    </div>\n  </div>\n' +
      f'  <p class="center small mt">Answers: {esc(cw["answer_line"])}</p>\n' +
      f'  <script>window.CW={json.dumps(cw["words"])};</script>\n'))

    # 17 — MATCH
    left = ''.join(f'      <p style="font-size:15pt; line-height:2.6;">{esc(m[0])} &nbsp; &bull;</p>\n' for m in b["match"])
    right = ''.join(f'      <p style="font-size:15pt; line-height:2.6;">&bull; &nbsp; {esc(m[1])}</p>\n' for m in list(b["match"])[::-1])
    ans = " · ".join(f'{m[0]}={m[1]}' for m in b["match"])
    A(page(T, 17, title("Match the Pairs", 22) + sub("Draw a line to match each word with its meaning") + divider() +
      instr("Match each word on the left to the right idea on the right.") +
      f'  <div class="grid2" style="gap:0 40px;">\n    <div>\n{left}    </div>\n    <div>\n{right}    </div>\n  </div>\n' +
      f'  <p class="center small mt">Answers: {esc(ans)}</p>\n'))

    # 18 — FILL IN THE BLANKS
    fb = b["fill_blanks"]
    bank = ''.join(f'<span>{esc(w)}</span>' for w in fb["bank"])
    sents = ''.join(f'    <p>{esc(s)}</p>\n' for s in fb["sentences"])
    A(page(T, 18, title("Fill in the Blanks", 22) + sub("Use the word bank") + divider() +
      f'  <div class="bank">{bank}</div>\n  <div class="story" style="font-size:15pt; line-height:2.2;">\n{sents}  </div>\n' +
      f'  <p class="center small mt">Answers: {esc(fb["answers"])}</p>\n'))

    # 19 — ACROSTIC
    word = b["acrostic"]
    colors = ["var(--primary)","var(--coral)","var(--gold)","var(--sky)","var(--purple)","var(--deep)","var(--primary)","var(--coral)"]
    ac2 = ''.join(f'    <p><strong style="color:{colors[i%len(colors)]};">{ch}</strong> ______________________________</p>\n' for i, ch in enumerate(word))
    A(page(T, 19, title(f'{"-".join(word)} Acrostic', 22) + sub("Write a word or idea for each letter") + divider() +
      instr(f"For each letter of {word}, write a word that reminds you of today's lesson.") +
      f'  <div style="font-size:22pt; line-height:2.4; margin-top:8mm;">\n{ac2}  </div>\n'))

    # 20 — SECRET CODE
    sc = b["secret_code"]
    key = ''.join(f'<span>{n}={c}</span>' for n, c in sc["key"])
    def encode(w): 
        return ' &nbsp; '.join(sc["l2n"][ch] for ch in w)
    l1blank = ' '.join('__' for _ in sc["line1"])
    l2words = sc["line2"].split()
    l2blank = ' &nbsp;&nbsp; '.join(' '.join('__' for _ in w) for w in l2words)
    l2nums = ' &nbsp;&nbsp; '.join(' '.join(sc["l2n"][ch] for ch in w) for w in l2words)
    A(page(T, 20, title("Crack the Secret Code", 22) + '  <span class="age">Ages 8&ndash;12</span>\n' +
      sub("Use the key to reveal the message") + divider() +
      instr("Each number stands for a letter. Write the letters to read the message!") +
      f'  <div class="bank" style="font-size:13pt;">{key}</div>\n' +
      f'  <p class="center" style="font-size:22pt; letter-spacing:8px; margin-top:12mm;">{l1blank}<br><span style="font-size:13pt; letter-spacing:4px;">{encode(sc["line1"])}</span></p>\n' +
      f'  <p class="center" style="font-size:22pt; letter-spacing:8px; margin-top:12mm;">{l2blank}<br><span style="font-size:13pt; letter-spacing:4px;">{l2nums}</span></p>\n' +
      f'  <p class="center small mt">Answers: line 1 = <strong>{esc(sc["line1"])}</strong> · line 2 = <strong>{esc(sc["line2"])}</strong></p>\n'))

    # 21–24 — COLOURING
    for i, cp in enumerate(b["colouring"]):
        A(page(T, 21 + i, title(cp["title"], 22) + sub(cp["sub"]) + divider() +
          art(f"p{21+i}-art") + f'  <p class="color-note">{esc(cp["note"])}</p>\n'))

    # 25 — COUNT & COLOUR
    A(page(T, 25, title("Count & Colour", 22) + '  <span class="age">Ages 4&ndash;7</span>\n' +
      sub(f'Count the {b["count_word"]}') + divider() +
      instr("Count each set, write the number in the box, and colour them in.") + art("p25-art")))

    # 26 — SPOT THE DIFFERENCE
    A(page(T, 26, title("Spot the Difference", 22) + sub("Find 5 differences") + divider() +
      instr("Look at the two pictures. Circle 5 things that are different in the second one.") +
      '  <div class="grid2">\n    <div class="art center" id="p26-a"><p class="small center">Picture 1</p></div>\n'
      '    <div class="art center" id="p26-b"><p class="small center">Picture 2</p></div>\n  </div>\n'))

    # 27 — MAZE
    A(page(T, 27, title(b["maze_title"], 22) + sub("Find the path through the maze") + divider() +
      instr(b["maze_instr"]) + '  <div class="art center" id="p27-art"></div>\n'))

    # 28 — DOT TO DOT
    A(page(T, 28, title("Dot to Dot", 22) + '  <span class="age">Ages 4&ndash;7</span>\n' +
      sub("Join the dots 1 to 12") + divider() +
      instr("Connect the dots in order, then colour the picture you made.") +
      '  <div class="art center" id="p28-art"></div>\n'))

    # 29 — LIVING IT OUT
    scen = ''
    for i, s in enumerate(b["scenarios"]):
        scen += f'  <div class="qwrap card"><p class="q">{i+1}. {esc(s["q"])}</p><p>{s["opts"]}</p></div>\n'
    A(page(T, 29, title("Living It Out", 22) + sub(b["apply_sub"]) + divider() +
      instr("Read each situation. Circle the choice that pleases God. Talk about it together.") +
      scen))

    # 30 — DRAMA / ACT IT OUT
    parts = ''.join(f'    <li>{esc(x)}</li>\n' for x in b["drama"])
    A(page(T, 30, title("Act It Out!", 22) + sub("Retell the story with a simple drama") + divider() +
      teacher("Give children simple roles and props. Acting the story helps them remember it.") +
      '  <h3 style="color:var(--primary); font-size:15pt;">Roles & steps</h3>\n' +
      f'  <ol class="list">\n{parts}  </ol>\n' + art("p30-art")))

    # 31 — GROUP GAME
    steps = ''.join(f'    <li>{esc(x)}</li>\n' for x in b["game_steps"])
    A(page(T, 31, title(b["game_title"], 22) + sub("A fun game for the whole group") + divider() +
      f'  <div class="aim"><b>You need:</b> {esc(b["game_need"])}</div>\n' +
      '  <h3 style="color:var(--primary); font-size:15pt;">How to play</h3>\n' +
      f'  <ol class="list">\n{steps}  </ol>\n' + teacher(b["game_tip"])))

    # 32 — CRAFT
    csteps = ''.join(f'    <li>{esc(x)}</li>\n' for x in b["craft_steps"])
    A(page(T, 32, title(b["craft_title"], 22) + sub(b["craft_sub"]) + divider() +
      f'  <div class="aim"><b>You need:</b> {esc(b["craft_need"])}</div>\n' +
      f'  <ol class="list">\n{csteps}  </ol>\n' + art("p32-art")))

    # 33 — CRAFT TEMPLATE
    A(page(T, 33, title(b["template_title"], 22) + sub("Cut along the lines") + divider() +
      '  <div class="art center" id="p33-art"></div>\n' +
      '  <p class="color-note">Adult help with scissors, please!</p>\n'))

    # 34 — SNACK + POSTER
    A(page(T, 34, title("Snack Idea & Memory Poster", 20) + divider() +
      f'  <div class="teacher"><b>Themed snack:</b> {esc(b["snack"])}</div>\n' +
      '  <div class="cert" style="border-color:var(--primary); padding:12mm;">\n'
      '    <div id="poster-art"></div>\n'
      f'    <p style="font-size:18pt; color:var(--deep); font-style:italic; margin-top:5mm;">&ldquo;{esc(v["text"])}&rdquo;</p>\n'
      f'    <p style="color:var(--gold); letter-spacing:2px; margin-top:3mm;">{esc(v["ref"].upper())}</p>\n  </div>\n'))

    # 35 — TAKE-HOME NOTE
    A(page(T, 35, title("Take-Home Note for Families", 20) + divider() +
      '  <div class="card" style="padding:16px;">\n'
      f'    <p class="story"><b>Dear family,</b> Today we learned about <b>{esc(b["short"])}</b>. {esc(b["takehome"])}</p>\n'
      f'    <p class="story"><b>This week at home:</b> {esc(b["home_activity"])}</p>\n'
      f'    <p class="story"><b>Memory verse:</b> &ldquo;{esc(v["text"])}&rdquo; — {esc(v["ref"])}</p>\n'
      '  </div>\n' +
      '  <h3 style="color:var(--primary); font-size:15pt; margin-top:8mm;">A prayer to pray together at home</h3>\n' +
      f'  <div class="verse" style="font-size:14pt;">{esc(b["family_prayer"])}</div>\n'))

    # 36 — DRAW YOUR FAVOURITE PART
    A(page(T, 36, title("My Favourite Part", 22) + sub("Draw and write") + divider() +
      '  <p class="q">Draw your favourite part of today\'s story:</p>\n'
      '  <div style="border:3px solid var(--primary); border-radius:14px; height:120mm; margin:6mm 0;"></div>\n'
      '  <p class="q">Why did you like it?</p>\n' + lines(2, True)))

    # 37 — WHAT I WILL DO
    A(page(T, 37, title("This Week I Will…", 22) + sub("Make a plan to live out the lesson") + divider() +
      instr("Write or draw one way you will live out today's lesson this week.") +
      f'  <div class="card q"><p class="q">One thing I will do: </p>{lines(2, True)}</div>\n'
      f'  <div class="card q mt"><p class="q">Someone I will show God\'s love to: </p>{lines(1, True)}</div>\n'
      f'  <div class="card q mt"><p class="q">I will thank God for: </p>{lines(1, True)}</div>\n'))

    # 38 — REVIEW
    lessons = b["three_lessons"]
    lc = ''.join(f'    <div class="card center"><strong style="color:{["var(--primary)","var(--coral)","var(--sky)"][i]};">{esc(l)}</strong></div>\n' for i, l in enumerate(lessons))
    A(page(T, 38, title("Let's Review!", 23) + divider() +
      f'  <p class="story center">{esc(b["review"])}</p>\n' +
      f'  <div class="grid3 mt">\n{lc}  </div>\n' + art("p38-art", "margin-top:6mm;") +
      '  <p class="center mt">Great work today! Turn the page to pray and finish.</p>\n'))

    # 39 — RESPONSE PRAYER
    A(page(T, 39, title("Closing Prayer", 22) + sub("Pray together to finish the lesson") + divider() +
      f'  <div class="verse" style="font-size:15pt;">{esc(b["closing_prayer"])}</div>\n' +
      instr("Now write your own short prayer to God.") + lines(4) + art("p39-art")))

    # 40 — WELL DONE
    A(page(T, 40, title("Well Done!", 24) + divider() +
      f'  <p class="story center">{esc(b["welldone"])}</p>\n' + art("p40-art", "margin-top:8mm;") +
      '  <p class="center mt">Turn the page for your special certificate!</p>\n'))

    # 41 — MEMORY VERSE BADGE
    A(page(T, 41, title("Memory Verse Badge", 22) + sub("Colour and wear it!") + divider() +
      '  <div class="grid2" style="gap:20px;">\n'
      '    <div style="border:3px solid var(--primary); border-radius:50%; padding:18px; text-align:center; aspect-ratio:1;">\n'
      '      <div id="badge-a"></div>\n'
      f'      <p style="color:var(--deep); font-weight:800; font-size:13pt;">I learned the verse!</p>\n'
      f'      <p class="small">{esc(v["ref"])}</p>\n    </div>\n'
      '    <div style="border:3px solid var(--coral); border-radius:50%; padding:18px; text-align:center; aspect-ratio:1;">\n'
      '      <div id="badge-b"></div>\n'
      f'      <p style="color:var(--coral); font-weight:800; font-size:13pt;">{esc(b["short"])}</p>\n'
      '      <p class="small">Sunday-School Star</p>\n    </div>\n  </div>\n'
      '  <p class="color-note mt">Cut out your badge and wear it with joy!</p>\n'))

    # 42 — CERTIFICATE
    A(page(T, 42, f'''  <div class="cert">
    <div id="cert-art"></div>
    <span class="badge" style="background:var(--gold);">Certificate of Completion</span>
    <h1 style="margin-top:6mm;">{esc(b["title"])}</h1>
    <p style="font-size:14pt; margin-top:8mm;">This certificate is proudly awarded to:</p>
    <div class="name-line"></div>
    <p style="font-size:13pt;">{esc(b["cert_line"])}</p>
    <div class="grid2 mt" style="margin-top:14mm;">
      <div><div style="border-bottom:2px solid var(--ink); margin:0 12%;"></div><p class="small">Date</p></div>
      <div><div style="border-bottom:2px solid var(--ink); margin:0 12%;"></div><p class="small">Teacher</p></div>
    </div>
    <p class="small" style="margin-top:10mm;">Written by {esc(AUTHOR)}</p>
  </div>'''))

    A(build_script(b))
    A('</body>\n</html>\n')
    return ''.join(P)



def build_script(b):
    icon = b["icon"]
    icon2 = b.get("icon2", icon)
    counts = b.get("count_sets", [2, 3, 1, 4])
    return f'''
<script src="../../assets/art.js"></script>
<script>
function put(id, svg){{ var el=document.getElementById(id); if(el) el.insertAdjacentHTML('beforeend', svg); }}
function repeat(fn,n,gap){{ var s='<div style="display:flex;justify-content:center;gap:'+(gap||10)+'px;flex-wrap:wrap;">'; for(var i=0;i<n;i++) s+=fn; return s+'</div>'; }}
var ICON='{icon}', ICON2='{icon2}';
function M(sz){{ return Art[ICON](sz); }}
function M2(sz){{ return Art[ICON2](sz); }}

put('cover-art', M(300));
put('p2-art', Art.cross(120));
put('p3-art', M(240));
put('p5-art', M2(200));
put('p6-art', M(200)); put('p7-art', M2(200)); put('p8-art', M(200)); put('p9-art', M2(200));
put('p10-art', Art.star(40)+Art.heart(50)+Art.star(40));
put('p12-art', M(150));
put('p21-art', M(360)); put('p22-art', M2(360)); put('p23-art', M(360)); put('p24-art', M2(340));
put('p30-art', M(180));
put('p32-art', M(200));
put('poster-art', M(150));
put('p38-art', M(200)); put('p39-art', Art.heart(70)); put('p40-art', M(220));
put('badge-a', Art.star(90)); put('badge-b', M(120));
put('cert-art', M(150));

/* Count & colour */
(function(){{
  var rows={json.dumps(counts)}, html='';
  rows.forEach(function(n){{
    html+='<div style="display:flex;align-items:center;gap:14px;margin:8px 0;border:2px solid #e0a327;border-radius:12px;padding:8px;">';
    html+= repeat(M(80), n, 8);
    html+='<div style="margin-left:auto;width:56px;height:56px;border:2px solid #2e7d5b;border-radius:10px;"></div></div>';
  }});
  put('p25-art', html);
}})();

/* Spot the difference */
put('p26-a', M(220)); put('p26-b', M(220));

/* Craft template — generic band */
put('p33-art', (function(){{
  var S='fill="none" stroke="#2b2b2b" stroke-width="3" stroke-linejoin="round"';
  var inner='<rect '+S+' x="20" y="30" width="450" height="120" rx="12"/>';
  inner+='<path stroke-dasharray="6 6" '+S+' d="M20 90 h450"/>';
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
  var h='';
  for(var r3=0;r3<N;r3++){{h+='<tr>';for(var c3=0;c3<N;c3++)h+='<td>'+grid[r3][c3]+'</td>';h+='</tr>';}}
  var t=document.getElementById('ws-table'); if(t) t.innerHTML=h;
  var bk=document.getElementById('ws-bank'); if(bk) bk.innerHTML=words.map(function(w){{return '<span>'+w+'</span>';}}).join('');
}})();

/* Crossword */
(function(){{
  var cw=window.CW; if(!cw) return;
  var N=cw.grid, g=[]; for(var r=0;r<N;r++){{g[r]=[];for(var c=0;c<N;c++)g[r][c]={{ch:null,num:0}};}}
  function across(w,r,c){{for(var i=0;i<w.length;i++)g[r][c+i].ch=w[i];}}
  function down(w,r,c){{for(var i=0;i<w.length;i++)g[r+i][c].ch=w[i];}}
  down(cw.spine.word, cw.spine.r, cw.spine.c); g[cw.spine.r][cw.spine.c].num=1;
  cw.cross.forEach(function(x){{ across(x.word, x.r, x.c); g[x.r][x.c].num=x.num; }});
  var h='';
  for(var r2=0;r2<N;r2++){{h+='<tr>';for(var c2=0;c2<N;c2++){{var cell=g[r2][c2];
    if(cell.ch===null) h+='<td class="blk"></td>'; else h+='<td>'+(cell.num?cell.num:'')+'</td>';
  }}h+='</tr>';}}
  var t=document.getElementById('cw-table'); if(t) t.innerHTML=h;
}})();

/* Maze */
put('p27-art',(function(){{
  var s='fill="none" stroke="#2b2b2b" stroke-width="3" stroke-linecap="round"';
  var inner='<rect x="10" y="10" width="380" height="380" '+s+'/>';
  ['M10 90 h300','M390 90 h-300','M90 90 v230','M90 320 h230','M170 10 v230','M170 240 h150','M250 90 v170','M330 170 v220','M250 320 h80','M10 240 h100'].forEach(function(w){{inner+='<path '+s+' d="'+w+'"/>';}});
  inner+='<text x="20" y="40" font-size="15" fill="#2e7d5b">START</text><text x="300" y="382" font-size="15" fill="#e8664e">END</text>';
  return '<svg viewBox="0 0 400 400" width="400" height="400" xmlns="http://www.w3.org/2000/svg">'+inner+'</svg>';
}})());

/* Dot to dot */
put('p28-art',(function(){{
  var pts=[[60,180],[90,120],[130,150],[150,90],[170,150],[210,120],[240,180],[240,220],[60,220],[60,180]];
  var inner='';
  pts.forEach(function(p,i){{ inner+='<circle cx="'+p[0]+'" cy="'+p[1]+'" r="4" fill="#2b2b2b"/>'; if(i<7) inner+='<text x="'+(p[0]+6)+'" y="'+(p[1]-6)+'" font-size="14" fill="#2e7d5b">'+(i+1)+'</text>'; }});
  [[90,200,8],[130,200,9],[150,200,10],[170,200,11],[210,200,12]].forEach(function(p){{inner+='<circle cx="'+p[0]+'" cy="'+p[1]+'" r="4" fill="#2b2b2b"/><text x="'+(p[0]+6)+'" y="'+(p[1]+16)+'" font-size="14" fill="#e8664e">'+p[2]+'</text>';}});
  return '<svg viewBox="0 0 300 260" width="300" height="260" xmlns="http://www.w3.org/2000/svg">'+inner+'</svg>';
}})());
</script>
'''


def make_crossword(spine, crossers, grid=13):
    spine = spine.upper()
    crossers = [w.upper() for w in crossers]
    spine_col = grid // 2
    spine_r = max(1, (grid - len(spine)) // 2)

    def options(w):
        opts = []
        for si in range(len(spine)):
            for wi in range(len(w)):
                if w[wi] == spine[si]:
                    sc = spine_col - wi
                    if 0 <= sc and sc + len(w) <= grid:
                        opts.append((si, sc))
        return opts

    placements, used = {}, set()

    def solve(i):
        if i == len(crossers):
            return True
        for (si, sc) in options(crossers[i]):
            row = spine_r + si
            if row in used:
                continue
            used.add(row); placements[i] = (row, sc)
            if solve(i + 1):
                return True
            used.discard(row); del placements[i]
        return False

    if not solve(0):
        raise ValueError(f"Crossword could not interlock {crossers} on '{spine}'")
    cross = [{"word": crossers[i], "r": placements[i][0], "c": placements[i][1], "num": i + 2}
             for i in range(len(crossers))]
    return {"grid": grid, "spine": {"word": spine, "r": spine_r, "c": spine_col}, "cross": cross}


def main():
    from lesson_data import BOOKS
    made = []
    for b in BOOKS:
        cw = b["crossword"]
        cw["words"] = make_crossword(cw["spine"], cw["crossers"], cw.get("grid", 13))
        out_dir = os.path.join(ROOT, "books", b["slug"])
        os.makedirs(out_dir, exist_ok=True)
        s = build_book(b)
        with open(os.path.join(out_dir, "index.html"), "w", encoding="utf-8") as f:
            f.write(s)
        n = s.count('class="page"')
        made.append((b["slug"], n))
        print(f"  ✓ {b['slug']:26s} — {n} pages")
    print(f"\nGenerated {len(made)} lesson pack(s).")


if __name__ == "__main__":
    main()
