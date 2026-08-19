#!/usr/bin/env python3
"""
PDF Engine - Core PDF generation library (no external dependencies).
Generates professional workbook-style PDFs with headers, footers, 
structured content, checkboxes, lined pages, and decorative elements.
"""


class PDFEngine:
    """Low-level PDF generator using raw PDF specification."""

    def __init__(self, title="Workbook", author=""):
        self.title = title
        self.author = author
        self.pages = []
        self.current_page_content = []
        self.page_height = 792  # Letter (11in)
        self.page_width = 612  # Letter (8.5in)
        self.margin_left = 55
        self.margin_right = 55
        self.margin_top = 65
        self.margin_bottom = 60
        self.y_position = self.page_height - self.margin_top
        self.content_width = self.page_width - self.margin_left - self.margin_right
        self.page_number = 0
        self.show_page_numbers = True
        self.header_text = ""
        self.footer_text = ""

    def _escape(self, text):
        """Escape special PDF characters and remove non-ASCII."""
        text = text.replace('\\', '\\\\')
        text = text.replace('(', '\\(')
        text = text.replace(')', '\\)')
        result = ''
        for ch in text:
            if ord(ch) < 128:
                result += ch
            elif ch in '\u2014\u2013':
                result += '-'
            elif ch in '\u201c\u201d\u2018\u2019':
                result += '"' if ch in '\u201c\u201d' else "'"
            elif ch == '\u2026':
                result += '...'
            elif ch == '\u2022':
                result += '*'
            else:
                result += ' '
        return result

    def _wrap_text(self, text, max_chars=88):
        """Word-wrap text."""
        words = text.split()
        lines = []
        current = ''
        for word in words:
            if len(current) + len(word) + 1 <= max_chars:
                current = current + ' ' + word if current else word
            else:
                if current:
                    lines.append(current)
                current = word
        if current:
            lines.append(current)
        return lines if lines else ['']

    def _check_page_break(self, needed=20):
        """Check if page break needed."""
        if self.y_position - needed < self.margin_bottom:
            self.end_page()
            self.start_page()

    def start_page(self):
        """Start a new page."""
        self.current_page_content = []
        self.y_position = self.page_height - self.margin_top
        self.page_number += 1

        # Add header if set
        if self.header_text and self.page_number > 1:
            self.current_page_content.append(
                f'BT\n0.5 0.5 0.5 rg\n/F1 8 Tf\n{self.margin_left} {self.page_height - 35} Td\n({self._escape(self.header_text)}) Tj\nET'
            )

    def end_page(self):
        """End current page and add footer."""
        if self.show_page_numbers and self.page_number > 0:
            # Page number centered at bottom
            page_str = f'- {self.page_number} -'
            self.current_page_content.append(
                f'BT\n0.4 0.4 0.4 rg\n/F1 9 Tf\n280 30 Td\n({page_str}) Tj\nET'
            )
        if self.footer_text:
            self.current_page_content.append(
                f'BT\n0.5 0.5 0.5 rg\n/F1 7 Tf\n{self.margin_left} 30 Td\n({self._escape(self.footer_text)}) Tj\nET'
            )
        self.pages.append(self.current_page_content[:])
        self.current_page_content = []

    def add_text(self, text, size=11, bold=False, italic=False, indent=0, color=(0, 0, 0), align='left'):
        """Add a line of text."""
        font = '/F2' if bold else ('/F3' if italic else '/F1')
        r, g, b = [c / 255.0 for c in color]
        x = self.margin_left + indent

        if align == 'center':
            approx_width = len(text) * size * 0.45
            x = (self.page_width - approx_width) / 2
        elif align == 'right':
            approx_width = len(text) * size * 0.45
            x = self.page_width - self.margin_right - approx_width

        self.current_page_content.append(
            f'BT\n{r:.3f} {g:.3f} {b:.3f} rg\n{font} {size} Tf\n{x:.1f} {self.y_position:.1f} Td\n({self._escape(text)}) Tj\nET'
        )
        self.y_position -= size * 1.4

    def add_wrapped_text(self, text, size=11, bold=False, italic=False, indent=0, color=(0, 0, 0), max_chars=88, spacing=1.4):
        """Add word-wrapped text."""
        adjusted = max_chars - int(indent / 5.5)
        lines = self._wrap_text(text, adjusted)
        for line in lines:
            self._check_page_break(size * spacing + 2)
            font = '/F2' if bold else ('/F3' if italic else '/F1')
            r, g, b = [c / 255.0 for c in color]
            x = self.margin_left + indent
            self.current_page_content.append(
                f'BT\n{r:.3f} {g:.3f} {b:.3f} rg\n{font} {size} Tf\n{x:.1f} {self.y_position:.1f} Td\n({self._escape(line)}) Tj\nET'
            )
            self.y_position -= size * spacing

    def add_space(self, points=12):
        """Add vertical space."""
        self.y_position -= points

    def add_line(self, thickness=0.5, color=(0.7, 0.7, 0.7), indent=0, width=None):
        """Add a horizontal line."""
        x1 = self.margin_left + indent
        x2 = (self.margin_left + (width if width else self.content_width))
        r, g, b = color
        self.current_page_content.append(
            f'{r:.3f} {g:.3f} {b:.3f} RG\n{thickness} w\n{x1:.1f} {self.y_position:.1f} m\n{x2:.1f} {self.y_position:.1f} l\nS'
        )
        self.y_position -= 8

    def add_rect(self, x, y, w, h, fill_color=None, stroke_color=None, stroke_width=0.5):
        """Add a rectangle."""
        cmds = ''
        if fill_color:
            r, g, b = fill_color
            cmds += f'{r:.3f} {g:.3f} {b:.3f} rg\n'
        if stroke_color:
            r, g, b = stroke_color
            cmds += f'{r:.3f} {g:.3f} {b:.3f} RG\n'
        cmds += f'{stroke_width} w\n{x:.1f} {y:.1f} {w:.1f} {h:.1f} re\n'
        if fill_color and stroke_color:
            cmds += 'B'
        elif fill_color:
            cmds += 'f'
        else:
            cmds += 'S'
        self.current_page_content.append(cmds)

    def add_checkbox(self, text, size=11, indent=0):
        """Add a checkbox with text."""
        self._check_page_break(size * 1.6)
        x = self.margin_left + indent
        # Draw checkbox square
        box_size = size * 0.8
        box_y = self.y_position - 2
        self.current_page_content.append(
            f'0.3 0.3 0.3 RG\n0.5 w\n{x:.1f} {box_y:.1f} {box_size:.1f} {box_size:.1f} re\nS'
        )
        # Add text after checkbox
        text_x = x + box_size + 6
        self.current_page_content.append(
            f'BT\n0.1 0.1 0.1 rg\n/F1 {size} Tf\n{text_x:.1f} {self.y_position:.1f} Td\n({self._escape(text)}) Tj\nET'
        )
        self.y_position -= size * 1.6

    def add_lined_space(self, num_lines=5, spacing=22, indent=0):
        """Add lined writing space."""
        for i in range(num_lines):
            self._check_page_break(spacing + 2)
            x1 = self.margin_left + indent
            x2 = self.page_width - self.margin_right
            self.current_page_content.append(
                f'0.75 0.75 0.75 RG\n0.3 w\n{x1:.1f} {self.y_position:.1f} m\n{x2:.1f} {self.y_position:.1f} l\nS'
            )
            self.y_position -= spacing

    def add_numbered_lines(self, start=1, count=5, spacing=22):
        """Add numbered lined space."""
        for i in range(count):
            self._check_page_break(spacing + 2)
            num = str(start + i) + '.'
            x_num = self.margin_left
            x_line_start = self.margin_left + 25
            x_line_end = self.page_width - self.margin_right
            self.current_page_content.append(
                f'BT\n0.3 0.3 0.3 rg\n/F1 10 Tf\n{x_num:.1f} {self.y_position:.1f} Td\n({num}) Tj\nET'
            )
            self.current_page_content.append(
                f'0.75 0.75 0.75 RG\n0.3 w\n{x_line_start:.1f} {self.y_position:.1f} m\n{x_line_end:.1f} {self.y_position:.1f} l\nS'
            )
            self.y_position -= spacing

    def add_section_header(self, text, size=14, color=(51, 51, 102)):
        """Add a styled section header with underline."""
        self._check_page_break(size * 2 + 15)
        self.add_space(8)
        self.add_text(text, size=size, bold=True, color=color)
        self.add_line(thickness=1.0, color=(color[0]/255, color[1]/255, color[2]/255))
        self.add_space(6)

    def add_chapter_title(self, text, subtitle=""):
        """Add a chapter title page element."""
        self._check_page_break(80)
        self.add_space(15)
        # Decorative line above
        self.add_line(thickness=1.5, color=(0.3, 0.3, 0.6))
        self.add_space(10)
        self.add_text(text, size=18, bold=True, color=(51, 51, 102), align='center')
        if subtitle:
            self.add_space(6)
            self.add_text(subtitle, size=11, italic=True, color=(100, 100, 140), align='center')
        self.add_space(10)
        self.add_line(thickness=1.5, color=(0.3, 0.3, 0.6))
        self.add_space(15)

    def add_quote_box(self, quote, reference="", bg_color=(0.95, 0.95, 0.98)):
        """Add a styled quote/verse box."""
        lines = self._wrap_text(quote, 75)
        box_height = len(lines) * 14 + (20 if reference else 10) + 20
        self._check_page_break(box_height + 10)

        # Background box
        box_y = self.y_position - box_height + 10
        self.add_rect(self.margin_left, box_y, self.content_width, box_height,
                      fill_color=bg_color, stroke_color=(0.7, 0.7, 0.8))
        self.add_space(8)
        for line in lines:
            self.add_text(f'  "{line}"' if line == lines[0] else f'  {line}',
                         size=10, italic=True, color=(60, 60, 100), indent=10)
        if reference:
            self.add_space(4)
            self.add_text(f'  -- {reference}', size=9, bold=True, color=(80, 80, 120), indent=10)
        self.add_space(10)

    def add_title_page(self, title, subtitle="", author="", extra_lines=None):
        """Add a full title/cover page."""
        self.start_page()
        self.show_page_numbers_temp = self.show_page_numbers
        # Decorative top bar
        self.add_rect(0, self.page_height - 120, self.page_width, 120,
                      fill_color=(0.25, 0.2, 0.45))
        # Title area
        self.y_position = self.page_height - 200
        self.add_space(40)
        # Main title
        title_lines = self._wrap_text(title, 35)
        for line in title_lines:
            self.add_text(line, size=24, bold=True, color=(51, 40, 100), align='center')
            self.add_space(4)
        self.add_space(20)
        if subtitle:
            sub_lines = self._wrap_text(subtitle, 50)
            for line in sub_lines:
                self.add_text(line, size=13, italic=True, color=(100, 80, 140), align='center')
                self.add_space(2)
        self.add_space(30)
        self.add_line(thickness=1, color=(0.4, 0.3, 0.6), indent=150, width=200)
        self.add_space(30)
        if author:
            self.add_text(author, size=12, color=(80, 80, 80), align='center')
        if extra_lines:
            self.add_space(20)
            for line in extra_lines:
                self.add_text(line, size=10, color=(120, 120, 120), align='center')
                self.add_space(3)
        # Bottom decorative bar
        self.add_rect(0, 0, self.page_width, 50, fill_color=(0.25, 0.2, 0.45))
        self.end_page()

    def add_toc_page(self, items):
        """Add table of contents. items = list of (title, page_num)."""
        self.start_page()
        self.add_space(10)
        self.add_text("TABLE OF CONTENTS", size=16, bold=True, color=(51, 51, 102), align='center')
        self.add_space(8)
        self.add_line(thickness=1, color=(0.3, 0.3, 0.6))
        self.add_space(15)
        for title, page in items:
            self._check_page_break(18)
            # Title on left
            self.add_text(title, size=10, color=(50, 50, 50), indent=10)
            self.add_space(-12)
            # Page number on right
            self.add_text(str(page), size=10, color=(50, 50, 50), align='right')
            self.add_space(4)
            self.add_line(thickness=0.2, color=(0.85, 0.85, 0.85), indent=10)
        self.end_page()

    def add_blank_journal_page(self, header="", num_lines=25, line_spacing=24):
        """Add a blank journal/writing page."""
        self.start_page()
        if header:
            self.add_text(header, size=12, bold=True, color=(80, 80, 120))
            self.add_space(10)
        self.add_lined_space(num_lines=num_lines, spacing=line_spacing)
        self.end_page()

    def save(self, filepath):
        """Save the PDF to a file."""
        # Ensure last page is ended
        if self.current_page_content:
            self.end_page()

        num_pages = len(self.pages)
        catalog_obj = 1
        pages_obj = 2
        font1_obj = 3
        font2_obj = 4
        font3_obj = 5
        first_page_obj = 6
        first_content_obj = first_page_obj + num_pages
        total_objs = first_content_obj + num_pages - 1

        output = []
        offsets = {}

        # Header
        output.append('%PDF-1.4\n%\xe2\xe3\xcf\xd3\n')

        # Catalog
        offsets[catalog_obj] = sum(len(o.encode('latin-1', errors='replace')) for o in output)
        output.append(f'{catalog_obj} 0 obj\n<< /Type /Catalog /Pages {pages_obj} 0 R >>\nendobj\n\n')

        # Pages
        page_refs = ' '.join(f'{first_page_obj + i} 0 R' for i in range(num_pages))
        offsets[pages_obj] = sum(len(o.encode('latin-1', errors='replace')) for o in output)
        output.append(f'{pages_obj} 0 obj\n<< /Type /Pages /Kids [{page_refs}] /Count {num_pages} >>\nendobj\n\n')

        # Fonts
        offsets[font1_obj] = sum(len(o.encode('latin-1', errors='replace')) for o in output)
        output.append(f'{font1_obj} 0 obj\n<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica /Encoding /WinAnsiEncoding >>\nendobj\n\n')

        offsets[font2_obj] = sum(len(o.encode('latin-1', errors='replace')) for o in output)
        output.append(f'{font2_obj} 0 obj\n<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Bold /Encoding /WinAnsiEncoding >>\nendobj\n\n')

        offsets[font3_obj] = sum(len(o.encode('latin-1', errors='replace')) for o in output)
        output.append(f'{font3_obj} 0 obj\n<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Oblique /Encoding /WinAnsiEncoding >>\nendobj\n\n')

        # Page objects
        for i in range(num_pages):
            pobj = first_page_obj + i
            cobj = first_content_obj + i
            offsets[pobj] = sum(len(o.encode('latin-1', errors='replace')) for o in output)
            output.append(
                f'{pobj} 0 obj\n<< /Type /Page /Parent {pages_obj} 0 R '
                f'/MediaBox [0 0 {self.page_width} {self.page_height}] '
                f'/Contents {cobj} 0 R '
                f'/Resources << /Font << /F1 {font1_obj} 0 R /F2 {font2_obj} 0 R /F3 {font3_obj} 0 R >> >> '
                f'>>\nendobj\n\n'
            )

        # Content streams
        for i in range(num_pages):
            cobj = first_content_obj + i
            stream = '\n'.join(self.pages[i])
            stream_bytes = stream.encode('latin-1', errors='replace')
            offsets[cobj] = sum(len(o.encode('latin-1', errors='replace')) for o in output)
            output.append(
                f'{cobj} 0 obj\n<< /Length {len(stream_bytes)} >>\nstream\n{stream}\nendstream\nendobj\n\n'
            )

        # Xref
        xref_offset = sum(len(o.encode('latin-1', errors='replace')) for o in output)
        output.append(f'xref\n0 {total_objs + 1}\n')
        output.append('0000000000 65535 f \n')
        for obj_id in range(1, total_objs + 1):
            if obj_id in offsets:
                output.append(f'{offsets[obj_id]:010d} 00000 n \n')
            else:
                output.append('0000000000 00000 f \n')

        # Trailer
        output.append(
            f'trailer\n<< /Size {total_objs + 1} /Root {catalog_obj} 0 R >>\n'
            f'startxref\n{xref_offset}\n%%EOF\n'
        )

        with open(filepath, 'wb') as f:
            for part in output:
                f.write(part.encode('latin-1', errors='replace'))

        return len(self.pages)
