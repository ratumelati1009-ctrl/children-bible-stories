# Christian Sunday-School Activity Books

Complete, print-ready Sunday-school **lesson packs** for children **ages 4&ndash;12**.
Each book is A4 (one section per page) with everything a teacher or family needs for a session:
lesson aim, teacher prep, opening prayer, the Bible story, memory verse (ICB), discussion,
comprehension, puzzles, colouring, "Living It Out" scenarios, a drama, a group game, a craft,
snack idea, a take-home note for families, review, closing prayer, and a completion certificate.

**Series written by Daniel Tesfamariam**

## 📚 Books — all 10 ready (42 pages each)

| # | Title | Theme | PDF |
|---|-------|-------|-----|
| 1 | Esther's Brave Choice | Courage & Faith | `pdf/01-Esther-Brave-Choice-Sunday-School.pdf` |
| 2 | Daniel and the Lions' Den | Prayer & Faith | `pdf/02-Daniel-and-the-Lions-Den-Sunday-School.pdf` |
| 3 | David and Goliath | Courage & God's Strength | `pdf/03-David-and-Goliath-Sunday-School.pdf` |
| 4 | Noah's Ark | Obedience & God's Promises | `pdf/04-Noahs-Ark-Sunday-School.pdf` |
| 5 | Jonah's Big Adventure | Obedience & Second Chances | `pdf/05-Jonahs-Big-Adventure-Sunday-School.pdf` |
| 6 | Joseph Forgives His Brothers | Forgiveness & God's Plan | `pdf/06-Joseph-Forgives-His-Brothers.pdf` |
| 7 | Moses and the Ten Commandments | God's Good Rules | `pdf/07-Moses-and-the-Ten-Commandments.pdf` |
| 8 | The Good Samaritan | Kindness & Loving Others | `pdf/08-The-Good-Samaritan-Kindness.pdf` |
| 9 | Jesus Loves Children | Jesus' Love for You | `pdf/09-Jesus-Loves-Children.pdf` |
| 10 | The Armor of God | Standing Strong in Faith | `pdf/10-The-Armor-of-God-Sunday-School.pdf` |

## 📂 Structure

```
sunday-school/
├── index.html               # Landing page linking every book + PDF
├── generate_lessons.py      # Generator: builds each 42-page lesson pack
├── lesson_data.py           # Lesson content for all 10 books
├── assets/
│   ├── lesson.css           # Shared print stylesheet (A4, green theme)
│   └── art.js               # Reusable line-art SVG illustrations
├── books/<nn>-<slug>/index.html   # Editable HTML source for each book
└── pdf/<Title>.pdf                # Ready-to-print PDF for each book
```

## 🔧 Regenerating

```
python3 generate_lessons.py     # rewrites books/*/index.html from lesson_data.py
```
Then print each `index.html` to PDF (A4, no margins), or use Chrome headless:
```
chrome --headless --no-pdf-header-footer --print-to-pdf=out.pdf file:///.../index.html
```

Memory verses are based on the **International Children's Bible (ICB)**.
