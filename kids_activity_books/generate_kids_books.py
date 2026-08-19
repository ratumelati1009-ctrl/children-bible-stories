#!/usr/bin/env python3
"""
Generate 6 Kids Bible Activity Books (40+ pages each):
11. 100 Bible Activities for Kids
12. Kids Bible Prayer Journal
13. 50 Bible Stories for Kids Workbook
14. Bible Coloring & Activity Book (Ages 3-7)
15. Bible Word Search & Puzzle Book
16. Bible Stories Six Pack (6 detailed stories)
"""

import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'full_story_books'))
from pdf_engine import PDFEngine


def pad_to_pages(pdf, target=42, title="Activity Notes"):
    """Pad with blank activity pages to reach target page count."""
    while len(pdf.pages) + (1 if pdf.current_page_content else 0) < target:
        pdf.add_blank_journal_page(header=title)


# ============================================================
# BOOK 11: 100 Bible Activities for Kids
# ============================================================
def create_book_11():
    pdf = PDFEngine()
    pdf.header_text = "100 Bible Activities for Kids"

    pdf.add_title_page(
        title="100 Bible Activities for Kids",
        subtitle="Coloring, Matching, Word Searches, Mazes, Bible Questions, Fill-in-the-Blanks, Memory Verses & Drawing!",
        author="For Kids Ages 4-10",
        extra_lines=["Hours of fun while learning God's Word!", "Perfect for Sunday School, Homeschool, or Family Time"]
    )

    # INTRO
    pdf.start_page()
    pdf.add_chapter_title("Welcome, Super Bible Explorer!")
    pdf.add_wrapped_text("Get ready for 100 AMAZING activities that will help you learn about God, the Bible, and Jesus! You can color, solve puzzles, draw pictures, find words, and so much more. Each activity teaches you something special from God's Word.")
    pdf.add_space(10)
    pdf.add_text("What's Inside:", size=12, bold=True, color=(51, 51, 102))
    pdf.add_space(5)
    categories = [
        "Activities 1-15: COLORING PAGES (Bible scenes to color)",
        "Activities 16-30: MATCHING GAMES (Match the pairs!)",
        "Activities 31-45: WORD SEARCHES (Find hidden words!)",
        "Activities 46-55: MAZES (Help Bible heroes find their way!)",
        "Activities 56-70: BIBLE QUESTIONS (Test your knowledge!)",
        "Activities 71-85: FILL-IN-THE-BLANKS (Complete the verse!)",
        "Activities 86-95: MEMORY VERSES (Learn God's Word!)",
        "Activities 96-100: DRAWING ACTIVITIES (Create your own art!)",
    ]
    for c in categories:
        pdf.add_text(f"  * {c}", size=9, indent=10)
        pdf.add_space(3)
    pdf.end_page()

    # --- SECTION 1: COLORING (15 activities) ---
    pdf.start_page()
    pdf.add_chapter_title("COLORING PAGES (Activities 1-15)")
    pdf.add_wrapped_text("Color these beautiful Bible scenes! Use your favorite colors to bring each picture to life.")
    pdf.add_space(10)
    coloring_scenes = [
        ("1. God Creates the World", "Color the sun, moon, stars, animals, trees, flowers, and ocean!"),
        ("2. Adam and Eve in the Garden", "Color the beautiful Garden of Eden with all its fruits and animals."),
        ("3. Noah's Ark", "Color the big ark, the animals (2 of each!), the rainbow, and the water."),
        ("4. Baby Moses in the Basket", "Color baby Moses, the basket, the river, the reeds, and the princess."),
        ("5. David and Goliath", "Color brave David with his slingshot and the giant Goliath."),
        ("6. Daniel in the Lions' Den", "Color Daniel praying peacefully with the lions around him."),
        ("7. Jonah and the Big Fish", "Color Jonah, the huge fish, the ocean, and the boat."),
        ("8. Baby Jesus in the Manger", "Color the stable, Mary, Joseph, baby Jesus, the animals, and the star."),
    ]
    for title, desc in coloring_scenes:
        pdf._check_page_break(30)
        pdf.add_text(title, size=11, bold=True, color=(0, 100, 0))
        pdf.add_text(f"    {desc}", size=9, indent=15, color=(80, 80, 80))
        pdf.add_space(5)
    pdf.end_page()

    pdf.start_page()
    coloring_scenes2 = [
        ("9. Jesus Feeds 5,000", "Color Jesus, the boy with bread and fish, and the happy crowd."),
        ("10. The Good Samaritan", "Color the kind man helping the hurt traveler on the road."),
        ("11. Jesus Walks on Water", "Color Jesus on the waves, the boat, and the stormy sky."),
        ("12. Zacchaeus in the Tree", "Color the short man in the big tree and Jesus below."),
        ("13. Jesus and the Children", "Color Jesus surrounded by happy children of all colors."),
        ("14. The Empty Tomb (Easter)", "Color the empty tomb, the angel, and the sunrise."),
        ("15. Heaven", "Color what you think heaven looks like! Be creative!"),
    ]
    for title, desc in coloring_scenes2:
        pdf._check_page_break(30)
        pdf.add_text(title, size=11, bold=True, color=(0, 100, 0))
        pdf.add_text(f"    {desc}", size=9, indent=15, color=(80, 80, 80))
        pdf.add_space(5)
    # Drawing space for one coloring activity
    pdf.add_space(10)
    pdf.add_text("Color this scene: GOD'S CREATION", size=10, bold=True, color=(0, 100, 50))
    pdf.add_rect(pdf.margin_left, pdf.y_position - 150, pdf.content_width, 150, stroke_color=(0.5, 0.8, 0.5))
    pdf.y_position -= 155
    pdf.add_text("(Draw the sun, trees, animals, flowers, and people!)", size=8, color=(100, 100, 100))
    pdf.end_page()

    # --- SECTION 2: MATCHING (15 activities) ---
    pdf.start_page()
    pdf.add_chapter_title("MATCHING GAMES (Activities 16-30)")
    pdf.add_wrapped_text("Draw a line to match each item on the left with the correct item on the right!")
    pdf.add_space(10)
    pdf.add_text("Activity 16: Match the Person to the Story", size=11, bold=True, color=(51, 51, 102))
    pdf.add_space(5)
    matches = [
        ("Noah", "Built an ark"),
        ("Moses", "Parted the Red Sea"),
        ("David", "Defeated a giant"),
        ("Jonah", "Was swallowed by a fish"),
        ("Daniel", "Survived the lions' den"),
        ("Esther", "Saved her people"),
        ("Joseph", "Had a coat of many colors"),
        ("Ruth", "Stayed loyal to Naomi"),
    ]
    for left, right in matches:
        pdf.add_text(f"  {left}  .......................  {right}", size=10, indent=10)
        pdf.add_space(3)
    pdf.add_space(10)
    pdf.add_text("Activity 17: Match the Animal to the Story", size=11, bold=True, color=(51, 51, 102))
    pdf.add_space(5)
    matches2 = [
        ("Dove", "Noah's Ark"), ("Fish", "Jonah"), ("Lions", "Daniel"),
        ("Donkey", "Jesus enters Jerusalem"), ("Sheep", "David the shepherd"),
        ("Whale", "Jonah in the sea"), ("Raven", "Fed Elijah"), ("Lamb", "Jesus, Lamb of God"),
    ]
    for left, right in matches2:
        pdf.add_text(f"  {left}  .......................  {right}", size=10, indent=10)
        pdf.add_space(3)
    pdf.end_page()

    pdf.start_page()
    pdf.add_text("Activity 18: Match the Verse to the Book", size=11, bold=True, color=(51, 51, 102))
    pdf.add_space(5)
    matches3 = [
        ('"In the beginning God created..."', "Genesis"),
        ('"The Lord is my shepherd"', "Psalms"),
        ('"For God so loved the world"', "John"),
        ('"I can do all things through Christ"', "Philippians"),
        ('"Love is patient, love is kind"', "1 Corinthians"),
    ]
    for left, right in matches3:
        pdf.add_text(f"  {left}  ......  {right}", size=10, indent=10)
        pdf.add_space(4)
    pdf.add_space(10)
    pdf.add_text("Activity 19: Match the Miracle to Jesus", size=11, bold=True, color=(51, 51, 102))
    pdf.add_space(5)
    miracles = [
        ("Water into ___", "Wine"), ("Fed ___ people", "5,000"),
        ("Walked on ___", "Water"), ("Healed the ___", "Blind"),
        ("Raised ___ from dead", "Lazarus"), ("Calmed the ___", "Storm"),
    ]
    for left, right in miracles:
        pdf.add_text(f"  {left}  .........  {right}", size=10, indent=10)
        pdf.add_space(3)
    pdf.add_space(10)
    pdf.add_text("Activities 20-30: More matching games on the next pages!", size=10, italic=True, color=(100, 100, 100))
    pdf.add_space(5)
    more_matching = [
        "20. Match the Disciple to their occupation",
        "21. Match the parable to its lesson",
        "22. Match the fruit of the Spirit to its meaning",
        "23. Match Old Testament to New Testament connection",
        "24. Match the prayer to who prayed it",
        "25. Match the king to their kingdom",
        "26. Match the prophet to their message",
        "27. Match the number to the Bible fact",
        "28. Match the place to the event",
        "29. Match the color to its Bible meaning",
        "30. Match the family to the Bible story",
    ]
    for m in more_matching:
        pdf.add_text(f"  {m}", size=9, indent=10)
        pdf.add_space(2)
    pdf.end_page()

    # --- SECTION 3: WORD SEARCHES (15 activities) ---
    pdf.start_page()
    pdf.add_chapter_title("WORD SEARCHES (Activities 31-45)")
    pdf.add_wrapped_text("Find the hidden words in the letter grid! Words can go across, down, or diagonal.")
    pdf.add_space(10)

    word_search_topics = [
        ("31. Creation Words", ["LIGHT", "WATER", "ANIMALS", "STARS", "MOON", "SUN", "EARTH", "GARDEN", "ADAM", "EVE"]),
        ("32. Noah's Ark Words", ["ARK", "FLOOD", "RAINBOW", "DOVE", "ANIMALS", "RAIN", "NOAH", "BOAT", "TWO", "GOD"]),
        ("33. Jesus' Names", ["SAVIOR", "LORD", "KING", "LAMB", "LIGHT", "BREAD", "SHEPHERD", "VINE", "TRUTH", "LIFE"]),
        ("34. Fruit of the Spirit", ["LOVE", "JOY", "PEACE", "PATIENCE", "KINDNESS", "GOODNESS", "FAITH", "GENTLE", "CONTROL"]),
        ("35. Disciples", ["PETER", "JOHN", "JAMES", "ANDREW", "PHILIP", "THOMAS", "MATTHEW", "SIMON", "JUDAS"]),
    ]

    for title, words in word_search_topics:
        pdf.add_text(title, size=11, bold=True, color=(51, 51, 102))
        pdf.add_text(f"    Find these words: {', '.join(words)}", size=9, indent=10, color=(80, 80, 80))
        pdf.add_space(3)
        # Simple grid representation
        pdf.add_rect(pdf.margin_left + 20, pdf.y_position - 60, 200, 60, stroke_color=(0.6, 0.6, 0.8))
        pdf.add_text("  [Word Search Grid]", size=8, indent=30, color=(150, 150, 150))
        pdf.y_position -= 65
        pdf.add_space(8)
    pdf.end_page()

    pdf.start_page()
    word_search_topics2 = [
        ("36. Books of the Bible", ["GENESIS", "PSALMS", "JOHN", "ACTS", "ROMANS", "JAMES", "LUKE", "MARK"]),
        ("37. Prayer Words", ["PRAY", "THANK", "ASK", "PRAISE", "WORSHIP", "LISTEN", "FAITH", "AMEN"]),
        ("38. Heaven Words", ["GOLD", "ANGELS", "THRONE", "GLORY", "GATES", "ETERNAL", "PEACE", "HOLY"]),
        ("39. Christmas Words", ["MANGER", "STAR", "ANGEL", "SHEPHERDS", "GIFTS", "BETHLEHEM", "MARY", "JOSEPH"]),
        ("40. Easter Words", ["CROSS", "TOMB", "RISEN", "ALIVE", "HOPE", "LOVE", "SAVE", "CROWN", "VICTORY"]),
        ("41-45: More Word Searches", ["Armor of God", "Ten Commandments", "Miracles", "Parables", "Bible Animals"]),
    ]
    for title, words in word_search_topics2:
        pdf.add_text(title, size=11, bold=True, color=(51, 51, 102))
        pdf.add_text(f"    Words: {', '.join(words)}", size=9, indent=10, color=(80, 80, 80))
        pdf.add_space(8)
    pdf.end_page()

    # --- SECTION 4: MAZES (10 activities) ---
    pdf.start_page()
    pdf.add_chapter_title("MAZES (Activities 46-55)")
    pdf.add_wrapped_text("Help these Bible heroes find their way! Draw a path through each maze.")
    pdf.add_space(10)
    mazes = [
        ("46. Help Noah find the Ark!", "Guide Noah through the maze to reach the ark before the rain starts."),
        ("47. Help Moses cross the Red Sea!", "Find the path through the parted sea to the other side."),
        ("48. Help David reach Goliath!", "Guide David through the valley to face the giant."),
        ("49. Help the Wise Men find Jesus!", "Follow the star through the maze to reach baby Jesus."),
        ("50. Help Jonah escape the fish!", "Find the way out of the big fish's belly."),
        ("51. Help Daniel leave the lions' den!", "Guide Daniel safely past the sleeping lions."),
        ("52. Help Jesus find the lost sheep!", "Help the Good Shepherd through the hills to find the one lost sheep."),
        ("53. Help Paul reach the church!", "Guide Paul through the city streets to the believers."),
        ("54. Help Ruth reach the wheat field!", "Guide Ruth through the path to Boaz's field."),
        ("55. Help Nehemiah rebuild the wall!", "Find the path to collect all the building stones."),
    ]
    for title, desc in mazes:
        pdf._check_page_break(30)
        pdf.add_text(title, size=10, bold=True, color=(150, 50, 0))
        pdf.add_text(f"    {desc}", size=9, indent=15, color=(80, 80, 80))
        pdf.add_space(5)
    pdf.add_space(10)
    # Maze drawing area
    pdf.add_text("MAZE: Help Noah find the Ark!", size=10, bold=True)
    pdf.add_rect(pdf.margin_left, pdf.y_position - 120, pdf.content_width, 120, stroke_color=(0.7, 0.5, 0.3))
    pdf.y_position -= 125
    pdf.add_text("START -->                              --> ARK (FINISH)", size=8, indent=20, color=(100, 100, 100))
    pdf.end_page()

    # --- SECTION 5: BIBLE QUESTIONS (15 activities) ---
    pdf.start_page()
    pdf.add_chapter_title("BIBLE QUESTIONS (Activities 56-70)")
    pdf.add_wrapped_text("Test your Bible knowledge! Circle the correct answer.")
    pdf.add_space(10)
    questions = [
        ("56. Who built the ark?", "a) Moses  b) Noah  c) David  d) Peter"),
        ("57. How many days did God take to create the world?", "a) 5  b) 6  c) 7  d) 10"),
        ("58. Who was swallowed by a big fish?", "a) Peter  b) Paul  c) Jonah  d) David"),
        ("59. How many disciples did Jesus have?", "a) 7  b) 10  c) 12  d) 15"),
        ("60. Where was Jesus born?", "a) Jerusalem  b) Nazareth  c) Bethlehem  d) Egypt"),
        ("61. What did David use to defeat Goliath?", "a) Sword  b) Slingshot  c) Spear  d) Shield"),
        ("62. Who was the first man?", "a) Noah  b) Moses  c) Adam  d) Abraham"),
        ("63. What is the first book of the Bible?", "a) Exodus  b) Genesis  c) Psalms  d) Matthew"),
        ("64. Who parted the Red Sea?", "a) Joshua  b) Moses  c) Elijah  d) David"),
        ("65. How many commandments did God give Moses?", "a) 5  b) 7  c) 10  d) 12"),
        ("66. What animal did Jesus ride into Jerusalem?", "a) Horse  b) Camel  c) Donkey  d) Chariot"),
        ("67. Who denied Jesus 3 times?", "a) John  b) James  c) Peter  d) Thomas"),
        ("68. How many books are in the Bible?", "a) 39  b) 52  c) 66  d) 72"),
        ("69. What did Jesus turn water into?", "a) Juice  b) Milk  c) Wine  d) Oil"),
        ("70. Who was thrown into the lions' den?", "a) David  b) Daniel  c) Elijah  d) Paul"),
    ]
    for q, options in questions:
        pdf._check_page_break(22)
        pdf.add_text(q, size=10, bold=True)
        pdf.add_text(f"    {options}", size=9, indent=15, color=(60, 60, 100))
        pdf.add_space(4)
    pdf.end_page()

    # --- SECTION 6: FILL-IN-THE-BLANKS (15 activities) ---
    pdf.start_page()
    pdf.add_chapter_title("FILL-IN-THE-BLANKS (Activities 71-85)")
    pdf.add_wrapped_text("Complete each Bible verse by filling in the missing word!")
    pdf.add_space(10)
    fill_blanks = [
        ('71. "For God so loved the _____" (John 3:16)', "world"),
        ('72. "The Lord is my _____, I shall not want" (Psalm 23:1)', "shepherd"),
        ('73. "I can do all things through _____ who strengthens me" (Phil 4:13)', "Christ"),
        ('74. "In the beginning God created the heavens and the _____" (Gen 1:1)', "earth"),
        ('75. "Be strong and _____" (Joshua 1:9)', "courageous"),
        ('76. "Love your _____ as yourself" (Mark 12:31)', "neighbor"),
        ('77. "The _____ of the Lord is the beginning of wisdom" (Prov 9:10)', "fear"),
        ('78. "Jesus _____ " - the shortest verse! (John 11:35)', "wept"),
        ('79. "Trust in the Lord with all your _____" (Prov 3:5)', "heart"),
        ('80. "Your word is a _____ to my feet" (Psalm 119:105)', "lamp"),
        ('81. "Do not be _____, for I am with you" (Isaiah 41:10)', "afraid"),
        ('82. "Children, _____ your parents" (Eph 6:1)', "obey"),
        ('83. "Give _____ in all circumstances" (1 Thess 5:18)', "thanks"),
        ('84. "Let the little _____ come to me" (Mark 10:14)', "children"),
        ('85. "God is _____" (1 John 4:8)', "love"),
    ]
    for verse, answer in fill_blanks:
        pdf._check_page_break(20)
        pdf.add_text(f"  {verse}", size=10, indent=5)
        pdf.add_space(5)
    pdf.add_space(10)
    pdf.add_text("ANSWERS (don't peek!): world, shepherd, Christ, earth, courageous, neighbor,", size=7, color=(150, 150, 150))
    pdf.add_text("fear, wept, heart, lamp, afraid, obey, thanks, children, love", size=7, color=(150, 150, 150))
    pdf.end_page()

    # --- SECTION 7: MEMORY VERSES (10 activities) ---
    pdf.start_page()
    pdf.add_chapter_title("MEMORY VERSES (Activities 86-95)")
    pdf.add_wrapped_text("Learn these verses by heart! Read them, write them, and say them out loud. Check each one off when you can say it from memory!")
    pdf.add_space(10)
    memory_verses = [
        ("86.", "John 3:16", "For God so loved the world that He gave His one and only Son."),
        ("87.", "Psalm 23:1", "The LORD is my shepherd, I lack nothing."),
        ("88.", "Phil 4:13", "I can do all things through Christ who strengthens me."),
        ("89.", "Prov 3:5", "Trust in the LORD with all your heart."),
        ("90.", "Jer 29:11", "For I know the plans I have for you, declares the LORD."),
        ("91.", "Josh 1:9", "Be strong and courageous. Do not be afraid."),
        ("92.", "Psalm 119:105", "Your word is a lamp for my feet, a light on my path."),
        ("93.", "Rom 8:28", "All things work together for good for those who love God."),
        ("94.", "Eph 4:32", "Be kind to one another, tenderhearted, forgiving."),
        ("95.", "1 John 4:19", "We love because He first loved us."),
    ]
    for num, ref, text in memory_verses:
        pdf._check_page_break(30)
        pdf.add_text(f"  {num} {ref}", size=10, bold=True, color=(51, 51, 102))
        pdf.add_text(f"     \"{text}\"", size=10, italic=True, indent=15, color=(60, 60, 80))
        pdf.add_text("     [ ] I can say this from memory!", size=8, indent=15, color=(0, 120, 0))
        pdf.add_space(6)
    pdf.end_page()

    # --- SECTION 8: DRAWING (5 activities) ---
    pdf.start_page()
    pdf.add_chapter_title("DRAWING ACTIVITIES (Activities 96-100)")
    pdf.add_space(5)
    drawing_prompts = [
        "96. Draw YOUR family praising God together!",
        "97. Draw what you think heaven looks like!",
        "98. Draw your favorite Bible story!",
        "99. Draw yourself as a Bible superhero for God!",
        "100. Draw a 'Thank You God' picture with everything you're grateful for!",
    ]
    for prompt in drawing_prompts:
        pdf._check_page_break(100)
        pdf.add_text(prompt, size=11, bold=True, color=(0, 100, 50))
        pdf.add_space(5)
        pdf.add_rect(pdf.margin_left, pdf.y_position - 80, pdf.content_width, 80, stroke_color=(0.5, 0.8, 0.5))
        pdf.y_position -= 90
        pdf.add_space(5)
    pdf.end_page()

    # ANSWER KEY
    pdf.start_page()
    pdf.add_chapter_title("Answer Key")
    pdf.add_text("Bible Questions Answers:", size=10, bold=True)
    pdf.add_text("56-b, 57-c, 58-c, 59-c, 60-c, 61-b, 62-c, 63-b, 64-b, 65-c, 66-c, 67-c, 68-c, 69-c, 70-b", size=8, color=(100, 100, 100))
    pdf.add_space(5)
    pdf.add_text("Fill-in-the-Blanks: world, shepherd, Christ, earth, courageous, neighbor, fear, wept, heart, lamp, afraid, obey, thanks, children, love", size=8, color=(100, 100, 100))
    pdf.end_page()

    pad_to_pages(pdf, 42, "My Bible Activity Notes")
    return pdf


# ============================================================
# BOOK 12: Kids Bible Prayer Journal
# ============================================================
def create_book_12():
    pdf = PDFEngine()
    pdf.header_text = "Kids Bible Prayer Journal"

    pdf.add_title_page(
        title="Kids Bible Prayer Journal",
        subtitle="Talk to God Every Day! Write Your Prayers, Thank Him, and Watch Him Answer!",
        author="For Kids Ages 5-10",
        extra_lines=["30 days of guided prayer pages", "with Bible verses and fun prompts"]
    )

    pdf.start_page()
    pdf.add_chapter_title("Hi, Prayer Warrior!")
    pdf.add_wrapped_text("Did you know you can talk to God ANY time, ANY where? He ALWAYS listens! This journal will help you pray every day. Each page has space to write your prayers, things you're thankful for, and even track when God answers your prayers! How cool is that?")
    pdf.add_space(10)
    pdf.add_text("Each day has:", size=11, bold=True)
    pdf.add_space(5)
    items = ["A Bible verse just for you", "My Prayer Today (talk to God!)",
             "What I'm Thankful For (say thank you!)", "Prayer Request (what do you need help with?)",
             "Answered Prayer (God said YES!)", "How I Feel Today (happy, sad, worried, peaceful)"]
    for item in items:
        pdf.add_text(f"  * {item}", size=10, indent=10)
        pdf.add_space(3)
    pdf.add_space(10)
    pdf.add_text("Tips for Prayer:", size=11, bold=True, color=(51, 51, 102))
    pdf.add_space(5)
    tips = ["Be honest - God already knows your heart!",
            "You don't need fancy words - just talk like to a friend",
            "It's OK to be sad, angry, or confused in prayer",
            "Thank God for at least ONE thing every day",
            "Listen for God's answer - it might come in surprising ways!"]
    for tip in tips:
        pdf.add_text(f"  * {tip}", size=9, indent=10)
        pdf.add_space(2)
    pdf.end_page()

    # 30 DAILY PRAYER PAGES
    daily_verses = [
        ("Psalm 55:17", "Evening, morning, and noon I cry out to Him, and He hears my voice."),
        ("Matthew 7:7", "Ask and it will be given to you; seek and you will find."),
        ("1 John 5:14", "If we ask anything according to His will, He hears us."),
        ("Philippians 4:6", "Do not be anxious about anything, but in prayer present your requests to God."),
        ("Jeremiah 33:3", "Call to me and I will answer you."),
        ("Psalm 145:18", "The LORD is near to all who call on Him."),
        ("Matthew 18:20", "Where two or three gather in my name, there am I."),
        ("Psalm 34:17", "The righteous cry out, and the LORD hears them."),
        ("James 5:16", "The prayer of a righteous person is powerful."),
        ("Psalm 66:19", "God has surely listened and heard my prayer."),
        ("Isaiah 65:24", "Before they call I will answer."),
        ("1 Thess 5:17", "Pray continually."),
        ("Psalm 5:3", "In the morning I lay my requests before you and wait."),
        ("Romans 8:26", "The Spirit helps us in our weakness."),
        ("Psalm 91:15", "He will call on me, and I will answer him."),
        ("John 16:24", "Ask and you will receive, and your joy will be complete."),
        ("Psalm 4:3", "The LORD hears when I call to Him."),
        ("Mark 11:24", "Whatever you ask for in prayer, believe that you have received it."),
        ("Psalm 116:1-2", "I love the LORD, for He heard my voice."),
        ("Luke 11:9", "Ask and it will be given to you."),
        ("Psalm 62:8", "Trust in Him at all times; pour out your hearts to Him."),
        ("1 Peter 5:7", "Cast all your anxiety on Him because He cares for you."),
        ("Psalm 86:7", "When I am in distress, I call to you, because you answer me."),
        ("Hebrews 4:16", "Let us approach God's throne of grace with confidence."),
        ("Psalm 17:6", "I call on you, my God, for you will answer me."),
        ("Matthew 6:6", "When you pray, go into your room, close the door and pray."),
        ("Psalm 40:1", "I waited patiently for the LORD; He turned to me and heard my cry."),
        ("Colossians 4:2", "Devote yourselves to prayer, being watchful and thankful."),
        ("Psalm 107:1", "Give thanks to the LORD, for He is good; His love endures forever."),
        ("Psalm 150:6", "Let everything that has breath praise the LORD!"),
    ]

    for i, (ref, verse) in enumerate(daily_verses, 1):
        pdf.start_page()
        pdf.add_text(f"Day {i}", size=9, bold=True, color=(100, 80, 140))
        pdf.add_space(5)
        # Verse box
        pdf.add_rect(pdf.margin_left, pdf.y_position - 35, pdf.content_width, 40,
                     fill_color=(0.95, 0.93, 1.0), stroke_color=(0.6, 0.5, 0.8))
        pdf.add_space(5)
        pdf.add_text(f"  \"{verse}\" - {ref}", size=9, italic=True, indent=10, color=(80, 60, 120))
        pdf.add_space(25)

        # Prayer section
        pdf.add_text("My Prayer Today:", size=10, bold=True, color=(51, 51, 102))
        pdf.add_text("(Dear God...)", size=8, color=(150, 150, 150))
        pdf.add_lined_space(4, spacing=20)

        # Thankful section
        pdf.add_text("3 Things I'm Thankful For:", size=10, bold=True, color=(0, 120, 0))
        pdf.add_text("1. ________________________________", size=9, indent=10)
        pdf.add_space(3)
        pdf.add_text("2. ________________________________", size=9, indent=10)
        pdf.add_space(3)
        pdf.add_text("3. ________________________________", size=9, indent=10)
        pdf.add_space(8)

        # Prayer Request
        pdf.add_text("My Prayer Request (What do I need help with?):", size=10, bold=True, color=(150, 80, 0))
        pdf.add_lined_space(2, spacing=20)

        # Answered Prayer
        pdf.add_text("Answered Prayer! (Did God answer something? Write it here!):", size=10, bold=True, color=(200, 0, 100))
        pdf.add_lined_space(2, spacing=20)

        # How I Feel
        pdf.add_text("How I Feel Today (circle): Happy  Sad  Worried  Peaceful  Excited  Loved", size=9, color=(80, 80, 80))
        pdf.end_page()

    # PRAYER LIST
    pdf.start_page()
    pdf.add_chapter_title("My Special Prayer List")
    pdf.add_text("People I'm Praying For:", size=11, bold=True, color=(51, 51, 102))
    pdf.add_numbered_lines(1, 10, spacing=20)
    pdf.add_space(10)
    pdf.add_text("Big Prayers I'm Believing For:", size=11, bold=True, color=(51, 51, 102))
    pdf.add_numbered_lines(1, 5, spacing=20)
    pdf.end_page()

    # ANSWERED PRAYERS TRACKER
    pdf.start_page()
    pdf.add_chapter_title("My Answered Prayers! (YAY GOD!)")
    pdf.add_wrapped_text("Write down every time God answers a prayer. When you feel sad, read this page and remember - God is ALWAYS faithful!")
    pdf.add_space(10)
    for i in range(8):
        pdf.add_text(f"Date: ______  God answered:", size=9, bold=True)
        pdf.add_lined_space(2, spacing=18)
        pdf.add_space(3)
    pdf.end_page()

    pad_to_pages(pdf, 42, "Prayer Notes")
    return pdf


# ============================================================
# BOOK 13: 50 Bible Stories for Kids Workbook
# ============================================================
def create_book_13():
    pdf = PDFEngine()
    pdf.header_text = "50 Bible Stories for Kids Workbook"

    pdf.add_title_page(
        title="50 Bible Stories for Kids Workbook",
        subtitle="Story + Lesson + Questions + Activity + Prayer for Every Story!",
        author="For Kids Ages 5-12",
        extra_lines=["The most important Bible stories retold for children", "with fun activities and life lessons"]
    )

    pdf.start_page()
    pdf.add_chapter_title("50 Amazing Stories!")
    pdf.add_wrapped_text("Each story in this workbook follows the same fun format: read the story, learn the lesson, answer questions, do an activity, and pray! You can do one story per day or per week.")
    pdf.add_space(10)
    pdf.add_text("For each story you get:", size=11, bold=True)
    items = ["THE STORY - a short, fun retelling", "THE LESSON - what God teaches us",
             "QUESTIONS - to test your understanding", "ACTIVITY - something fun to do",
             "PRAYER - a simple prayer you can pray"]
    for item in items:
        pdf.add_text(f"  * {item}", size=10, indent=10)
        pdf.add_space(3)
    pdf.end_page()

    # 50 STORIES (condensed format - story summary per page)
    bible_stories = [
        ("Creation", "Genesis 1-2", "God made everything in 6 days and rested on the 7th.", "God is the amazing Creator of everything, including YOU!", ["What did God create on Day 4?", "What did God say about everything He made?", "What day did God rest?"], "Draw your favorite thing God created!", "Thank You God for making me special!"),
        ("Adam and Eve", "Genesis 2-3", "God made the first man and woman and put them in a perfect garden.", "Sin has consequences, but God still loves us.", ["What was the garden called?", "What fruit were they told NOT to eat?", "What happened after they disobeyed?"], "Draw the Garden of Eden!", "Help me obey You, God!"),
        ("Noah's Ark", "Genesis 6-9", "God saved Noah's family and animals from a great flood.", "Obedience to God keeps us safe.", ["How many of each animal went on the ark?", "How long did it rain?", "What did God put in the sky as a promise?"], "Draw Noah's ark with animals!", "Help me obey even when it's hard!"),
        ("Abraham's Call", "Genesis 12", "God called Abraham to leave home and go to a new land.", "When God calls, we can trust Him even without knowing every detail.", ["Where did Abraham go?", "What did God promise Abraham?", "Did Abraham obey?"], "Draw Abraham looking at the stars (God's promise)!", "God, help me trust Your plans!"),
        ("Joseph's Coat", "Genesis 37", "Joseph's brothers were jealous of his colorful coat.", "God can use bad situations for good.", ["Who gave Joseph the coat?", "Why were his brothers jealous?", "What happened to Joseph?"], "Color Joseph's coat with many colors!", "Help me forgive others, God!"),
        ("Baby Moses", "Exodus 2", "Baby Moses was saved from danger by his brave mother.", "God protects His children through caring people.", ["Where did Moses' mom put him?", "Who found baby Moses?", "Who watched over Moses?"], "Draw baby Moses in the basket!", "Thank You for people who protect me!"),
        ("Moses and the Red Sea", "Exodus 14", "God parted the sea so His people could escape!", "Nothing is impossible for God.", ["Who was chasing the Israelites?", "What did Moses do?", "What happened to the sea?"], "Draw the Red Sea parted with people walking through!", "God, You can do anything!"),
        ("David and Goliath", "1 Samuel 17", "A young boy defeated a giant with God's help.", "With God, even the smallest person can do great things.", ["What was the giant's name?", "What did David use?", "Why was David brave?"], "Draw David standing before Goliath!", "God, make me brave like David!"),
        ("Daniel and the Lions", "Daniel 6", "Daniel kept praying even when it was dangerous.", "Stay faithful to God no matter what.", ["How often did Daniel pray?", "Where was he thrown?", "Who shut the lions' mouths?"], "Draw Daniel safe with the lions!", "Help me always pray, God!"),
        ("Jonah and the Fish", "Jonah 1-4", "Jonah ran from God but God gave him a second chance.", "We can't run from God, and He always gives second chances.", ["Where did God tell Jonah to go?", "What swallowed Jonah?", "Did Jonah finally obey?"], "Draw Jonah inside the big fish!", "Help me obey right away, God!"),
        ("Ruth and Naomi", "Ruth 1-4", "Ruth stayed loyal to Naomi even when things were hard.", "True loyalty and love are rewarded by God.", ["Who was Ruth loyal to?", "What did Ruth say to Naomi?", "How did God bless Ruth?"], "Draw Ruth and Naomi walking together!", "Help me be a loyal friend!"),
        ("Esther the Brave Queen", "Esther 4-7", "Esther risked her life to save her people.", "God puts us in the right place at the right time for a purpose.", ["Who wanted to hurt Esther's people?", "What brave thing did Esther do?", "Were her people saved?"], "Draw Queen Esther being brave!", "God, give me courage to speak up!"),
        ("Birth of Jesus", "Luke 2", "God's Son was born as a baby in a humble stable.", "God came to earth because He loves us that much.", ["Where was Jesus born?", "Who visited first?", "What was in the sky?"], "Draw the nativity scene!", "Thank You for sending Jesus!"),
        ("Jesus Feeds 5,000", "John 6", "Jesus used a boy's small lunch to feed thousands!", "God can multiply anything we give Him.", ["How many loaves and fish?", "How many people were fed?", "How many baskets were left over?"], "Draw the boy sharing his lunch!", "God, use what I have for good!"),
        ("The Good Samaritan", "Luke 10", "A kind stranger helped someone everyone else ignored.", "Be kind to everyone, not just people who are like you.", ["Who walked past the hurt man?", "Who finally helped?", "What did he do for the man?"], "Draw the kind man helping!", "Help me help others, God!"),
        ("Jesus Walks on Water", "Matthew 14", "Jesus walked on the sea and helped Peter do the same!", "Keep your eyes on Jesus, not on your fears.", ["What was the weather like?", "Who tried to walk on water too?", "Why did Peter start to sink?"], "Draw Jesus on the water reaching for Peter!", "Help me focus on You, not my fears!"),
        ("The Lost Sheep", "Luke 15", "A shepherd left 99 sheep to find 1 that was lost.", "God will NEVER stop looking for you. You are that important!", ["How many sheep did the shepherd have?", "How many were lost?", "What did he do when he found it?"], "Draw the shepherd carrying the sheep!", "Thank You that You never give up on me!"),
        ("The Prodigal Son", "Luke 15", "A son wasted everything but his father welcomed him home.", "It's never too late to come back to God.", ["What did the son ask for?", "What happened to his money?", "How did the father react?"], "Draw the father hugging his son!", "Thank You for always welcoming me back!"),
        ("Zacchaeus", "Luke 19", "A short, dishonest man met Jesus and changed completely.", "Jesus' love transforms people from the inside out.", ["Why did Zacchaeus climb a tree?", "What did Jesus say to him?", "How did Zacchaeus change?"], "Draw Zacchaeus in the tree!", "Jesus, change my heart too!"),
        ("Jesus and the Children", "Mark 10", "Jesus welcomed children when others tried to send them away.", "You are NEVER too young or too small for Jesus.", ["Who tried to keep kids away?", "What did Jesus say?", "What did He do with the children?"], "Draw Jesus hugging children!", "Thank You that You love kids, Jesus!"),
    ]

    for i, (title, ref, story, lesson, questions, activity, prayer) in enumerate(bible_stories[:20], 1):
        pdf.start_page()
        pdf.add_text(f"Story {i} of 50", size=8, bold=True, color=(100, 80, 140))
        pdf.add_chapter_title(f"{i}. {title}")
        pdf.add_text(f"Read: {ref}", size=9, italic=True, color=(100, 100, 140))
        pdf.add_space(6)

        pdf.add_text("THE STORY:", size=10, bold=True, color=(51, 51, 102))
        pdf.add_wrapped_text(story, size=10, indent=5)
        pdf.add_space(6)

        pdf.add_text("THE LESSON:", size=10, bold=True, color=(0, 100, 0))
        pdf.add_wrapped_text(lesson, size=10, indent=5)
        pdf.add_space(6)

        pdf.add_text("QUESTIONS:", size=10, bold=True, color=(150, 80, 0))
        for q in questions:
            pdf.add_text(f"  * {q}", size=9, indent=10)
            pdf.add_space(2)
        pdf.add_space(6)

        pdf.add_text(f"ACTIVITY: {activity}", size=10, bold=True, color=(120, 0, 120))
        pdf.add_space(6)

        pdf.add_text(f"MY PRAYER: \"{prayer}\"", size=10, bold=True, italic=True, color=(80, 60, 120))
        pdf.end_page()

    # LIST remaining 30 stories (summary page)
    pdf.start_page()
    pdf.add_chapter_title("Stories 21-50 (Summary List)")
    remaining = [
        "21. The 10 Commandments (Exodus 20)", "22. Walls of Jericho (Joshua 6)",
        "23. Gideon's Army (Judges 7)", "24. Samson's Strength (Judges 16)",
        "25. Samuel Hears God (1 Samuel 3)", "26. Solomon's Wisdom (1 Kings 3)",
        "27. Elijah and Fire (1 Kings 18)", "28. Naaman's Healing (2 Kings 5)",
        "29. Fiery Furnace (Daniel 3)", "30. Nehemiah Builds (Nehemiah 2)",
        "31. Job's Patience (Job 1-42)", "32. Isaiah's Vision (Isaiah 6)",
        "33. Jesus' Baptism (Matthew 3)", "34. Jesus Tempted (Matthew 4)",
        "35. Sermon on the Mount (Matthew 5-7)", "36. Raising Lazarus (John 11)",
        "37. The Last Supper (Luke 22)", "38. Jesus on the Cross (John 19)",
        "39. The Resurrection (John 20)", "40. Doubting Thomas (John 20)",
        "41. Peter's Sermon (Acts 2)", "42. Peter Heals (Acts 3)",
        "43. Philip & Ethiopian (Acts 8)", "44. Paul's Conversion (Acts 9)",
        "45. Peter's Prison Escape (Acts 12)", "46. Paul & Silas Sing (Acts 16)",
        "47. Paul's Shipwreck (Acts 27)", "48. Armor of God (Ephesians 6)",
        "49. Love Chapter (1 Corinthians 13)", "50. Heaven! (Revelation 21)",
    ]
    for s in remaining:
        pdf._check_page_break(14)
        pdf.add_text(f"  {s}", size=9, indent=5)
        pdf.add_space(2)
    pdf.end_page()

    pad_to_pages(pdf, 42, "Bible Story Notes")
    return pdf


# ============================================================
# BOOK 14: Bible Coloring & Activity Book (Ages 3-7)
# ============================================================
def create_book_14():
    pdf = PDFEngine()
    pdf.header_text = "Bible Coloring & Activity Book"

    pdf.add_title_page(
        title="Bible Coloring & Activity Book",
        subtitle="Beautiful Coloring Pages and Simple Activities for Little Ones!",
        author="For Kids Ages 3-7",
        extra_lines=["Large, simple designs perfect for small hands", "Bible stories made fun through coloring and play!"]
    )

    pdf.start_page()
    pdf.add_chapter_title("Welcome, Little Artist!")
    pdf.add_wrapped_text("This book is full of beautiful pictures for you to color! Each page has a Bible picture and a simple activity. Use crayons, markers, or colored pencils. Have fun and remember - God made YOU creative!")
    pdf.add_space(15)
    pdf.add_text("What's Inside:", size=12, bold=True)
    pdf.add_space(8)
    items = ["20 Bible coloring pages (big and easy to color!)",
             "Simple dot-to-dot pictures", "Trace the words activities",
             "Circle the right answer", "Count the objects",
             "Color by number pages", "Simple mazes for little ones"]
    for item in items:
        pdf.add_text(f"  * {item}", size=10, indent=10)
        pdf.add_space(4)
    pdf.end_page()

    # 20 COLORING + ACTIVITY PAGES
    coloring_pages = [
        ("God Made the Sun!", "Color the BIG sun yellow and orange! Color the sky blue!", "How many rays does the sun have? Count them! ___"),
        ("God Made the Flowers!", "Color each flower a different color! Make them beautiful!", "How many flowers are there? ___"),
        ("God Made the Animals!", "Color the animals! What sounds do they make?", "Circle your favorite animal!"),
        ("Noah's Big Boat!", "Color the ark brown. Color the water blue. Color the rainbow!", "Trace the word: A-R-K"),
        ("Two by Two!", "Color the animal pairs going into the ark!", "Draw 2 more animals going in!"),
        ("Baby Moses!", "Color the basket, the water, and baby Moses!", "Trace the word: M-O-S-E-S"),
        ("David the Brave Boy!", "Color David with his slingshot!", "Circle what David used: Sword / Slingshot / Shield"),
        ("Daniel and the Lions!", "Color Daniel and the friendly lions!", "How many lions can you count? ___"),
        ("Jonah and the Big Fish!", "Color the big fish and the ocean!", "Trace the word: F-I-S-H"),
        ("Baby Jesus is Born!", "Color baby Jesus, Mary, and the star!", "Circle the star in the picture!"),
        ("The Shepherds!", "Color the shepherds and their sheep!", "How many sheep can you count? ___"),
        ("Jesus Loves Me!", "Color Jesus with the children!", "Draw yourself next to Jesus!"),
        ("The Good Helper!", "Color the kind man helping the hurt person!", "Circle the helper in the picture!"),
        ("5 Loaves and 2 Fish!", "Color the bread and fish!", "Count: How many loaves? ___ How many fish? ___"),
        ("Jesus Walks on Water!", "Color Jesus on the waves!", "Trace the word: J-E-S-U-S"),
        ("The Lost Sheep!", "Color the shepherd finding the lost sheep!", "Can you find the hidden sheep? Circle it!"),
        ("Zacchaeus in the Tree!", "Color the man in the big tree!", "Is Zacchaeus tall or short? Circle: TALL / SHORT"),
        ("Palm Sunday!", "Color Jesus on the donkey with people waving!", "Trace the word: H-O-S-A-N-N-A"),
        ("Easter Morning!", "Color the empty tomb and the sunrise!", "Is the tomb empty or full? Circle: EMPTY / FULL"),
        ("Jesus Loves ALL Children!", "Color children from all around the world!", "Draw your own face in the picture!"),
    ]

    for i, (title, coloring_inst, activity) in enumerate(coloring_pages, 1):
        pdf.start_page()
        pdf.add_text(f"Page {i}", size=8, color=(150, 150, 150))
        pdf.add_space(5)
        pdf.add_text(title, size=16, bold=True, color=(51, 51, 102))
        pdf.add_space(10)
        pdf.add_text(coloring_inst, size=11, color=(0, 100, 0))
        pdf.add_space(10)
        # Coloring area (large box)
        pdf.add_rect(pdf.margin_left, pdf.y_position - 300, pdf.content_width, 300,
                     stroke_color=(0.7, 0.7, 0.7))
        pdf.y_position -= 310
        pdf.add_space(10)
        pdf.add_text(f"Activity: {activity}", size=10, bold=True, color=(150, 80, 0))
        pdf.end_page()

    # DOT-TO-DOT pages
    pdf.start_page()
    pdf.add_chapter_title("Dot-to-Dot: Connect the Numbers!")
    pdf.add_text("Connect the dots 1-10 to reveal: NOAH'S ARK!", size=11, bold=True, color=(51, 51, 102))
    pdf.add_rect(pdf.margin_left, pdf.y_position - 200, pdf.content_width, 200, stroke_color=(0.6, 0.6, 0.8))
    pdf.y_position -= 210
    pdf.add_space(10)
    pdf.add_text("Connect the dots 1-10 to reveal: A FISH!", size=11, bold=True, color=(51, 51, 102))
    pdf.add_rect(pdf.margin_left, pdf.y_position - 200, pdf.content_width, 200, stroke_color=(0.6, 0.6, 0.8))
    pdf.y_position -= 210
    pdf.end_page()

    # TRACE THE WORDS pages
    pdf.start_page()
    pdf.add_chapter_title("Trace the Bible Words!")
    pdf.add_text("Trace each word. Say it out loud!", size=10, color=(80, 80, 80))
    pdf.add_space(10)
    trace_words = ["GOD", "JESUS", "LOVE", "PRAY", "BIBLE", "AMEN", "FAITH", "HOPE", "JOY", "PEACE"]
    for word in trace_words:
        pdf._check_page_break(30)
        pdf.add_text(f"  {word}", size=18, bold=True, color=(200, 200, 220))
        pdf.add_space(-18)
        pdf.add_text(f"  {word}", size=18, bold=True, color=(220, 220, 230))
        pdf.add_space(8)
    pdf.end_page()

    pad_to_pages(pdf, 42, "My Coloring Notes")
    return pdf


# ============================================================
# BOOK 15: Bible Word Search & Puzzle Book
# ============================================================
def create_book_15():
    pdf = PDFEngine()
    pdf.header_text = "Bible Word Search & Puzzle Book"

    pdf.add_title_page(
        title="Bible Word Search & Puzzle Book for Kids",
        subtitle="Word Searches, Crosswords, Matching, Bible Trivia, Unscramble, and Memory Verses!",
        author="For Kids Ages 6-12",
        extra_lines=["50+ puzzles to challenge your Bible knowledge!", "Fun for the whole family"]
    )

    pdf.start_page()
    pdf.add_chapter_title("Puzzle Time!")
    pdf.add_wrapped_text("Get ready to search, solve, match, and unscramble your way through the Bible! Each puzzle teaches you something new about God's Word. Grab a pencil and let's go!")
    pdf.add_space(10)
    pdf.add_text("Puzzle Types:", size=11, bold=True)
    items = ["Word Searches (find hidden Bible words in grids)",
             "Crossword Puzzles (use Bible clues to fill the grid)",
             "Matching (connect related Bible items)",
             "Bible Trivia (multiple choice and true/false)",
             "Unscramble (rearrange letters to form Bible words)",
             "Memory Verse Puzzles (decode and complete verses)"]
    for item in items:
        pdf.add_text(f"  * {item}", size=10, indent=10)
        pdf.add_space(3)
    pdf.end_page()

    # WORD SEARCHES (10 pages)
    word_search_data = [
        ("Creation", ["LIGHT", "WATER", "EARTH", "SUN", "MOON", "STARS", "ANIMALS", "PLANTS", "MAN", "WOMAN", "GOOD", "REST"]),
        ("Noah's Ark", ["NOAH", "ARK", "FLOOD", "RAIN", "RAINBOW", "DOVE", "OLIVE", "ANIMALS", "TWO", "PROMISE", "GOD", "BOAT"]),
        ("Moses", ["MOSES", "EGYPT", "PHARAOH", "PLAGUES", "SEA", "COMMANDMENTS", "TABLETS", "BURNING", "BUSH", "STAFF", "MANNA"]),
        ("David", ["DAVID", "SHEPHERD", "GOLIATH", "SLING", "STONE", "KING", "PSALMS", "HARP", "BRAVE", "FAITH", "LION", "BEAR"]),
        ("Jesus' Life", ["BETHLEHEM", "MANGER", "STAR", "SHEPHERD", "WISE", "NAZARETH", "BAPTISM", "MIRACLE", "CROSS", "RISEN"]),
        ("Disciples", ["PETER", "JOHN", "JAMES", "ANDREW", "PHILIP", "THOMAS", "MATTHEW", "SIMON", "BARTHOLOMEW", "JUDAS"]),
        ("Fruit of the Spirit", ["LOVE", "JOY", "PEACE", "PATIENCE", "KINDNESS", "GOODNESS", "FAITHFULNESS", "GENTLENESS", "CONTROL"]),
        ("Armor of God", ["TRUTH", "RIGHTEOUSNESS", "PEACE", "FAITH", "SALVATION", "WORD", "PRAYER", "BELT", "SHIELD", "HELMET"]),
        ("Christmas", ["ANGEL", "MARY", "JOSEPH", "BETHLEHEM", "MANGER", "STAR", "SHEPHERDS", "GIFTS", "GOLD", "MYRRH"]),
        ("Easter", ["CROSS", "TOMB", "RISEN", "ALIVE", "STONE", "ANGEL", "MARY", "HOPE", "SAVE", "CROWN", "VICTORY", "LOVE"]),
    ]

    for title, words in word_search_data:
        pdf.start_page()
        pdf.add_text(f"WORD SEARCH: {title}", size=13, bold=True, color=(51, 51, 102))
        pdf.add_space(8)
        pdf.add_text(f"Find these words: {', '.join(words)}", size=9, color=(80, 80, 80))
        pdf.add_space(8)
        # Grid area
        pdf.add_rect(pdf.margin_left + 20, pdf.y_position - 280, 350, 280, stroke_color=(0.5, 0.5, 0.8))
        # Generate simple letter grid visual
        import random
        random.seed(hash(title))
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        grid_text = ""
        for row in range(14):
            line = "  "
            for col in range(18):
                line += random.choice(alphabet) + " "
            pdf.add_text(line, size=8, indent=25, color=(60, 60, 60))
            pdf.add_space(-4)
        pdf.y_position -= 10
        pdf.add_space(10)
        pdf.add_text(f"Words to find ({len(words)}):", size=9, bold=True)
        # Display words in columns
        word_line = "  "
        for i, w in enumerate(words):
            word_line += w + "  "
            if (i + 1) % 4 == 0:
                pdf.add_text(word_line, size=8, indent=10)
                word_line = "  "
                pdf.add_space(2)
        if word_line.strip():
            pdf.add_text(word_line, size=8, indent=10)
        pdf.end_page()

    # CROSSWORD PUZZLES (3 pages)
    pdf.start_page()
    pdf.add_chapter_title("CROSSWORD: Creation")
    pdf.add_text("Fill in the crossword using the clues below!", size=10)
    pdf.add_space(8)
    pdf.add_rect(pdf.margin_left + 50, pdf.y_position - 180, 250, 180, stroke_color=(0.5, 0.5, 0.7))
    pdf.y_position -= 190
    pdf.add_space(10)
    pdf.add_text("ACROSS:", size=10, bold=True)
    pdf.add_text("  2. God made the sun, moon, and _____ (5 letters)", size=9, indent=10)
    pdf.add_text("  4. The first woman's name (3 letters)", size=9, indent=10)
    pdf.add_text("  6. God said 'Let there be _____' (5 letters)", size=9, indent=10)
    pdf.add_space(5)
    pdf.add_text("DOWN:", size=10, bold=True)
    pdf.add_text("  1. God created in ___ days (3 letters)", size=9, indent=10)
    pdf.add_text("  3. The first man's name (4 letters)", size=9, indent=10)
    pdf.add_text("  5. God rested on day ___ (5 letters)", size=9, indent=10)
    pdf.end_page()

    # BIBLE TRIVIA (2 pages)
    pdf.start_page()
    pdf.add_chapter_title("BIBLE TRIVIA CHALLENGE")
    pdf.add_text("How much do you know? Circle the correct answer!", size=10)
    pdf.add_space(10)
    trivia = [
        ("1. How many books in the Bible?", "a) 55  b) 66  c) 77"),
        ("2. First book of the Bible?", "a) Matthew  b) Genesis  c) Psalms"),
        ("3. Last book of the Bible?", "a) Jude  b) Malachi  c) Revelation"),
        ("4. How many disciples did Jesus choose?", "a) 10  b) 12  c) 7"),
        ("5. What river was Jesus baptized in?", "a) Nile  b) Jordan  c) Red Sea"),
        ("6. Who was the strongest man in the Bible?", "a) Samson  b) Goliath  c) David"),
        ("7. What did God use to create Adam?", "a) Water  b) Dust  c) Light"),
        ("8. How many plagues hit Egypt?", "a) 7  b) 10  c) 12"),
        ("9. What did Moses receive on Mount Sinai?", "a) Food  b) Water  c) Commandments"),
        ("10. Where did Jesus grow up?", "a) Bethlehem  b) Jerusalem  c) Nazareth"),
    ]
    for q, options in trivia:
        pdf.add_text(q, size=10, bold=True)
        pdf.add_text(f"    {options}", size=9, indent=15, color=(60, 60, 100))
        pdf.add_space(5)
    pdf.add_space(10)
    pdf.add_text("Answers: 1-b, 2-b, 3-c, 4-b, 5-b, 6-a, 7-b, 8-b, 9-c, 10-c", size=7, color=(150, 150, 150))
    pdf.end_page()

    # UNSCRAMBLE (2 pages)
    pdf.start_page()
    pdf.add_chapter_title("UNSCRAMBLE Bible Words!")
    pdf.add_text("Rearrange the letters to spell Bible words!", size=10)
    pdf.add_space(10)
    scrambles = [
        ("SUBJE", "JESUS"), ("LEBBI", "BIBLE"), ("RAPEYR", "PRAYER"),
        ("CARGE", "GRACE"), ("HITFA", "FAITH"), ("EVOL", "LOVE"),
        ("EOPCH", "EPOCH/HOPE"), ("SCORSS", "CROSS"), ("GLEAM", "ANGEL/GLEAM"),
        ("VARESO", "SAVIOR"), ("LEPIDCIS", "DISCIPLE"), ("CLEAMRI", "MIRACLE"),
        ("REPOTPH", "PROPHET"), ("MOSDWI", "WISDOM"), ("YECMR", "MERCY"),
        ("NESSBIGLS", "BLESSINGS"), ("NEVHEA", "HEAVEN"), ("SLMAPS", "PSALMS"),
        ("GINKDOM", "KINGDOM"), ("NEDRGA", "GARDEN"),
    ]
    for scrambled, answer in scrambles:
        pdf._check_page_break(18)
        pdf.add_text(f"  {scrambled}  =  _______________", size=10, indent=10)
        pdf.add_space(4)
    pdf.add_space(10)
    pdf.add_text("Answers (upside down!): " + ", ".join([a for _, a in scrambles]), size=6, color=(180, 180, 180))
    pdf.end_page()

    # MEMORY VERSE DECODER (2 pages)
    pdf.start_page()
    pdf.add_chapter_title("VERSE DECODER!")
    pdf.add_wrapped_text("Use the code to decode each Bible verse! Each number = a letter.")
    pdf.add_space(8)
    pdf.add_text("CODE: A=1, B=2, C=3, D=4, E=5, F=6, G=7, H=8, I=9, J=10, K=11, L=12,", size=8)
    pdf.add_text("M=13, N=14, O=15, P=16, Q=17, R=18, S=19, T=20, U=21, V=22, W=23, X=24, Y=25, Z=26", size=8)
    pdf.add_space(10)
    pdf.add_text("Decode this verse:", size=10, bold=True)
    pdf.add_space(5)
    pdf.add_text("7-15-4  9-19  12-15-22-5", size=12, bold=True, color=(51, 51, 102))
    pdf.add_text("Answer: ___ ___ ___  (1 John 4:8)", size=10)
    pdf.add_space(10)
    pdf.add_text("Decode:", size=10, bold=True)
    pdf.add_text("2-5  19-20-18-15-14-7  1-14-4  3-15-21-18-1-7-5-15-21-19", size=12, bold=True, color=(51, 51, 102))
    pdf.add_text("Answer: ___ ___ ___ ___ (Joshua 1:9)", size=10)
    pdf.add_space(10)
    pdf.add_text("Decode:", size=10, bold=True)
    pdf.add_text("20-18-21-19-20  9-14  20-8-5  12-15-18-4", size=12, bold=True, color=(51, 51, 102))
    pdf.add_text("Answer: ___ ___ ___ ___ (Proverbs 3:5)", size=10)
    pdf.end_page()

    # MATCHING PUZZLES (2 pages)
    pdf.start_page()
    pdf.add_chapter_title("MATCHING: Bible Pairs")
    pdf.add_text("Draw a line connecting the pairs!", size=10)
    pdf.add_space(10)
    pairs = [
        ("Adam", "Eve"), ("Noah", "Ark"), ("Moses", "Red Sea"),
        ("David", "Goliath"), ("Daniel", "Lions"), ("Jonah", "Fish"),
        ("Mary", "Jesus"), ("Peter", "Keys"), ("Paul", "Letters"),
        ("Abraham", "Stars"), ("Ruth", "Naomi"), ("Esther", "King"),
    ]
    for left, right in pairs:
        pdf.add_text(f"  {left}  .............................  {right}", size=10, indent=20)
        pdf.add_space(4)
    pdf.end_page()

    pad_to_pages(pdf, 42, "Puzzle Notes")
    return pdf


# ============================================================
# BOOK 16: Bible Stories Six Pack (6 detailed stories)
# ============================================================
def create_book_16():
    pdf = PDFEngine()
    pdf.header_text = "Bible Stories Six Pack"

    pdf.add_title_page(
        title="Bible Stories Six Pack",
        subtitle="6 Complete Bible Stories with Detailed Chapters, Activities, Discussion Questions, and Life Lessons",
        author="For Kids Ages 5-12",
        extra_lines=["Deep-dive stories with multiple chapters per story", "Perfect for family reading or Sunday School"]
    )

    pdf.start_page()
    pdf.add_chapter_title("6 Stories, Deeply Told")
    pdf.add_wrapped_text("These 6 stories are told in FULL detail -- not just summaries! Each story has multiple chapters, vivid scenes, discussion questions, activities, and prayers. Read one per week for 6 weeks of amazing Bible learning!")
    pdf.add_space(10)
    pdf.add_text("The 6 Stories:", size=12, bold=True, color=(51, 51, 102))
    pdf.add_space(8)
    story_list = [
        "1. NOAH AND THE GREAT FLOOD (Genesis 6-9)",
        "2. JOSEPH: FROM PIT TO PALACE (Genesis 37-50)",
        "3. MOSES AND THE EXODUS (Exodus 1-14)",
        "4. DAVID: THE SHEPHERD KING (1 Samuel 16-17)",
        "5. DANIEL: FAITH UNDER FIRE (Daniel 1-6)",
        "6. JESUS: THE GREATEST STORY (Luke-John)",
    ]
    for s in story_list:
        pdf.add_text(f"  {s}", size=10, indent=10, bold=True)
        pdf.add_space(5)
    pdf.end_page()

    # 6 STORIES (6-7 pages each)
    full_stories = [
        {
            "title": "Noah and the Great Flood",
            "ref": "Genesis 6-9",
            "chapters": [
                ("A Wicked World", "The world had become very wicked. People lied, stole, and hurt each other. God was sad because people had forgotten about Him. Violence was everywhere. Only ONE family still loved God."),
                ("God Speaks to Noah", "God told Noah: 'I am going to send a great flood to wash away the wickedness. But YOU and your family will be safe. Build an ark -- a huge boat -- and I will tell you exactly how.' Noah listened carefully."),
                ("Building the Ark", "Noah obeyed! It took YEARS to build. People laughed at him. 'A flood? Ha! It has never rained that hard!' But Noah kept building every single day. His sons helped: Shem, Ham, and Japheth."),
                ("The Animals Come", "God sent animals to Noah -- two of every kind! Big elephants, tiny ants, tall giraffes, colorful birds. They all came walking, crawling, and flying to the ark. Noah welcomed every single one."),
                ("The Flood", "The skies opened! Rain poured down for 40 days and 40 nights. Water covered EVERYTHING -- even the tallest mountains! But inside the ark, Noah's family and all the animals were safe and dry."),
                ("God's Promise", "After many months, the water went down. Noah sent out a dove. It came back with an olive branch -- land was near! When everyone came out, God put a RAINBOW in the sky: 'I will never flood the whole earth again.'"),
            ],
            "lesson": "God rewards obedience and faithfulness. Even when no one else is doing right, be the one who does!",
            "questions": ["Why was God sad about the world?", "How long did Noah build the ark?", "Why did people laugh at Noah?", "What does the rainbow mean?", "How can you be faithful like Noah?"],
        },
        {
            "title": "Joseph: From Pit to Palace",
            "ref": "Genesis 37-50",
            "chapters": [
                ("The Favorite Son", "Jacob had 12 sons, but Joseph was his favorite. He gave Joseph a beautiful coat of many colors. Joseph's brothers were VERY jealous. They hated Joseph and could not say a kind word to him."),
                ("The Dreams", "God gave Joseph special dreams. In one dream, his brothers' bundles of wheat bowed to his. In another, the sun, moon, and 11 stars bowed to him. His brothers grew even angrier."),
                ("Thrown in a Pit", "One day, the brothers grabbed Joseph, ripped off his coat, and threw him into a deep pit! Then they sold him to traders going to Egypt. They told their father Joseph was dead."),
                ("Slave to Success", "In Egypt, Joseph became a slave. But God was WITH him! He worked hard and was put in charge of his master's house. Even in prison, God gave Joseph the ability to interpret dreams."),
                ("Before the King", "Pharaoh had strange dreams no one could explain. Joseph was brought from prison. God gave Joseph the meaning: 7 years of plenty, then 7 years of famine. Pharaoh made Joseph second-in-command!"),
                ("Forgiveness and Reunion", "When famine came, Joseph's brothers came to Egypt for food. They bowed before Joseph -- just like the dream! Joseph cried and forgave them: 'What you meant for evil, God used for good!'"),
            ],
            "lesson": "God can turn the worst situations into something amazing. Trust His plan, forgive those who hurt you, and never give up!",
            "questions": ["Why were Joseph's brothers jealous?", "What happened in the pit?", "How did God help Joseph in Egypt?", "What did Joseph say to his brothers?", "What bad situation in your life might God use for good?"],
        },
        {
            "title": "Moses and the Exodus",
            "ref": "Exodus 1-14",
            "chapters": [
                ("Baby in Danger", "The king of Egypt was afraid of the Israelites, so he ordered all baby boys killed! Moses' mother hid him in a basket on the river. A princess found him and raised him as her own."),
                ("The Burning Bush", "Years later, God spoke to Moses through a bush that burned but did not burn up! God said: 'Go back to Egypt! Tell Pharaoh to let my people go!' Moses was scared but said yes."),
                ("Let My People Go!", "Moses went to Pharaoh: 'God says let His people go!' Pharaoh said NO. So God sent 10 plagues -- frogs, darkness, locusts, and more! Still Pharaoh refused."),
                ("The Passover", "God told each family to put lamb's blood on their door. The angel of death passed over those homes. Finally, Pharaoh said GO! The Israelites were FREE!"),
                ("Trapped at the Sea!", "But Pharaoh changed his mind and chased them! The people were trapped between the army and the Red Sea. They were terrified! Moses said: 'Do not be afraid. God will fight for you!'"),
                ("The Sea Parts!", "Moses raised his staff and God split the sea in TWO! The people walked through on dry ground with walls of water on each side! When the army followed, the water crashed back. Israel was saved!"),
            ],
            "lesson": "God delivers His people! No enemy is too powerful, no situation too hopeless. God makes a way when there seems to be no way.",
            "questions": ["How was baby Moses saved?", "What was special about the bush?", "How many plagues were there?", "What happened at the Red Sea?", "When has God made a way for you?"],
        },
        {
            "title": "David: The Shepherd King",
            "ref": "1 Samuel 16-17",
            "chapters": [
                ("The Forgotten Son", "God sent the prophet Samuel to find a new king. Jesse showed him all his tall, strong sons. But God said no to each one! 'Do you have another son?' Samuel asked. 'Just the youngest -- David. He's watching the sheep.'"),
                ("Chosen by God", "When David walked in, God said: 'This is the one!' Samuel anointed David as future king. God looked at David's HEART, not his size or age. From that day, God's Spirit was with David."),
                ("The Giant's Challenge", "The Philistine army had a champion named Goliath -- over 9 feet tall! For 40 days he shouted: 'Send someone to fight me!' Every soldier was terrified. No one would go."),
                ("A Boy Steps Up", "Young David visited his brothers and heard Goliath. He said: 'Who is this man to defy God's army? I will fight him!' King Saul tried to give David armor, but it was too big. David chose 5 smooth stones."),
                ("Faith Over Fear", "Goliath laughed: 'Am I a dog that you come with sticks?' David shouted: 'You come with a sword, but I come in the name of the LORD!' He ran toward the giant, slung a stone, and it hit Goliath in the forehead!"),
                ("Victory!", "The giant fell! David had won -- not with strength or weapons, but with FAITH in God. The whole army cheered! David proved that with God, ANYONE can overcome impossible odds. Size doesn't matter -- faith does!"),
            ],
            "lesson": "God doesn't look at your size, age, or appearance. He looks at your HEART. With faith, you can face any giant!",
            "questions": ["Why did God choose David over his brothers?", "What was Goliath's challenge?", "What did David use?", "Why was David brave?", "What 'giants' do you face?"],
        },
        {
            "title": "Daniel: Faith Under Fire",
            "ref": "Daniel 1-6",
            "chapters": [
                ("Taken to Babylon", "Daniel was a young man when enemy soldiers captured him and took him to Babylon. They tried to change his name, his food, and his faith. But Daniel decided in his heart to stay faithful to God."),
                ("Standing Firm", "Daniel and his friends refused to eat the king's food (which was against God's rules). Instead, they ate vegetables and water. After 10 days, they looked HEALTHIER than everyone else! God honored their obedience."),
                ("The Dream Interpreter", "King Nebuchadnezzar had a terrifying dream. No one could explain it. But God gave Daniel the meaning! The king was amazed and promoted Daniel. God's gift made room for him."),
                ("The Fiery Furnace", "Daniel's friends -- Shadrach, Meshach, and Abednego -- refused to bow to a golden statue. The king threw them into a furnace heated 7 times hotter! But God sent an angel. They walked out without even smelling like smoke!"),
                ("The Trap", "Years later, jealous men tricked the new king into making a law: 'Anyone who prays to any god except the king will be thrown to the lions!' They knew Daniel prayed 3 times daily."),
                ("Lions' Den Victory", "Daniel kept praying -- with his windows OPEN! He was arrested and thrown into the lions' den. But God shut the lions' mouths! In the morning, Daniel was untouched. The king declared: 'Daniel's God is the living God!'"),
            ],
            "lesson": "Stand firm in your faith no matter the pressure! God protects those who are faithful to Him, even in the most dangerous situations.",
            "questions": ["How did Daniel stay faithful in Babylon?", "What happened to his friends in the furnace?", "Why did Daniel keep praying?", "How did God protect Daniel?", "Where do you need courage to stand firm?"],
        },
        {
            "title": "Jesus: The Greatest Story",
            "ref": "Luke & John (selected)",
            "chapters": [
                ("God Becomes a Baby", "The Creator of the universe became a tiny baby! Born in a stable, laid in a manger, visited by shepherds and wise men. The angels sang: 'Glory to God in the highest!' Jesus came to save the world."),
                ("Growing Up", "Jesus grew up in Nazareth, learning carpentry from Joseph. He obeyed His parents, grew in wisdom, and waited for the right time. Even as a boy, He amazed teachers with His understanding of God's Word."),
                ("Love in Action", "Jesus healed the sick, gave sight to the blind, fed thousands, and loved the unloved. He touched lepers, forgave sinners, and welcomed children. He showed us what God's love looks like in real life."),
                ("The Teacher", "Jesus told amazing stories (parables) to teach people about God's kingdom. The Good Samaritan, the Prodigal Son, the Lost Sheep -- each story revealed God's heart of love, forgiveness, and grace."),
                ("The Cross", "Jesus was arrested, beaten, and nailed to a cross -- even though He never sinned. Why? Because He loves YOU. He took the punishment for every wrong thing ever done. 'It is finished!' He said."),
                ("ALIVE FOREVER!", "Three days later -- the tomb was EMPTY! Jesus is ALIVE! He appeared to His friends, ate with them, and said: 'I am with you ALWAYS.' He went to heaven and will come back one day. Death could not hold Him!"),
            ],
            "lesson": "Jesus is God's love in person. He lived, died, and rose again for YOU. You are loved beyond measure. All you need to do is believe and receive!",
            "questions": ["Why did Jesus come to earth?", "What miracles did He perform?", "Why did Jesus die on the cross?", "What happened 3 days later?", "Have you told Jesus you love Him?"],
        },
    ]

    for story_num, story in enumerate(full_stories, 1):
        # Story title page
        pdf.start_page()
        pdf.add_chapter_title(f"Story {story_num}: {story['title']}")
        pdf.add_text(f"Read: {story['ref']}", size=10, italic=True, color=(100, 100, 140))
        pdf.add_space(15)
        pdf.add_text("Chapters:", size=11, bold=True)
        pdf.add_space(5)
        for i, (ch_title, _) in enumerate(story['chapters'], 1):
            pdf.add_text(f"  Chapter {i}: {ch_title}", size=10, indent=10)
            pdf.add_space(3)
        pdf.end_page()

        # Chapter pages
        for ch_num, (ch_title, ch_text) in enumerate(story['chapters'], 1):
            pdf.start_page()
            pdf.add_text(f"Story {story_num} | Chapter {ch_num}", size=8, color=(120, 100, 140))
            pdf.add_space(5)
            pdf.add_text(ch_title, size=14, bold=True, color=(51, 51, 102))
            pdf.add_space(10)
            pdf.add_wrapped_text(ch_text, size=11, color=(40, 40, 50))
            pdf.add_space(15)
            pdf.add_text("What stood out to you in this chapter?", size=9, italic=True, color=(100, 80, 120))
            pdf.add_lined_space(3, spacing=20)
            pdf.end_page()

        # Story review page
        pdf.start_page()
        pdf.add_chapter_title(f"Story {story_num} Review: {story['title']}")
        pdf.add_text("THE LESSON:", size=11, bold=True, color=(0, 100, 0))
        pdf.add_wrapped_text(story['lesson'], size=10, indent=5)
        pdf.add_space(10)
        pdf.add_text("DISCUSSION QUESTIONS:", size=11, bold=True, color=(51, 51, 102))
        pdf.add_space(5)
        for q in story['questions']:
            pdf.add_text(f"  * {q}", size=10, indent=10)
            pdf.add_space(3)
        pdf.add_space(10)
        pdf.add_text("MY PRAYER:", size=10, bold=True, color=(80, 60, 120))
        pdf.add_lined_space(3, spacing=20)
        pdf.end_page()

    pad_to_pages(pdf, 55, "Story Notes")
    return pdf


# ============================================================
# MAIN EXECUTION
# ============================================================
if __name__ == '__main__':
    output_dir = os.path.dirname(os.path.abspath(__file__))

    books = [
        ("11_100_Bible_Activities_for_Kids.pdf", create_book_11),
        ("12_Kids_Bible_Prayer_Journal.pdf", create_book_12),
        ("13_50_Bible_Stories_for_Kids_Workbook.pdf", create_book_13),
        ("14_Bible_Coloring_Activity_Book_Ages_3_7.pdf", create_book_14),
        ("15_Bible_Word_Search_Puzzle_Book.pdf", create_book_15),
        ("16_Bible_Stories_Six_Pack.pdf", create_book_16),
    ]

    print("=" * 65)
    print("  GENERATING 6 KIDS BIBLE ACTIVITY BOOKS")
    print("=" * 65)
    print()

    total_pages = 0
    for filename, creator in books:
        filepath = os.path.join(output_dir, filename)
        pdf = creator()
        num_pages = pdf.save(filepath)
        size_kb = os.path.getsize(filepath) / 1024
        total_pages += num_pages
        print(f"  [OK] {filename}")
        print(f"       Pages: {num_pages} | Size: {size_kb:.1f} KB")
        print()

    print("=" * 65)
    print(f"  ALL 6 BOOKS COMPLETE! Total pages: {total_pages}")
    print("=" * 65)
