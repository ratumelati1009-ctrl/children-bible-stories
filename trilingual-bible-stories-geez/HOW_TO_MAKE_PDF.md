# 📄 How to Make the PDF (with perfect Ge'ez/Fidel text)

The storybook contains **Ethiopic (Fidel) script** for Tigrinya, Amharic, and Ge'ez.
A PDF will only show that text correctly if an **Ethiopic font is available**.
This sandbox has no Ethiopic font and no internet to fetch one, so the PDF must be
generated on a machine that has one (any normal computer, or a free online tool).

The layout, design, and English text are already 100% finished in
`Trilingual_Bible_Stories_for_Kids.html`.

---

## ✅ Easiest way (no installs) — Print from a browser
1. Open `Trilingual_Bible_Stories_for_Kids.html` in **Chrome, Edge, or Firefox**.
   (These auto-download the Ethiopic font from Google Fonts when you're online — the
   HTML already links it.)
2. Confirm the Amharic/Tigrinya/Ge'ez text shows as **real letters, not boxes**.
3. Press **Ctrl+P** (or Cmd+P on Mac) → **Destination: Save as PDF** →
   enable **"Background graphics"** → Save.

That's it — you get a clean, print-ready PDF.

---

## 🖥️ One-command way (on your computer) — using the included script
Requires an Ethiopic font installed on your system. Free options:
- **Noto Serif Ethiopic** — https://fonts.google.com/noto/specimen/Noto+Serif+Ethiopic (click "Get font")
- **Abyssinica SIL** — https://software.sil.org/abyssinica/
- Windows already includes **Nyala**; macOS already includes **Kefa**.

Then run either:

**Option A — Chromium/Chrome (best quality):**
```bash
python3 make_pdf.py
```
This auto-detects Chrome/Playwright/wkhtmltopdf/WeasyPrint/LibreOffice and uses whichever you have.

**Option B — wkhtmltopdf directly:**
```bash
wkhtmltopdf --enable-local-file-access \
  Trilingual_Bible_Stories_for_Kids.html \
  Trilingual_Bible_Stories_for_Kids.pdf
```

**Option C — WeasyPrint (pip install weasyprint):**
```bash
weasyprint Trilingual_Bible_Stories_for_Kids.html Trilingual_Bible_Stories_for_Kids.pdf
```

---

## 🌐 No computer setup? Use a free online converter
Upload `Trilingual_Bible_Stories_for_Kids.html` to any HTML→PDF service
(these have Ethiopic fonts server-side). Search "HTML to PDF converter".

---

## ⚠️ Always verify before publishing
Open the finished PDF and check that **every** Amharic, Tigrinya, and Ge'ez line
shows real letters — **not empty boxes (□□□)**. If you see boxes, the machine that
made the PDF was missing the Ethiopic font; install one (above) and remake it.

For a book you're selling, also embed the font in the PDF so it displays on every
device — Chrome's "Save as PDF" and wkhtmltopdf both embed fonts automatically.
