#!/usr/bin/env python3
"""
Generate 5 Colorful Arabic Kids Stories with Morals as a PDF.
Features RTL (right-to-left) text support for Arabic.
Each story has: title, colorful image description, the story, and a moral lesson.
"""

import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'full_story_books'))


class ArabicPDF:
    """PDF generator with RTL Arabic text support."""

    def __init__(self):
        self.pages = []
        self.current_page_content = []
        self.page_height = 792
        self.page_width = 612
        self.margin_left = 50
        self.margin_right = 50
        self.margin_top = 60
        self.margin_bottom = 60
        self.y_position = self.page_height - self.margin_top
        self.content_width = self.page_width - self.margin_left - self.margin_right
        self.page_number = 0

    def _escape(self, text):
        """Escape PDF special characters."""
        text = text.replace('\\', '\\\\')
        text = text.replace('(', '\\(')
        text = text.replace(')', '\\)')
        return text

    def _to_utf16be(self, text):
        """Convert text to UTF-16BE hex string for PDF (supports Arabic)."""
        encoded = text.encode('utf-16-be')
        hex_str = encoded.hex()
        return f'<FEFF{hex_str}>'

    def _check_page_break(self, needed=20):
        if self.y_position - needed < self.margin_bottom:
            self.end_page()
            self.start_page()

    def start_page(self):
        self.current_page_content = []
        self.y_position = self.page_height - self.margin_top
        self.page_number += 1

    def end_page(self):
        # Page number
        page_str = f'- {self.page_number} -'
        self.current_page_content.append(
            f'BT\n0.4 0.4 0.4 rg\n/F1 9 Tf\n280 30 Td\n({page_str}) Tj\nET'
        )
        self.pages.append(self.current_page_content[:])
        self.current_page_content = []

    def add_arabic_text(self, text, size=14, bold=False, color=(0, 0, 0), align='right'):
        """Add Arabic RTL text."""
        self._check_page_break(size * 1.5)
        font = '/F4' if bold else '/F3'
        r, g, b = [c / 255.0 for c in color]
        hex_text = self._to_utf16be(text)

        if align == 'right':
            x = self.page_width - self.margin_right
        elif align == 'center':
            x = self.page_width / 2
        else:
            x = self.margin_left

        self.current_page_content.append(
            f'BT\n{r:.3f} {g:.3f} {b:.3f} rg\n{font} {size} Tf\n{x:.1f} {self.y_position:.1f} Td\n{hex_text} Tj\nET'
        )
        self.y_position -= size * 1.6

    def add_english_text(self, text, size=11, bold=False, color=(0, 0, 0), align='left', indent=0):
        """Add English LTR text."""
        self._check_page_break(size * 1.5)
        font = '/F2' if bold else '/F1'
        r, g, b = [c / 255.0 for c in color]
        x = self.margin_left + indent

        if align == 'center':
            approx_width = len(text) * size * 0.45
            x = (self.page_width - approx_width) / 2
        elif align == 'right':
            approx_width = len(text) * size * 0.45
            x = self.page_width - self.margin_right - approx_width

        escaped = self._escape(text)
        self.current_page_content.append(
            f'BT\n{r:.3f} {g:.3f} {b:.3f} rg\n{font} {size} Tf\n{x:.1f} {self.y_position:.1f} Td\n({escaped}) Tj\nET'
        )
        self.y_position -= size * 1.5

    def add_wrapped_english(self, text, size=11, bold=False, color=(0, 0, 0), indent=0, max_chars=85):
        """Add word-wrapped English text."""
        adjusted = max_chars - int(indent / 5.5)
        words = text.split()
        lines = []
        current = ''
        for word in words:
            if len(current) + len(word) + 1 <= adjusted:
                current = current + ' ' + word if current else word
            else:
                if current:
                    lines.append(current)
                current = word
        if current:
            lines.append(current)

        for line in lines:
            self._check_page_break(size * 1.5)
            self.add_english_text(line, size, bold, color, indent=indent)

    def add_space(self, points=12):
        self.y_position -= points

    def add_rect(self, x, y, w, h, fill_color=None, stroke_color=None):
        cmds = ''
        if fill_color:
            r, g, b = fill_color
            cmds += f'{r:.3f} {g:.3f} {b:.3f} rg\n'
        if stroke_color:
            r, g, b = stroke_color
            cmds += f'{r:.3f} {g:.3f} {b:.3f} RG\n'
        cmds += f'1 w\n{x:.1f} {y:.1f} {w:.1f} {h:.1f} re\n'
        if fill_color and stroke_color:
            cmds += 'B'
        elif fill_color:
            cmds += 'f'
        else:
            cmds += 'S'
        self.current_page_content.append(cmds)

    def add_line(self, color=(0.7, 0.7, 0.7)):
        x1 = self.margin_left
        x2 = self.page_width - self.margin_right
        r, g, b = color
        self.current_page_content.append(
            f'{r:.3f} {g:.3f} {b:.3f} RG\n0.5 w\n{x1:.1f} {self.y_position:.1f} m\n{x2:.1f} {self.y_position:.1f} l\nS'
        )
        self.y_position -= 10

    def add_colorful_box(self, text_lines_en, bg_color=(0.9, 0.95, 1.0), border_color=(0.4, 0.5, 0.8)):
        """Add a colorful description box."""
        box_height = len(text_lines_en) * 16 + 30
        self._check_page_break(box_height + 10)
        box_y = self.y_position - box_height + 10
        self.add_rect(self.margin_left, box_y, self.content_width, box_height,
                      fill_color=bg_color, stroke_color=border_color)
        self.add_space(10)
        for line in text_lines_en:
            self.add_english_text(f"  {line}", size=10, color=(40, 50, 80), indent=10)
        self.add_space(10)

    def save(self, filepath):
        """Save PDF with Arabic font support."""
        if self.current_page_content:
            self.end_page()

        num_pages = len(self.pages)
        catalog_obj = 1
        pages_obj = 2
        font1_obj = 3  # Helvetica
        font2_obj = 4  # Helvetica-Bold
        font3_obj = 5  # Arabic - we'll use a CIDFont
        font4_obj = 6  # Arabic Bold
        # For Arabic we need CIDFont with Identity-H encoding
        # Objects: 7 = CIDFont descriptor for font3, 8 = CIDSystemInfo, 9 = FontDescriptor
        # Simplified: use built-in with Identity-H

        first_page_obj = 10
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

        # Font 1: Helvetica
        offsets[font1_obj] = sum(len(o.encode('latin-1', errors='replace')) for o in output)
        output.append(f'{font1_obj} 0 obj\n<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica /Encoding /WinAnsiEncoding >>\nendobj\n\n')

        # Font 2: Helvetica-Bold
        offsets[font2_obj] = sum(len(o.encode('latin-1', errors='replace')) for o in output)
        output.append(f'{font2_obj} 0 obj\n<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Bold /Encoding /WinAnsiEncoding >>\nendobj\n\n')

        # Font 3: Arabic CIDFont (Type0 with Identity-H)
        # This uses a standard Arabic font approach
        offsets[font3_obj] = sum(len(o.encode('latin-1', errors='replace')) for o in output)
        output.append(f'{font3_obj} 0 obj\n<< /Type /Font /Subtype /Type0 /BaseFont /ArialMT /Encoding /Identity-H /DescendantFonts [{font3_obj + 3} 0 R] >>\nendobj\n\n')

        offsets[font4_obj] = sum(len(o.encode('latin-1', errors='replace')) for o in output)
        output.append(f'{font4_obj} 0 obj\n<< /Type /Font /Subtype /Type0 /BaseFont /Arial-BoldMT /Encoding /Identity-H /DescendantFonts [{font4_obj + 3} 0 R] >>\nendobj\n\n')

        # CIDFont for font3 (obj 7)  -- simplified
        offsets[7] = sum(len(o.encode('latin-1', errors='replace')) for o in output)
        output.append('7 0 obj\n<< /Type /Font /Subtype /CIDFontType2 /BaseFont /ArialMT '
                      '/CIDSystemInfo << /Registry (Adobe) /Ordering (Identity) /Supplement 0 >> '
                      '/DW 1000 >>\nendobj\n\n')

        # Placeholder obj 8
        offsets[8] = sum(len(o.encode('latin-1', errors='replace')) for o in output)
        output.append('8 0 obj\n<< /Type /Font /Subtype /CIDFontType2 /BaseFont /ArialMT '
                      '/CIDSystemInfo << /Registry (Adobe) /Ordering (Identity) /Supplement 0 >> '
                      '/DW 1000 >>\nendobj\n\n')

        # CIDFont for font4 (obj 9) -- simplified
        offsets[9] = sum(len(o.encode('latin-1', errors='replace')) for o in output)
        output.append('9 0 obj\n<< /Type /Font /Subtype /CIDFontType2 /BaseFont /Arial-BoldMT '
                      '/CIDSystemInfo << /Registry (Adobe) /Ordering (Identity) /Supplement 0 >> '
                      '/DW 1000 >>\nendobj\n\n')

        # Page objects
        for i in range(num_pages):
            pobj = first_page_obj + i
            cobj = first_content_obj + i
            offsets[pobj] = sum(len(o.encode('latin-1', errors='replace')) for o in output)
            output.append(
                f'{pobj} 0 obj\n<< /Type /Page /Parent {pages_obj} 0 R '
                f'/MediaBox [0 0 {self.page_width} {self.page_height}] '
                f'/Contents {cobj} 0 R '
                f'/Resources << /Font << /F1 {font1_obj} 0 R /F2 {font2_obj} 0 R '
                f'/F3 {font3_obj} 0 R /F4 {font4_obj} 0 R >> >> '
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

        output.append(
            f'trailer\n<< /Size {total_objs + 1} /Root {catalog_obj} 0 R >>\n'
            f'startxref\n{xref_offset}\n%%EOF\n'
        )

        with open(filepath, 'wb') as f:
            for part in output:
                f.write(part.encode('latin-1', errors='replace'))

        return len(self.pages)


# ============================================================
# STORY DATA - 5 Arabic Stories with English Translation
# ============================================================

stories = [
    {
        "number": 1,
        "title_ar": "الأرنب والسلحفاة",
        "title_en": "The Rabbit and the Tortoise",
        "colors": ((0.45, 0.75, 0.45), (0.2, 0.55, 0.2)),  # Green theme
        "image_desc": [
            "A proud rabbit with long ears racing ahead on a sunny forest path.",
            "A small, determined tortoise slowly walking with a big smile.",
            "Colorful flowers, butterflies, and cheering forest animals along the road.",
            "Finish line with a banner. The tortoise crosses it while the rabbit sleeps under a tree!",
        ],
        "story_ar": [
            "كان يا ما كان، في غابة جميلة، أرنب سريع جداً يفتخر بنفسه.",
            "قال الأرنب للسلحفاة: \"أنا أسرع منكِ! هيا نتسابق!\"",
            "قالت السلحفاة بهدوء: \"حسناً، لنتسابق.\"",
            "بدأ السباق! ركض الأرنب بسرعة كبيرة ثم قال: \"السلحفاة بطيئة جداً!\"",
            "نام الأرنب تحت شجرة. لكن السلحفاة لم تتوقف أبداً.",
            "مشت السلحفاة ببطء... ببطء... ببطء... حتى وصلت خط النهاية!",
            "استيقظ الأرنب وركض بسرعة لكنه وجد السلحفاة قد فازت!",
            "قال الأرنب: \"تعلمت درساً مهماً اليوم!\"",
        ],
        "story_en": [
            "Once upon a time, in a beautiful forest, there was a very fast rabbit who was proud of himself.",
            "The rabbit said to the tortoise: 'I am faster than you! Let's race!'",
            "The tortoise said calmly: 'Okay, let's race.'",
            "The race started! The rabbit ran very fast then said: 'The tortoise is so slow!'",
            "The rabbit fell asleep under a tree. But the tortoise never stopped.",
            "The tortoise walked slowly... slowly... slowly... until she reached the finish line!",
            "The rabbit woke up and ran fast but found the tortoise had won!",
            "The rabbit said: 'I learned an important lesson today!'",
        ],
        "moral_ar": "الدرس: المثابرة والعمل الجاد يتغلبان على الغرور والكسل. لا تستهزئ بالآخرين!",
        "moral_en": "MORAL: Perseverance and hard work overcome pride and laziness. Never underestimate others!",
    },
    {
        "number": 2,
        "title_ar": "الولد الذي كذب",
        "title_en": "The Boy Who Cried Wolf",
        "colors": ((0.85, 0.65, 0.3), (0.6, 0.4, 0.1)),  # Orange theme
        "image_desc": [
            "A shepherd boy on a green hill with fluffy white sheep around him.",
            "The boy shouts with a mischievous smile while villagers run toward him.",
            "The villagers look angry when they discover there is no wolf.",
            "Finally, a real wolf appears and the boy cries for help, but no one comes.",
        ],
        "story_ar": [
            "كان هناك ولد يرعى الأغنام على التل كل يوم.",
            "شعر الولد بالملل فصرخ: \"الذئب! الذئب! ساعدوني!\"",
            "ركض أهل القرية لمساعدته، لكنهم لم يجدوا ذئباً!",
            "ضحك الولد وقال: \"خدعتكم!\"",
            "في اليوم التالي، كذب مرة أخرى: \"الذئب! الذئب!\"",
            "جاء أهل القرية مرة أخرى ولم يجدوا شيئاً. غضبوا كثيراً.",
            "في اليوم الثالث، جاء ذئب حقيقي! صرخ الولد: \"الذئب! الذئب!\"",
            "لكن لم يأتِ أحد لمساعدته. لم يصدقه أحد.",
            "تعلم الولد أن الكذب يجعل الناس لا يثقون بك.",
        ],
        "story_en": [
            "There was a boy who shepherded sheep on the hill every day.",
            "The boy got bored and shouted: 'Wolf! Wolf! Help me!'",
            "The villagers ran to help him, but they found no wolf!",
            "The boy laughed and said: 'I tricked you!'",
            "The next day, he lied again: 'Wolf! Wolf!'",
            "The villagers came again and found nothing. They were very angry.",
            "On the third day, a REAL wolf came! The boy shouted: 'Wolf! Wolf!'",
            "But no one came to help him. No one believed him.",
            "The boy learned that lying makes people lose trust in you.",
        ],
        "moral_ar": "الدرس: الكذب يفقدك ثقة الناس. قل الصدق دائماً حتى يصدقك الآخرون عندما تحتاجهم.",
        "moral_en": "MORAL: Lying makes people lose trust in you. Always tell the truth so others believe you when you need them.",
    },
    {
        "number": 3,
        "title_ar": "الأسد والفأر",
        "title_en": "The Lion and the Mouse",
        "colors": ((0.85, 0.75, 0.3), (0.7, 0.5, 0.0)),  # Gold theme
        "image_desc": [
            "A mighty golden lion sleeping peacefully under a large tree in the African savanna.",
            "A tiny, cute mouse accidentally runs over the lion's nose, waking him up!",
            "The lion holds the tiny mouse gently in his huge paw. The mouse looks scared but brave.",
            "Later: the lion is caught in a net. The little mouse chews through the ropes to free him!",
            "The lion and mouse stand together as friends. Big and small, side by side.",
        ],
        "story_ar": [
            "في يوم من الأيام، كان أسد كبير نائماً في الغابة.",
            "ركض فأر صغير فوق أنف الأسد! استيقظ الأسد غاضباً!",
            "قال الأسد: \"سأأكلك أيها الفأر الصغير!\"",
            "قال الفأر: \"أرجوك أطلقني! ربما أساعدك يوماً ما!\"",
            "ضحك الأسد: \"أنت صغير جداً! كيف تساعدني؟\" لكنه أطلقه.",
            "بعد أيام، وقع الأسد في شبكة صيادين! لم يستطع الهروب!",
            "سمع الفأر صراخ الأسد وركض لمساعدته!",
            "قضم الفأر الحبال بأسنانه الصغيرة حتى تحرر الأسد!",
            "قال الأسد: \"شكراً لك يا صديقي الصغير. كنت مخطئاً!\"",
        ],
        "story_en": [
            "One day, a big lion was sleeping in the forest.",
            "A little mouse ran over the lion's nose! The lion woke up angry!",
            "The lion said: 'I will eat you, little mouse!'",
            "The mouse said: 'Please let me go! Maybe I can help you someday!'",
            "The lion laughed: 'You're too small! How can you help me?' But he let him go.",
            "Days later, the lion got caught in hunters' net! He couldn't escape!",
            "The mouse heard the lion's cries and ran to help!",
            "The mouse chewed through the ropes with his tiny teeth until the lion was free!",
            "The lion said: 'Thank you, my little friend. I was wrong!'",
        ],
        "moral_ar": "الدرس: لا تستصغر أحداً. حتى أصغر صديق يمكن أن يكون أكبر مساعدة. كن لطيفاً مع الجميع!",
        "moral_en": "MORAL: Never look down on anyone. Even the smallest friend can be the biggest help. Be kind to everyone!",
    },
    {
        "number": 4,
        "title_ar": "الشجرة الكريمة",
        "title_en": "The Generous Tree",
        "colors": ((0.3, 0.7, 0.5), (0.1, 0.5, 0.3)),  # Teal/green theme
        "image_desc": [
            "A beautiful, large apple tree with bright red apples and lush green leaves.",
            "A little boy plays happily under the tree, climbing its branches.",
            "Years pass: the boy grows up. The tree gives him apples to sell.",
            "The tree gives its branches for a house, its trunk for a boat.",
            "Finally, an old stump remains, and the old man sits on it. Both are happy together.",
        ],
        "story_ar": [
            "كانت هناك شجرة تفاح كبيرة وجميلة.",
            "كل يوم، كان ولد صغير يأتي للعب معها. كانت الشجرة سعيدة جداً!",
            "كبر الولد وقال: \"أحتاج مالاً.\" قالت الشجرة: \"خذ تفاحي وبعه.\"",
            "كبر أكثر وقال: \"أحتاج بيتاً.\" قالت الشجرة: \"خذ أغصاني.\"",
            "كبر أكثر وقال: \"أحتاج قارباً.\" قالت الشجرة: \"خذ جذعي.\"",
            "لم يبقَ من الشجرة إلا جذع صغير.",
            "عاد الرجل وهو عجوز وقال: \"أنا متعب. أحتاج مكاناً للراحة.\"",
            "قالت الشجرة: \"اجلس على جذعي واسترح يا حبيبي.\"",
            "جلس الرجل وكانت الشجرة سعيدة لأنها أعطت كل ما عندها بحب.",
        ],
        "story_en": [
            "There was a big, beautiful apple tree.",
            "Every day, a little boy came to play with it. The tree was very happy!",
            "The boy grew up and said: 'I need money.' The tree said: 'Take my apples and sell them.'",
            "He grew more and said: 'I need a house.' The tree said: 'Take my branches.'",
            "He grew more and said: 'I need a boat.' The tree said: 'Take my trunk.'",
            "Nothing was left of the tree except a small stump.",
            "The man returned as an old man and said: 'I'm tired. I need a place to rest.'",
            "The tree said: 'Sit on my stump and rest, my dear.'",
            "The man sat and the tree was happy because she gave everything with love.",
        ],
        "moral_ar": "الدرس: العطاء يجلب السعادة. كن كريماً مع من تحب. وتذكر أن تشكر من يعطيك — مثل والديك!",
        "moral_en": "MORAL: Giving brings happiness. Be generous with those you love. And remember to thank those who give to you - like your parents!",
    },
    {
        "number": 5,
        "title_ar": "النملة والجندب",
        "title_en": "The Ant and the Grasshopper",
        "colors": ((0.4, 0.6, 0.85), (0.2, 0.3, 0.6)),  # Blue theme
        "image_desc": [
            "A beautiful summer meadow with colorful flowers and bright sunshine.",
            "Hardworking ants carrying food in a long line toward their home.",
            "A lazy grasshopper playing music and laughing at the busy ants.",
            "Winter arrives: snow covers everything. The grasshopper shivers in the cold.",
            "The kind ants share their food with the grasshopper. Everyone is warm inside.",
        ],
        "story_ar": [
            "في فصل الصيف الجميل، كانت النملة تعمل بجد كل يوم.",
            "حملت النملة الطعام إلى بيتها استعداداً لفصل الشتاء.",
            "رآها الجندب وضحك: \"لماذا تعملين كثيراً؟ تعالي العبي معي!\"",
            "قالت النملة: \"يجب أن أستعد للشتاء. أنصحك أن تفعل مثلي.\"",
            "قال الجندب: \"الشتاء بعيد! سأستمتع بوقتي!\" ولعب طوال الصيف.",
            "جاء الشتاء! كان الجو بارداً جداً والثلج في كل مكان.",
            "لم يكن عند الجندب طعام ولا مكان دافئ! كان جائعاً وبارداً.",
            "ذهب الجندب إلى النملة: \"أرجوكِ ساعديني! أنا جائع!\"",
            "قالت النملة اللطيفة: \"تعال، سأشاركك طعامي. لكن تعلّم الدرس!\"",
            "شكر الجندب النملة وقرر أن يعمل بجد في الصيف القادم.",
        ],
        "story_en": [
            "In the beautiful summer, the ant worked hard every day.",
            "The ant carried food to her home preparing for winter.",
            "The grasshopper saw her and laughed: 'Why work so much? Come play with me!'",
            "The ant said: 'I must prepare for winter. I advise you to do the same.'",
            "The grasshopper said: 'Winter is far away! I'll enjoy my time!' He played all summer.",
            "Winter came! It was very cold and snow was everywhere.",
            "The grasshopper had no food and no warm place! He was hungry and cold.",
            "The grasshopper went to the ant: 'Please help me! I'm hungry!'",
            "The kind ant said: 'Come, I'll share my food. But learn the lesson!'",
            "The grasshopper thanked the ant and decided to work hard next summer.",
        ],
        "moral_ar": "الدرس: اعمل بجد واستعد للمستقبل. لا تضيع وقتك في اللعب فقط. العمل اليوم يصنع راحة الغد!",
        "moral_en": "MORAL: Work hard and prepare for the future. Don't waste all your time playing. Today's work creates tomorrow's comfort!",
    },
]


def generate_stories_pdf():
    """Generate the complete PDF with all 5 Arabic stories."""
    pdf = ArabicPDF()

    # === COVER PAGE ===
    pdf.start_page()
    pdf.add_rect(0, pdf.page_height - 150, pdf.page_width, 150, fill_color=(0.25, 0.2, 0.5))
    pdf.y_position = pdf.page_height - 80
    pdf.add_english_text("5 COLORFUL STORIES FOR KIDS", size=22, bold=True, color=(255, 255, 255), align='center')
    pdf.add_space(8)
    pdf.add_english_text("WITH MORALS - IN ARABIC & ENGLISH", size=14, bold=True, color=(255, 220, 150), align='center')

    pdf.y_position = pdf.page_height - 200
    pdf.add_space(20)
    # Arabic title
    pdf.add_arabic_text("خمس قصص ملونة للأطفال", size=22, bold=True, color=(80, 40, 120), align='center')
    pdf.add_space(10)
    pdf.add_arabic_text("مع دروس أخلاقية", size=16, color=(100, 80, 140), align='center')

    pdf.y_position = 350
    pdf.add_english_text("Stories included:", size=12, bold=True, color=(60, 60, 60), align='center')
    pdf.add_space(10)
    for s in stories:
        pdf.add_english_text(f"{s['number']}. {s['title_en']} / {s['title_ar']}", size=11, color=(80, 80, 80), align='center')
        pdf.add_space(3)

    pdf.y_position = 150
    pdf.add_english_text("Bilingual: Arabic + English", size=11, color=(100, 100, 100), align='center')
    pdf.add_space(5)
    pdf.add_english_text("Beautiful Image Descriptions Included", size=10, color=(120, 120, 120), align='center')

    pdf.add_rect(0, 0, pdf.page_width, 50, fill_color=(0.25, 0.2, 0.5))
    pdf.end_page()

    # === TABLE OF CONTENTS ===
    pdf.start_page()
    pdf.add_english_text("TABLE OF CONTENTS", size=16, bold=True, color=(80, 40, 120), align='center')
    pdf.add_space(5)
    pdf.add_arabic_text("فهرس القصص", size=16, bold=True, color=(80, 40, 120), align='center')
    pdf.add_space(15)
    pdf.add_line(color=(0.4, 0.3, 0.6))
    pdf.add_space(10)

    page_num = 3
    for s in stories:
        pdf.add_english_text(f"Story {s['number']}: {s['title_en']} ({s['title_ar']}) ........... page {page_num}", size=11, color=(50, 50, 50), indent=20)
        pdf.add_space(8)
        page_num += 4  # Each story takes ~4 pages

    pdf.add_space(20)
    pdf.add_line(color=(0.4, 0.3, 0.6))
    pdf.end_page()

    # === STORY PAGES ===
    for story in stories:
        bg_color = story['colors'][0]
        accent_color = story['colors'][1]

        # PAGE 1: Title + Image Description
        pdf.start_page()
        # Colored header bar
        pdf.add_rect(0, pdf.page_height - 90, pdf.page_width, 90, fill_color=bg_color)
        pdf.y_position = pdf.page_height - 50
        pdf.add_english_text(f"Story {story['number']}", size=10, bold=True, color=(255, 255, 255), align='center')
        pdf.add_space(5)
        pdf.add_english_text(story['title_en'], size=18, bold=True, color=(255, 255, 255), align='center')

        pdf.y_position = pdf.page_height - 110
        pdf.add_space(10)
        # Arabic title
        pdf.add_arabic_text(story['title_ar'], size=20, bold=True, color=(int(accent_color[0]*255), int(accent_color[1]*255), int(accent_color[2]*255)), align='center')
        pdf.add_space(15)

        # Image description box
        pdf.add_english_text("IMAGINE THIS BEAUTIFUL SCENE:", size=9, bold=True, color=(100, 80, 140))
        pdf.add_space(5)
        pdf.add_colorful_box(story['image_desc'], bg_color=(bg_color[0]*0.3+0.7, bg_color[1]*0.3+0.7, bg_color[2]*0.3+0.7), border_color=accent_color)

        pdf.add_space(15)
        pdf.add_line(color=accent_color)
        pdf.end_page()

        # PAGE 2: Arabic Story
        pdf.start_page()
        pdf.add_rect(0, pdf.page_height - 50, pdf.page_width, 50, fill_color=bg_color)
        pdf.y_position = pdf.page_height - 35
        pdf.add_arabic_text(f"القصة: {story['title_ar']}", size=14, bold=True, color=(255, 255, 255), align='center')

        pdf.y_position = pdf.page_height - 75
        pdf.add_space(15)
        pdf.add_arabic_text("القصة بالعربية:", size=13, bold=True, color=(int(accent_color[0]*255), int(accent_color[1]*255), int(accent_color[2]*255)))
        pdf.add_space(10)

        for line in story['story_ar']:
            pdf._check_page_break(22)
            pdf.add_arabic_text(line, size=12, color=(40, 40, 60))
            pdf.add_space(4)

        pdf.add_space(15)
        # Moral in Arabic
        pdf.add_rect(pdf.margin_left, pdf.y_position - 40, pdf.content_width, 45,
                     fill_color=(1.0, 0.95, 0.8), stroke_color=(0.8, 0.6, 0.0))
        pdf.add_space(5)
        pdf.add_arabic_text(story['moral_ar'], size=11, bold=True, color=(120, 80, 0))
        pdf.add_space(25)
        pdf.end_page()

        # PAGE 3: English Story
        pdf.start_page()
        pdf.add_rect(0, pdf.page_height - 50, pdf.page_width, 50, fill_color=bg_color)
        pdf.y_position = pdf.page_height - 35
        pdf.add_english_text(f"Story: {story['title_en']}", size=14, bold=True, color=(255, 255, 255), align='center')

        pdf.y_position = pdf.page_height - 75
        pdf.add_space(15)
        pdf.add_english_text("The Story in English:", size=13, bold=True, color=(int(accent_color[0]*255), int(accent_color[1]*255), int(accent_color[2]*255)))
        pdf.add_space(10)

        for line in story['story_en']:
            pdf._check_page_break(18)
            pdf.add_wrapped_english(line, size=11, color=(40, 40, 60), indent=10)
            pdf.add_space(5)

        pdf.add_space(15)
        # Moral in English
        pdf.add_rect(pdf.margin_left, pdf.y_position - 35, pdf.content_width, 40,
                     fill_color=(0.85, 0.95, 0.85), stroke_color=(0.2, 0.6, 0.2))
        pdf.add_space(8)
        pdf.add_wrapped_english(story['moral_en'], size=10, bold=True, color=(0, 100, 0), indent=10)
        pdf.add_space(20)
        pdf.end_page()

        # PAGE 4: Activity Page
        pdf.start_page()
        pdf.add_rect(0, pdf.page_height - 50, pdf.page_width, 50, fill_color=bg_color)
        pdf.y_position = pdf.page_height - 35
        pdf.add_english_text(f"Activity Page: {story['title_en']}", size=12, bold=True, color=(255, 255, 255), align='center')

        pdf.y_position = pdf.page_height - 75
        pdf.add_space(10)
        pdf.add_english_text("What did you learn from this story?", size=11, bold=True, color=(60, 40, 100))
        pdf.add_arabic_text("ماذا تعلمت من هذه القصة؟", size=12, bold=True, color=(60, 40, 100))
        pdf.add_space(5)
        # Lines for writing
        for _ in range(3):
            x1 = pdf.margin_left
            x2 = pdf.page_width - pdf.margin_right
            pdf.current_page_content.append(
                f'0.75 0.75 0.75 RG\n0.3 w\n{x1:.1f} {pdf.y_position:.1f} m\n{x2:.1f} {pdf.y_position:.1f} l\nS'
            )
            pdf.y_position -= 25

        pdf.add_space(10)
        pdf.add_english_text("Draw your favorite scene from the story:", size=11, bold=True, color=(60, 40, 100))
        pdf.add_arabic_text("ارسم مشهدك المفضل من القصة:", size=12, bold=True, color=(60, 40, 100))
        pdf.add_space(10)
        # Drawing box
        pdf.add_rect(pdf.margin_left, pdf.y_position - 200, pdf.content_width, 200,
                     stroke_color=(0.5, 0.5, 0.5))
        pdf.y_position -= 210

        pdf.add_space(10)
        pdf.add_english_text("How can you apply this lesson in your life?", size=10, bold=True, color=(60, 40, 100))
        pdf.add_arabic_text("كيف يمكنك تطبيق هذا الدرس في حياتك؟", size=11, bold=True, color=(60, 40, 100))
        # Lines
        for _ in range(3):
            x1 = pdf.margin_left
            x2 = pdf.page_width - pdf.margin_right
            pdf.current_page_content.append(
                f'0.75 0.75 0.75 RG\n0.3 w\n{x1:.1f} {pdf.y_position:.1f} m\n{x2:.1f} {pdf.y_position:.1f} l\nS'
            )
            pdf.y_position -= 25

        pdf.end_page()

    # === FINAL PAGE ===
    pdf.start_page()
    pdf.add_rect(0, pdf.page_height - 150, pdf.page_width, 150, fill_color=(0.25, 0.2, 0.5))
    pdf.y_position = pdf.page_height - 70
    pdf.add_english_text("The End!", size=22, bold=True, color=(255, 255, 255), align='center')
    pdf.add_space(5)
    pdf.add_arabic_text("النهاية!", size=22, bold=True, color=(255, 220, 150), align='center')

    pdf.y_position = pdf.page_height - 200
    pdf.add_space(20)
    pdf.add_english_text("5 Lessons We Learned:", size=14, bold=True, color=(80, 40, 120), align='center')
    pdf.add_space(10)
    pdf.add_arabic_text("خمسة دروس تعلمناها:", size=14, bold=True, color=(80, 40, 120), align='center')
    pdf.add_space(15)

    lessons = [
        ("1.", "Hard work beats laziness", "العمل الجاد يتغلب على الكسل"),
        ("2.", "Always tell the truth", "قل الصدق دائماً"),
        ("3.", "Be kind to everyone, big or small", "كن لطيفاً مع الجميع"),
        ("4.", "Be generous and grateful", "كن كريماً وشكوراً"),
        ("5.", "Prepare for the future", "استعد للمستقبل"),
    ]
    for num, en, ar in lessons:
        pdf.add_english_text(f"  {num} {en}", size=11, indent=30, color=(60, 60, 80))
        pdf.add_space(-14)
        pdf.add_arabic_text(f"{ar}", size=11, color=(60, 60, 80))
        pdf.add_space(8)

    pdf.y_position = 120
    pdf.add_english_text("Made with love for little ones!", size=10, color=(150, 150, 150), align='center')
    pdf.add_space(5)
    pdf.add_arabic_text("صُنع بحب لأطفالنا الصغار!", size=11, color=(150, 150, 150), align='center')

    pdf.add_rect(0, 0, pdf.page_width, 50, fill_color=(0.25, 0.2, 0.5))
    pdf.end_page()

    return pdf


if __name__ == '__main__':
    output_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(output_dir, '5_Arabic_Kids_Stories_with_Morals.pdf')

    print("=" * 60)
    print("  GENERATING: 5 Colorful Arabic Stories for Kids")
    print("=" * 60)

    pdf = generate_stories_pdf()
    num_pages = pdf.save(output_path)

    file_size = os.path.getsize(output_path) / 1024
    print(f"  SUCCESS!")
    print(f"  File: {output_path}")
    print(f"  Pages: {num_pages}")
    print(f"  Size: {file_size:.1f} KB")
    print()
    print("  Stories included:")
    for s in stories:
        print(f"    {s['number']}. {s['title_en']} / {s['title_ar']}")
    print()
    print("=" * 60)
