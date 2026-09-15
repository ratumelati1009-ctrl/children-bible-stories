# English–Tigrigna Bible Activity Books

Printable, bilingual (English &ndash; ትግርኛ) Bible activity packs for children **ages 4&ndash;12**.
Each book is A4, print-ready (one activity per page), with line-art coloring illustrations,
a Bible story, memory verse (ICB), comprehension, puzzles, crafts, prayer, and a completion certificate.

**Series written by Daniel Tesfamariam · ብዳንኤል ተስፋማርያም**

## 📚 Books — all 10 ready (42 pages each)

| # | Title | Tigrigna | PDF |
|---|-------|----------|-----|
| 1 | Esther's Brave Choice | ጅግንነት ኣስቴር | `pdf/01-Esthers-Brave-Choice.pdf` |
| 2 | Daniel and the Lions' Den | ዳንኤልን ጉድጓድ ኣናብስን | `pdf/02-Daniel-and-the-Lions-Den.pdf` |
| 3 | David and Goliath | ዳዊትን ጎልያድን | `pdf/03-David-and-Goliath.pdf` |
| 4 | Noah's Ark | መርከብ ኖህ | `pdf/04-Noahs-Ark.pdf` |
| 5 | Jonah and the Big Fish | ዮናስን እታ ዓባይ ዓሳን | `pdf/05-Jonah-and-the-Big-Fish.pdf` |
| 6 | Joseph's Amazing Journey | ዜደንቕ ጕዕዞ ዮሴፍ | `pdf/06-Josephs-Amazing-Journey.pdf` |
| 7 | Moses and the Red Sea | ሙሴን ቀይሕ ባሕርን | `pdf/07-Moses-and-the-Red-Sea.pdf` |
| 8 | The Good Samaritan | እቲ ሕያዋይ ሳምራዊ | `pdf/08-The-Good-Samaritan.pdf` |
| 9 | Jesus Feeds the Five Thousand | የሱስ ንሓሙሽተ ሽሕ መገበ | `pdf/09-Jesus-Feeds-the-Five-Thousand.pdf` |
| 10 | The Lost Sheep | እታ ዝጠፍአት በጊዕ | `pdf/10-The-Lost-Sheep.pdf` |

## 📂 Structure

```
english-tigrigna-activity-books/
├── index.html               # Landing page linking every book + PDF
├── generate_books.py        # Generator: builds each 42-page book from data
├── book_data.py             # Story + activity data for Books 2–10
├── assets/
│   ├── book.css             # Shared print stylesheet (A4, Ethiopic font)
│   └── art.js               # Reusable line-art SVG illustrations
├── books/<nn>-<slug>/index.html   # Editable HTML source for each book
└── pdf/<Title>.pdf                # Ready-to-print PDF for each book
```

## 🔧 Regenerating

```
python3 generate_books.py     # rewrites books/*/index.html from book_data.py
```
Then print each `index.html` to PDF (A4, no margins), or use Chrome headless:
```
chrome --headless --no-pdf-header-footer --print-to-pdf=out.pdf file:///.../index.html
```
Tigrigna renders with **Noto Serif Ethiopic** (SIL OFL); the PDFs embed the font.

## 🖨️ How to print / export

- **Use the PDF** in `pdf/` — already generated, A4, with the Tigrigna (Ge'ez) font embedded.
- **Or from the HTML:** open a book's `index.html` in a browser and click **🖨️ Print / Save PDF**
  (or Ctrl/Cmd + P). Choose *Save as PDF*, paper **A4**, margins **None**.

## ✍️ Fonts & credits

- Tigrigna renders in **Noto Serif Ethiopic** (SIL Open Font License) for offline PDFs,
  with **Noto Sans Ethiopic** loaded online.
- Memory verses are based on the **International Children's Bible (ICB)**.

## ⚠️ Translation note

The Tigrigna (ትግርኛ) text was prepared with care but has **not yet been checked by a
professional native-speaker translator**. Please have it proofread by a fluent native
speaker before selling, publishing, or widely distributing these materials.
