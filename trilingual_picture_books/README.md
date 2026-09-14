# Trilingual Bible Picture Books — 10 Books, Each 42+ Pages

Ten full-length **children's picture books**, one per Bible story. Each book tells the
story **one scene per page** — a big illustration with short, easy text — in three languages:

- **English**
- **ትግርኛ (Tigrinya)** — Geʼez / Fidel script
- **አማርኛ (Amharic)** — Geʼez / Fidel script

The Ethiopic font (**Noto Sans Ethiopic**) is embedded in every PDF, so the Fidel text
displays correctly on any device.

## The 10 books

| # | Title | Pages |
|---|-------|-------|
| 01 | Noah Builds the Ark | 45 |
| 02 | Joseph and His Colorful Coat | 45 |
| 03 | Baby Moses in the Basket | 45 |
| 04 | David and the Giant | 45 |
| 05 | Daniel in the Lions' Den | 45 |
| 06 | Jonah and the Big Fish | 45 |
| 07 | The Good Samaritan | 45 |
| 08 | The Lost Sheep | 44 |
| 09 | Zacchaeus in the Tree | 45 |
| 10 | Jesus Blesses the Children | 44 |

**Every book has more than 42 pages** (cover + 43–44 scene pages).

Each scene page has: a large colorful illustration, the sentence in English, Tigrinya, and
Amharic, the Bible verse reference, a scene counter, and a page number.

## Files

- `NN_<title>.pdf` — the ten print-ready picture books
- `NN_<title>.html` — source HTML for each book (viewable in a browser)
- `scenes_data.py` — all the story text (10 books × ~44 scenes, in three languages)
- `generate_picture_books.py` — the generator that builds the HTML + PDFs
- `eth_font.ttf` — the embedded Ethiopic (Fidel) font

## Regenerate all PDFs

```bash
python3 generate_picture_books.py
```

## About the illustrations

The pictures are simple, friendly built-in drawings (SVG). To keep the books long,
illustrations are reused across scenes within a book. The text is original and written
fresh for every page. If you want unique artwork on each page for a premium printed edition,
you would use a human illustrator or an image-generation tool for the pictures.

## ⚠️ Note about the translations

The Tigrinya and Amharic text is a careful draft. Before printing or selling commercially,
please have a **native Tigrinya and Amharic speaker** proofread the text for final polish.
