#!/usr/bin/env python3
"""Generate Books 11-20 (Tier 2 Part 2 + Tier 3)"""

import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pdf_engine import PDFEngine


def make_30_day_journal(pdf, title, days_data, daily_sections):
    """Helper to create consistent 30-day journal structure with 40+ pages."""
    for i, day_data in enumerate(days_data, 1):
        pdf.start_page()
        theme = day_data[0]
        verse_ref = day_data[1]
        verse_text = day_data[2]
        pdf.add_text(f"DAY {i}", size=9, bold=True, color=(80, 60, 120))
        pdf.add_chapter_title(f"Day {i}: {theme}")
        pdf.add_quote_box(verse_text, verse_ref)
        pdf.add_space(6)
        for section_title, section_type in daily_sections:
            if section_type == 'prompt':
                prompt = day_data[3] if len(day_data) > 3 else ""
                pdf.add_text(f"{section_title}:", size=10, bold=True, color=(51, 51, 102))
                pdf.add_wrapped_text(prompt, size=10, indent=5)
                pdf.add_space(5)
            elif section_type == 'lines':
                pdf.add_text(f"{section_title}:", size=10, bold=True, color=(51, 51, 102))
                pdf.add_lined_space(4, spacing=20)
                pdf.add_space(5)
            elif section_type == 'question':
                question = day_data[4] if len(day_data) > 4 else ""
                pdf.add_text(f"{section_title}:", size=10, bold=True, color=(51, 51, 102))
                pdf.add_wrapped_text(question, size=10, italic=True, indent=5)
                pdf.add_lined_space(3, spacing=18)
        pdf.end_page()


def pad_to_40_pages(pdf, title="Journal Notes"):
    """Add extra pages if needed to reach 40+ pages."""
    while len(pdf.pages) + (1 if pdf.current_page_content else 0) < 40:
        pdf.add_blank_journal_page(header=title)


def create_book_11():
    """100 Bible Activities for Kids"""
    pdf = PDFEngine()
    pdf.header_text = "100 Bible Activities for Kids"

    pdf.add_title_page(
        title="100 Bible Activities for Kids",
        subtitle="Puzzles, Quizzes, Games, and Creative Fun Based on God's Word!",
        author="For Kids Ages 5-12",
        extra_lines=["Fill-in-the-blanks, matching, true/false,", "drawing prompts, word games, and more!"]
    )

    pdf.start_page()
    pdf.add_chapter_title("100 Fun Bible Activities!")
    pdf.add_wrapped_text("Get ready for 100 awesome activities based on Bible stories and verses! Each page has fun challenges to test your Bible knowledge and help you learn God's Word. You can do them alone or with friends and family!")
    pdf.add_space(10)
    pdf.add_text("Activity Types:", size=11, bold=True)
    types = ["True or False Quizzes", "Fill in the Blank", "Matching Games",
             "Word Scrambles", "Drawing Challenges", "Bible Math",
             "Verse Decoders", "Story Sequencing", "Who Said It?", "Character Profiles"]
    for t in types:
        pdf.add_text(f"  * {t}", size=10, indent=10)
        pdf.add_space(2)
    pdf.end_page()

    # Generate 100 activities across multiple pages (5 per page = 20 pages)
    activities_batch = [
        # TRUE OR FALSE (20 questions)
        ("TRUE OR FALSE - Old Testament", [
            "1. God created the world in 7 days. (T/F)", "2. Noah built an ark. (T/F)",
            "3. Moses parted the Red Sea. (T/F)", "4. David fought a lion named Goliath. (T/F)",
            "5. Jonah was swallowed by a shark. (T/F)", "6. Daniel was thrown into a pit of snakes. (T/F)",
            "7. Joseph had a coat of many colors. (T/F)", "8. Abraham had a son named Isaac. (T/F)",
            "9. The 10 Commandments were given to Moses. (T/F)", "10. Ruth was Naomi's daughter-in-law. (T/F)",
        ]),
        ("TRUE OR FALSE - New Testament", [
            "11. Jesus was born in Jerusalem. (T/F)", "12. Jesus had 12 disciples. (T/F)",
            "13. Jesus turned water into juice. (T/F)", "14. Jesus walked on water. (T/F)",
            "15. Zacchaeus climbed a tree to see Jesus. (T/F)", "16. Jesus fed 5,000 with 5 loaves and 2 fish. (T/F)",
            "17. Peter denied Jesus 3 times. (T/F)", "18. Jesus rose from the dead on the 3rd day. (T/F)",
            "19. Paul was once called Saul. (T/F)", "20. The book of Revelation is the first book. (T/F)",
        ]),
        # FILL IN THE BLANK (20)
        ("FILL IN THE BLANK - Part 1", [
            "21. In the beginning, God created the _____ and the _____.",
            "22. Jesus said, 'I am the way, the _____, and the _____.'",
            "23. 'For God so loved the _____ that He gave His only _____.'",
            "24. The Lord is my _____, I shall not _____.",
            "25. 'Be strong and _____. Do not be _____.'",
            "26. Jesus was baptized in the _____ River.",
            "27. Moses led the people out of _____.",
            "28. David was the king of _____.",
            "29. Jesus was born in _____.",
            "30. Noah's ark landed on Mount _____.",
        ]),
        ("FILL IN THE BLANK - Part 2", [
            "31. The first book of the Bible is _____.",
            "32. The last book of the Bible is _____.",
            "33. Jesus' mother was named _____.",
            "34. The garden where Adam and Eve lived was called _____.",
            "35. God gave Moses the _____ Commandments.",
            "36. Jesus died on a _____.",
            "37. Goliath was from the land of the _____.",
            "38. The angel _____ appeared to Mary.",
            "39. Jesus was tempted for _____ days in the wilderness.",
            "40. Peter was a _____ before following Jesus.",
        ]),
        # WHO SAID IT? (10)
        ("WHO SAID IT?", [
            "41. 'Let there be light!' - _____",
            "42. 'Here am I. Send me!' - _____",
            "43. 'Am I my brother's keeper?' - _____",
            "44. 'You meant it for evil, but God meant it for good.' - _____",
            "45. 'The Lord is my shepherd.' - _____",
            "46. 'I have fought the good fight.' - _____",
            "47. 'Follow me, and I will make you fishers of men.' - _____",
            "48. 'My God, my God, why have you forsaken me?' - _____",
            "49. 'Lord, to whom shall we go? You have words of eternal life.' - _____",
            "50. 'If I perish, I perish.' - _____",
        ]),
        # MATCHING (10)
        ("MATCHING - Match the Person to the Event", [
            "51. Noah           a. Killed a giant",
            "52. Moses          b. Built an ark",
            "53. David          c. Was swallowed by a fish",
            "54. Jonah          d. Parted the Red Sea",
            "55. Daniel         e. Interpreted dreams in Egypt",
            "56. Joseph         f. Survived a lions' den",
            "57. Esther         g. Led Israel around Jericho",
            "58. Joshua         h. Saved her people from death",
            "59. Ruth           i. Walked on water",
            "60. Peter          j. Stayed loyal to Naomi",
        ]),
        # WORD SCRAMBLE (10)
        ("WORD SCRAMBLE - Unscramble Bible Words", [
            "61. ELBBI = _____", "62. SEPUJ = _____",
            "63. SESCO = _____", "64. REPRAY = _____",
            "65. CAGRE = _____", "66. HITFA = _____",
            "67. OVEL = _____", "68. PROHEPT = _____",
            "69. CLEPIDIS = _____", "70. CLEAMIR = _____",
        ]),
        # BIBLE MATH (10)
        ("BIBLE MATH", [
            "71. Days of creation (___) + tribes of Israel (___) = ___",
            "72. Commandments (___) x disciples (___) = ___",
            "73. Days Jesus was in tomb (___) + loaves feeding 5000 (___) = ___",
            "74. Books in Bible (___) - Old Testament books (___) = ___ (NT books)",
            "75. Days of flood rain (___) - days Jonah in fish (___) = ___",
            "76. Plagues in Egypt (___) + fruit of the Spirit (___) = ___",
            "77. Years in wilderness (___) / commandments (___) = ___",
            "78. Jesus' age at ministry start (___) - disciples (___) = ___",
            "79. Psalms in the Bible (___) - Proverbs chapters (___) = ___",
            "80. Letters Paul wrote (___) + Gospels (___) = ___",
        ]),
        # STORY SEQUENCING (10)
        ("PUT IN ORDER - Number these events 1-5", [
            "81-85: Creation Story",
            "  ___ God makes animals", "  ___ God makes light", "  ___ God rests",
            "  ___ God makes people", "  ___ God makes the sky",
            "",
            "86-90: Easter Story",
            "  ___ Jesus rises from the dead", "  ___ Jesus is arrested",
            "  ___ Jesus eats the Last Supper", "  ___ Jesus appears to disciples",
            "  ___ Jesus dies on the cross",
        ]),
        # DRAWING CHALLENGES (10)
        ("DRAWING CHALLENGES", [
            "91. Draw Noah's Ark with 10 different animals",
            "92. Draw baby Jesus in the manger",
            "93. Draw David facing Goliath",
            "94. Draw yourself as one of Jesus' disciples",
            "95. Draw the Garden of Eden",
            "96. Draw the 5 loaves and 2 fish multiplied",
            "97. Draw Daniel peaceful with the lions",
            "98. Draw Jonah and the big fish",
            "99. Draw your family praising God",
            "100. Draw what heaven might look like",
        ]),
    ]

    for section_title, items in activities_batch:
        pdf.start_page()
        pdf.add_chapter_title(section_title)
        pdf.add_space(5)
        for item in items:
            pdf._check_page_break(16)
            pdf.add_text(f"  {item}", size=10, indent=5)
            pdf.add_space(4)
        pdf.end_page()

    # DRAWING PAGES (large space)
    for i in range(5):
        pdf.start_page()
        pdf.add_text(f"Drawing Page - Activity #{91+i}", size=12, bold=True, color=(0, 120, 0))
        pdf.add_space(5)
        prompts = ["Draw Noah's Ark with animals", "Draw baby Jesus in the manger",
                   "Draw David vs Goliath", "Draw your family praising God", "Draw heaven"]
        pdf.add_text(prompts[i], size=11, italic=True)
        pdf.add_space(10)
        pdf.add_rect(55, 100, pdf.content_width, 550, stroke_color=(0.7, 0.7, 0.7))
        pdf.end_page()

    # ANSWER KEY
    pdf.start_page()
    pdf.add_chapter_title("Answer Key")
    pdf.add_text("True/False: 1-T, 2-T, 3-T, 4-F(man), 5-F(fish), 6-F(lions), 7-T, 8-T, 9-T, 10-T", size=8, color=(100,100,100))
    pdf.add_text("11-F(Bethlehem), 12-T, 13-F(wine), 14-T, 15-T, 16-T, 17-T, 18-T, 19-T, 20-F(last)", size=8, color=(100,100,100))
    pdf.add_space(5)
    pdf.add_text("Who Said It: 41-God, 42-Isaiah, 43-Cain, 44-Joseph, 45-David, 46-Paul, 47-Jesus, 48-Jesus, 49-Peter, 50-Esther", size=8, color=(100,100,100))
    pdf.add_space(5)
    pdf.add_text("Matching: 51-b, 52-d, 53-a, 54-c, 55-f, 56-e, 57-h, 58-g, 59-j, 60-i", size=8, color=(100,100,100))
    pdf.add_space(5)
    pdf.add_text("Scramble: BIBLE, JESUS, CROSS, PRAYER, GRACE, FAITH, LOVE, PROPHET, DISCIPLE, MIRACLE", size=8, color=(100,100,100))
    pdf.end_page()

    # Extra journal pages to reach 40
    pad_to_40_pages(pdf, "My Bible Notes")

    return pdf


def create_book_12():
    """Bible Study Journal - All 66 Books"""
    pdf = PDFEngine()
    pdf.header_text = "Bible Study Journal - All 66 Books"

    pdf.add_title_page(
        title="Bible Study Journal -- All 66 Books of the Bible",
        subtitle="A Comprehensive Study Guide and Journal for Every Book from Genesis to Revelation",
        author="Read, Reflect, Record, Apply",
        extra_lines=["Structured pages for each book of the Bible", "with study prompts and journaling space"]
    )

    pdf.start_page()
    pdf.add_chapter_title("How to Use This Journal")
    pdf.add_wrapped_text("This journal provides a structured page for each of the 66 books of the Bible. As you read through each book, use the prompts to guide your study. You do not need to complete these in order -- start wherever you are currently reading!")
    pdf.add_space(10)
    pdf.add_text("For each book, record:", size=11, bold=True)
    items = ["Key theme and summary", "Favorite verse", "What you learned about God",
             "How it applies to your life", "Questions you have", "Your prayer response"]
    for item in items:
        pdf.add_text(f"  * {item}", size=10, indent=10)
        pdf.add_space(3)
    pdf.end_page()

    # All 66 books
    books_of_bible = [
        ("Genesis", "Beginnings", "OT"), ("Exodus", "Deliverance", "OT"), ("Leviticus", "Holiness", "OT"),
        ("Numbers", "Wandering", "OT"), ("Deuteronomy", "Covenant Renewal", "OT"),
        ("Joshua", "Conquest", "OT"), ("Judges", "Cycles", "OT"), ("Ruth", "Loyalty", "OT"),
        ("1 Samuel", "Kingdom Begins", "OT"), ("2 Samuel", "David's Reign", "OT"),
        ("1 Kings", "Division", "OT"), ("2 Kings", "Exile", "OT"),
        ("1 Chronicles", "David's Legacy", "OT"), ("2 Chronicles", "Temple & Kings", "OT"),
        ("Ezra", "Return", "OT"), ("Nehemiah", "Rebuilding", "OT"), ("Esther", "Providence", "OT"),
        ("Job", "Suffering", "OT"), ("Psalms", "Worship", "OT"), ("Proverbs", "Wisdom", "OT"),
        ("Ecclesiastes", "Meaning", "OT"), ("Song of Solomon", "Love", "OT"),
        ("Isaiah", "Salvation", "OT"), ("Jeremiah", "Warning", "OT"),
        ("Lamentations", "Grief", "OT"), ("Ezekiel", "Visions", "OT"), ("Daniel", "Faith", "OT"),
        ("Hosea", "Faithfulness", "OT"), ("Joel", "Restoration", "OT"), ("Amos", "Justice", "OT"),
        ("Obadiah", "Judgment", "OT"), ("Jonah", "Mercy", "OT"), ("Micah", "Hope", "OT"),
        ("Nahum", "Comfort", "OT"), ("Habakkuk", "Trust", "OT"), ("Zephaniah", "Day of Lord", "OT"),
        ("Haggai", "Priorities", "OT"), ("Zechariah", "Future Hope", "OT"), ("Malachi", "Messenger", "OT"),
        ("Matthew", "King", "NT"), ("Mark", "Servant", "NT"), ("Luke", "Savior", "NT"),
        ("John", "Son of God", "NT"), ("Acts", "Church", "NT"), ("Romans", "Righteousness", "NT"),
        ("1 Corinthians", "Church Issues", "NT"), ("2 Corinthians", "Comfort", "NT"),
        ("Galatians", "Freedom", "NT"), ("Ephesians", "Unity", "NT"),
        ("Philippians", "Joy", "NT"), ("Colossians", "Supremacy", "NT"),
        ("1 Thessalonians", "Return", "NT"), ("2 Thessalonians", "Endurance", "NT"),
        ("1 Timothy", "Leadership", "NT"), ("2 Timothy", "Faithfulness", "NT"),
        ("Titus", "Good Works", "NT"), ("Philemon", "Forgiveness", "NT"),
        ("Hebrews", "Better", "NT"), ("James", "Action", "NT"),
        ("1 Peter", "Suffering", "NT"), ("2 Peter", "Growth", "NT"),
        ("1 John", "Love", "NT"), ("2 John", "Truth", "NT"), ("3 John", "Hospitality", "NT"),
        ("Jude", "Contend", "NT"), ("Revelation", "Victory", "NT"),
    ]

    # 2 books per page to keep it manageable but comprehensive
    for i in range(0, len(books_of_bible), 2):
        pdf.start_page()
        for j in range(2):
            if i + j < len(books_of_bible):
                book_name, theme, testament = books_of_bible[i + j]
                pdf.add_text(f"{book_name} ({testament}) - Theme: {theme}", size=11, bold=True, color=(51, 51, 102))
                pdf.add_space(4)
                pdf.add_text("Key verse:", size=9, bold=True)
                pdf.add_lined_space(1, spacing=16)
                pdf.add_text("Summary in my words:", size=9, bold=True)
                pdf.add_lined_space(2, spacing=16)
                pdf.add_text("Application:", size=9, bold=True)
                pdf.add_lined_space(1, spacing=16)
                pdf.add_space(12)
        pdf.end_page()

    pad_to_40_pages(pdf, "Bible Study Notes")
    return pdf


def create_book_13():
    """Christian Forgiveness & Healing Workbook"""
    pdf = PDFEngine()
    pdf.header_text = "Christian Forgiveness & Healing Workbook"

    pdf.add_title_page(
        title="Christian Forgiveness & Healing Workbook",
        subtitle="Break Free from Bitterness, Find Peace, and Experience God's Restorative Power",
        author="A 6-Week Guided Healing Journey",
        extra_lines=["For anyone carrying unforgiveness, hurt,", "past trauma, or broken relationships"]
    )

    pdf.start_page()
    pdf.add_chapter_title("You Deserve to Be Free")
    pdf.add_wrapped_text("Unforgiveness is like drinking poison and expecting the other person to get sick. It hurts YOU more than anyone else. This workbook will guide you through a biblical, step-by-step process of releasing bitterness, forgiving those who hurt you (and yourself), and experiencing the deep healing only God can provide.")
    pdf.add_space(10)
    pdf.add_quote_box("Bear with each other and forgive one another if any of you has a grievance against someone. Forgive as the Lord forgave you.", "Colossians 3:13")
    pdf.add_space(10)
    pdf.add_text("Important: Forgiveness is NOT:", size=11, bold=True, color=(150, 50, 50))
    nots = ["Saying what happened was okay", "Trusting the person again immediately",
            "Forgetting what happened", "Letting them continue to hurt you",
            "Denying your pain"]
    for n in nots:
        pdf.add_text(f"  X {n}", size=10, indent=10, color=(150, 50, 50))
        pdf.add_space(2)
    pdf.add_space(8)
    pdf.add_text("Forgiveness IS:", size=11, bold=True, color=(0, 120, 0))
    is_list = ["Releasing THEM from YOUR judgment", "Giving the situation to God",
               "Choosing freedom over bitterness", "A process (not a one-time event)",
               "Possible through God's power (not your own)"]
    for item in is_list:
        pdf.add_text(f"  * {item}", size=10, indent=10, color=(0, 100, 0))
        pdf.add_space(2)
    pdf.end_page()

    weeks = [
        ("Acknowledging the Pain", [
            ("Naming the Hurt", "What happened? Write it honestly."),
            ("How It Affected Me", "How did this hurt change me?"),
            ("The Weight I Carry", "What does unforgiveness feel like?"),
            ("God Sees My Pain", "God knows and cares about your suffering."),
            ("Permission to Grieve", "It is okay to be sad about what happened."),
        ]),
        ("Understanding Forgiveness", [
            ("What the Bible Says", "God commands forgiveness -- but also provides the power."),
            ("How God Forgave Us", "We deserved judgment but received mercy."),
            ("Forgiveness vs. Trust", "You can forgive and still have boundaries."),
            ("The Freedom of Letting Go", "Forgiveness is a gift you give yourself."),
            ("Forgiving Does Not Mean Forgetting", "You can remember without bitterness."),
        ]),
        ("The Process of Forgiving", [
            ("Choosing to Forgive", "Forgiveness is a choice, not a feeling."),
            ("Writing a Forgiveness Letter", "Write what you need to say (you may not send it)."),
            ("Praying for Those Who Hurt You", "The hardest prayer you will ever pray."),
            ("Releasing Revenge", "Give justice to God -- He is the righteous judge."),
            ("Daily Recommitment", "Some days you will need to forgive again. That is normal."),
        ]),
        ("Forgiving Yourself", [
            ("Guilt and Shame", "What are you holding against yourself?"),
            ("God's Forgiveness of You", "If God has forgiven you, who are you to disagree?"),
            ("Letting Go of Regret", "You cannot change the past, but God redeems it."),
            ("Self-Compassion", "Treat yourself with the grace God gives you."),
            ("A New Identity", "You are not your worst mistake."),
        ]),
        ("Healing and Restoration", [
            ("Emotional Healing", "Allowing God to heal your wounded heart."),
            ("Rebuilding Trust (If Appropriate)", "When and how to trust again."),
            ("Healthy Boundaries", "Protecting yourself going forward."),
            ("Finding Purpose in Pain", "How God uses broken things for beauty."),
            ("Testimony of Healing", "Your healing story can help others."),
        ]),
        ("Walking in Freedom", [
            ("Living Offense-Free", "Choosing not to be easily offended."),
            ("Extending Grace Daily", "Becoming a person of grace."),
            ("Preventing Bitterness", "Catching unforgiveness early."),
            ("Being an Agent of Reconciliation", "Helping others find forgiveness."),
            ("Celebration of Freedom", "You are FREE!"),
        ]),
    ]

    for week_num, (week_title, days) in enumerate(weeks, 1):
        for day_num, (day_title, day_desc) in enumerate(days, 1):
            pdf.start_page()
            pdf.add_text(f"WEEK {week_num} | Day {day_num}", size=9, bold=True, color=(100, 60, 80))
            pdf.add_chapter_title(f"{day_title}")
            pdf.add_text(f"Theme: {week_title}", size=10, italic=True, color=(100, 80, 120))
            pdf.add_space(8)
            pdf.add_text("Today's Focus:", size=11, bold=True, color=(51, 51, 102))
            pdf.add_wrapped_text(day_desc, size=10, indent=5)
            pdf.add_space(8)
            pdf.add_text("My Honest Reflection:", size=10, bold=True, color=(51, 51, 102))
            pdf.add_lined_space(5, spacing=20)
            pdf.add_text("Prayer:", size=10, bold=True, color=(80, 60, 100))
            pdf.add_lined_space(3, spacing=18)
            pdf.end_page()

    # FORGIVENESS LETTER PAGE
    pdf.start_page()
    pdf.add_chapter_title("My Forgiveness Letter")
    pdf.add_wrapped_text("Write a letter to the person who hurt you. You do NOT need to send this. This is for YOUR healing.", size=10, italic=True)
    pdf.add_space(10)
    pdf.add_text("Dear _______________,", size=10)
    pdf.add_lined_space(18, spacing=22)
    pdf.end_page()

    pad_to_40_pages(pdf, "Healing Journal")
    return pdf


def create_book_14():
    """Christian Singles Prayer & Purpose Workbook"""
    pdf = PDFEngine()
    pdf.header_text = "Christian Singles Prayer & Purpose Workbook"

    pdf.add_title_page(
        title="Christian Singles Prayer & Purpose Workbook",
        subtitle="Thrive in Your Season of Singleness with God-Centered Purpose and Intentional Prayer",
        author="A 30-Day Guided Workbook",
        extra_lines=["For single Christians who want to grow,", "prepare, and live with purpose NOW"]
    )

    pdf.start_page()
    pdf.add_chapter_title("Your Single Season Has Purpose")
    pdf.add_wrapped_text("Singleness is NOT a waiting room. It is a greenhouse -- a place where God grows you, shapes you, and prepares you for everything He has ahead. Whether you desire marriage someday or are called to long-term singleness, THIS season matters. This workbook will help you embrace it fully.")
    pdf.add_space(10)
    pdf.add_quote_box("I wish that all of you were as I am. But each of you has your own gift from God; one has this gift, another has that.", "1 Corinthians 7:7")
    pdf.add_space(10)
    pdf.add_text("This workbook covers:", size=11, bold=True)
    items = ["Identity and worth apart from relationship status", "Contentment vs. settling",
             "Preparing for future relationships (if desired)", "Building deep community",
             "Pursuing purpose with undivided devotion", "Handling loneliness with faith",
             "Purity and boundaries", "Financial wisdom in singleness"]
    for item in items:
        pdf.add_text(f"  * {item}", size=10, indent=10)
        pdf.add_space(2)
    pdf.end_page()

    singles_days = [
        ("Complete in Christ", "Colossians 2:10", "You have been made complete in Christ.", "You are already complete. You do not need another person to be whole.", "What would change if you truly believed you are complete right now?"),
        ("Not Alone", "Psalm 68:6", "God sets the lonely in families.", "God has placed community around you. You are not alone.", "Who has God placed in your life for companionship and support?"),
        ("Undivided Devotion", "1 Cor 7:35", "An unmarried person is concerned about the Lord's affairs.", "Your singleness gives you unique freedom to serve God.", "How can you use your undivided time and attention for God?"),
        ("Contentment Now", "Phil 4:11-12", "I have learned to be content whatever the circumstances.", "Contentment is not getting what you want -- it is wanting what you have.", "What are the GIFTS of your current season?"),
        ("Loneliness vs. Solitude", "Mark 1:35", "Very early in the morning, Jesus went off to a solitary place.", "Turn loneliness into sacred solitude with God.", "How can you transform lonely moments into God-moments?"),
        ("Identity Beyond Status", "1 Peter 2:9", "You are a chosen people, a royal priesthood.", "Your value has nothing to do with your relationship status.", "Who does God say you are -- regardless of being single or married?"),
        ("Guarding Your Heart", "Proverbs 4:23", "Above all else, guard your heart.", "Be intentional about what and who you let into your heart.", "What boundaries do you need to set in dating/relationships?"),
        ("Purity with Purpose", "1 Thess 4:3-4", "God's will is for you to be sanctified.", "Purity is not just about rules -- it is about honoring God with your body.", "What does purity look like practically in your life?"),
        ("Community & Friendship", "Prov 27:17", "As iron sharpens iron, so one person sharpens another.", "Deep friendships are essential in singleness.", "How can you invest more deeply in friendships?"),
        ("Serving Others", "Gal 5:13", "Use your freedom to serve one another humbly in love.", "Singles have unique flexibility to serve.", "Where is God calling you to serve in this season?"),
        ("Financial Wisdom", "Prov 21:20", "The wise store up choice food and olive oil.", "Use this season to build financial health.", "What financial goals can you pursue while single?"),
        ("Career & Calling", "Col 3:23", "Whatever you do, work at it with all your heart.", "Pour yourself into meaningful work.", "How is God using your career for His purposes?"),
        ("Healing Past Hurts", "Psalm 147:3", "He heals the brokenhearted.", "Let God heal you BEFORE your next relationship.", "What past hurt needs healing before you move forward?"),
        ("Dealing with Pressure", "Gal 1:10", "Am I now trying to please people, or God?", "Do not let cultural or family pressure define your timeline.", "Whose timeline are you on -- God's or other people's?"),
        ("Trusting God's Timing", "Eccl 3:11", "He has made everything beautiful in its time.", "God's timing is perfect, even when it feels slow.", "What are you trusting God for regarding timing?"),
        ("Becoming the Right Person", "Matt 7:3-5", "First take the plank out of your own eye.", "Focus on becoming the right person, not finding the right person.", "What areas of growth does God want to develop in you?"),
        ("Healthy Standards", "2 Cor 6:14", "Do not be unequally yoked.", "Having standards is not being picky -- it is being wise.", "What non-negotiable values do you hold for a future partner?"),
        ("Embracing Adventure", "Psalm 37:4", "Delight yourself in the LORD.", "Your single years can be the most adventurous of your life!", "What adventure or experience do you want to pursue?"),
        ("Mentorship", "Titus 2:7", "In everything set them an example by doing what is good.", "Find a mentor AND be a mentor.", "Who can you learn from? Who can you pour into?"),
        ("Mental Health", "Phil 4:8", "Think about such things.", "Take care of your mental and emotional health.", "What do you need for better mental health right now?"),
        ("Spiritual Disciplines", "1 Tim 4:7", "Train yourself to be godly.", "Use this season to build unshakeable spiritual habits.", "What spiritual discipline do you want to strengthen?"),
        ("Dealing with Desire", "Psalm 37:4", "He will give you the desires of your heart.", "Your desires are valid. Bring them to God.", "What desires do you need to honestly bring before God?"),
        ("The Gift of Time", "Eph 5:15-16", "Making the most of every opportunity.", "Time is your greatest resource right now.", "How are you stewarding your time?"),
        ("Building Legacy", "Psalm 78:4", "We will tell the next generation.", "You do not need to be married to leave a legacy.", "What legacy are you building right now?"),
        ("Joy in Every Season", "James 1:2", "Consider it pure joy.", "Choose joy -- not when circumstances change, but NOW.", "What brings you genuine joy in this season?"),
        ("Preparing for the Future", "Prov 24:27", "Put your outdoor work in order.", "Prepare yourself spiritually, emotionally, and practically.", "What preparation work should you focus on?"),
        ("Gratitude for Now", "1 Thess 5:18", "Give thanks in all circumstances.", "There are gifts in singleness that married people miss.", "List 10 things about your current life you are grateful for:"),
        ("Living Fully", "John 10:10", "I have come that they may have life, and have it to the full.", "Full life starts NOW -- not when you find a partner.", "What does 'full life' look like for you right now?"),
        ("Surrender", "Prov 3:5-6", "Trust in the LORD with all your heart.", "Surrender your timeline, your desires, and your future to God.", "Write a prayer of full surrender:"),
        ("Moving Forward", "Phil 3:13-14", "Forgetting what is behind and straining toward what is ahead.", "Step into tomorrow with confidence and purpose.", "What is your next bold step of faith?"),
    ]

    for i, (theme, verse_ref, verse_text, prompt, question) in enumerate(singles_days, 1):
        pdf.start_page()
        pdf.add_text(f"DAY {i}", size=9, bold=True, color=(80, 100, 60))
        pdf.add_chapter_title(f"Day {i}: {theme}")
        pdf.add_quote_box(verse_text, verse_ref)
        pdf.add_space(5)
        pdf.add_text("Today's Focus:", size=10, bold=True, color=(51, 51, 102))
        pdf.add_wrapped_text(prompt, size=10, indent=5)
        pdf.add_space(6)
        pdf.add_text("Reflection:", size=10, bold=True, color=(51, 51, 102))
        pdf.add_wrapped_text(question, size=10, italic=True, indent=5)
        pdf.add_lined_space(4, spacing=20)
        pdf.add_text("My Prayer:", size=10, bold=True, color=(80, 60, 100))
        pdf.add_lined_space(3, spacing=18)
        pdf.end_page()

    pad_to_40_pages(pdf, "Singles Prayer Journal")
    return pdf


def create_book_15():
    """Christian Premarital Bible Study Workbook"""
    pdf = PDFEngine()
    pdf.header_text = "Christian Premarital Bible Study Workbook"

    pdf.add_title_page(
        title="Christian Premarital Bible Study Workbook",
        subtitle="Build Your Marriage on God's Foundation Before You Say 'I Do'",
        author="An 8-Week Couples Study",
        extra_lines=["Essential conversations, Bible study, and planning", "for engaged couples and those considering marriage"]
    )

    pdf.start_page()
    pdf.add_chapter_title("Congratulations on Your Commitment!")
    pdf.add_wrapped_text("The fact that you are doing premarital study shows wisdom and intentionality. This workbook will guide you through the most important conversations every couple needs to have BEFORE marriage. Each week covers a critical topic with scripture, discussion, and practical exercises.")
    pdf.add_space(10)
    pdf.add_quote_box("Unless the LORD builds the house, the builders labor in vain.", "Psalm 127:1")
    pdf.add_space(10)
    pdf.add_text("8 Weeks Covering:", size=11, bold=True)
    weeks_list = ["Week 1: God's Design for Marriage", "Week 2: Communication & Conflict",
                  "Week 3: Roles & Expectations", "Week 4: Finances & Stewardship",
                  "Week 5: Intimacy & Sexuality", "Week 6: Family & In-Laws",
                  "Week 7: Spiritual Life Together", "Week 8: Vision & Commitment"]
    for w in weeks_list:
        pdf.add_text(f"  * {w}", size=10, indent=10)
        pdf.add_space(3)
    pdf.end_page()

    premarital_weeks = [
        ("God's Design for Marriage", "Genesis 2:24", "A man shall leave his father and mother and hold fast to his wife.", [
            "What is God's purpose for marriage?",
            "What does 'leave and cleave' mean practically?",
            "How is marriage a picture of Christ and the church?",
            "What are your expectations for marriage?",
            "What do you fear most about marriage?",
        ]),
        ("Communication & Conflict", "Eph 4:26-27", "In your anger do not sin. Do not let the sun go down while you are still angry.", [
            "How did your family of origin handle conflict?",
            "What is your communication style?",
            "What topics are hardest for you to discuss?",
            "How will you resolve disagreements?",
            "What are your ground rules for fighting fair?",
        ]),
        ("Roles & Expectations", "Eph 5:21-33", "Submit to one another out of reverence for Christ.", [
            "What do you expect from a husband/wife?",
            "How will you divide household responsibilities?",
            "What does leadership look like in your marriage?",
            "What cultural expectations do you need to address?",
            "How will you handle decision-making together?",
        ]),
        ("Finances & Stewardship", "Prov 21:5", "The plans of the diligent lead to profit.", [
            "What is your current financial situation (debts, savings)?",
            "Will you combine finances or keep separate accounts?",
            "What are your financial goals for year 1, 5, and 10?",
            "How much will you give/tithe?",
            "What is your biggest financial fear?",
        ]),
        ("Intimacy & Sexuality", "1 Cor 7:3-5", "The husband should fulfill his marital duty to his wife, and likewise the wife.", [
            "What are your expectations for physical intimacy?",
            "How will you prioritize your intimate life?",
            "What boundaries are important to you?",
            "How will you handle differences in desire?",
            "What does honoring God look like in this area?",
        ]),
        ("Family & In-Laws", "Gen 2:24", "Therefore a man shall leave his father and mother.", [
            "What is your relationship with your in-laws?",
            "How will you handle holidays and family time?",
            "Do you want children? How many? When?",
            "How were you raised and how will you raise your children?",
            "What boundaries do you need with extended family?",
        ]),
        ("Spiritual Life Together", "Josh 24:15", "As for me and my household, we will serve the LORD.", [
            "How will you worship together?",
            "What church will you attend?",
            "How will you pray together?",
            "What spiritual disciplines will you practice?",
            "How will you serve together?",
        ]),
        ("Vision & Commitment", "Hab 2:2", "Write the vision; make it plain.", [
            "What is your shared vision for your marriage?",
            "Write your personal wedding vows",
            "What will you do when times get hard?",
            "Who will be your marriage mentors?",
            "What does 'til death do us part' mean to you?",
        ]),
    ]

    for week_num, (title, verse_ref, verse_text, questions) in enumerate(premarital_weeks, 1):
        # Week intro page
        pdf.start_page()
        pdf.add_chapter_title(f"Week {week_num}: {title}")
        pdf.add_quote_box(verse_text, verse_ref)
        pdf.add_space(10)
        pdf.add_wrapped_text(f"This week focuses on {title.lower()}. Set aside at least 1 hour together to work through these questions honestly. Remember: there are no wrong answers -- only honest ones.", size=10)
        pdf.end_page()

        # Question pages
        for q_num, question in enumerate(questions, 1):
            pdf.start_page()
            pdf.add_text(f"Week {week_num} | Question {q_num}", size=9, bold=True, color=(100, 60, 80))
            pdf.add_space(10)
            pdf.add_text(question, size=12, bold=True, color=(51, 51, 102))
            pdf.add_space(12)
            pdf.add_text("His Answer:", size=10, bold=True, color=(40, 60, 120))
            pdf.add_lined_space(5, spacing=20)
            pdf.add_space(8)
            pdf.add_text("Her Answer:", size=10, bold=True, color=(120, 40, 80))
            pdf.add_lined_space(5, spacing=20)
            pdf.add_space(8)
            pdf.add_text("What we agreed on:", size=10, bold=True, color=(0, 100, 0))
            pdf.add_lined_space(3, spacing=18)
            pdf.end_page()

    pad_to_40_pages(pdf, "Premarital Notes")
    return pdf


def create_book_16():
    """How to Start Selling Digital Products on Etsy"""
    pdf = PDFEngine()
    pdf.header_text = "How to Start Selling Digital Products on Etsy"

    pdf.add_title_page(
        title="How to Start Selling Digital Products on Etsy",
        subtitle="A Complete Step-by-Step Guide to Building a Profitable Etsy Shop from Scratch",
        author="The Beginner's Business Blueprint",
        extra_lines=["No inventory, no shipping, unlimited sales potential", "Start earning passive income today"]
    )

    pdf.start_page()
    pdf.add_chapter_title("Why Digital Products on Etsy?")
    pdf.add_wrapped_text("Digital products are the ultimate online business model: create once, sell unlimited times, no inventory, no shipping, and customers receive their product instantly. Etsy is the perfect marketplace with over 90 million active buyers already searching for digital products.")
    pdf.add_space(10)
    pdf.add_text("What You Will Learn:", size=11, bold=True)
    items = ["How to set up your Etsy shop from scratch", "What digital products sell best (with examples)",
             "How to create products with free tools", "Pricing strategies that maximize profit",
             "SEO and keywords to get found", "How to create stunning mockups and listings",
             "Marketing strategies beyond Etsy", "Scaling to a full-time income"]
    for item in items:
        pdf.add_text(f"  * {item}", size=10, indent=10)
        pdf.add_space(3)
    pdf.end_page()

    chapters = [
        ("Understanding the Digital Product Market", [
            "Why digital products are the best business model",
            "The Etsy marketplace: 90+ million buyers",
            "Types of digital products that sell well",
            "Passive income potential: create once, sell forever",
            "Low startup cost -- you can start with $0",
        ]),
        ("Setting Up Your Etsy Shop", [
            "Creating your Etsy account step by step",
            "Choosing your shop name (tips and strategies)",
            "Setting up shop policies and about section",
            "Payment and billing setup",
            "Understanding Etsy fees (listing, transaction, payment)",
        ]),
        ("Choosing Your Niche & Products", [
            "How to research profitable niches",
            "Tools for finding what buyers want",
            "Analyzing competition (what works, what does not)",
            "Validating your product idea before creating it",
            "Top 20 digital product categories on Etsy",
        ]),
        ("Creating Your Digital Products", [
            "Free tools: Canva, Google Docs, PowerPoint",
            "Paid tools: Adobe, Affinity, Procreate",
            "Creating printable PDFs (planners, journals, art)",
            "Creating editable templates (Canva templates)",
            "Quality standards that get 5-star reviews",
        ]),
        ("Etsy SEO & Getting Found", [
            "How Etsy search works (algorithm basics)",
            "Keyword research for digital products",
            "Optimizing your title (13 keyword slots)",
            "Writing tags that rank (all 13 tags)",
            "Descriptions that convert browsers to buyers",
        ]),
        ("Creating Listings That Sell", [
            "Product photography/mockups for digital goods",
            "Writing compelling listing descriptions",
            "Pricing psychology: how to price for profit",
            "Creating urgency and social proof",
            "A/B testing your listings for improvement",
        ]),
        ("Marketing & Growing Your Shop", [
            "Pinterest marketing for Etsy sellers",
            "Instagram and social media strategies",
            "Etsy ads: when and how to use them",
            "Email marketing for repeat customers",
            "Building a brand beyond Etsy",
        ]),
        ("Scaling to Full-Time Income", [
            "From 1 product to a full product line",
            "Automating your business",
            "Expanding to other platforms",
            "Hiring help and outsourcing",
            "Goal setting: from side hustle to full-time",
        ]),
    ]

    for ch_num, (ch_title, points) in enumerate(chapters, 1):
        pdf.start_page()
        pdf.add_chapter_title(f"Chapter {ch_num}: {ch_title}")
        pdf.add_space(5)
        for point in points:
            pdf.add_text(f"  * {point}", size=10, indent=10)
            pdf.add_space(5)
        pdf.add_space(15)
        pdf.add_text("Key Takeaways:", size=10, bold=True)
        pdf.add_lined_space(3, spacing=18)
        pdf.add_text("My Action Steps:", size=10, bold=True)
        pdf.add_numbered_lines(1, 3, spacing=18)
        pdf.end_page()

    # WORKSHEETS
    pdf.start_page()
    pdf.add_chapter_title("Shop Setup Checklist")
    checklist = [
        "Created Etsy account", "Chose shop name", "Wrote shop announcement",
        "Added shop banner and logo", "Set up payment method",
        "Wrote shop policies (returns, delivery)", "Created first listing",
        "Added all 13 tags to listing", "Created mockup images",
        "Set up automatic delivery", "Published first product",
        "Shared on social media", "Asked for first review",
    ]
    for item in checklist:
        pdf.add_checkbox(item)
    pdf.end_page()

    pdf.start_page()
    pdf.add_chapter_title("Product Brainstorm Worksheet")
    pdf.add_text("My skills and interests:", size=10, bold=True)
    pdf.add_lined_space(3)
    pdf.add_text("Problems I can solve:", size=10, bold=True)
    pdf.add_lined_space(3)
    pdf.add_text("Product ideas (list 20!):", size=10, bold=True)
    pdf.add_numbered_lines(1, 15, spacing=18)
    pdf.end_page()

    pdf.start_page()
    pdf.add_chapter_title("Keyword Research Worksheet")
    pdf.add_text("My main product type:", size=10, bold=True)
    pdf.add_lined_space(1)
    pdf.add_text("Keywords buyers search for:", size=10, bold=True)
    pdf.add_numbered_lines(1, 13, spacing=18)
    pdf.add_text("Long-tail keywords:", size=10, bold=True)
    pdf.add_numbered_lines(1, 5, spacing=18)
    pdf.end_page()

    # INCOME TRACKER
    pdf.start_page()
    pdf.add_chapter_title("Monthly Income Tracker")
    pdf.add_text("Month: ___________", size=10, bold=True)
    pdf.add_space(8)
    pdf.add_text("Products listed: ___", size=10)
    pdf.add_text("Total sales: ___", size=10)
    pdf.add_text("Revenue: $___", size=10)
    pdf.add_text("Etsy fees: $___", size=10)
    pdf.add_text("Net profit: $___", size=10)
    pdf.add_space(10)
    pdf.add_text("Top selling product:", size=10, bold=True)
    pdf.add_lined_space(1)
    pdf.add_text("What worked well:", size=10, bold=True)
    pdf.add_lined_space(3)
    pdf.add_text("What to improve:", size=10, bold=True)
    pdf.add_lined_space(3)
    pdf.add_text("Goals for next month:", size=10, bold=True)
    pdf.add_lined_space(3)
    pdf.end_page()

    pad_to_40_pages(pdf, "Business Notes")
    return pdf


def create_book_17():
    """100 Digital Products You Can Create & Sell"""
    pdf = PDFEngine()
    pdf.header_text = "100 Digital Products You Can Create & Sell"

    pdf.add_title_page(
        title="100 Digital Products You Can Create & Sell",
        subtitle="The Ultimate Idea Book for Online Entrepreneurs and Digital Creators",
        author="Never Run Out of Product Ideas Again",
        extra_lines=["Categorized by niche, difficulty, and profit potential", "With creation tips for each product type"]
    )

    pdf.start_page()
    pdf.add_chapter_title("100 Ideas, Unlimited Potential")
    pdf.add_wrapped_text("This book gives you 100 proven digital product ideas organized by category. Each idea includes what it is, who buys it, how to create it, and estimated profit potential. Stop wondering WHAT to sell and start creating!")
    pdf.add_space(10)
    pdf.add_text("Categories covered:", size=11, bold=True)
    cats = ["Printable Planners & Journals (1-15)", "Educational Resources (16-30)",
            "Business Templates (31-45)", "Creative & Design Assets (46-60)",
            "Health & Wellness (61-70)", "Wedding & Events (71-80)",
            "Kids & Parenting (81-90)", "Spiritual & Faith-Based (91-100)"]
    for c in cats:
        pdf.add_text(f"  * {c}", size=10, indent=10)
        pdf.add_space(3)
    pdf.end_page()

    # All 100 products in groups
    product_groups = [
        ("Printable Planners & Journals", [
            "1. Daily Planner Printable", "2. Weekly Meal Planner", "3. Budget Tracker Printable",
            "4. Habit Tracker Journal", "5. Gratitude Journal Pages", "6. Goal Setting Workbook",
            "7. Fitness Tracker Printable", "8. Reading Log Journal", "9. Travel Planner",
            "10. Self-Care Planner", "11. Student Planner", "12. Teacher Planner",
            "13. Cleaning Schedule Printable", "14. Bill Payment Tracker", "15. Pregnancy Journal",
        ]),
        ("Educational Resources", [
            "16. Homeschool Curriculum Planner", "17. Flashcard Sets", "18. Worksheet Bundles (Math/Reading)",
            "19. Language Learning Printables", "20. Study Guide Templates", "21. Lesson Plan Templates",
            "22. Educational Posters", "23. Science Experiment Cards", "24. History Timeline Printables",
            "25. Phonics Activity Sheets", "26. Multiplication Tables Poster", "27. Writing Prompt Cards",
            "28. Book Report Templates", "29. Classroom Decor Bundle", "30. Report Card Templates",
        ]),
        ("Business Templates", [
            "31. Resume/CV Templates", "32. Invoice Templates", "33. Social Media Templates (Canva)",
            "34. Business Card Designs", "35. Email Marketing Templates", "36. Proposal Templates",
            "37. Contract Templates", "38. Brand Kit Templates", "39. Presentation Templates",
            "40. Media Kit Templates", "41. Business Plan Template", "42. Client Onboarding Packet",
            "43. Project Management Templates", "44. Meeting Agenda Templates", "45. Employee Handbook Template",
        ]),
        ("Creative & Design Assets", [
            "46. Digital Art Prints", "47. Clipart Sets", "48. Digital Paper/Backgrounds",
            "49. Font Pairings Guide", "50. Color Palette Collections", "51. Instagram Story Templates",
            "52. Pinterest Pin Templates", "53. Logo Templates", "54. Pattern Designs",
            "55. Brush Sets (Procreate/Photoshop)", "56. Mockup Templates", "57. Invitation Designs",
            "58. Bookmark Printables", "59. Sticker Sheets (Digital)", "60. Wall Art Printables",
        ]),
        ("Health & Wellness", [
            "61. Workout Plan PDFs", "62. Meal Prep Guides", "63. Calorie Counting Tracker",
            "64. Mental Health Journal", "65. Meditation Guide", "66. Sleep Tracker",
            "67. Water Intake Tracker", "68. Symptom Tracker (Medical)", "69. Yoga Pose Cards",
            "70. Weight Loss Tracker & Journal",
        ]),
        ("Wedding & Events", [
            "71. Wedding Planner Printable", "72. Wedding Timeline Template", "73. Seating Chart Template",
            "74. Save the Date Designs", "75. Wedding Invitation Suite", "76. Bridal Shower Games",
            "77. Baby Shower Games Bundle", "78. Party Planning Checklist", "79. Birthday Invitation Templates",
            "80. Event Budget Tracker",
        ]),
        ("Kids & Parenting", [
            "81. Chore Chart Printables", "82. Coloring Pages Bundle", "83. Learning Activity Sheets",
            "84. Kids Journal/Diary Pages", "85. Reward/Sticker Charts", "86. Lunchbox Note Cards",
            "87. Kids Birthday Party Kit", "88. Screen Time Tracker", "89. Kids Recipe Cards",
            "90. Growth Chart Printable",
        ]),
        ("Spiritual & Faith-Based", [
            "91. Prayer Journal", "92. Bible Study Workbook", "93. Scripture Memory Cards",
            "94. Church Bulletin Templates", "95. Devotional eBook", "96. Bible Reading Plan",
            "97. Christian Planner", "98. Worship Setlist Template", "99. Church Event Flyer Templates",
            "100. Faith-Based Wall Art Prints",
        ]),
    ]

    for group_title, products in product_groups:
        pdf.start_page()
        pdf.add_chapter_title(group_title)
        pdf.add_space(5)
        for product in products:
            pdf._check_page_break(16)
            pdf.add_text(f"  {product}", size=10, indent=5)
            pdf.add_space(4)
        pdf.end_page()

    # PROFIT POTENTIAL PAGE
    pdf.start_page()
    pdf.add_chapter_title("Profit Potential Guide")
    pdf.add_text("Pricing Tiers:", size=11, bold=True)
    pdf.add_space(5)
    pdf.add_text("  Low ($1-$5): Simple printables, single-page designs", size=10, indent=10)
    pdf.add_text("  Medium ($5-$15): Multi-page workbooks, template bundles", size=10, indent=10)
    pdf.add_text("  High ($15-$50): Comprehensive courses, large bundles", size=10, indent=10)
    pdf.add_text("  Premium ($50+): Business kits, complete systems", size=10, indent=10)
    pdf.add_space(15)
    pdf.add_text("Top Earning Categories:", size=11, bold=True)
    pdf.add_space(5)
    pdf.add_text("  1. Business templates (highest average price)", size=10, indent=10)
    pdf.add_text("  2. Wedding printables (emotional purchase)", size=10, indent=10)
    pdf.add_text("  3. Educational resources (repeat buyers)", size=10, indent=10)
    pdf.add_text("  4. Planners & journals (New Year spike)", size=10, indent=10)
    pdf.add_text("  5. Faith-based products (loyal audience)", size=10, indent=10)
    pdf.end_page()

    # BRAINSTORM WORKSHEET
    pdf.start_page()
    pdf.add_chapter_title("My Product Ideas Worksheet")
    pdf.add_text("My skills:", size=10, bold=True)
    pdf.add_lined_space(2)
    pdf.add_text("My interests:", size=10, bold=True)
    pdf.add_lined_space(2)
    pdf.add_text("Problems I can solve:", size=10, bold=True)
    pdf.add_lined_space(2)
    pdf.add_text("My top 10 product ideas from this book:", size=10, bold=True)
    pdf.add_numbered_lines(1, 10, spacing=18)
    pdf.end_page()

    # ACTION PLAN
    pdf.start_page()
    pdf.add_chapter_title("My Action Plan")
    pdf.add_text("First product I will create:", size=10, bold=True)
    pdf.add_lined_space(2)
    pdf.add_text("Tools I will use:", size=10, bold=True)
    pdf.add_lined_space(2)
    pdf.add_text("Target launch date:", size=10, bold=True)
    pdf.add_lined_space(1)
    pdf.add_text("My 30-day product creation schedule:", size=10, bold=True)
    pdf.add_text("  Week 1:", size=10)
    pdf.add_lined_space(1)
    pdf.add_text("  Week 2:", size=10)
    pdf.add_lined_space(1)
    pdf.add_text("  Week 3:", size=10)
    pdf.add_lined_space(1)
    pdf.add_text("  Week 4:", size=10)
    pdf.add_lined_space(1)
    pdf.end_page()

    pad_to_40_pages(pdf, "Business Notes & Ideas")
    return pdf


def create_book_18():
    """Beginner's Guide to Creating eBooks in Canva"""
    pdf = PDFEngine()
    pdf.header_text = "Beginner's Guide to Creating eBooks in Canva"

    pdf.add_title_page(
        title="Beginner's Guide to Creating eBooks in Canva",
        subtitle="Design Professional eBooks, Workbooks, and Lead Magnets Using Free Tools",
        author="Step-by-Step Visual Guide",
        extra_lines=["No design experience needed!", "From blank page to polished PDF in hours"]
    )

    chapters_content = [
        ("Why Canva for eBook Creation", "Canva is free, powerful, and requires zero design experience. Learn why it is the perfect tool for creating professional digital products."),
        ("Setting Up Your Canva Account", "Step-by-step setup, understanding the dashboard, navigating templates, and organizing your designs into folders."),
        ("Choosing the Right Template", "How to find and customize templates. Understanding sizes: A4, US Letter, square formats. When to start from scratch vs. using a template."),
        ("Design Fundamentals for eBooks", "Typography basics: font pairing, hierarchy, readability. Color theory: choosing palettes that look professional. Layout principles: white space, alignment, consistency."),
        ("Creating Your eBook Cover", "First impressions matter! How to design covers that grab attention. Title placement, imagery, branding, and making it stand out in search results."),
        ("Building Interior Pages", "Creating consistent page layouts. Adding text boxes, images, shapes, and decorative elements. Building master pages for efficiency."),
        ("Adding Interactive Elements", "Checkboxes, fillable fields, clickable links, table of contents. Making your eBooks functional as workbooks and journals."),
        ("Working with Images & Graphics", "Using Canva's free image library. Uploading your own photos. Using illustrations and icons effectively. Image sizing and quality."),
        ("Creating Workbook Pages", "Lined pages, checkboxes, trackers, tables, and forms. Making your eBook a functional workbook people actually USE."),
        ("Exporting & Selling Your eBook", "Export settings for perfect quality. PDF optimization. Setting up automatic delivery on Etsy. Pricing and launching your product."),
    ]

    for ch_num, (title, desc) in enumerate(chapters_content, 1):
        pdf.start_page()
        pdf.add_chapter_title(f"Chapter {ch_num}: {title}")
        pdf.add_wrapped_text(desc, size=10)
        pdf.add_space(15)
        pdf.add_text("Key Steps:", size=10, bold=True)
        pdf.add_numbered_lines(1, 5, spacing=20)
        pdf.add_space(10)
        pdf.add_text("Notes:", size=10, bold=True)
        pdf.add_lined_space(5, spacing=18)
        pdf.end_page()

    # CHECKLISTS AND WORKSHEETS
    pdf.start_page()
    pdf.add_chapter_title("eBook Creation Checklist")
    checklist = [
        "Defined target audience", "Outlined chapters/content", "Chose Canva template or size",
        "Selected color palette (2-3 colors)", "Chose fonts (heading + body)",
        "Designed cover page", "Created table of contents", "Built all interior pages",
        "Added page numbers", "Checked all text for errors", "Exported as PDF (high quality)",
        "Tested on multiple devices", "Created listing mockups", "Published on Etsy/platform",
    ]
    for item in checklist:
        pdf.add_checkbox(item)
    pdf.end_page()

    pdf.start_page()
    pdf.add_chapter_title("Design Decisions Worksheet")
    pdf.add_text("My eBook title:", size=10, bold=True)
    pdf.add_lined_space(1)
    pdf.add_text("Target audience:", size=10, bold=True)
    pdf.add_lined_space(1)
    pdf.add_text("Page size (Letter/A4):", size=10, bold=True)
    pdf.add_lined_space(1)
    pdf.add_text("Color palette (hex codes):", size=10, bold=True)
    pdf.add_lined_space(1)
    pdf.add_text("Heading font:", size=10, bold=True)
    pdf.add_lined_space(1)
    pdf.add_text("Body font:", size=10, bold=True)
    pdf.add_lined_space(1)
    pdf.add_text("Number of pages:", size=10, bold=True)
    pdf.add_lined_space(1)
    pdf.add_text("Chapter outline:", size=10, bold=True)
    pdf.add_numbered_lines(1, 10, spacing=18)
    pdf.end_page()

    pad_to_40_pages(pdf, "Design Notes")
    return pdf


def create_book_19():
    """30-Day Etsy Shop Success Workbook"""
    pdf = PDFEngine()
    pdf.header_text = "30-Day Etsy Shop Success Workbook"

    pdf.add_title_page(
        title="30-Day Etsy Shop Success Workbook",
        subtitle="Launch, Optimize, and Scale Your Etsy Shop in 30 Days with Daily Action Steps",
        author="The Complete Daily Action Plan",
        extra_lines=["Day-by-day tasks, strategies, and tracking", "for new and struggling Etsy sellers"]
    )

    pdf.start_page()
    pdf.add_chapter_title("Your 30-Day Etsy Transformation")
    pdf.add_wrapped_text("This workbook gives you ONE specific, actionable task every single day for 30 days. By the end, you will have a fully optimized, marketing-ready Etsy shop with multiple products, strong SEO, and a growth strategy in place.")
    pdf.add_space(10)
    pdf.add_text("Week 1: Foundation & First Products (Days 1-7)", size=10, bold=True)
    pdf.add_text("Week 2: Optimization & SEO (Days 8-14)", size=10, bold=True)
    pdf.add_text("Week 3: Marketing & Visibility (Days 15-21)", size=10, bold=True)
    pdf.add_text("Week 4: Scaling & Systems (Days 22-30)", size=10, bold=True)
    pdf.end_page()

    etsy_days = [
        ("Set Up Shop Basics", "Create/optimize your Etsy shop: name, banner, about section, policies."),
        ("Research Your Niche", "Analyze top 10 competitors. Note their prices, photos, tags, descriptions."),
        ("Plan Your First 5 Products", "Brainstorm and outline 5 products based on research."),
        ("Create Product #1", "Design and create your first digital product."),
        ("Create Product #2", "Design and create your second product (related to #1)."),
        ("Write Your First Listing", "Craft an optimized title, description, and all 13 tags."),
        ("Create Mockup Images", "Design 5+ listing images using Canva mockup templates."),
        ("Keyword Research Deep-Dive", "Find 50+ keywords for your niche using Etsy search, eRank, Marmalead."),
        ("Optimize All Titles", "Rewrite all listing titles with researched keywords."),
        ("Optimize All Tags", "Fill all 13 tags per listing with relevant keywords."),
        ("Write Converting Descriptions", "Rewrite descriptions with benefits, features, and calls to action."),
        ("Improve Your Photos", "Reshoot/redesign listing images. Test lifestyle mockups."),
        ("Create Product #3-4", "Add 2 more products to expand your shop."),
        ("Set Up Shop Sections", "Organize products into logical shop sections."),
        ("Set Up Pinterest", "Create a Pinterest business account and pin your products."),
        ("Create 10 Pinterest Pins", "Design beautiful pins linking to your Etsy listings."),
        ("Join Pinterest Group Boards", "Find and join relevant group boards in your niche."),
        ("Create Instagram Content", "Post 3-5 posts showcasing your products."),
        ("Reach Out for Reviews", "Ask friends/family to purchase and leave honest reviews."),
        ("Run an Etsy Ad", "Set up a small Etsy ad budget ($1-5/day) to test."),
        ("Analyze Your Stats", "Check Etsy analytics. What is working? What is not?"),
        ("Create Product #5-7", "Scale up! Add 3 more products to your shop."),
        ("Create a Bundle", "Bundle related products together at a discount."),
        ("Email List Setup", "Create a free lead magnet and email signup (Mailchimp/ConvertKit)."),
        ("Create a Freebie", "Make a free sample product to drive traffic and get emails."),
        ("Batch Create Content", "Create 2 weeks of social media content in one day."),
        ("Study Analytics", "Analyze what is selling, what is getting views, what needs change."),
        ("Plan Next Month", "Set revenue goals, product goals, and marketing goals for month 2."),
        ("Automate & Systematize", "Set up templates, schedules, and systems for efficiency."),
        ("Celebrate & Review", "Celebrate your progress! Review all 30 days and plan ahead."),
    ]

    for i, (title, task) in enumerate(etsy_days, 1):
        pdf.start_page()
        week = (i - 1) // 7 + 1
        pdf.add_text(f"DAY {i} | Week {week}", size=9, bold=True, color=(50, 100, 80))
        pdf.add_chapter_title(f"Day {i}: {title}")
        pdf.add_text("Today's Task:", size=11, bold=True, color=(51, 51, 102))
        pdf.add_wrapped_text(task, size=10, indent=5)
        pdf.add_space(10)
        pdf.add_checkbox("Task completed")
        pdf.add_space(5)
        pdf.add_text("What I did today:", size=10, bold=True)
        pdf.add_lined_space(4, spacing=20)
        pdf.add_text("Results/Observations:", size=10, bold=True)
        pdf.add_lined_space(3, spacing=20)
        pdf.add_text("Tomorrow's priority:", size=10, bold=True)
        pdf.add_lined_space(1, spacing=20)
        pdf.end_page()

    # TRACKING PAGES
    pdf.start_page()
    pdf.add_chapter_title("Monthly Revenue Tracker")
    pdf.add_text("Week 1 sales: $___  |  Orders: ___", size=10)
    pdf.add_text("Week 2 sales: $___  |  Orders: ___", size=10)
    pdf.add_text("Week 3 sales: $___  |  Orders: ___", size=10)
    pdf.add_text("Week 4 sales: $___  |  Orders: ___", size=10)
    pdf.add_space(10)
    pdf.add_text("Total revenue: $___", size=11, bold=True)
    pdf.add_text("Total orders: ___", size=11, bold=True)
    pdf.add_text("Best selling product:", size=10, bold=True)
    pdf.add_lined_space(1)
    pdf.add_text("Lessons learned:", size=10, bold=True)
    pdf.add_lined_space(5)
    pdf.end_page()

    pad_to_40_pages(pdf, "Etsy Business Notes")
    return pdf


def create_book_20():
    """Faceless YouTube Business Starter Guide"""
    pdf = PDFEngine()
    pdf.header_text = "Faceless YouTube Business Starter Guide"

    pdf.add_title_page(
        title="Faceless YouTube Business Starter Guide",
        subtitle="Build a Profitable YouTube Channel Without Showing Your Face",
        author="The Complete Blueprint for Faceless Content",
        extra_lines=["Monetization strategies, niche selection,", "content creation, and growth hacking"]
    )

    pdf.start_page()
    pdf.add_chapter_title("Why Faceless YouTube?")
    pdf.add_wrapped_text("YouTube is the second largest search engine in the world with over 2 billion monthly users. Faceless channels earn millions in ad revenue, affiliate commissions, and product sales -- all without ever showing your face on camera. This guide shows you exactly how.")
    pdf.add_space(10)
    pdf.add_text("Benefits of Faceless YouTube:", size=11, bold=True)
    benefits = ["Complete privacy and anonymity", "No expensive camera equipment needed",
                "Easily outsourceable (hire editors, VOs)", "Multiple channels possible",
                "Focus on content quality over personality", "Passive income potential"]
    for b in benefits:
        pdf.add_text(f"  * {b}", size=10, indent=10)
        pdf.add_space(3)
    pdf.end_page()

    chapters = [
        ("Profitable Faceless Niches", [
            "Top 20 faceless YouTube niches (with examples)",
            "How to validate a niche before starting",
            "Analyzing competition and opportunity",
            "Niches to AVOID (oversaturated, low CPM)",
            "Finding your unique angle within a niche",
        ]),
        ("Channel Setup & Branding", [
            "Creating your Google/YouTube account",
            "Channel name strategies for faceless brands",
            "Designing channel art and logo (Canva)",
            "Writing your channel description for SEO",
            "Setting up channel sections and playlists",
        ]),
        ("Content Creation Methods", [
            "Screen recordings with voiceover",
            "Stock footage compilation videos",
            "Animation and motion graphics (free tools)",
            "Slideshow/list videos",
            "AI-assisted content creation tools",
            "Text-to-speech options",
        ]),
        ("Free Tools for Production", [
            "Video editing: DaVinci Resolve, CapCut",
            "Screen recording: OBS Studio",
            "Thumbnails: Canva",
            "Stock footage: Pexels, Pixabay",
            "Music: YouTube Audio Library",
            "AI voiceover options",
        ]),
        ("YouTube SEO & Discovery", [
            "How the YouTube algorithm works",
            "Keyword research for YouTube",
            "Crafting titles that get clicks",
            "Thumbnail design psychology",
            "Tags, descriptions, and closed captions",
            "Playlists for increased watch time",
        ]),
        ("Monetization Strategies", [
            "YouTube Partner Program (ad revenue)",
            "Affiliate marketing in descriptions",
            "Selling digital products",
            "Sponsorship deals (even for faceless channels)",
            "Channel memberships and Super Chats",
            "Cross-platform monetization",
        ]),
        ("Growth & Scaling", [
            "Posting schedule and consistency",
            "Analyzing YouTube analytics",
            "Outsourcing video editing",
            "Building a team (editors, scriptwriters, VOs)",
            "Running multiple channels",
            "Compound growth strategies",
        ]),
        ("30-Day Launch Plan", [
            "Day 1-5: Research, setup, branding",
            "Day 6-10: Create first 3 videos",
            "Day 11-15: Optimize and publish",
            "Day 16-20: Create next batch + promote",
            "Day 21-25: Analyze, optimize, improve",
            "Day 26-30: Scale and systematize",
        ]),
    ]

    for ch_num, (title, points) in enumerate(chapters, 1):
        pdf.start_page()
        pdf.add_chapter_title(f"Chapter {ch_num}: {title}")
        pdf.add_space(5)
        for point in points:
            pdf.add_text(f"  * {point}", size=10, indent=10)
            pdf.add_space(5)
        pdf.add_space(10)
        pdf.add_text("Key Takeaways:", size=10, bold=True)
        pdf.add_lined_space(3, spacing=18)
        pdf.add_text("My Action Steps:", size=10, bold=True)
        pdf.add_numbered_lines(1, 3, spacing=18)
        pdf.end_page()

    # WORKSHEETS
    pdf.start_page()
    pdf.add_chapter_title("Niche Selection Worksheet")
    pdf.add_text("My interests/knowledge areas:", size=10, bold=True)
    pdf.add_lined_space(3)
    pdf.add_text("Top 5 niche ideas:", size=10, bold=True)
    pdf.add_numbered_lines(1, 5, spacing=20)
    pdf.add_text("Competition analysis (views, subs of top 5 channels):", size=10, bold=True)
    pdf.add_lined_space(5, spacing=18)
    pdf.add_text("My chosen niche:", size=10, bold=True)
    pdf.add_lined_space(1)
    pdf.end_page()

    pdf.start_page()
    pdf.add_chapter_title("Content Calendar (First Month)")
    for week in range(1, 5):
        pdf.add_text(f"Week {week}:", size=10, bold=True)
        pdf.add_text("  Video 1: _________________________________", size=9, indent=10)
        pdf.add_text("  Video 2: _________________________________", size=9, indent=10)
        pdf.add_space(8)
    pdf.add_space(10)
    pdf.add_text("Content creation schedule:", size=10, bold=True)
    pdf.add_text("  Research day: ___________", size=10, indent=10)
    pdf.add_text("  Script day: ___________", size=10, indent=10)
    pdf.add_text("  Recording day: ___________", size=10, indent=10)
    pdf.add_text("  Editing day: ___________", size=10, indent=10)
    pdf.add_text("  Publishing day: ___________", size=10, indent=10)
    pdf.end_page()

    pdf.start_page()
    pdf.add_chapter_title("Channel Setup Checklist")
    checklist = [
        "Created YouTube channel", "Designed channel banner", "Created logo/avatar",
        "Wrote channel description with keywords", "Set up channel sections",
        "Created intro/outro template", "Found background music sources",
        "Set up video editing software", "Created thumbnail template",
        "Recorded first video", "Optimized title, tags, description",
        "Published first video", "Shared on social media", "Planned next 4 videos",
    ]
    for item in checklist:
        pdf.add_checkbox(item)
    pdf.end_page()

    # INCOME TRACKER
    pdf.start_page()
    pdf.add_chapter_title("YouTube Income Tracker")
    pdf.add_text("Month: ___________", size=10, bold=True)
    pdf.add_space(5)
    pdf.add_text("Videos published: ___", size=10)
    pdf.add_text("Total views: ___", size=10)
    pdf.add_text("New subscribers: ___", size=10)
    pdf.add_text("Watch hours: ___", size=10)
    pdf.add_text("Ad revenue: $___", size=10)
    pdf.add_text("Affiliate income: $___", size=10)
    pdf.add_text("Product sales: $___", size=10)
    pdf.add_text("Total income: $___", size=11, bold=True)
    pdf.add_space(10)
    pdf.add_text("Best performing video:", size=10, bold=True)
    pdf.add_lined_space(1)
    pdf.add_text("Why it performed well:", size=10, bold=True)
    pdf.add_lined_space(2)
    pdf.add_text("Goals for next month:", size=10, bold=True)
    pdf.add_lined_space(3)
    pdf.end_page()

    pad_to_40_pages(pdf, "YouTube Business Notes")
    return pdf


if __name__ == '__main__':
    output_dir = os.path.dirname(os.path.abspath(__file__))

    books = [
        ("11_100_Bible_Activities_for_Kids.pdf", create_book_11),
        ("12_Bible_Study_Journal_All_66_Books.pdf", create_book_12),
        ("13_Christian_Forgiveness_Healing_Workbook.pdf", create_book_13),
        ("14_Christian_Singles_Prayer_Purpose.pdf", create_book_14),
        ("15_Christian_Premarital_Bible_Study.pdf", create_book_15),
        ("16_How_to_Sell_Digital_Products_on_Etsy.pdf", create_book_16),
        ("17_100_Digital_Products_You_Can_Sell.pdf", create_book_17),
        ("18_Beginners_Guide_Creating_eBooks_Canva.pdf", create_book_18),
        ("19_30_Day_Etsy_Shop_Success_Workbook.pdf", create_book_19),
        ("20_Faceless_YouTube_Business_Starter.pdf", create_book_20),
    ]

    print("=" * 65)
    print("  GENERATING BOOKS 11-20 (Tier 2 Part 2 + Tier 3)")
    print("=" * 65)

    for filename, creator in books:
        filepath = os.path.join(output_dir, filename)
        pdf = creator()
        num_pages = pdf.save(filepath)
        size_kb = os.path.getsize(filepath) / 1024
        print(f"  [OK] {filename}")
        print(f"       Pages: {num_pages} | Size: {size_kb:.1f} KB")

    print()
    print("=" * 65)
    print("  BOOKS 11-20 COMPLETE!")
    print("=" * 65)
