# 📚 10 New Trilingual Bible Story Books (English • ትግርኛ • አማርኛ)

Ten brand-new children's Bible story books (ages 6–13), in the same trilingual
format as the original `trilingual_books` set. Each book has a decorated cover
plus 12 stories. Every story page shows:

- ✝️ Bible verse reference
- 🖼️ A simple illustration
- 📖 The story in **English**, **ትግርኛ (Tigrinya)**, and **አማርኛ (Amharic)**
- 💡 A LESSON / ትምህርቲ / ትምህርት in all three languages

The Ethiopic (Fidel) font is embedded in every HTML/PDF, so the Tigrinya and
Amharic text displays correctly on any device without needing a special font.

## The 10 Books

| # | Title | ትግርኛ | Stories | PDF |
|---|-------|------|:-------:|-----|
| 1 | The Psalms for Little Hearts | መዝሙራት ንንኣሽቱ ልቢ | 12 | `01_psalms_for_little_hearts.pdf` |
| 2 | Wisdom of Proverbs | ጥበብ ምሳሌታት | 12 | `02_wisdom_of_proverbs.pdf` |
| 3 | The Kings of Israel | ነገስታት እስራኤል | 12 | `03_kings_of_israel.pdf` |
| 4 | The Prophets Speak | ነብያት ይዛረቡ | 12 | `04_the_prophets_speak.pdf` |
| 5 | Women of the Bible | ኣንስቲ መጽሓፍ ቅዱስ | 12 | `05_women_of_the_bible.pdf` |
| 6 | Miracles of Jesus | ተኣምራት የሱስ | 12 | `06_miracles_of_jesus.pdf` |
| 7 | More Parables of Jesus | ተወሰኽቲ ምሳሌታት የሱስ | 12 | `07_more_parables_of_jesus.pdf` |
| 8 | The Apostles and the Early Church | ሃዋርያትን ቀዳመይቲ ቤተ ክርስትያንን | 12 | `08_the_apostles.pdf` |
| 9 | The Exodus Journey | ጕዕዞ ናይ ወጻእ | 12 | `09_the_exodus_journey.pdf` |
| 10 | Angels and God's Messengers | መላእኽትን መልእኽተኛታት ኣምላኽን | 12 | `10_angels_and_gods_messengers.pdf` |

**120 stories in total.** None of these stories duplicate the stories in the
original four books (Creation, Heroes of Faith, Life of Jesus, Teachings &
Early Church) or the 20 virtue books.

## How to Regenerate

```bash
python3 generate_new_books.py
```

- `generate_new_books.py` — the rendering engine (embeds the font, builds each
  page, and calls headless Chrome to print the PDF).
- `books_data.py` — all the story content (titles, text, lessons in 3 languages).
- `eth_font.ttf` — the embedded Noto Sans Ethiopic font.

## Note on the Translations

The Tigrinya and Amharic text is a strong first draft. For a polished,
publish-ready product, have a native speaker review the translations before
printing or selling.
