# Large Trilingual Children's Bible Storybooks (45–46 pages each)

Two big trilingual illustrated Bible storybooks for children, each with **more than 42 pages**.
Every story is written in three languages:

- **English**
- **ትግርኛ (Tigrinya)** — in Geʼez / Fidel script
- **አማርኛ (Amharic)** — in Geʼez / Fidel script

The Ethiopic font (**Noto Sans Ethiopic**) is embedded directly in each PDF, so the Fidel
text displays correctly on any device without needing extra fonts installed.

## The books

| # | Title | Stories | Pages |
|---|-------|---------|-------|
| 01 | **The Big Story of the Bible** — from Creation to the New Heaven | 45 | 46 |
| 02 | **Jesus, Friend of All** — the life, love, and miracles of Jesus | 44 | 45 |

Total: **89 illustrated Bible stories** across 2 books.

Each page contains:
- Story title in all three languages
- A Bible verse reference
- The full story in English, Tigrinya, and Amharic
- A short "moral / lesson" line in all three languages
- A simple, colorful illustration

## Files

- `01_the_big_story_of_the_bible.pdf` — ready to print / read (≈2.1 MB)
- `02_jesus_friend_of_all.pdf` — ready to print / read (≈2.1 MB)
- `*.html` — the source HTML for each book (also viewable in a browser)
- `books_data_large.py` — the story content (all three languages)
- `generate_large_books.py` — the generator that builds HTML + PDF
- `eth_font.ttf` — the embedded Ethiopic (Fidel) font

## Regenerating the PDFs

```bash
python3 generate_large_books.py
```

## ⚠️ Important note about the translations

The Tigrinya and Amharic text is a **strong, careful draft**, but before you sell or print
these books commercially I strongly recommend having a **native Tigrinya and Amharic speaker
review and proofread** the text. Small wording and grammar refinements from a native speaker
will make the books feel truly polished to your customers.
