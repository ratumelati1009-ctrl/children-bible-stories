#!/usr/bin/env python3
"""
Generate all 20 workbook/journal PDFs (40+ pages each).
Each book is a comprehensive, standalone workbook ready for Etsy.
"""

import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pdf_engine import PDFEngine


def create_book_01():
    """30-Day Prayer & Fasting Challenge Workbook"""
    pdf = PDFEngine()
    pdf.header_text = "30-Day Prayer & Fasting Challenge Workbook"
    pdf.footer_text = ""

    # COVER PAGE
    pdf.add_title_page(
        title="30-Day Prayer & Fasting Challenge Workbook",
        subtitle="A Transformative Journey of Spiritual Discipline, Deeper Prayer, and Drawing Closer to God",
        author="A Daily Guided Workbook",
        extra_lines=["Includes daily prayers, fasting plans, reflection prompts,", "scripture readings, and journaling space"]
    )

    # COPYRIGHT / INTRO
    pdf.start_page()
    pdf.add_space(40)
    pdf.add_text("Copyright Notice", size=12, bold=True, color=(80, 80, 80))
    pdf.add_space(10)
    pdf.add_wrapped_text("All rights reserved. No part of this workbook may be reproduced without written permission. Scripture quotations are from the Holy Bible. This workbook is designed for personal spiritual growth and may be used individually or in group settings.", size=9, color=(100, 100, 100))
    pdf.add_space(30)
    pdf.add_text("How to Use This Workbook", size=14, bold=True, color=(51, 51, 102))
    pdf.add_space(10)
    pdf.add_wrapped_text("This 30-day workbook is designed to guide you through a transformative prayer and fasting journey. Each day includes: a scripture focus, a prayer prompt, fasting guidance, reflection questions, and journaling space. You can fast from food, social media, entertainment, or anything that distracts from God.", size=10)
    pdf.add_space(15)
    pdf.add_text("Types of Fasting Covered:", size=11, bold=True)
    pdf.add_space(6)
    items = ["Full Fast (water only) - for experienced fasters", "Partial Fast (Daniel Fast - fruits, vegetables, water)",
             "Intermittent Fast (skip one meal daily)", "Media Fast (no social media/TV/phone)",
             "Specific Item Fast (coffee, sugar, entertainment)"]
    for item in items:
        pdf.add_text(f"  * {item}", size=10, indent=10)
        pdf.add_space(3)
    pdf.end_page()

    # TABLE OF CONTENTS
    toc_items = [("Introduction & Preparation", 3), ("Week 1: Breaking Ground (Days 1-7)", 5),
                 ("Week 2: Going Deeper (Days 8-14)", 15), ("Week 3: Breakthrough (Days 15-21)", 25),
                 ("Week 4: Transformation (Days 22-28)", 35), ("Days 29-30: Celebration & Commitment", 43),
                 ("Final Reflection & Next Steps", 45)]
    pdf.add_toc_page(toc_items)

    # PREPARATION PAGE
    pdf.start_page()
    pdf.add_chapter_title("Preparation: Before You Begin")
    pdf.add_wrapped_text("Before starting your 30-day journey, take time to prepare your heart and mind. Answer these questions honestly:")
    pdf.add_space(10)
    pdf.add_text("Why am I starting this prayer & fasting challenge?", size=10, bold=True)
    pdf.add_lined_space(4)
    pdf.add_text("What do I hope God will do in my life during these 30 days?", size=10, bold=True)
    pdf.add_lined_space(4)
    pdf.add_text("What type of fast am I committing to?", size=10, bold=True)
    pdf.add_lined_space(3)
    pdf.add_text("My commitment prayer:", size=10, bold=True)
    pdf.add_lined_space(4)
    pdf.end_page()

    # 30 DAILY PAGES
    daily_content = [
        ("Surrender", "Romans 12:1-2", "Present your bodies as a living sacrifice, holy and acceptable to God.", "Surrendering control to God", "What area of your life have you been holding back from God?"),
        ("Seeking God First", "Matthew 6:33", "But seek first the kingdom of God and His righteousness, and all these things shall be added to you.", "Making God the priority", "What competes with God for first place in your life?"),
        ("Listening to God", "1 Samuel 3:10", "Speak, LORD, for your servant is listening.", "Quieting your mind to hear God", "What has God been trying to tell you that you haven't listened to?"),
        ("Repentance", "Psalm 51:10", "Create in me a clean heart, O God, and renew a right spirit within me.", "Turning away from sin", "Is there anything you need to confess and turn away from?"),
        ("Trust", "Proverbs 3:5-6", "Trust in the LORD with all your heart and lean not on your own understanding.", "Trusting God completely", "What situation do you need to trust God with right now?"),
        ("Gratitude", "1 Thessalonians 5:18", "Give thanks in all circumstances; for this is God's will for you.", "Thankfulness even in difficulty", "List 10 things you are grateful for today:"),
        ("Rest in God", "Psalm 46:10", "Be still, and know that I am God.", "Finding peace in God's presence", "How can you create more space for stillness with God?"),
        ("Strength", "Isaiah 40:31", "Those who hope in the LORD will renew their strength.", "Finding strength in weakness", "Where do you feel weak and need God's strength?"),
        ("Forgiveness", "Ephesians 4:32", "Be kind to one another, tenderhearted, forgiving one another, as God in Christ forgave you.", "Releasing bitterness", "Is there someone you need to forgive? Write their name and pray for them."),
        ("Purpose", "Jeremiah 29:11", "For I know the plans I have for you, declares the LORD, plans to prosper you.", "Discovering God's plan", "What do you believe God is calling you to do?"),
        ("Faith", "Hebrews 11:1", "Now faith is confidence in what we hope for and assurance about what we do not see.", "Believing without seeing", "What are you believing God for that seems impossible?"),
        ("Patience", "James 1:4", "Let patience have its perfect work, that you may be perfect and complete, lacking nothing.", "Waiting on God's timing", "What are you waiting for? How can you wait with faith?"),
        ("Love", "1 Corinthians 13:4-7", "Love is patient, love is kind. It does not envy, it does not boast.", "Loving like Jesus", "How can you show sacrificial love to someone today?"),
        ("Courage", "Joshua 1:9", "Be strong and courageous. Do not be afraid; do not be discouraged.", "Facing fear with faith", "What fear is holding you back from obeying God?"),
        ("Humility", "James 4:10", "Humble yourselves before the Lord, and He will lift you up.", "Putting others first", "Where has pride crept into your life?"),
        ("Provision", "Philippians 4:19", "And my God will meet all your needs according to the riches of His glory.", "Trusting God as provider", "What need are you asking God to provide for?"),
        ("Wisdom", "James 1:5", "If any of you lacks wisdom, let him ask God, who gives generously to all.", "Seeking God's guidance", "What decision do you need wisdom for right now?"),
        ("Joy", "Nehemiah 8:10", "The joy of the LORD is your strength.", "Finding joy in hardship", "How can you choose joy today regardless of circumstances?"),
        ("Peace", "Philippians 4:6-7", "Do not be anxious about anything, but in everything by prayer present your requests to God.", "Trading anxiety for peace", "What anxieties do you need to give to God right now?"),
        ("Boldness", "Acts 4:31", "They were all filled with the Holy Spirit and spoke the word of God boldly.", "Speaking truth with courage", "Where is God asking you to be bold?"),
        ("Breakthrough", "Isaiah 43:19", "See, I am doing a new thing! Now it springs up; do you not perceive it?", "Expecting God to move", "What breakthrough are you believing for?"),
        ("Healing", "Jeremiah 17:14", "Heal me, LORD, and I will be healed; save me and I will be saved.", "Spiritual and physical healing", "What area of your life needs God's healing touch?"),
        ("Identity", "2 Corinthians 5:17", "If anyone is in Christ, the new creation has come: The old has gone, the new is here!", "Knowing who you are in Christ", "What lies about yourself do you need to replace with God's truth?"),
        ("Generosity", "2 Corinthians 9:7", "God loves a cheerful giver.", "Giving with a joyful heart", "How can you be more generous with your time, money, or talent?"),
        ("Obedience", "John 14:15", "If you love me, keep my commands.", "Obeying God fully", "What is God asking you to do that you've been delaying?"),
        ("Community", "Hebrews 10:25", "Not giving up meeting together, as some are in the habit of doing.", "The power of togetherness", "How can you invest more deeply in Christian community?"),
        ("Perseverance", "Galatians 6:9", "Let us not become weary in doing good, for at the proper time we will reap.", "Not giving up", "What have you been tempted to give up on?"),
        ("Revival", "2 Chronicles 7:14", "If my people will humble themselves and pray and seek my face, I will heal their land.", "Praying for revival", "What does personal and community revival look like to you?"),
        ("Celebration", "Psalm 150:6", "Let everything that has breath praise the LORD!", "Celebrating God's faithfulness", "How has God moved during these 30 days? Celebrate!"),
        ("Commitment", "Psalm 37:5", "Commit your way to the LORD; trust in Him and He will do this.", "Committing beyond 30 days", "What spiritual habits will you continue after this challenge?"),
    ]

    for i, (theme, verse_ref, verse_text, focus, question) in enumerate(daily_content, 1):
        pdf.start_page()
        week = (i - 1) // 7 + 1
        pdf.add_text(f"DAY {i} - Week {week}", size=9, bold=True, color=(120, 100, 140))
        pdf.add_space(5)
        pdf.add_chapter_title(f"Day {i}: {theme}")

        # Scripture
        pdf.add_quote_box(verse_text, verse_ref)
        pdf.add_space(8)

        # Today's Focus
        pdf.add_text("Today's Focus:", size=11, bold=True, color=(51, 51, 102))
        pdf.add_wrapped_text(focus, size=10, indent=5)
        pdf.add_space(10)

        # Fasting Check-in
        pdf.add_text("Fasting Check-in:", size=11, bold=True, color=(51, 51, 102))
        pdf.add_checkbox("I maintained my fast today")
        pdf.add_text("How I feel physically/spiritually:", size=9, indent=5)
        pdf.add_lined_space(2, spacing=18)
        pdf.add_space(5)

        # Prayer Focus
        pdf.add_text("Prayer Focus:", size=11, bold=True, color=(51, 51, 102))
        pdf.add_wrapped_text(f"Spend at least 15 minutes in focused prayer about: {theme.lower()}. Ask God to reveal His will and transform your heart in this area.", size=10, indent=5)
        pdf.add_space(8)

        # Reflection Question
        pdf.add_text("Reflection Question:", size=11, bold=True, color=(51, 51, 102))
        pdf.add_wrapped_text(question, size=10, italic=True, indent=5)
        pdf.add_space(5)
        pdf.add_lined_space(4, spacing=20)

        # Journal space
        pdf.add_space(5)
        pdf.add_text("My Prayer & Thoughts Today:", size=10, bold=True, color=(80, 80, 120))
        pdf.add_lined_space(3, spacing=20)

        pdf.end_page()

    # WEEK REVIEW PAGES (4 weeks)
    for week in range(1, 5):
        pdf.start_page()
        pdf.add_chapter_title(f"Week {week} Review & Reflection")
        pdf.add_text("What did God teach me this week?", size=11, bold=True)
        pdf.add_lined_space(4)
        pdf.add_text("How has fasting affected my prayer life?", size=11, bold=True)
        pdf.add_lined_space(4)
        pdf.add_text("Prayers answered this week:", size=11, bold=True)
        pdf.add_lined_space(3)
        pdf.add_text("Biggest challenge this week:", size=11, bold=True)
        pdf.add_lined_space(3)
        pdf.add_text("My faith level (circle): 1  2  3  4  5  6  7  8  9  10", size=10, indent=10)
        pdf.end_page()

    # FINAL REFLECTION
    pdf.start_page()
    pdf.add_chapter_title("Final Reflection: 30 Days Complete!")
    pdf.add_quote_box("I can do all things through Christ who strengthens me.", "Philippians 4:13")
    pdf.add_space(10)
    pdf.add_text("How has this 30-day journey changed me?", size=11, bold=True)
    pdf.add_lined_space(5)
    pdf.add_text("Top 5 things God revealed to me:", size=11, bold=True)
    pdf.add_numbered_lines(1, 5)
    pdf.add_text("My commitment going forward:", size=11, bold=True)
    pdf.add_lined_space(4)
    pdf.end_page()

    # PRAYER LIST PAGE
    pdf.start_page()
    pdf.add_chapter_title("Ongoing Prayer List")
    pdf.add_text("People I'm praying for:", size=11, bold=True)
    pdf.add_numbered_lines(1, 10, spacing=20)
    pdf.add_space(10)
    pdf.add_text("Situations I'm praying about:", size=11, bold=True)
    pdf.add_numbered_lines(1, 8, spacing=20)
    pdf.end_page()

    # ANSWERED PRAYERS
    pdf.start_page()
    pdf.add_chapter_title("Answered Prayers - Testimonies")
    pdf.add_wrapped_text("Record answered prayers here as a testimony of God's faithfulness!", size=10, italic=True)
    pdf.add_space(10)
    for i in range(1, 9):
        pdf.add_text(f"Date: ________  Prayer Answered:", size=9, bold=True)
        pdf.add_lined_space(2, spacing=18)
        pdf.add_space(5)
    pdf.end_page()

    return pdf


def create_book_02():
    """Christian Couples 30-Day Bible Study Workbook"""
    pdf = PDFEngine()
    pdf.header_text = "Christian Couples 30-Day Bible Study Workbook"

    pdf.add_title_page(
        title="Christian Couples 30-Day Bible Study Workbook",
        subtitle="Strengthen Your Marriage Through Scripture, Prayer, and Intentional Connection",
        author="A Guided Study for Husbands & Wives",
        extra_lines=["Daily devotions, couple discussions, prayer prompts,", "and relationship-building activities"]
    )

    # INTRO
    pdf.start_page()
    pdf.add_chapter_title("Welcome, Couples!")
    pdf.add_wrapped_text("This 30-day Bible study is designed to help you and your spouse grow closer to God and to each other. Each day includes a scripture passage, a brief teaching, discussion questions for couples, a prayer you can pray together, and an action step to strengthen your bond.")
    pdf.add_space(15)
    pdf.add_text("How to Use This Workbook:", size=12, bold=True, color=(51, 51, 102))
    pdf.add_space(8)
    items = ["Set aside 20-30 minutes together daily (morning or evening)",
             "Take turns reading the scripture and teaching aloud",
             "Answer discussion questions honestly and lovingly",
             "Pray together at the end of each session",
             "Complete the action step before the next day",
             "Write personal reflections in the journal space"]
    for item in items:
        pdf.add_checkbox(item)
    pdf.add_space(15)
    pdf.add_quote_box("Though one may be overpowered, two can defend themselves. A cord of three strands is not quickly broken.", "Ecclesiastes 4:12")
    pdf.end_page()

    # TOC
    toc = [("Introduction & Couple Covenant", 2), ("Week 1: Foundation of Love (Days 1-7)", 4),
           ("Week 2: Communication & Trust (Days 8-14)", 14), ("Week 3: Intimacy & Service (Days 15-21)", 24),
           ("Week 4: Vision & Legacy (Days 22-28)", 34), ("Days 29-30: Renewal & Covenant", 44),
           ("Couple's Prayer List & Notes", 46)]
    pdf.add_toc_page(toc)

    # COUPLE COVENANT PAGE
    pdf.start_page()
    pdf.add_chapter_title("Our Couple Covenant")
    pdf.add_wrapped_text("Before beginning this journey together, make a covenant commitment to each other and to God:")
    pdf.add_space(15)
    pdf.add_text("We, _________________________ and _________________________,", size=11, indent=20)
    pdf.add_space(10)
    pdf.add_wrapped_text("commit to spending the next 30 days growing closer to God and to each other through this Bible study. We will be honest, patient, loving, and supportive as we learn and grow together.", size=10, indent=20)
    pdf.add_space(15)
    pdf.add_text("Husband's Signature: ______________________  Date: _________", size=10, indent=20)
    pdf.add_space(10)
    pdf.add_text("Wife's Signature: ________________________  Date: _________", size=10, indent=20)
    pdf.add_space(20)
    pdf.add_text("Our biggest hope for these 30 days:", size=10, bold=True)
    pdf.add_lined_space(4)
    pdf.end_page()

    couple_days = [
        ("The Foundation of Love", "1 Corinthians 13:4-8", "Love is patient, love is kind. It does not envy, it does not boast, it is not proud.", "What does patient love look like in your daily life together?", "Tell your spouse 3 specific things you love about them."),
        ("Leaving and Cleaving", "Genesis 2:24", "Therefore a man shall leave his father and mother and hold fast to his wife, and they shall become one flesh.", "Are there any outside influences that compete for your unity?", "Discuss one boundary you can set together to protect your marriage."),
        ("Speaking Life", "Proverbs 18:21", "The tongue has the power of life and death.", "How do your words build up or tear down your spouse?", "Speak 5 words of affirmation to each other right now."),
        ("Forgiving Each Other", "Colossians 3:13", "Bear with each other and forgive one another if any of you has a grievance. Forgive as the Lord forgave you.", "Is there anything unresolved between you that needs forgiveness?", "If needed, apologize for something specific and choose to forgive."),
        ("Praying Together", "Matthew 18:20", "Where two or three gather in my name, there am I with them.", "How often do you pray together? What holds you back?", "Pray together for 5 minutes right now, holding hands."),
        ("Serving One Another", "Galatians 5:13", "Serve one another humbly in love.", "How can you serve your spouse better this week?", "Do one unexpected act of service for your spouse today."),
        ("Trust and Faithfulness", "Proverbs 31:11", "The heart of her husband trusts in her, and he will have no lack of gain.", "What builds trust in your relationship? What erodes it?", "Share one way your spouse has earned your trust."),
        ("Handling Conflict", "Ephesians 4:26-27", "In your anger do not sin. Do not let the sun go down while you are still angry.", "What is your conflict style? How can you fight fair?", "Agree on 3 rules for how you will handle disagreements."),
        ("Emotional Intimacy", "Song of Solomon 2:16", "My beloved is mine, and I am his.", "Do you feel emotionally connected? What helps you feel close?", "Share something you haven't told your spouse recently."),
        ("Financial Unity", "Luke 14:28", "Suppose one of you wants to build a tower. Won't you first sit down and estimate the cost?", "Are you on the same page financially? What causes tension?", "Set one financial goal together and write it down."),
        ("Roles and Responsibilities", "Ephesians 5:21", "Submit to one another out of reverence for Christ.", "How do you divide responsibilities? Is it fair and loving?", "Discuss one area where you can better support each other."),
        ("Physical Intimacy", "1 Corinthians 7:3-5", "The husband should fulfill his marital duty to his wife, and likewise the wife to her husband.", "Are you both satisfied with your physical connection? Be honest.", "Plan a date night this week focused on connection."),
        ("Dealing with In-Laws", "Ruth 1:16", "Where you go I will go, and where you stay I will stay.", "How do extended family dynamics affect your marriage?", "Agree on one boundary regarding extended family."),
        ("Parenting Together", "Proverbs 22:6", "Start children off on the way they should go, and even when they are old they will not turn from it.", "Are you united in your parenting approach?", "Discuss one parenting value you both want to prioritize."),
        ("Dreams and Vision", "Habakkuk 2:2", "Write the vision and make it plain.", "What are your shared dreams for the next 5 years?", "Write down 3 goals you want to accomplish together."),
        ("Spiritual Leadership", "Joshua 24:15", "As for me and my household, we will serve the LORD.", "How can you both lead spiritually in your home?", "Choose one spiritual habit to start as a couple."),
        ("Gratitude for Each Other", "1 Thessalonians 5:18", "Give thanks in all circumstances.", "When was the last time you expressed gratitude to your spouse?", "Write a short love letter to your spouse tonight."),
        ("Managing Stress Together", "Psalm 55:22", "Cast your cares on the LORD and He will sustain you.", "How does stress affect your marriage? How can you support each other?", "Share your current biggest stressor and pray about it together."),
        ("Quality Time", "Ecclesiastes 3:1", "There is a time for everything, and a season for every activity under the heavens.", "Are you prioritizing quality time together?", "Schedule a weekly date night for the next month."),
        ("Supporting Each Other's Calling", "Romans 12:6", "We have different gifts, according to the grace given to each of us.", "Do you know your spouse's dreams and calling? Do you support them?", "Ask your spouse: How can I better support your calling?"),
        ("Building a Legacy", "Psalm 127:1", "Unless the LORD builds the house, the builders labor in vain.", "What legacy do you want to leave as a couple?", "Write a family mission statement together."),
        ("Friendship in Marriage", "Proverbs 17:17", "A friend loves at all times.", "Is your spouse your best friend? What makes them a good friend?", "Do something fun together that you did when you were dating."),
        ("Protecting Your Marriage", "1 Peter 5:8", "Be alert and of sober mind. Your enemy the devil prowls around like a roaring lion.", "What threats does your marriage face? How do you guard against them?", "Identify one area of vulnerability and create a plan to protect it."),
        ("Celebrating Differences", "1 Corinthians 12:14-20", "The body is not made up of one part but of many.", "What differences between you are actually strengths?", "Thank your spouse for a quality they have that you lack."),
        ("Growing Through Seasons", "Ecclesiastes 3:11", "He has made everything beautiful in its time.", "What season is your marriage in? How can you thrive in it?", "Discuss what the next season might look like and how to prepare."),
        ("Love Languages", "1 John 3:18", "Let us not love with words or speech but with actions and in truth.", "Do you know each other's love languages? Are you speaking them?", "Identify each other's top love language and do it today."),
        ("Overcoming Past Hurts", "Isaiah 43:18-19", "Forget the former things; do not dwell on the past. See, I am doing a new thing!", "Are past hurts still affecting your marriage?", "Choose to release one past hurt and pray together for healing."),
        ("Renewing Your Vows", "Song of Solomon 8:6", "Place me like a seal over your heart, like a seal on your arm; for love is as strong as death.", "What do your wedding vows mean to you now?", "Rewrite your vows to each other with what you know now."),
        ("Our Future Together", "Jeremiah 29:11", "For I know the plans I have for you, declares the LORD, plans to prosper you and not to harm you.", "What does your future look like together?", "Dream together about the next decade of your marriage."),
        ("Renewed Commitment", "Revelation 2:4-5", "You have forsaken the love you had at first. Consider how far you have fallen! Repent and do the things you did at first.", "How can you keep the passion alive?", "Commit to continuing daily couple devotions after this workbook."),
    ]

    for i, (theme, verse_ref, verse_text, discussion_q, action) in enumerate(couple_days, 1):
        pdf.start_page()
        pdf.add_text(f"DAY {i} | Week {(i-1)//7 + 1}", size=9, bold=True, color=(120, 80, 120))
        pdf.add_chapter_title(f"Day {i}: {theme}")
        pdf.add_quote_box(verse_text, verse_ref)
        pdf.add_space(6)

        pdf.add_text("Teaching:", size=11, bold=True, color=(51, 51, 102))
        pdf.add_wrapped_text(f"Today we explore the theme of {theme.lower()}. God designed marriage to reflect His love for the church. As you study this passage together, ask the Holy Spirit to reveal how you can grow in this area as a couple.", size=10, indent=5)
        pdf.add_space(8)

        pdf.add_text("Discussion Question:", size=11, bold=True, color=(51, 51, 102))
        pdf.add_wrapped_text(discussion_q, size=10, italic=True, indent=5)
        pdf.add_space(5)
        pdf.add_text("His thoughts:", size=9, color=(100, 100, 100))
        pdf.add_lined_space(2, spacing=18)
        pdf.add_text("Her thoughts:", size=9, color=(100, 100, 100))
        pdf.add_lined_space(2, spacing=18)

        pdf.add_text("Action Step:", size=11, bold=True, color=(51, 51, 102))
        pdf.add_wrapped_text(action, size=10, indent=5)
        pdf.add_space(5)

        pdf.add_text("Couple Prayer (pray together):", size=10, bold=True, color=(80, 80, 120))
        pdf.add_lined_space(2, spacing=18)
        pdf.end_page()

    # WEEKLY CHECK-INS
    for week in range(1, 5):
        pdf.start_page()
        pdf.add_chapter_title(f"Week {week} Check-In")
        pdf.add_text("Rate your connection this week (1-10): _____", size=10, bold=True)
        pdf.add_space(8)
        pdf.add_text("What was the best moment we shared?", size=10, bold=True)
        pdf.add_lined_space(3)
        pdf.add_text("What could we improve next week?", size=10, bold=True)
        pdf.add_lined_space(3)
        pdf.add_text("One thing I appreciate about my spouse:", size=10, bold=True)
        pdf.add_lined_space(3)
        pdf.add_text("Our prayer for next week:", size=10, bold=True)
        pdf.add_lined_space(4)
        pdf.end_page()

    # FINAL PAGES
    pdf.start_page()
    pdf.add_chapter_title("Our Marriage Prayer List")
    pdf.add_text("Prayers for our marriage:", size=10, bold=True)
    pdf.add_numbered_lines(1, 8, spacing=20)
    pdf.add_space(8)
    pdf.add_text("Prayers for our family:", size=10, bold=True)
    pdf.add_numbered_lines(1, 8, spacing=20)
    pdf.end_page()

    pdf.start_page()
    pdf.add_chapter_title("Love Notes to Each Other")
    pdf.add_text("From Him to Her:", size=11, bold=True, color=(51, 51, 102))
    pdf.add_lined_space(8)
    pdf.add_space(10)
    pdf.add_text("From Her to Him:", size=11, bold=True, color=(51, 51, 102))
    pdf.add_lined_space(8)
    pdf.end_page()

    return pdf


def create_book_03():
    """Christian Marriage Reset Workbook"""
    pdf = PDFEngine()
    pdf.header_text = "Christian Marriage Reset Workbook"

    pdf.add_title_page(
        title="Christian Marriage Reset Workbook",
        subtitle="Rebuild, Restore, and Renew Your Marriage on God's Foundation",
        author="A 6-Week Guided Workbook for Couples",
        extra_lines=["For couples seeking healing, restoration,", "and a fresh start in their marriage"]
    )

    pdf.start_page()
    pdf.add_chapter_title("Introduction: Why a Marriage Reset?")
    pdf.add_wrapped_text("Every marriage goes through seasons of difficulty. Whether you are facing communication breakdown, trust issues, emotional distance, or simply feeling stuck, this workbook is designed to help you and your spouse hit the 'reset' button and rebuild your marriage on the solid foundation of God's Word.")
    pdf.add_space(10)
    pdf.add_wrapped_text("This is not about blame. It's not about who's right or wrong. It's about two people choosing to humble themselves before God and each other, to heal what's broken, and to create something beautiful together.", size=10)
    pdf.add_space(15)
    pdf.add_text("This workbook covers 6 key areas:", size=11, bold=True)
    pdf.add_space(6)
    areas = ["Week 1: Honest Assessment - Where are we now?",
             "Week 2: Forgiveness & Healing - Releasing the past",
             "Week 3: Communication Reset - Learning to truly listen",
             "Week 4: Trust Rebuilding - One step at a time",
             "Week 5: Intimacy Restoration - Reconnecting heart to heart",
             "Week 6: Vision Renewal - Building our future together"]
    for a in areas:
        pdf.add_text(f"  * {a}", size=10, indent=10)
        pdf.add_space(4)
    pdf.end_page()

    toc = [("Introduction", 2), ("Week 1: Honest Assessment", 4), ("Week 2: Forgiveness & Healing", 11),
           ("Week 3: Communication Reset", 18), ("Week 4: Trust Rebuilding", 25),
           ("Week 5: Intimacy Restoration", 32), ("Week 6: Vision Renewal", 39),
           ("Ongoing Maintenance Plan", 44), ("Marriage Prayer & Journal Pages", 46)]
    pdf.add_toc_page(toc)

    # PRE-ASSESSMENT
    pdf.start_page()
    pdf.add_chapter_title("Marriage Health Assessment")
    pdf.add_wrapped_text("Before beginning, honestly rate each area (1=crisis, 5=great, 10=thriving):")
    pdf.add_space(10)
    assessment_items = ["Communication", "Trust", "Emotional Connection", "Physical Intimacy",
                        "Conflict Resolution", "Spiritual Unity", "Fun & Friendship",
                        "Financial Agreement", "Parenting Unity", "Future Vision Alignment"]
    for item in assessment_items:
        pdf.add_text(f"  {item}: ___ /10", size=10, indent=10)
        pdf.add_space(5)
    pdf.add_space(10)
    pdf.add_text("Overall Marriage Health Score: ___ /100", size=11, bold=True)
    pdf.add_space(10)
    pdf.add_text("The area that needs the most attention:", size=10, bold=True)
    pdf.add_lined_space(2)
    pdf.end_page()

    # 6 WEEKS OF CONTENT (7 days each = 42 days of content)
    weeks = [
        ("Honest Assessment", [
            ("Acknowledging the Pain", "Where does it hurt in our marriage?"),
            ("My Part in Our Problems", "What have I contributed to our struggles?"),
            ("What I Miss About Us", "What do I long to restore?"),
            ("Unrealistic Expectations", "What expectations have been unfair?"),
            ("Our Strengths", "What is still good about our marriage?"),
            ("What God Says About Us", "How does God see our marriage?"),
            ("Choosing Hope", "Why am I choosing to fight for this marriage?"),
        ]),
        ("Forgiveness & Healing", [
            ("The Weight of Unforgiveness", "What bitterness am I carrying?"),
            ("Understanding Forgiveness", "What forgiveness IS and IS NOT"),
            ("Forgiving My Spouse", "Releasing specific hurts"),
            ("Forgiving Myself", "Letting go of guilt and shame"),
            ("Healing Conversations", "Speaking truth with love"),
            ("Setting New Boundaries", "What healthy boundaries do we need?"),
            ("Moving Forward Free", "Choosing to not bring up the past"),
        ]),
        ("Communication Reset", [
            ("How We Got Here", "Where did communication break down?"),
            ("Active Listening", "Hearing without defending"),
            ("Speaking with Love", "Words that build, not destroy"),
            ("Non-Verbal Communication", "What our body language says"),
            ("Conflict without Contempt", "Fighting fair"),
            ("Daily Check-ins", "Building communication habits"),
            ("Asking Better Questions", "Going deeper in conversation"),
        ]),
        ("Trust Rebuilding", [
            ("Understanding Broken Trust", "What happened and how it felt"),
            ("Transparency", "Open phones, open hearts"),
            ("Consistency Over Time", "Trust is rebuilt daily"),
            ("Accountability", "Who holds us accountable?"),
            ("Vulnerability Again", "The courage to be open"),
            ("Rebuilding Safety", "Creating emotional security"),
            ("Choosing to Trust God Together", "When we can't trust each other fully yet"),
        ]),
        ("Intimacy Restoration", [
            ("Emotional Intimacy", "Being truly known and accepted"),
            ("Spiritual Intimacy", "Praying and worshipping together"),
            ("Physical Touch", "Rebuilding physical connection"),
            ("Quality Time", "Being present with each other"),
            ("Words of Affirmation", "Building each other up daily"),
            ("Acts of Service", "Showing love through action"),
            ("Romantic Renewal", "Dating your spouse again"),
        ]),
        ("Vision Renewal", [
            ("Dreaming Together Again", "What do we want our future to look like?"),
            ("Family Mission Statement", "Defining our purpose as a couple"),
            ("Financial Goals", "Getting on the same page with money"),
            ("Spiritual Goals", "Growing together in faith"),
            ("Relationship Maintenance", "Preventing future drift"),
            ("Getting Help When Needed", "The strength of asking for counseling"),
            ("Our Renewed Covenant", "Recommitting to each other and to God"),
        ]),
    ]

    for week_num, (week_title, days) in enumerate(weeks, 1):
        for day_num, (day_title, day_prompt) in enumerate(days, 1):
            pdf.start_page()
            overall_day = (week_num - 1) * 7 + day_num
            pdf.add_text(f"WEEK {week_num} | Day {day_num}", size=9, bold=True, color=(120, 80, 100))
            pdf.add_chapter_title(f"{day_title}")
            pdf.add_text(f"Theme: {week_title}", size=10, italic=True, color=(100, 80, 120))
            pdf.add_space(10)

            pdf.add_text("Today's Focus:", size=11, bold=True, color=(51, 51, 102))
            pdf.add_wrapped_text(day_prompt, size=10, indent=5)
            pdf.add_space(8)

            pdf.add_text("Individual Reflection (answer separately):", size=10, bold=True, color=(51, 51, 102))
            pdf.add_text("His Response:", size=9, color=(80, 80, 80))
            pdf.add_lined_space(3, spacing=18)
            pdf.add_text("Her Response:", size=9, color=(80, 80, 80))
            pdf.add_lined_space(3, spacing=18)

            pdf.add_text("Together Discussion:", size=10, bold=True, color=(51, 51, 102))
            pdf.add_lined_space(3, spacing=18)

            pdf.add_text("Prayer Together:", size=10, bold=True, color=(80, 80, 120))
            pdf.add_lined_space(2, spacing=18)
            pdf.end_page()

    # POST-ASSESSMENT
    pdf.start_page()
    pdf.add_chapter_title("Post-Reset Assessment")
    pdf.add_wrapped_text("After completing 6 weeks, rate each area again:")
    pdf.add_space(10)
    for item in assessment_items:
        pdf.add_text(f"  {item}: ___ /10  (Change: +/- ___)", size=10, indent=10)
        pdf.add_space(5)
    pdf.add_space(10)
    pdf.add_text("New Overall Score: ___ /100", size=11, bold=True)
    pdf.add_space(10)
    pdf.add_text("Our biggest growth area:", size=10, bold=True)
    pdf.add_lined_space(3)
    pdf.end_page()

    # MAINTENANCE PLAN
    pdf.start_page()
    pdf.add_chapter_title("Ongoing Marriage Maintenance Plan")
    pdf.add_text("Daily habits we commit to:", size=10, bold=True)
    pdf.add_lined_space(3)
    pdf.add_text("Weekly habits we commit to:", size=10, bold=True)
    pdf.add_lined_space(3)
    pdf.add_text("Monthly habits we commit to:", size=10, bold=True)
    pdf.add_lined_space(3)
    pdf.add_text("Our accountability couple/mentor:", size=10, bold=True)
    pdf.add_lined_space(2)
    pdf.add_text("When to seek professional help:", size=10, bold=True)
    pdf.add_lined_space(3)
    pdf.end_page()

    # JOURNAL PAGES
    for i in range(4):
        pdf.add_blank_journal_page(header="Marriage Journal & Notes")

    # EXTRA: Date Night Ideas
    pdf.start_page()
    pdf.add_chapter_title("Date Night Ideas")
    date_ideas = [
        "Cook a new recipe together", "Take a sunset walk and talk",
        "Have a picnic in your living room", "Read a book together",
        "Play a board game (no phones!)", "Recreate your first date",
        "Write love letters to each other", "Star gaze and pray together",
        "Take a dance class (even on YouTube!)", "Volunteer together at church",
        "Go on a breakfast date", "Visit a place you've never been",
        "Create a vision board for your marriage", "Watch your wedding video",
        "Take photos together like you're dating again"
    ]
    for i, idea in enumerate(date_ideas, 1):
        pdf.add_checkbox(f"{i}. {idea}")
    pdf.end_page()

    # EXTRA: Communication Tools
    pdf.start_page()
    pdf.add_chapter_title("Communication Toolkit")
    pdf.add_text("Phrases to USE:", size=11, bold=True, color=(0, 120, 0))
    pdf.add_space(5)
    good_phrases = ['"I feel ___ when you ___"', '"Help me understand..."', '"What I hear you saying is..."',
                    '"I appreciate when you..."', '"Can we talk about this calmly?"', '"I was wrong. I am sorry."',
                    '"How can I support you?"', '"I love you even when we disagree"']
    for p in good_phrases:
        pdf.add_text(f"  * {p}", size=10, indent=10)
        pdf.add_space(3)
    pdf.add_space(10)
    pdf.add_text("Phrases to AVOID:", size=11, bold=True, color=(180, 0, 0))
    pdf.add_space(5)
    bad_phrases = ['"You ALWAYS..." / "You NEVER..."', '"Whatever."', '"My mom/dad was right about you"',
                   '"I do not care"', '"You are just like your father/mother"', '"Fine." (when it is not fine)']
    for p in bad_phrases:
        pdf.add_text(f"  X {p}", size=10, indent=10, color=(150, 50, 50))
        pdf.add_space(3)
    pdf.end_page()

    return pdf


def create_book_04():
    """30-Day Christian Gratitude Journal"""
    pdf = PDFEngine()
    pdf.header_text = "30-Day Christian Gratitude Journal"

    pdf.add_title_page(
        title="30-Day Christian Gratitude Journal",
        subtitle="Transform Your Heart Through Daily Thanksgiving and Scripture",
        author="A Guided Gratitude & Bible Devotional",
        extra_lines=["Daily scripture, gratitude prompts, reflection space,", "and prayers of thanksgiving"]
    )

    pdf.start_page()
    pdf.add_chapter_title("The Power of Gratitude")
    pdf.add_quote_box("Give thanks to the LORD, for He is good; His love endures forever.", "Psalm 107:1")
    pdf.add_space(10)
    pdf.add_wrapped_text("Scientific studies show that practicing gratitude rewires our brains for happiness, reduces stress, improves sleep, and strengthens relationships. But as Christians, we know that gratitude is more than a self-help tool -- it is an act of worship that draws us closer to God.")
    pdf.add_space(10)
    pdf.add_wrapped_text("This 30-day journal will guide you to:")
    pdf.add_space(5)
    items = ["Recognize God's blessings in every area of life",
             "Develop a thankful heart that overcomes negativity",
             "Find gratitude even in difficult circumstances",
             "Deepen your prayer life through thanksgiving",
             "Transform your perspective from scarcity to abundance"]
    for item in items:
        pdf.add_text(f"  * {item}", size=10, indent=10)
        pdf.add_space(3)
    pdf.end_page()

    toc = [("Introduction & How to Use", 2), ("Days 1-7: Gratitude for the Basics", 4),
           ("Days 8-14: Gratitude for Relationships", 14), ("Days 15-21: Gratitude in Difficulty", 24),
           ("Days 22-28: Gratitude for the Spiritual", 34), ("Days 29-30: Gratitude Going Forward", 44),
           ("Gratitude List & Overflow Pages", 46)]
    pdf.add_toc_page(toc)

    gratitude_days = [
        ("Grateful for Life", "Psalm 139:14", "I praise you because I am fearfully and wonderfully made.", "Thank God for the gift of life itself. You are alive today - that is a miracle!"),
        ("Grateful for Health", "3 John 1:2", "I pray that you may enjoy good health.", "Thank God for your body - even the parts that work imperfectly."),
        ("Grateful for Food", "Psalm 104:14-15", "He makes grass grow for the cattle, and plants for people to cultivate.", "Thank God for every meal. Many go without."),
        ("Grateful for Shelter", "Psalm 91:1-2", "Whoever dwells in the shelter of the Most High will rest in the shadow of the Almighty.", "Thank God for a roof over your head and a place to rest."),
        ("Grateful for Nature", "Psalm 19:1", "The heavens declare the glory of God; the skies proclaim the work of His hands.", "Step outside and notice God's creation around you."),
        ("Grateful for Rest", "Matthew 11:28", "Come to me, all you who are weary and burdened, and I will give you rest.", "Thank God for sleep, weekends, and moments of peace."),
        ("Grateful for Today", "Psalm 118:24", "This is the day the LORD has made; let us rejoice and be glad in it.", "Today is a gift. What makes today worth celebrating?"),
        ("Grateful for Family", "Psalm 127:3", "Children are a heritage from the LORD, offspring a reward from Him.", "Thank God for your family - even the complicated ones."),
        ("Grateful for Friends", "Proverbs 27:17", "As iron sharpens iron, so one person sharpens another.", "Who are the friends God has placed in your life?"),
        ("Grateful for Spouse/Partner", "Proverbs 18:22", "He who finds a wife finds what is good and receives favor from the LORD.", "Thank God for love and companionship."),
        ("Grateful for Mentors", "Proverbs 27:9", "The heartfelt counsel of a friend is as sweet as perfume.", "Who has spoken wisdom into your life?"),
        ("Grateful for Children", "Psalm 127:3-5", "Like arrows in the hands of a warrior are children born in one's youth.", "Thank God for the children in your life."),
        ("Grateful for Community", "Acts 2:42", "They devoted themselves to the apostles' teaching and to fellowship.", "Thank God for your church and spiritual family."),
        ("Grateful for Kindness Received", "Galatians 6:2", "Carry each other's burdens.", "When has someone shown you unexpected kindness?"),
        ("Grateful in Difficulty", "James 1:2-4", "Consider it pure joy when you face trials of many kinds.", "What trials have actually made you stronger?"),
        ("Grateful for Growth", "Romans 5:3-4", "Suffering produces perseverance; perseverance, character; character, hope.", "How has pain produced growth in your life?"),
        ("Grateful for God's Timing", "Ecclesiastes 3:11", "He has made everything beautiful in its time.", "When did waiting lead to something better than expected?"),
        ("Grateful for Unanswered Prayers", "Isaiah 55:8-9", "My thoughts are not your thoughts, neither are your ways my ways.", "What prayer are you now thankful God didn't answer your way?"),
        ("Grateful for Second Chances", "Lamentations 3:22-23", "His mercies are new every morning.", "When has God given you a fresh start?"),
        ("Grateful for Lessons Learned", "Proverbs 3:11-12", "Do not despise the LORD's discipline.", "What hard lesson are you now grateful for?"),
        ("Grateful Through Tears", "Psalm 30:5", "Weeping may stay for the night, but rejoicing comes in the morning.", "Even in sorrow, what can you be thankful for?"),
        ("Grateful for Salvation", "Ephesians 2:8-9", "For it is by grace you have been saved, through faith.", "Thank God for the free gift of salvation."),
        ("Grateful for the Bible", "Psalm 119:105", "Your word is a lamp for my feet, a light on my path.", "How has God's Word guided your life?"),
        ("Grateful for Prayer", "Philippians 4:6", "In every situation, by prayer, present your requests to God.", "Thank God that you can talk to Him anytime, anywhere."),
        ("Grateful for the Holy Spirit", "John 14:26", "The Helper, the Holy Spirit, will teach you all things.", "How has the Holy Spirit guided, comforted, or convicted you?"),
        ("Grateful for God's Faithfulness", "Deuteronomy 7:9", "The LORD your God is God; He is the faithful God.", "Recall a time when God proved His faithfulness to you."),
        ("Grateful for Heaven", "John 14:2-3", "In my Father's house are many rooms. I am going to prepare a place for you.", "Thank God for the hope of eternity."),
        ("Grateful for Grace", "2 Corinthians 12:9", "My grace is sufficient for you, for my power is made perfect in weakness.", "Where have you experienced undeserved grace?"),
        ("Grateful for Everything", "1 Thessalonians 5:18", "Give thanks in all circumstances; for this is God's will for you in Christ Jesus.", "Commit to gratitude as a lifestyle, not just a 30-day challenge."),
        ("Gratitude Going Forward", "Colossians 3:15", "Let the peace of Christ rule in your hearts...And be thankful.", "How will you maintain a grateful heart beyond these 30 days?"),
    ]

    for i, (theme, verse_ref, verse_text, prompt) in enumerate(gratitude_days, 1):
        pdf.start_page()
        pdf.add_text(f"DAY {i}", size=9, bold=True, color=(120, 100, 50))
        pdf.add_chapter_title(f"Day {i}: {theme}")
        pdf.add_quote_box(verse_text, verse_ref, bg_color=(0.98, 0.97, 0.92))
        pdf.add_space(6)

        pdf.add_text("Today's Gratitude Focus:", size=11, bold=True, color=(120, 100, 50))
        pdf.add_wrapped_text(prompt, size=10, indent=5)
        pdf.add_space(10)

        pdf.add_text("3 Things I'm Grateful For Today:", size=10, bold=True, color=(51, 51, 102))
        pdf.add_numbered_lines(1, 3, spacing=22)

        pdf.add_text("How I Saw God Today:", size=10, bold=True, color=(51, 51, 102))
        pdf.add_lined_space(3, spacing=20)

        pdf.add_text("My Prayer of Thanks:", size=10, bold=True, color=(80, 80, 120))
        pdf.add_lined_space(3, spacing=20)

        pdf.add_space(5)
        pdf.add_text("Today's mood: (circle)  Joyful  Peaceful  Struggling  Hopeful  Blessed", size=9, color=(100, 100, 100))
        pdf.end_page()

    # GRATITUDE LIST PAGES
    for page_num in range(4):
        pdf.start_page()
        pdf.add_chapter_title("100 Things I'm Grateful For" if page_num == 0 else "...continued")
        start = page_num * 25 + 1
        pdf.add_numbered_lines(start, 25, spacing=22)
        pdf.end_page()

    # WEEKLY REFLECTION PAGES
    for week in range(1, 5):
        pdf.start_page()
        pdf.add_chapter_title(f"Week {week} Gratitude Reflection")
        pdf.add_text("My top 3 blessings this week:", size=10, bold=True)
        pdf.add_numbered_lines(1, 3, spacing=22)
        pdf.add_text("Something unexpected I was grateful for:", size=10, bold=True)
        pdf.add_lined_space(3)
        pdf.add_text("How gratitude changed my attitude this week:", size=10, bold=True)
        pdf.add_lined_space(3)
        pdf.add_text("A person I want to thank:", size=10, bold=True)
        pdf.add_lined_space(2)
        pdf.add_text("My prayer of thanksgiving:", size=10, bold=True)
        pdf.add_lined_space(4)
        pdf.end_page()

    # GRATITUDE LETTER
    pdf.start_page()
    pdf.add_chapter_title("Gratitude Letter")
    pdf.add_wrapped_text("Write a letter of gratitude to someone who has impacted your life. Consider sending it to them!", size=10, italic=True)
    pdf.add_space(10)
    pdf.add_text("Dear _________________________,", size=10)
    pdf.add_space(8)
    pdf.add_lined_space(20, spacing=22)
    pdf.end_page()

    # GRATITUDE IN HARD TIMES
    pdf.start_page()
    pdf.add_chapter_title("Finding Gratitude in Hard Seasons")
    pdf.add_quote_box("And we know that in all things God works for the good of those who love Him.", "Romans 8:28")
    pdf.add_space(10)
    pdf.add_text("My current struggle:", size=10, bold=True)
    pdf.add_lined_space(3)
    pdf.add_text("3 things I can STILL be grateful for despite this:", size=10, bold=True)
    pdf.add_numbered_lines(1, 3, spacing=22)
    pdf.add_text("How has God been faithful in past difficulties?", size=10, bold=True)
    pdf.add_lined_space(4)
    pdf.add_text("A promise from God's Word I'm holding onto:", size=10, bold=True)
    pdf.add_lined_space(3)
    pdf.end_page()

    # FINAL CELEBRATION
    pdf.start_page()
    pdf.add_chapter_title("30 Days Complete! Celebration!")
    pdf.add_wrapped_text("You made it! 30 days of intentional gratitude. Look back and see how God has worked:")
    pdf.add_space(10)
    pdf.add_text("How has my perspective changed?", size=10, bold=True)
    pdf.add_lined_space(4)
    pdf.add_text("My biggest gratitude breakthrough:", size=10, bold=True)
    pdf.add_lined_space(3)
    pdf.add_text("Habits I want to continue:", size=10, bold=True)
    pdf.add_lined_space(3)
    pdf.add_text("My commitment: I will continue practicing gratitude by:", size=10, bold=True)
    pdf.add_lined_space(4)
    pdf.add_space(10)
    pdf.add_quote_box("Enter His gates with thanksgiving and His courts with praise; give thanks to Him and praise His name.", "Psalm 100:4")
    pdf.end_page()

    return pdf


def create_book_05():
    """Bible Study Workbook for Beginners"""
    pdf = PDFEngine()
    pdf.header_text = "Bible Study Workbook for Beginners"

    pdf.add_title_page(
        title="Bible Study Workbook for Beginners",
        subtitle="Your Complete Guide to Understanding, Studying, and Applying God's Word",
        author="A Step-by-Step Workbook",
        extra_lines=["Perfect for new believers, curious seekers,", "and anyone wanting to go deeper in Scripture"]
    )

    pdf.start_page()
    pdf.add_chapter_title("Welcome to Bible Study!")
    pdf.add_wrapped_text("Congratulations on taking this step! Whether you are a brand new Christian, someone returning to faith, or simply curious about what the Bible says, this workbook will guide you through the basics of studying God's Word in a way that is practical, engaging, and life-changing.")
    pdf.add_space(10)
    pdf.add_text("What you'll learn:", size=11, bold=True)
    pdf.add_space(5)
    items = ["How the Bible is organized (Old Testament & New Testament)",
             "Different methods of Bible study (SOAP, Inductive, Topical)",
             "How to understand context, culture, and application",
             "Key Bible stories and themes you need to know",
             "How to apply what you read to your daily life",
             "How to develop a consistent Bible reading habit"]
    for item in items:
        pdf.add_text(f"  * {item}", size=10, indent=10)
        pdf.add_space(3)
    pdf.add_space(10)
    pdf.add_quote_box("All Scripture is God-breathed and is useful for teaching, rebuking, correcting and training in righteousness.", "2 Timothy 3:16")
    pdf.end_page()

    toc = [("Introduction & Welcome", 2), ("Part 1: Understanding the Bible (Overview)", 4),
           ("Part 2: Bible Study Methods", 10), ("Part 3: Key Stories & Themes", 18),
           ("Part 4: Books of the Bible Guide", 26), ("Part 5: Practical Application", 34),
           ("Part 6: Building Your Bible Habit", 40), ("Journal & Notes Pages", 44)]
    pdf.add_toc_page(toc)

    # PART 1: UNDERSTANDING THE BIBLE
    pdf.start_page()
    pdf.add_chapter_title("Part 1: Understanding the Bible", "How is the Bible organized?")
    pdf.add_wrapped_text("The Bible is a library of 66 books written by about 40 authors over 1,500 years. Yet it tells one unified story: God's love for humanity and His plan to save us through Jesus Christ.")
    pdf.add_space(10)
    pdf.add_text("The Bible is divided into two main parts:", size=11, bold=True)
    pdf.add_space(8)
    pdf.add_text("OLD TESTAMENT (39 books) - Before Jesus", size=11, bold=True, color=(120, 80, 50))
    pdf.add_text("  * Law (Genesis-Deuteronomy): God's rules and Israel's beginning", size=10, indent=10)
    pdf.add_text("  * History (Joshua-Esther): Israel's story as a nation", size=10, indent=10)
    pdf.add_text("  * Poetry (Job-Song of Solomon): Wisdom, worship, and life", size=10, indent=10)
    pdf.add_text("  * Prophets (Isaiah-Malachi): God's messengers and warnings", size=10, indent=10)
    pdf.add_space(10)
    pdf.add_text("NEW TESTAMENT (27 books) - Jesus and After", size=11, bold=True, color=(50, 80, 120))
    pdf.add_text("  * Gospels (Matthew-John): The life and teachings of Jesus", size=10, indent=10)
    pdf.add_text("  * Acts: The early church's story", size=10, indent=10)
    pdf.add_text("  * Letters (Romans-Jude): Teaching for Christians", size=10, indent=10)
    pdf.add_text("  * Revelation: The future and God's ultimate victory", size=10, indent=10)
    pdf.add_space(10)
    pdf.add_text("Where should a beginner start?", size=11, bold=True)
    pdf.add_wrapped_text("Start with the Gospel of John (the story of Jesus), then read Genesis (the beginning), then Psalms (prayers and worship), then Romans (core Christian beliefs).", size=10, indent=5)
    pdf.end_page()

    # BIBLE OVERVIEW EXERCISE
    pdf.start_page()
    pdf.add_chapter_title("Exercise: Bible Overview")
    pdf.add_text("Fill in what you know (don't worry if you can't answer all):", size=10, italic=True)
    pdf.add_space(10)
    questions = [
        "How many books are in the Bible total?",
        "What are the first 5 books called?",
        "Name the 4 Gospels:",
        "Who wrote most of the New Testament letters?",
        "What is the longest book in the Bible?",
        "What is the shortest book?",
        "Where would you find the 10 Commandments?",
        "What book tells the story of Jesus' birth?",
    ]
    for q in questions:
        pdf.add_text(q, size=10, bold=True)
        pdf.add_lined_space(1, spacing=20)
        pdf.add_space(5)
    pdf.end_page()

    # PART 2: BIBLE STUDY METHODS
    pdf.start_page()
    pdf.add_chapter_title("Part 2: Bible Study Methods")
    pdf.add_text("Method 1: SOAP Method", size=13, bold=True, color=(51, 51, 102))
    pdf.add_space(8)
    soap = [("S - Scripture", "Write out the verse or passage that stands out to you"),
            ("O - Observation", "What do you notice? Who is speaking? What is happening?"),
            ("A - Application", "How does this apply to your life today?"),
            ("P - Prayer", "Write a prayer based on what you learned")]
    for letter, desc in soap:
        pdf.add_text(f"  {letter}", size=11, bold=True, color=(80, 50, 120))
        pdf.add_text(f"    {desc}", size=10, indent=15)
        pdf.add_space(5)
    pdf.add_space(15)
    pdf.add_text("Method 2: 5 W's + H Method", size=13, bold=True, color=(51, 51, 102))
    pdf.add_space(8)
    ws = ["WHO is speaking/being spoken to?", "WHAT is happening in this passage?",
          "WHEN did this take place?", "WHERE is this happening?",
          "WHY is this important?", "HOW does this apply to me?"]
    for w in ws:
        pdf.add_text(f"  * {w}", size=10, indent=10)
        pdf.add_space(3)
    pdf.end_page()

    # SOAP PRACTICE PAGES (multiple)
    soap_passages = [
        ("John 3:16", "For God so loved the world that He gave His one and only Son, that whoever believes in Him shall not perish but have eternal life."),
        ("Psalm 23:1-3", "The LORD is my shepherd, I lack nothing. He makes me lie down in green pastures, He leads me beside quiet waters, He refreshes my soul."),
        ("Philippians 4:13", "I can do all this through Him who gives me strength."),
        ("Jeremiah 29:11", "For I know the plans I have for you, declares the LORD, plans to prosper you and not to harm you, plans to give you hope and a future."),
        ("Romans 8:28", "And we know that in all things God works for the good of those who love Him, who have been called according to His purpose."),
    ]

    for verse_ref, verse_text in soap_passages:
        pdf.start_page()
        pdf.add_chapter_title(f"SOAP Practice: {verse_ref}")
        pdf.add_quote_box(verse_text, verse_ref)
        pdf.add_space(8)
        pdf.add_text("S - Scripture (Write it in your own words):", size=10, bold=True)
        pdf.add_lined_space(2, spacing=20)
        pdf.add_text("O - Observation (What do you notice?):", size=10, bold=True)
        pdf.add_lined_space(3, spacing=20)
        pdf.add_text("A - Application (How does this apply to YOUR life?):", size=10, bold=True)
        pdf.add_lined_space(3, spacing=20)
        pdf.add_text("P - Prayer (Write a prayer based on this verse):", size=10, bold=True)
        pdf.add_lined_space(3, spacing=20)
        pdf.end_page()

    # KEY STORIES
    pdf.start_page()
    pdf.add_chapter_title("Part 3: Key Bible Stories to Know")
    stories = [
        ("Creation", "Genesis 1-2", "God made everything and it was good"),
        ("The Fall", "Genesis 3", "Sin entered the world through disobedience"),
        ("Noah's Ark", "Genesis 6-9", "God saved the faithful through the flood"),
        ("Abraham's Call", "Genesis 12", "God chose a people for Himself"),
        ("The Exodus", "Exodus 14", "God delivered His people from slavery"),
        ("David & Goliath", "1 Samuel 17", "Faith overcomes impossible odds"),
        ("The Birth of Jesus", "Luke 2", "God became human to save us"),
        ("Jesus' Teachings", "Matthew 5-7", "How to live in God's kingdom"),
        ("The Cross", "John 19", "Jesus died for our sins"),
        ("The Resurrection", "John 20", "Jesus conquered death"),
        ("Pentecost", "Acts 2", "The Holy Spirit came to believers"),
        ("Paul's Conversion", "Acts 9", "God transforms the worst sinners"),
    ]
    for title, ref, summary in stories:
        pdf.add_text(f"  {title} ({ref})", size=10, bold=True, indent=5)
        pdf.add_text(f"    {summary}", size=9, indent=15, color=(80, 80, 80))
        pdf.add_space(4)
    pdf.end_page()

    # KEY STORIES WORKSHEET
    pdf.start_page()
    pdf.add_chapter_title("Key Stories Worksheet")
    pdf.add_text("Read ONE story from the list and answer:", size=10, italic=True)
    pdf.add_space(10)
    pdf.add_text("Story I read: ____________________________", size=10, bold=True)
    pdf.add_space(8)
    pdf.add_text("What happened in this story?", size=10, bold=True)
    pdf.add_lined_space(4)
    pdf.add_text("What does this teach me about God?", size=10, bold=True)
    pdf.add_lined_space(4)
    pdf.add_text("What does this teach me about people?", size=10, bold=True)
    pdf.add_lined_space(3)
    pdf.add_text("How does this connect to Jesus?", size=10, bold=True)
    pdf.add_lined_space(3)
    pdf.add_text("What can I apply to my life today?", size=10, bold=True)
    pdf.add_lined_space(3)
    pdf.end_page()

    # BOOKS OF THE BIBLE GUIDE
    pdf.start_page()
    pdf.add_chapter_title("Part 4: Books of the Bible Quick Guide")
    pdf.add_text("OLD TESTAMENT", size=12, bold=True, color=(120, 80, 50))
    pdf.add_space(5)
    ot_books = ["Genesis - The beginning of everything", "Exodus - God rescues Israel from Egypt",
                "Psalms - Songs of worship and prayer", "Proverbs - Practical wisdom for life",
                "Isaiah - The coming Messiah prophesied", "Jeremiah - God's faithfulness in judgment",
                "Daniel - Faith under pressure"]
    for b in ot_books:
        pdf.add_text(f"  * {b}", size=9, indent=10)
        pdf.add_space(2)
    pdf.add_space(10)
    pdf.add_text("NEW TESTAMENT", size=12, bold=True, color=(50, 80, 120))
    pdf.add_space(5)
    nt_books = ["Matthew - Jesus as King", "Mark - Jesus as Servant",
                "Luke - Jesus as perfect human", "John - Jesus as God",
                "Acts - The early church's story", "Romans - Core Christian theology",
                "1 Corinthians - Church problems and solutions",
                "Ephesians - Our identity in Christ", "Philippians - Joy in all circumstances",
                "James - Faith in action", "Revelation - God's ultimate victory"]
    for b in nt_books:
        pdf.add_text(f"  * {b}", size=9, indent=10)
        pdf.add_space(2)
    pdf.end_page()

    # READING PLANS
    pdf.start_page()
    pdf.add_chapter_title("Part 5: Your First Reading Plan")
    pdf.add_wrapped_text("Here is a 14-day reading plan perfect for beginners. Check off each day as you complete it:")
    pdf.add_space(10)
    reading_plan = [
        "Day 1: John 1 - Jesus is the Word",
        "Day 2: John 3 - You must be born again",
        "Day 3: John 4 - The woman at the well",
        "Day 4: John 10 - The Good Shepherd",
        "Day 5: John 11 - Jesus raises Lazarus",
        "Day 6: John 13-14 - The Last Supper",
        "Day 7: John 19-20 - The Cross & Resurrection",
        "Day 8: Genesis 1-2 - Creation",
        "Day 9: Genesis 3 - The Fall",
        "Day 10: Psalm 23 - The LORD is my shepherd",
        "Day 11: Psalm 91 - God's protection",
        "Day 12: Romans 3 - All have sinned",
        "Day 13: Romans 8 - Nothing separates us from God",
        "Day 14: Ephesians 2 - Saved by grace",
    ]
    for day in reading_plan:
        pdf.add_checkbox(day)
    pdf.end_page()

    # BUILDING HABITS
    pdf.start_page()
    pdf.add_chapter_title("Part 6: Building Your Bible Habit")
    pdf.add_text("Tips for Daily Bible Reading:", size=11, bold=True)
    pdf.add_space(8)
    tips = [
        "Choose a consistent time (morning is best for most people)",
        "Start small - even 5 minutes counts!",
        "Find a quiet, comfortable place",
        "Keep a journal or notebook nearby",
        "Use a Bible reading plan to stay on track",
        "Don't try to understand everything at once",
        "Ask God to speak to you before you read",
        "Talk to someone about what you're learning",
    ]
    for tip in tips:
        pdf.add_checkbox(tip)
    pdf.add_space(15)
    pdf.add_text("My Bible Study Commitment:", size=11, bold=True, color=(51, 51, 102))
    pdf.add_space(8)
    pdf.add_text("I will read my Bible at: ____________ (time)", size=10)
    pdf.add_space(5)
    pdf.add_text("In this place: ________________________", size=10)
    pdf.add_space(5)
    pdf.add_text("For at least: _____ minutes per day", size=10)
    pdf.add_space(5)
    pdf.add_text("Starting: _______________", size=10)
    pdf.add_space(5)
    pdf.add_text("Signature: ________________________  Date: _________", size=10)
    pdf.end_page()

    # JOURNAL PAGES
    for i in range(3):
        pdf.start_page()
        pdf.add_chapter_title("Bible Study Notes")
        pdf.add_text("Date: _________  Passage: _________________________", size=9)
        pdf.add_space(8)
        pdf.add_text("S - Scripture:", size=10, bold=True)
        pdf.add_lined_space(3, spacing=18)
        pdf.add_text("O - Observation:", size=10, bold=True)
        pdf.add_lined_space(3, spacing=18)
        pdf.add_text("A - Application:", size=10, bold=True)
        pdf.add_lined_space(3, spacing=18)
        pdf.add_text("P - Prayer:", size=10, bold=True)
        pdf.add_lined_space(3, spacing=18)
        pdf.end_page()

    # ADDITIONAL: KEY VERSES TO MEMORIZE
    pdf.start_page()
    pdf.add_chapter_title("Key Verses to Memorize")
    pdf.add_wrapped_text("Start by memorizing these foundational verses. Check each one off as you learn it:")
    pdf.add_space(10)
    memory_verses = [
        ("John 3:16", "For God so loved the world..."),
        ("Romans 3:23", "For all have sinned and fall short..."),
        ("Romans 6:23", "For the wages of sin is death..."),
        ("Ephesians 2:8-9", "For it is by grace you have been saved..."),
        ("Philippians 4:13", "I can do all things through Christ..."),
        ("Jeremiah 29:11", "For I know the plans I have for you..."),
        ("Proverbs 3:5-6", "Trust in the LORD with all your heart..."),
        ("Romans 8:28", "All things work together for good..."),
        ("Isaiah 41:10", "Fear not, for I am with you..."),
        ("Psalm 23:1", "The LORD is my shepherd, I lack nothing..."),
        ("Matthew 28:19-20", "Go and make disciples of all nations..."),
        ("Galatians 5:22-23", "The fruit of the Spirit is love, joy, peace..."),
    ]
    for ref, start in memory_verses:
        pdf.add_checkbox(f"{ref} - {start}")
    pdf.end_page()

    # ADDITIONAL: TOPICAL BIBLE STUDY GUIDE
    pdf.start_page()
    pdf.add_chapter_title("Topical Study Guide")
    pdf.add_wrapped_text("When you face specific situations, here's where to look in the Bible:")
    pdf.add_space(10)
    topics = [
        ("When you're afraid", "Psalm 91, Isaiah 41:10, 2 Timothy 1:7"),
        ("When you're sad", "Psalm 34:18, Matthew 5:4, Revelation 21:4"),
        ("When you need wisdom", "James 1:5, Proverbs 2:6, Psalm 119:105"),
        ("When you feel alone", "Deuteronomy 31:6, Psalm 139, Matthew 28:20"),
        ("When you're tempted", "1 Corinthians 10:13, James 4:7, Hebrews 4:15-16"),
        ("When you need peace", "Philippians 4:6-7, John 14:27, Isaiah 26:3"),
        ("When you need strength", "Isaiah 40:31, Philippians 4:13, 2 Corinthians 12:9"),
        ("When you need forgiveness", "1 John 1:9, Psalm 103:12, Romans 8:1"),
        ("When you're grateful", "Psalm 100, 1 Thessalonians 5:18, Psalm 107:1"),
        ("When facing decisions", "Proverbs 3:5-6, James 1:5, Psalm 32:8"),
    ]
    for topic, refs in topics:
        pdf.add_text(f"  {topic}:", size=10, bold=True, indent=5)
        pdf.add_text(f"    {refs}", size=9, indent=15, color=(80, 80, 120))
        pdf.add_space(4)
    pdf.end_page()

    # ADDITIONAL: BIBLE READING TRACKER
    pdf.start_page()
    pdf.add_chapter_title("Bible Reading Tracker")
    pdf.add_wrapped_text("Track your daily Bible reading. Color in or check off each day you read:")
    pdf.add_space(10)
    pdf.add_text("Month: _____________", size=10, bold=True)
    pdf.add_space(8)
    for week in range(1, 6):
        pdf.add_text(f"Week {week}:", size=9, bold=True)
        pdf.add_text("  [ ] Mon  [ ] Tue  [ ] Wed  [ ] Thu  [ ] Fri  [ ] Sat  [ ] Sun", size=10, indent=10)
        pdf.add_text("  Passage read: ________________________________", size=9, indent=10, color=(100, 100, 100))
        pdf.add_space(8)
    pdf.add_space(10)
    pdf.add_text("Days read this month: ___ / 30", size=11, bold=True)
    pdf.add_text("Favorite passage this month:", size=10, bold=True)
    pdf.add_lined_space(2)
    pdf.end_page()

    # ADDITIONAL: UNDERSTANDING CONTEXT
    pdf.start_page()
    pdf.add_chapter_title("Understanding Bible Context")
    pdf.add_wrapped_text("Context is KEY to understanding the Bible correctly. Always ask these questions:")
    pdf.add_space(10)
    pdf.add_text("1. Historical Context", size=11, bold=True, color=(51, 51, 102))
    pdf.add_wrapped_text("When was this written? What was happening in the world at that time? What culture were the people living in?", size=10, indent=10)
    pdf.add_space(8)
    pdf.add_text("2. Literary Context", size=11, bold=True, color=(51, 51, 102))
    pdf.add_wrapped_text("What comes before and after this passage? What type of writing is this (history, poetry, prophecy, letter)?", size=10, indent=10)
    pdf.add_space(8)
    pdf.add_text("3. Author's Intent", size=11, bold=True, color=(51, 51, 102))
    pdf.add_wrapped_text("Who wrote this? Who were they writing to? What problem were they addressing?", size=10, indent=10)
    pdf.add_space(8)
    pdf.add_text("4. The Big Picture", size=11, bold=True, color=(51, 51, 102))
    pdf.add_wrapped_text("How does this passage fit into the overall story of the Bible? How does it point to Jesus?", size=10, indent=10)
    pdf.add_space(15)
    pdf.add_text("Common Mistakes to Avoid:", size=11, bold=True, color=(150, 50, 50))
    pdf.add_space(5)
    mistakes = [
        "Taking a verse out of context to prove a point",
        "Ignoring the original audience and culture",
        "Reading modern ideas back into ancient texts",
        "Cherry-picking verses while ignoring surrounding passages",
        "Treating poetry/metaphor as literal history (or vice versa)",
    ]
    for m in mistakes:
        pdf.add_text(f"  X {m}", size=9, indent=10, color=(150, 50, 50))
        pdf.add_space(3)
    pdf.end_page()

    # ADDITIONAL: MY BIBLE STUDY PLAN
    pdf.start_page()
    pdf.add_chapter_title("My Personal Bible Study Plan")
    pdf.add_text("After completing this workbook, here's my ongoing plan:", size=10, italic=True)
    pdf.add_space(10)
    pdf.add_text("Daily time commitment: _______ minutes", size=10, bold=True)
    pdf.add_space(5)
    pdf.add_text("Time of day: _______________", size=10, bold=True)
    pdf.add_space(5)
    pdf.add_text("Place: ___________________________", size=10, bold=True)
    pdf.add_space(5)
    pdf.add_text("Bible translation I'll use: _______________", size=10, bold=True)
    pdf.add_space(5)
    pdf.add_text("Study method I'll use: _______________", size=10, bold=True)
    pdf.add_space(5)
    pdf.add_text("Book I'll start with: _______________", size=10, bold=True)
    pdf.add_space(5)
    pdf.add_text("Accountability partner: _______________", size=10, bold=True)
    pdf.add_space(15)
    pdf.add_text("My 3-month Bible reading goals:", size=11, bold=True, color=(51, 51, 102))
    pdf.add_numbered_lines(1, 3, spacing=22)
    pdf.add_space(10)
    pdf.add_text("My 1-year Bible reading goals:", size=11, bold=True, color=(51, 51, 102))
    pdf.add_numbered_lines(1, 3, spacing=22)
    pdf.end_page()

    # ADDITIONAL: GOSPEL OVERVIEW
    pdf.start_page()
    pdf.add_chapter_title("The Gospel in Simple Terms")
    pdf.add_text("The entire Bible tells ONE story. Here it is in 5 parts:", size=10, italic=True)
    pdf.add_space(12)
    gospel_parts = [
        ("1. CREATION", "God created everything good. He made people to know and love Him. (Genesis 1-2)"),
        ("2. THE FALL", "Humanity chose to disobey God (sin), breaking our relationship with Him. Every person is affected by sin. (Genesis 3, Romans 3:23)"),
        ("3. THE PROMISE", "God promised to send a Savior who would fix what was broken. The entire Old Testament points to this coming Rescuer. (Genesis 3:15, Isaiah 53)"),
        ("4. JESUS", "God Himself came as a human - Jesus. He lived a perfect life, died on the cross to pay for our sins, and rose from the dead. (John 1:14, Romans 5:8, 1 Cor 15:3-4)"),
        ("5. RESTORATION", "Through faith in Jesus, we are forgiven and restored to relationship with God. One day He will make ALL things new. (Ephesians 2:8-9, Revelation 21:5)"),
    ]
    for title, desc in gospel_parts:
        pdf.add_text(f"  {title}", size=11, bold=True, color=(51, 51, 102))
        pdf.add_wrapped_text(desc, size=10, indent=15)
        pdf.add_space(8)
    pdf.add_space(10)
    pdf.add_text("Your Response:", size=11, bold=True)
    pdf.add_wrapped_text("Have you personally accepted this gift? Write your thoughts:", size=10)
    pdf.add_lined_space(4)
    pdf.end_page()

    # ADDITIONAL: QUESTIONS NEW BELIEVERS ASK
    pdf.start_page()
    pdf.add_chapter_title("Common Questions New Believers Ask")
    pdf.add_space(5)
    faqs = [
        ("How do I know I'm saved?", "If you have believed in Jesus and received Him as Lord, you are saved (John 1:12, Romans 10:9). Salvation is a gift, not earned by works."),
        ("What if I still sin?", "Christians still struggle with sin, but the Holy Spirit helps us grow. Confess, repent, and trust God's grace (1 John 1:9)."),
        ("How do I pray?", "Prayer is simply talking to God. You can pray anytime, anywhere. Be honest - He already knows your heart (Matthew 6:9-13)."),
        ("Which Bible translation should I use?", "Start with an easy-to-read version like NIV, NLT, or ESV. The best Bible is one you actually read!"),
        ("Do I need to go to church?", "Yes! Church is where you grow, serve, and find community. You need other believers (Hebrews 10:25)."),
        ("How do I know God's will?", "Read His Word, pray, seek wise counsel, and pay attention to the Holy Spirit's leading (Proverbs 3:5-6)."),
    ]
    for question, answer in faqs:
        pdf.add_text(f"Q: {question}", size=10, bold=True, color=(51, 51, 102))
        pdf.add_wrapped_text(f"A: {answer}", size=9, indent=10, color=(60, 60, 60))
        pdf.add_space(8)
    pdf.end_page()

    # ADDITIONAL: WORD STUDY WORKSHEET
    pdf.start_page()
    pdf.add_chapter_title("Word Study Worksheet")
    pdf.add_wrapped_text("Choose a key word from your reading (like 'grace', 'faith', 'love', 'hope') and explore it deeply:", size=10, italic=True)
    pdf.add_space(10)
    pdf.add_text("My word: ___________________________", size=10, bold=True)
    pdf.add_space(8)
    pdf.add_text("Dictionary definition:", size=10, bold=True)
    pdf.add_lined_space(2)
    pdf.add_text("How is it used in this passage?", size=10, bold=True)
    pdf.add_lined_space(3)
    pdf.add_text("Other verses that use this word:", size=10, bold=True)
    pdf.add_lined_space(3)
    pdf.add_text("What does this word mean for my life?", size=10, bold=True)
    pdf.add_lined_space(4)
    pdf.add_text("How can I live this word out today?", size=10, bold=True)
    pdf.add_lined_space(3)
    pdf.end_page()

    # MORE SOAP PRACTICE PAGES
    extra_passages = [
        ("Matthew 6:33", "But seek first His kingdom and His righteousness, and all these things will be given to you as well."),
        ("Isaiah 40:31", "But those who hope in the LORD will renew their strength. They will soar on wings like eagles."),
        ("Hebrews 11:1", "Now faith is confidence in what we hope for and assurance about what we do not see."),
        ("James 1:2-4", "Consider it pure joy whenever you face trials, because the testing of your faith produces perseverance."),
        ("Psalm 46:10", "Be still, and know that I am God."),
        ("1 Peter 5:7", "Cast all your anxiety on Him because He cares for you."),
        ("Colossians 3:23", "Whatever you do, work at it with all your heart, as working for the Lord, not for human masters."),
        ("Deuteronomy 31:6", "Be strong and courageous. Do not be afraid, for the LORD your God goes with you."),
        ("Micah 6:8", "Act justly, love mercy, and walk humbly with your God."),
        ("Romans 12:2", "Do not conform to the pattern of this world, but be transformed by the renewing of your mind."),
        ("2 Timothy 1:7", "For God has not given us a spirit of fear, but of power, love, and a sound mind."),
        ("Psalm 37:4", "Delight yourself in the LORD, and He will give you the desires of your heart."),
    ]

    for verse_ref, verse_text in extra_passages:
        pdf.start_page()
        pdf.add_chapter_title(f"SOAP Practice: {verse_ref}")
        pdf.add_quote_box(verse_text, verse_ref)
        pdf.add_space(8)
        pdf.add_text("S - Scripture (Write it in your own words):", size=10, bold=True)
        pdf.add_lined_space(2, spacing=20)
        pdf.add_text("O - Observation (What do you notice?):", size=10, bold=True)
        pdf.add_lined_space(3, spacing=20)
        pdf.add_text("A - Application (How does this apply to YOUR life?):", size=10, bold=True)
        pdf.add_lined_space(3, spacing=20)
        pdf.add_text("P - Prayer (Write a prayer based on this verse):", size=10, bold=True)
        pdf.add_lined_space(3, spacing=20)
        pdf.end_page()

    # FINAL PAGE
    pdf.start_page()
    pdf.add_chapter_title("You Did It!")
    pdf.add_quote_box("Your word is a lamp for my feet, a light on my path.", "Psalm 119:105")
    pdf.add_space(15)
    pdf.add_wrapped_text("Congratulations on completing this workbook! You now have the tools to study the Bible on your own. Remember: Bible study is a lifelong journey. Keep reading, keep learning, keep growing. God's Word never runs out of treasures to discover.")
    pdf.add_space(15)
    pdf.add_text("What's Next?", size=12, bold=True)
    pdf.add_space(8)
    pdf.add_text("  * Join a Bible study group at your local church", size=10, indent=10)
    pdf.add_text("  * Try reading through an entire Gospel", size=10, indent=10)
    pdf.add_text("  * Start journaling daily using the SOAP method", size=10, indent=10)
    pdf.add_text("  * Find an accountability partner", size=10, indent=10)
    pdf.add_text("  * Download a Bible app for reading on the go", size=10, indent=10)
    pdf.end_page()

    return pdf


# ============================================================
# MAIN EXECUTION
# ============================================================

if __name__ == '__main__':
    output_dir = os.path.dirname(os.path.abspath(__file__))

    books = [
        ("01_30_Day_Prayer_Fasting_Challenge_Workbook.pdf", create_book_01),
        ("02_Christian_Couples_30_Day_Bible_Study.pdf", create_book_02),
        ("03_Christian_Marriage_Reset_Workbook.pdf", create_book_03),
        ("04_30_Day_Christian_Gratitude_Journal.pdf", create_book_04),
        ("05_Bible_Study_Workbook_for_Beginners.pdf", create_book_05),
    ]

    print("=" * 65)
    print("  GENERATING TIER 1 WORKBOOKS (Books 1-5)")
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
    print("  TIER 1 COMPLETE!")
    print("=" * 65)
