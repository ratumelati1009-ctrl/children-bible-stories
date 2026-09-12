#!/usr/bin/env python3
"""
Convert the trilingual storybook HTML into a PDF.

The book contains Ethiopic (Fidel) script for Tigrinya, Amharic, and Ge'ez.
For the PDF to render correctly you MUST have an Ethiopic font installed, e.g.:
  - "Noto Serif Ethiopic" / "Noto Sans Ethiopic"  (free: https://fonts.google.com/noto/specimen/Noto+Serif+Ethiopic)
  - "Abyssinica SIL"  (free: https://software.sil.org/abyssinica/)
  - "Nyala" (ships with Windows), "Kefa" (ships with macOS)

This script tries several engines in order and uses whichever is available:
  1. Playwright (Chromium)   -> best quality, uses system fonts
  2. wkhtmltopdf
  3. weasyprint
  4. LibreOffice (soffice)

Usage:
    python3 make_pdf.py
"""
import shutil
import subprocess
import sys
import pathlib

HERE = pathlib.Path(__file__).parent
HTML = HERE / "Trilingual_Bible_Stories_for_Kids.html"
PDF = HERE / "Trilingual_Bible_Stories_for_Kids.pdf"


def try_playwright() -> bool:
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        return False
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            page.goto(HTML.resolve().as_uri(), wait_until="networkidle")
            page.pdf(
                path=str(PDF),
                format="A4",
                print_background=True,
                margin={"top": "14mm", "bottom": "16mm", "left": "12mm", "right": "12mm"},
            )
            browser.close()
        return True
    except Exception as e:
        print(f"  playwright failed: {e}")
        return False


def try_chromium_cli() -> bool:
    """Use a headless Chrome/Chromium binary directly (no python bindings needed)."""
    candidates = [
        "google-chrome", "chromium", "chromium-browser", "chrome",
        "/usr/local/bin/chrome",
        "/opt/playwright/chromium-1232/chrome-linux64/chrome",
    ]
    binary = next((c for c in candidates if shutil.which(c) or pathlib.Path(c).exists()), None)
    if not binary:
        return False
    try:
        subprocess.run(
            [binary, "--headless=new", "--no-sandbox", "--disable-gpu",
             f"--print-to-pdf={PDF}", "--no-pdf-header-footer",
             HTML.resolve().as_uri()],
            check=True, capture_output=True, timeout=120,
        )
        return PDF.exists() and PDF.stat().st_size > 0
    except Exception as e:
        print(f"  chromium cli failed: {e}")
        return False


def try_wkhtmltopdf() -> bool:
    if not shutil.which("wkhtmltopdf"):
        return False
    try:
        subprocess.run(["wkhtmltopdf", "--enable-local-file-access",
                        str(HTML), str(PDF)], check=True, capture_output=True)
        return True
    except Exception as e:
        print(f"  wkhtmltopdf failed: {e}")
        return False


def try_weasyprint() -> bool:
    try:
        from weasyprint import HTML as WHTML
    except ImportError:
        return False
    try:
        WHTML(filename=str(HTML)).write_pdf(str(PDF))
        return True
    except Exception as e:
        print(f"  weasyprint failed: {e}")
        return False


def try_libreoffice() -> bool:
    binary = next((c for c in ("libreoffice", "soffice") if shutil.which(c)), None)
    if not binary:
        return False
    try:
        subprocess.run([binary, "--headless", "--convert-to", "pdf",
                        "--outdir", str(HERE), str(HTML)],
                       check=True, capture_output=True, timeout=120)
        return PDF.exists()
    except Exception as e:
        print(f"  libreoffice failed: {e}")
        return False


def main():
    if not HTML.exists():
        sys.exit(f"Missing {HTML}. Run build_html.py first.")

    engines = [
        ("Playwright/Chromium", try_playwright),
        ("Chromium CLI", try_chromium_cli),
        ("wkhtmltopdf", try_wkhtmltopdf),
        ("WeasyPrint", try_weasyprint),
        ("LibreOffice", try_libreoffice),
    ]
    for name, fn in engines:
        print(f"Trying {name}...")
        if fn():
            print(f"\n✅ PDF created with {name}: {PDF}")
            print("   ⚠️  Open it and confirm the Amharic/Tigrinya/Ge'ez text is")
            print("       readable (not empty boxes). If you see boxes, install an")
            print("       Ethiopic font (Noto Serif Ethiopic / Abyssinica SIL) and re-run.")
            return
    sys.exit("\n❌ No PDF engine available. Install one of: playwright, "
             "wkhtmltopdf, weasyprint, or LibreOffice — or open the HTML in a "
             "browser and use Print → Save as PDF.")


if __name__ == "__main__":
    main()
