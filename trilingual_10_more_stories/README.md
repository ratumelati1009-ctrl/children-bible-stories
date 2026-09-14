# Ten More Bible Stories — Trilingual Children's Storybook

A new illustrated storybook with **10 more Bible stories** for children, each written in
three languages:

- **English**
- **ትግርኛ (Tigrinya)** — Geʼez / Fidel script
- **አማርኛ (Amharic)** — Geʼez / Fidel script

The Ethiopic font (**Noto Sans Ethiopic**) is embedded in the PDF, so the Fidel text
displays correctly on any device.

## The 10 stories

1. Noah Builds the Ark
2. Joseph and His Colorful Coat
3. Baby Moses in the Basket
4. David and the Giant
5. Daniel in the Lions' Den
6. Jonah and the Big Fish
7. The Good Samaritan
8. The Lost Sheep
9. Zacchaeus in the Tree
10. Jesus Blesses the Children

Total: **11 pages** (cover + 10 story pages).

Each story page has the title in all three languages, a Bible verse reference, the story
text in English/Tigrinya/Amharic, a colorful illustration, and a short "lesson" line.

## Files

- `01_ten_more_bible_stories.pdf` — ready to print / read
- `01_ten_more_bible_stories.html` — source HTML (also viewable in a browser)
- `books_data_10_more.py` — the story content (all three languages)
- `generate_book.py` — the generator that builds the HTML + PDF
- `eth_font.ttf` — the embedded Ethiopic (Fidel) font

## Regenerate the PDF

```bash
python3 generate_book.py
```

## ⚠️ Note about the translations

The Tigrinya and Amharic text is a careful draft. Before printing or selling commercially,
have a **native Tigrinya and Amharic speaker** proofread the text for final polish.
