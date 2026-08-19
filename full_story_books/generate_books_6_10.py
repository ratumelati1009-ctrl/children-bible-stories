#!/usr/bin/env python3
"""Generate Books 6-10 (Tier 2 - Part 1)"""

import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pdf_engine import PDFEngine


def pad_to_40_pages(pdf, title="Journal Notes"):
    """Add extra pages if needed to reach 40+ pages."""
    while len(pdf.pages) + (1 if pdf.current_page_content else 0) < 40:
        pdf.add_blank_journal_page(header=title)


def create_book_06():
    """Christian Women's 30-Day Prayer Journal"""
    pdf = PDFEngine()
    pdf.header_text = "Christian Women's 30-Day Prayer Journal"

    pdf.add_title_page(
        title="Christian Women's 30-Day Prayer Journal",
        subtitle="A Beautiful Journey of Prayer, Scripture, and Spiritual Growth for Women of Faith",
        author="Daily Guided Prayers & Reflections",
        extra_lines=["Designed for busy women who want to deepen", "their prayer life and walk with God"]
    )

    pdf.start_page()
    pdf.add_chapter_title("Dear Sister in Christ,")
    pdf.add_wrapped_text("Welcome to this sacred space. This journal was created with YOU in mind -- the woman who juggles a thousand responsibilities yet longs for deeper connection with God. Whether you are a working professional, a stay-at-home mom, a student, or a retiree, this 30-day prayer journey will help you carve out intentional time with your Heavenly Father.")
    pdf.add_space(10)
    pdf.add_wrapped_text("Each day includes a scripture specifically chosen for women, a prayer prompt, space for your personal prayers, and a reflection question. There is no right or wrong way to use this journal -- simply come as you are.")
    pdf.add_space(15)
    pdf.add_quote_box("She is clothed with strength and dignity; she can laugh at the days to come.", "Proverbs 31:25")
    pdf.add_space(10)
    pdf.add_text("How to Use This Journal:", size=11, bold=True)
    pdf.add_space(5)
    items = ["Find a quiet moment each day (even 10 minutes counts!)",
             "Read the scripture slowly -- let it sink in",
             "Write your honest prayers -- God already knows your heart",
             "Answer the reflection question truthfully",
             "Close with a moment of silence, listening for God"]
    for item in items:
        pdf.add_text(f"  * {item}", size=10, indent=10)
        pdf.add_space(3)
    pdf.end_page()

    toc = [("Welcome & How to Use", 2), ("Days 1-7: Identity & Worth", 4),
           ("Days 8-14: Relationships & Love", 12), ("Days 15-21: Purpose & Calling", 20),
           ("Days 22-28: Strength & Courage", 28), ("Days 29-30: Celebration & Commitment", 36),
           ("Prayer Lists & Overflow Pages", 38)]
    pdf.add_toc_page(toc)

    women_days = [
        ("You Are Chosen", "1 Peter 2:9", "You are a chosen people, a royal priesthood, a holy nation, God's special possession.", "Pray about your identity: who does GOD say you are?", "What lies about your identity do you need to release today?"),
        ("Fearfully Made", "Psalm 139:14", "I praise you because I am fearfully and wonderfully made.", "Thank God for how He uniquely designed you.", "What part of yourself have you struggled to accept?"),
        ("Enough in Christ", "2 Corinthians 12:9", "My grace is sufficient for you, for my power is made perfect in weakness.", "Surrender your feelings of inadequacy to God.", "Where are you trying to be 'enough' in your own strength?"),
        ("Daughter of the King", "Galatians 3:26", "You are all children of God through faith in Christ Jesus.", "Pray knowing you have royal access to God's throne.", "How would your day change if you truly lived as royalty?"),
        ("Rest for the Weary", "Matthew 11:28-30", "Come to me, all you who are weary and burdened, and I will give you rest.", "Give God every burden you are carrying today.", "What are you carrying that God never asked you to carry?"),
        ("Inner Beauty", "1 Peter 3:3-4", "Your beauty should be that of your inner self, the unfading beauty of a gentle and quiet spirit.", "Pray for inner transformation over outward appearance.", "How does the world's beauty standard affect your self-image?"),
        ("Strength in Him", "Isaiah 40:31", "Those who hope in the LORD will renew their strength.", "Ask God for supernatural strength for this season.", "In which area of life do you feel most exhausted?"),
        ("Loving Others Well", "1 John 4:19", "We love because He first loved us.", "Pray for the people in your life -- family, friends, colleagues.", "Who needs your love and attention most right now?"),
        ("Marriage/Singleness", "Ecclesiastes 4:12", "A cord of three strands is not quickly broken.", "Pray for your current relationship status with contentment.", "How can God be the center of your relationships?"),
        ("Motherhood/Nurturing", "Isaiah 66:13", "As a mother comforts her child, so will I comfort you.", "Pray for the children in your life (yours or others).", "How can you nurture someone today?"),
        ("Friendships", "Proverbs 27:17", "As iron sharpens iron, so one person sharpens another.", "Thank God for godly friendships; pray for deeper connection.", "Do you have friendships that sharpen your faith?"),
        ("Forgiveness", "Ephesians 4:32", "Be kind and compassionate, forgiving each other, just as God forgave you.", "Release any bitterness you are holding.", "Is there someone you need to forgive -- including yourself?"),
        ("Boundaries", "Proverbs 4:23", "Above all else, guard your heart, for everything you do flows from it.", "Ask God for wisdom to set healthy boundaries.", "Where do you need stronger boundaries in your life?"),
        ("Dealing with Comparison", "Galatians 6:4", "Each one should test their own actions. Then they can take pride in themselves alone.", "Surrender your comparison habit to God.", "What triggers comparison for you? Social media? Others' success?"),
        ("Your Calling", "Jeremiah 1:5", "Before I formed you in the womb I knew you; before you were born I set you apart.", "Ask God to reveal or confirm your calling.", "What gifts and passions has God placed in you?"),
        ("Work & Career", "Colossians 3:23", "Whatever you do, work at it with all your heart, as working for the Lord.", "Pray about your work -- for purpose and excellence.", "How can you serve God through your daily work?"),
        ("Creativity", "Exodus 35:35", "He has filled them with skill to do all kinds of work.", "Thank God for your creative gifts.", "What creative outlet have you been neglecting?"),
        ("Ministry", "1 Peter 4:10", "Each of you should use whatever gift you have received to serve others.", "Pray about how God wants to use you to serve.", "Where is God calling you to serve in this season?"),
        ("Contentment", "Philippians 4:11-12", "I have learned to be content whatever the circumstances.", "Pray for contentment in your current season.", "What area of discontent is robbing your peace?"),
        ("Dreams & Goals", "Habakkuk 2:2", "Write the vision; make it plain.", "Present your dreams to God -- ask for His direction.", "What dream have you been afraid to pursue?"),
        ("Financial Peace", "Philippians 4:19", "My God will meet all your needs according to His riches in glory.", "Surrender your finances and worries to God.", "What financial fear do you need to release to God?"),
        ("Health & Body", "1 Corinthians 6:19-20", "Your bodies are temples of the Holy Spirit.", "Pray for wisdom to honor God with your body.", "How can you better steward the body God gave you?"),
        ("Anxiety & Fear", "Isaiah 41:10", "Do not fear, for I am with you; do not be dismayed, for I am your God.", "Name your fears out loud and give each one to God.", "What fear has the loudest voice in your life right now?"),
        ("Patience in Waiting", "Psalm 27:14", "Wait for the LORD; be strong and take heart and wait for the LORD.", "Pray for patience in the waiting season.", "What are you waiting for? How can you trust God's timing?"),
        ("Courage to Speak Up", "Esther 4:14", "Who knows but that you have come to your royal position for such a time as this?", "Ask God for courage to use your voice.", "Where is God asking you to be brave?"),
        ("Leading with Grace", "Titus 2:3-5", "The older women are to teach what is good and train the younger women.", "Pray for opportunities to mentor and lead.", "Who is looking to you for guidance?"),
        ("Spiritual Warfare", "Ephesians 6:12", "Our struggle is not against flesh and blood.", "Put on the full armor of God in prayer.", "What spiritual battle are you facing?"),
        ("Hope for Tomorrow", "Romans 15:13", "May the God of hope fill you with all joy and peace as you trust in Him.", "Pray with hope for the future God has planned.", "What gives you hope right now?"),
        ("Gratitude Overflow", "Psalm 100:4", "Enter His gates with thanksgiving and His courts with praise.", "Spend this entire prayer time in pure thanksgiving.", "List every blessing you can think of -- big and small."),
        ("Forward in Faith", "Hebrews 11:1", "Faith is confidence in what we hope for and assurance about what we do not see.", "Commit your next season to God with confident faith.", "What does faithful next-step obedience look like for you?"),
    ]

    for i, (theme, verse_ref, verse_text, prayer_prompt, reflection) in enumerate(women_days, 1):
        pdf.start_page()
        pdf.add_text(f"DAY {i}", size=9, bold=True, color=(150, 80, 120))
        pdf.add_chapter_title(f"Day {i}: {theme}")
        pdf.add_quote_box(verse_text, verse_ref, bg_color=(0.98, 0.95, 0.97))
        pdf.add_space(6)
        pdf.add_text("Prayer Prompt:", size=11, bold=True, color=(120, 50, 100))
        pdf.add_wrapped_text(prayer_prompt, size=10, indent=5)
        pdf.add_space(8)
        pdf.add_text("My Prayer Today:", size=10, bold=True, color=(80, 60, 100))
        pdf.add_lined_space(5, spacing=20)
        pdf.add_space(5)
        pdf.add_text("Reflection:", size=10, bold=True, color=(120, 50, 100))
        pdf.add_wrapped_text(reflection, size=10, italic=True, indent=5)
        pdf.add_lined_space(3, spacing=20)
        pdf.end_page()

    # WEEKLY REFLECTIONS
    for week in range(1, 5):
        pdf.start_page()
        pdf.add_chapter_title(f"Week {week} Reflection")
        pdf.add_text("How did God speak to me this week?", size=10, bold=True)
        pdf.add_lined_space(4)
        pdf.add_text("One prayer that was answered:", size=10, bold=True)
        pdf.add_lined_space(3)
        pdf.add_text("A verse that meant the most to me:", size=10, bold=True)
        pdf.add_lined_space(2)
        pdf.add_text("How I grew this week:", size=10, bold=True)
        pdf.add_lined_space(4)
        pdf.end_page()

    # PRAYER LIST PAGES
    pdf.start_page()
    pdf.add_chapter_title("My Prayer List")
    pdf.add_text("People I am praying for:", size=10, bold=True)
    pdf.add_numbered_lines(1, 12, spacing=20)
    pdf.add_space(10)
    pdf.add_text("Situations I am lifting to God:", size=10, bold=True)
    pdf.add_numbered_lines(1, 8, spacing=20)
    pdf.end_page()

    # ANSWERED PRAYERS
    pdf.start_page()
    pdf.add_chapter_title("Answered Prayers - My Testimonies")
    pdf.add_wrapped_text("Record God's faithfulness here. When you feel discouraged, read this page!", size=10, italic=True)
    pdf.add_space(10)
    for i in range(8):
        pdf.add_text("Date: ______  Answered Prayer:", size=9, bold=True)
        pdf.add_lined_space(2, spacing=18)
        pdf.add_space(3)
    pdf.end_page()

    # OVERFLOW JOURNAL
    for i in range(2):
        pdf.add_blank_journal_page(header="Prayer Journal Overflow")

    pad_to_40_pages(pdf, "Prayer Notes")
    return pdf


def create_book_07():
    """Christian Men's 30-Day Prayer & Purpose Workbook"""
    pdf = PDFEngine()
    pdf.header_text = "Christian Men's 30-Day Prayer & Purpose Workbook"

    pdf.add_title_page(
        title="Christian Men's 30-Day Prayer & Purpose Workbook",
        subtitle="Discover Your God-Given Purpose Through Daily Prayer, Scripture, and Action",
        author="A Guided Workbook for Men of Faith",
        extra_lines=["For men who want to lead well, pray boldly,", "and live with kingdom purpose"]
    )

    pdf.start_page()
    pdf.add_chapter_title("Brother, This Is For You")
    pdf.add_wrapped_text("You were made for more. God created you with a purpose, equipped you with unique gifts, and called you to lead -- in your home, your workplace, your community, and your church. But purpose without prayer is just ambition. This 30-day workbook combines focused prayer with practical purpose-discovery exercises.")
    pdf.add_space(10)
    pdf.add_quote_box("Be on your guard; stand firm in the faith; be courageous; be strong. Do everything in love.", "1 Corinthians 16:13-14")
    pdf.add_space(10)
    pdf.add_text("Each day includes:", size=11, bold=True)
    items = ["A scripture for men", "A focused prayer area", "A purpose-building exercise",
             "An action step for the day", "Journaling space for your thoughts"]
    for item in items:
        pdf.add_text(f"  * {item}", size=10, indent=10)
        pdf.add_space(3)
    pdf.end_page()

    toc = [("Introduction", 2), ("Week 1: Identity as a Man of God (Days 1-7)", 4),
           ("Week 2: Leadership & Responsibility (Days 8-14)", 12),
           ("Week 3: Purpose & Calling (Days 15-21)", 20),
           ("Week 4: Legacy & Impact (Days 22-28)", 28),
           ("Days 29-30: Commitment & Brotherhood", 36),
           ("Action Plan & Prayer Lists", 38)]
    pdf.add_toc_page(toc)

    men_days = [
        ("Man of God", "1 Timothy 6:11", "But you, man of God, pursue righteousness, godliness, faith, love, endurance and gentleness.", "Pray about what kind of man God is calling you to be.", "Define 'Man of God' in your own words:"),
        ("Created with Purpose", "Ephesians 2:10", "For we are God's handiwork, created in Christ Jesus to do good works, which God prepared in advance.", "Ask God to reveal the good works He prepared for you.", "What are you passionate about? What angers you about the world?"),
        ("Integrity", "Proverbs 10:9", "Whoever walks in integrity walks securely.", "Ask God to reveal any area where your integrity is compromised.", "Is your private life consistent with your public life?"),
        ("Discipline", "1 Corinthians 9:27", "I discipline my body and keep it under control.", "Pray for self-discipline in the areas you struggle most.", "What habits are controlling you instead of you controlling them?"),
        ("Humility", "Micah 6:8", "Act justly, love mercy, and walk humbly with your God.", "Ask God to remove pride and replace it with humble confidence.", "Where has pride been disguised as strength in your life?"),
        ("Courage", "Joshua 1:9", "Be strong and courageous. Do not be afraid; do not be discouraged.", "Pray for courage to do what God is asking of you.", "What courageous step have you been avoiding?"),
        ("Identity in Christ", "2 Corinthians 5:17", "If anyone is in Christ, the new creation has come.", "Release who the world says you should be; embrace who God made you.", "What false identity have you been living under?"),
        ("Leading Your Home", "Joshua 24:15", "As for me and my household, we will serve the LORD.", "Pray for wisdom to lead your family spiritually.", "How can you better serve and lead your household?"),
        ("Being a Godly Husband/Partner", "Ephesians 5:25", "Husbands, love your wives, just as Christ loved the church.", "Pray for sacrificial, servant-leadership love.", "How can you love your wife/partner more like Christ?"),
        ("Fatherhood/Mentoring", "Proverbs 22:6", "Start children off on the way they should go.", "Pray for wisdom in raising/mentoring the next generation.", "What legacy are you passing to the next generation?"),
        ("Brotherhood", "Proverbs 27:17", "As iron sharpens iron, so one person sharpens another.", "Pray for deeper, authentic friendships with other men.", "Do you have men in your life who hold you accountable?"),
        ("Work & Excellence", "Colossians 3:23", "Whatever you do, work at it with all your heart, as working for the Lord.", "Dedicate your work to God -- ask Him to use you there.", "How is your work serving God's kingdom?"),
        ("Financial Stewardship", "Proverbs 21:20", "The wise store up choice food and olive oil, but fools gulp theirs down.", "Pray for wisdom with your finances.", "Are you being a faithful steward of what God has given you?"),
        ("Purity", "Job 31:1", "I made a covenant with my eyes not to look lustfully.", "Pray for purity in mind, heart, and actions.", "What boundaries do you need to establish for purity?"),
        ("Your Calling", "Romans 12:6-8", "We have different gifts, according to the grace given to each of us.", "Ask God: What am I here to do? What is my assignment?", "What are your top 3 gifts/strengths?"),
        ("Serving Others", "Mark 10:45", "The Son of Man did not come to be served, but to serve.", "Pray for a servant's heart in every area of life.", "Where can you serve someone this week?"),
        ("Overcoming Temptation", "1 Corinthians 10:13", "God is faithful; He will not let you be tempted beyond what you can bear.", "Confess your greatest temptation and ask for strength.", "What is your escape plan when temptation comes?"),
        ("Dealing with Anger", "James 1:19-20", "Everyone should be quick to listen, slow to speak and slow to become angry.", "Ask God to heal the root of your anger.", "What triggers your anger? What is underneath it?"),
        ("Mental Health", "Philippians 4:8", "Whatever is true, noble, right, pure, lovely, admirable -- think about such things.", "Pray for a renewed mind and freedom from negative patterns.", "How is your mental health? What support do you need?"),
        ("Physical Health", "1 Corinthians 6:19", "Your bodies are temples of the Holy Spirit.", "Commit your physical health to God.", "What one change would honor God with your body?"),
        ("Generosity", "2 Corinthians 9:7", "God loves a cheerful giver.", "Ask God where He wants you to be more generous.", "How can you increase your generosity this month?"),
        ("Spiritual Warfare", "Ephesians 6:10-11", "Be strong in the Lord and in His mighty power. Put on the full armor of God.", "Pray on the full armor of God piece by piece.", "What spiritual battle are you currently in?"),
        ("Leaving a Legacy", "Psalm 78:4", "We will tell the next generation the praiseworthy deeds of the LORD.", "Pray about the legacy you want to leave.", "What do you want to be remembered for?"),
        ("Impact in Community", "Matthew 5:13-16", "You are the salt of the earth...You are the light of the world.", "Pray for impact beyond your immediate circle.", "How can you make your community better?"),
        ("Wisdom in Decisions", "James 1:5", "If any of you lacks wisdom, let him ask God, who gives generously.", "Bring your biggest decision to God right now.", "What decision do you need God's wisdom for?"),
        ("Perseverance", "Galatians 6:9", "Let us not become weary in doing good.", "Pray for endurance in the areas you want to quit.", "What are you tempted to give up on?"),
        ("Forgiveness", "Matthew 6:14-15", "If you forgive other people when they sin against you, your heavenly Father will also forgive you.", "Release anyone you are holding unforgiveness toward.", "Who do you need to forgive?"),
        ("Vision for the Future", "Habakkuk 2:2", "Write the vision and make it plain.", "Ask God for a clear vision for your next season.", "Where do you see yourself in 5 years serving God?"),
        ("Brotherhood Commitment", "Hebrews 10:24-25", "Let us consider how we may spur one another on toward love and good deeds.", "Commit to deeper community with other Christian men.", "Who will you invite into accountability this week?"),
        ("The Man God Made You To Be", "Philippians 1:6", "He who began a good work in you will carry it on to completion.", "Pray a prayer of total surrender and recommitment.", "Write your personal mission statement as a man of God:"),
    ]

    for i, (theme, verse_ref, verse_text, prayer_prompt, exercise) in enumerate(men_days, 1):
        pdf.start_page()
        pdf.add_text(f"DAY {i}", size=9, bold=True, color=(50, 80, 120))
        pdf.add_chapter_title(f"Day {i}: {theme}")
        pdf.add_quote_box(verse_text, verse_ref, bg_color=(0.94, 0.96, 0.98))
        pdf.add_space(6)
        pdf.add_text("Prayer Focus:", size=11, bold=True, color=(40, 60, 100))
        pdf.add_wrapped_text(prayer_prompt, size=10, indent=5)
        pdf.add_space(5)
        pdf.add_text("My Prayer:", size=10, bold=True, color=(60, 60, 100))
        pdf.add_lined_space(4, spacing=20)
        pdf.add_space(5)
        pdf.add_text("Purpose Exercise:", size=11, bold=True, color=(40, 60, 100))
        pdf.add_wrapped_text(exercise, size=10, italic=True, indent=5)
        pdf.add_lined_space(4, spacing=20)
        pdf.add_text("Today's Action Step:", size=10, bold=True)
        pdf.add_lined_space(1, spacing=20)
        pdf.end_page()

    # WEEKLY CHECK-INS
    for week in range(1, 5):
        pdf.start_page()
        pdf.add_chapter_title(f"Week {week} Check-In")
        pdf.add_text("What did God reveal about my purpose this week?", size=10, bold=True)
        pdf.add_lined_space(4)
        pdf.add_text("Action steps I completed:", size=10, bold=True)
        pdf.add_lined_space(3)
        pdf.add_text("Biggest challenge this week:", size=10, bold=True)
        pdf.add_lined_space(3)
        pdf.add_text("Prayer for next week:", size=10, bold=True)
        pdf.add_lined_space(4)
        pdf.end_page()

    # PURPOSE STATEMENT
    pdf.start_page()
    pdf.add_chapter_title("My Personal Mission Statement")
    pdf.add_wrapped_text("Based on what God has revealed over 30 days, write your personal mission statement:")
    pdf.add_space(10)
    pdf.add_text("My God-given purpose is:", size=10, bold=True)
    pdf.add_lined_space(4)
    pdf.add_text("The gifts God gave me to fulfill it:", size=10, bold=True)
    pdf.add_lined_space(3)
    pdf.add_text("The people I am called to serve:", size=10, bold=True)
    pdf.add_lined_space(3)
    pdf.add_text("My 1-year action plan:", size=10, bold=True)
    pdf.add_numbered_lines(1, 5, spacing=20)
    pdf.end_page()

    # PRAYER LIST
    pdf.start_page()
    pdf.add_chapter_title("Prayer & Accountability")
    pdf.add_text("Men I am praying for:", size=10, bold=True)
    pdf.add_numbered_lines(1, 8, spacing=20)
    pdf.add_space(10)
    pdf.add_text("My accountability partners:", size=10, bold=True)
    pdf.add_numbered_lines(1, 3, spacing=20)
    pdf.add_space(10)
    pdf.add_text("Things I am believing God for:", size=10, bold=True)
    pdf.add_numbered_lines(1, 5, spacing=20)
    pdf.end_page()

    pad_to_40_pages(pdf, "Men's Prayer Journal")
    return pdf


def create_book_08():
    """30-Day Prayer & Purpose Journal"""
    pdf = PDFEngine()
    pdf.header_text = "30-Day Prayer & Purpose Journal"

    pdf.add_title_page(
        title="30-Day Prayer & Purpose Journal",
        subtitle="Discover God's Plan for Your Life Through Focused Prayer and Intentional Reflection",
        author="A Guided Journal for Every Believer",
        extra_lines=["Uncover your calling, align your priorities,", "and live with holy intention"]
    )

    pdf.start_page()
    pdf.add_chapter_title("Finding Your Purpose Through Prayer")
    pdf.add_wrapped_text("Do you ever feel like you are just going through the motions? Like there must be MORE to life than what you are currently experiencing? You are right. God created you ON purpose, WITH purpose, FOR a purpose. This 30-day journal will help you discover (or rediscover) what that purpose is through the power of focused, intentional prayer.")
    pdf.add_space(10)
    pdf.add_quote_box("For we are God's handiwork, created in Christ Jesus to do good works, which God prepared in advance for us to do.", "Ephesians 2:10")
    pdf.add_space(10)
    pdf.add_text("This journal is structured in 4 phases:", size=11, bold=True)
    phases = ["Week 1: PAUSE - Slowing down to hear God",
              "Week 2: DISCOVER - Uncovering your gifts and passions",
              "Week 3: ALIGN - Aligning your life with God's will",
              "Week 4: LAUNCH - Taking purposeful action"]
    for p in phases:
        pdf.add_text(f"  * {p}", size=10, indent=10)
        pdf.add_space(3)
    pdf.end_page()

    toc = [("Introduction", 2), ("Week 1: PAUSE - Hearing God (Days 1-7)", 4),
           ("Week 2: DISCOVER - Gifts & Passions (Days 8-14)", 12),
           ("Week 3: ALIGN - God's Will (Days 15-21)", 20),
           ("Week 4: LAUNCH - Taking Action (Days 22-28)", 28),
           ("Days 29-30: My Purpose Statement", 36), ("Resources & Next Steps", 40)]
    pdf.add_toc_page(toc)

    purpose_days = [
        ("Be Still", "Psalm 46:10", "Be still, and know that I am God.", "Spend 10 minutes in complete silence. Write what comes to mind.", "What did the silence reveal?"),
        ("Listening Prayer", "1 Samuel 3:10", "Speak, LORD, for your servant is listening.", "Practice listening prayer: ask God a question, then wait.", "What question did you ask? What did you sense?"),
        ("Surrendering Plans", "Proverbs 16:9", "In their hearts humans plan their course, but the LORD establishes their steps.", "Lay YOUR plans down. Tell God you are open to HIS plan.", "What plans are you holding too tightly?"),
        ("Clearing the Noise", "Mark 1:35", "Very early in the morning, Jesus went off to a solitary place to pray.", "Identify and eliminate one distraction today.", "What noise drowns out God's voice in your life?"),
        ("Past Reflections", "Psalm 77:11", "I will remember the deeds of the LORD.", "Look back: where has God clearly led you before?", "List 3 moments God clearly directed your path:"),
        ("Holy Discontent", "Nehemiah 1:3-4", "When I heard these things, I sat down and wept.", "What breaks your heart? That might be your calling.", "What injustice or need makes you say 'Someone should do something!'?"),
        ("God's Voice vs. Others", "John 10:27", "My sheep listen to my voice; I know them, and they follow me.", "Practice distinguishing God's voice from fear, culture, and ego.", "How do you recognize God's voice vs. your own thoughts?"),
        ("Spiritual Gifts", "1 Corinthians 12:7", "To each one the manifestation of the Spirit is given for the common good.", "Identify your spiritual gifts (teaching, serving, leading, etc.).", "What do others say you are good at? What energizes you?"),
        ("Natural Talents", "Exodus 35:35", "He has filled them with skill to do all kinds of work.", "List every talent and skill you have -- natural and learned.", "What comes easily to you that others find difficult?"),
        ("Passions & Burdens", "Philippians 2:13", "It is God who works in you to will and to act.", "What topics make you come alive? What needs burden you?", "If money were no object, what would you do with your life?"),
        ("Life Experiences", "Romans 8:28", "In all things God works for the good of those who love Him.", "How has God used your pain and experiences to shape you?", "What difficult experience has given you unique understanding?"),
        ("Personality & Wiring", "Psalm 139:13", "You created my inmost being; you knit me together.", "Embrace how God wired you (introvert/extrovert, detail/big-picture).", "How does your personality point toward your purpose?"),
        ("Values Clarification", "Matthew 6:21", "Where your treasure is, there your heart will be also.", "Identify your top 5 core values.", "What values are non-negotiable for you?"),
        ("Season Awareness", "Ecclesiastes 3:1", "There is a time for everything.", "Purpose looks different in different seasons. What season are you in?", "What is God calling you to in THIS specific season?"),
        ("Alignment Check", "Matthew 6:33", "Seek first His kingdom and His righteousness.", "Is your current life aligned with what you know God wants?", "What is OUT of alignment that needs to change?"),
        ("Saying No", "Matthew 5:37", "All you need to say is simply Yes or No.", "What good things do you need to say NO to for the BEST things?", "List 3 things you need to stop doing to make room for purpose:"),
        ("Obedience Step", "James 1:22", "Do not merely listen to the word. Do what it says.", "What is one thing God has clearly told you to do that you have not done?", "What is holding you back from obedience?"),
        ("Fear vs. Faith", "2 Timothy 1:7", "God has not given us a spirit of fear, but of power, love, and self-discipline.", "Name the fear blocking your purpose. Give it to God.", "What would you do if you were not afraid?"),
        ("Mentors & Models", "Hebrews 13:7", "Remember your leaders who spoke the word of God to you. Consider the outcome of their way of life.", "Who is living the kind of purposeful life you admire?", "What can you learn from their journey?"),
        ("Community & Calling", "1 Corinthians 12:14", "The body is not made up of one part but of many.", "Your calling connects to others. How does your purpose serve the body?", "Who needs what God has placed in you?"),
        ("Taking the First Step", "Proverbs 16:3", "Commit to the LORD whatever you do, and He will establish your plans.", "What is the very first step toward your purpose?", "What can you do THIS WEEK to move toward your calling?"),
        ("Building Habits", "Galatians 6:9", "Let us not become weary in doing good.", "Purpose requires daily habits. What habits support your calling?", "List 3 daily habits that move you toward purpose:"),
        ("Accountability", "Proverbs 27:17", "As iron sharpens iron, so one person sharpens another.", "Who will hold you accountable to live your purpose?", "Name 1-2 people you will share your purpose statement with:"),
        ("Overcoming Obstacles", "Philippians 4:13", "I can do all things through Christ who strengthens me.", "What obstacles stand between you and your purpose? God is bigger.", "List your top 3 obstacles and God's promise for each:"),
        ("Provision & Trust", "Philippians 4:19", "My God will meet all your needs according to His riches in glory.", "Trust that God will provide what you need to fulfill your purpose.", "Where do you need to trust God for provision?"),
        ("Patience in Process", "Habakkuk 2:3", "Though it linger, wait for it; it will certainly come.", "Purpose unfolds over time. Be patient with the process.", "How can you be faithful in the small things right now?"),
        ("Celebration", "Psalm 150:6", "Let everything that has breath praise the LORD!", "Celebrate how far you have come in 30 days!", "What has God revealed about your purpose?"),
        ("My Purpose Statement", "Jeremiah 29:11", "For I know the plans I have for you, declares the LORD.", "Write your purpose statement below.", "Who am I? What am I here to do? Who am I here to serve?"),
        ("Action Plan", "James 2:17", "Faith by itself, if it is not accompanied by action, is dead.", "Create a 90-day action plan for your purpose.", "List 5 action steps for the next 90 days:"),
        ("Sending Prayer", "Isaiah 6:8", "Here am I. Send me!", "Pray a prayer of commissioning: God, send me!", "I am ready to go where You send me because:"),
    ]

    for i, (theme, verse_ref, verse_text, prayer_prompt, exercise) in enumerate(purpose_days, 1):
        pdf.start_page()
        pdf.add_text(f"DAY {i} | Phase: {'PAUSE' if i<=7 else 'DISCOVER' if i<=14 else 'ALIGN' if i<=21 else 'LAUNCH'}", size=9, bold=True, color=(80, 60, 120))
        pdf.add_chapter_title(f"Day {i}: {theme}")
        pdf.add_quote_box(verse_text, verse_ref)
        pdf.add_space(5)
        pdf.add_text("Prayer & Exercise:", size=11, bold=True, color=(60, 40, 100))
        pdf.add_wrapped_text(prayer_prompt, size=10, indent=5)
        pdf.add_space(6)
        pdf.add_text("Reflection:", size=10, bold=True, color=(60, 40, 100))
        pdf.add_wrapped_text(exercise, size=10, italic=True, indent=5)
        pdf.add_lined_space(5, spacing=20)
        pdf.add_text("What I sense God saying:", size=10, bold=True, color=(80, 60, 120))
        pdf.add_lined_space(3, spacing=18)
        pdf.end_page()

    # PURPOSE BLUEPRINT
    pdf.start_page()
    pdf.add_chapter_title("My Purpose Blueprint")
    pdf.add_text("My Spiritual Gifts:", size=10, bold=True)
    pdf.add_lined_space(2)
    pdf.add_text("My Natural Talents:", size=10, bold=True)
    pdf.add_lined_space(2)
    pdf.add_text("My Passions:", size=10, bold=True)
    pdf.add_lined_space(2)
    pdf.add_text("My Life Experiences:", size=10, bold=True)
    pdf.add_lined_space(2)
    pdf.add_text("People I Am Called to Serve:", size=10, bold=True)
    pdf.add_lined_space(2)
    pdf.add_text("MY PURPOSE STATEMENT:", size=12, bold=True, color=(51, 51, 102))
    pdf.add_lined_space(4)
    pdf.end_page()

    # 90-DAY ACTION PLAN
    pdf.start_page()
    pdf.add_chapter_title("90-Day Purpose Action Plan")
    pdf.add_text("Month 1 Goals:", size=10, bold=True)
    pdf.add_numbered_lines(1, 3, spacing=20)
    pdf.add_text("Month 2 Goals:", size=10, bold=True)
    pdf.add_numbered_lines(1, 3, spacing=20)
    pdf.add_text("Month 3 Goals:", size=10, bold=True)
    pdf.add_numbered_lines(1, 3, spacing=20)
    pdf.add_text("Accountability Partner:", size=10, bold=True)
    pdf.add_lined_space(1)
    pdf.add_text("Check-in Date:", size=10, bold=True)
    pdf.add_lined_space(1)
    pdf.end_page()

    pad_to_40_pages(pdf, "Prayer & Purpose Journal")
    return pdf


def create_book_09():
    """Christian Family Devotional - 30 Days"""
    pdf = PDFEngine()
    pdf.header_text = "Christian Family Devotional - 30 Days"

    pdf.add_title_page(
        title="Christian Family Devotional -- 30 Days",
        subtitle="Fun, Engaging Daily Devotions for the Whole Family to Grow in Faith Together",
        author="For Families with Children Ages 4-12",
        extra_lines=["Includes stories, discussion questions, activities,", "prayers, and memory verses for every day"]
    )

    pdf.start_page()
    pdf.add_chapter_title("Welcome, Family!")
    pdf.add_wrapped_text("Family devotion time is one of the most powerful investments you can make. This 30-day devotional is designed to be FUN, engaging, and age-appropriate for the whole family. Each devotion takes only 10-15 minutes and includes something for every age group.")
    pdf.add_space(10)
    pdf.add_text("Each Day Includes:", size=11, bold=True)
    items = ["A Bible verse to read aloud together", "A short story or teaching (read by a parent)",
             "Discussion questions for all ages", "A fun family activity",
             "A simple prayer everyone can say", "A memory verse challenge"]
    for item in items:
        pdf.add_text(f"  * {item}", size=10, indent=10)
        pdf.add_space(3)
    pdf.add_space(10)
    pdf.add_text("Tips for Success:", size=11, bold=True)
    tips = ["Pick a consistent time (breakfast, dinner, or bedtime)",
            "Keep it SHORT -- better to do 10 minutes daily than skip it",
            "Let kids participate by reading, holding the Bible, or praying",
            "Make it fun! Use silly voices, act things out, draw pictures",
            "Celebrate when you finish all 30 days!"]
    for tip in tips:
        pdf.add_text(f"  * {tip}", size=10, indent=10)
        pdf.add_space(3)
    pdf.end_page()

    family_days = [
        ("God Made You Special", "Psalm 139:14", "God made you unique and wonderful. No one else is exactly like you!", "What makes each family member special?", "Have each person share one thing they like about every other family member."),
        ("God's Love Never Stops", "Romans 8:38-39", "Nothing can separate us from God's love -- not trouble, not danger, nothing!", "Can you think of a time you felt really loved?", "Group hug! Say 'God loves us and WE love each other!'"),
        ("Being Kind", "Ephesians 4:32", "God wants us to be kind to everyone, even when it is hard.", "When is it hardest to be kind?", "Each person does one secret act of kindness tomorrow and reports back."),
        ("Telling the Truth", "Proverbs 12:22", "God loves it when we tell the truth, even when we are scared.", "Why is honesty important in our family?", "Practice saying 'I am sorry, I was not truthful' -- it takes courage!"),
        ("Helping Others", "Galatians 6:2", "God asks us to help carry each other's burdens.", "Who can our family help this week?", "Plan one thing you can do as a family to help someone."),
        ("Being Thankful", "1 Thessalonians 5:18", "We should give thanks in EVERY situation -- good or bad!", "What are 5 things our family is thankful for?", "Make a 'Thank You God' poster together and hang it up."),
        ("Forgiving Each Other", "Colossians 3:13", "Just as God forgives us, we should forgive each other.", "Is there anything anyone needs to forgive?", "Practice saying 'I forgive you' and giving a hug."),
        ("Being Brave", "Isaiah 41:10", "God is with us, so we do not need to be afraid!", "What are you afraid of? Tell God about it.", "Pray together: 'God, help us be brave because You are with us!'"),
        ("Obeying Parents", "Ephesians 6:1", "Children, obey your parents -- this is the right thing to do.", "Why do parents make rules?", "Kids: say one rule you appreciate. Parents: say why you made it."),
        ("Sharing", "Acts 2:44-45", "The first Christians shared everything they had!", "What is hardest for you to share?", "Each person shares something with another family member tonight."),
        ("Using Kind Words", "Proverbs 15:1", "A gentle answer turns away anger, but harsh words stir up conflict.", "How do our words affect each other?", "Practice speaking gently -- even when frustrated. Role-play!"),
        ("Praying Together", "Matthew 18:20", "When two or more gather in Jesus' name, He is there!", "What should we pray about as a family?", "Each person prays ONE sentence out loud. Simple and honest."),
        ("God's Creation", "Genesis 1:31", "God made everything and said it was VERY good!", "What is your favorite thing God created?", "Go outside (or look out a window) and list 10 things God made."),
        ("Trusting God", "Proverbs 3:5-6", "We can trust God even when we do not understand.", "What is something hard to understand right now?", "Write your worry on paper, pray about it, then tear it up!"),
        ("Loving Your Neighbor", "Mark 12:31", "Love your neighbor as yourself.", "Who are our neighbors? How can we love them?", "Bake cookies, draw cards, or wave to neighbors this week!"),
        ("Jesus the Good Shepherd", "John 10:14", "Jesus knows us each by name, like a shepherd knows each sheep.", "How does it feel to know Jesus knows YOUR name?", "Play a game: blindfold one person and guide them by voice -- like a shepherd!"),
        ("The Armor of God", "Ephesians 6:11", "God gives us special armor to be strong!", "What does each piece of armor mean?", "Draw yourselves wearing God's armor. Label each piece!"),
        ("Being Patient", "James 1:4", "Patience helps us grow strong and mature.", "When is it hardest to be patient?", "Set a timer for 2 minutes of silence. Practice patience together!"),
        ("God Hears Our Prayers", "1 John 5:14", "We can be confident that God hears us when we pray!", "Do you really believe God hears you?", "Pray about something specific together. Write it down. Watch for the answer!"),
        ("The Golden Rule", "Matthew 7:12", "Treat others the way you want to be treated.", "How do YOU want to be treated?", "Role-play: act out doing the Golden Rule at school, work, and home."),
        ("Being a Light", "Matthew 5:14-16", "You are the light of the world! Let your light shine!", "How can our family be a light in dark places?", "Light a candle together. Pray: 'God, help us shine Your light!'"),
        ("God's Promises", "2 Corinthians 1:20", "Every promise God makes is YES in Jesus!", "What is a promise God has made to us?", "Find 3 promises in the Bible. Write them on cards for the fridge."),
        ("Joy in Hard Times", "James 1:2", "We can have joy even when things are difficult.", "Can you be joyful when things go wrong? How?", "Sing a worship song together -- even a silly one counts!"),
        ("Serving as a Family", "Galatians 5:13", "Use your freedom to serve one another in love.", "How can we serve each other better?", "Plan a family service project for this weekend."),
        ("The Bible Is Our Guide", "Psalm 119:105", "God's Word is like a flashlight for our path!", "Why is reading the Bible important?", "In the dark, use a flashlight and talk about how the Bible guides us."),
        ("Saying Sorry", "1 John 1:9", "When we say sorry to God, He forgives us every time!", "Is there anything you need to say sorry for?", "Practice: say sorry, ask forgiveness, make it right. No guilt -- just grace!"),
        ("Heaven Is Real", "John 14:2-3", "Jesus is preparing an amazing place for us in heaven!", "What do you think heaven is like?", "Draw pictures of what you think heaven looks like. Share them!"),
        ("Loving God Most", "Matthew 22:37", "Love the Lord your God with ALL your heart, soul, and mind.", "How do we show God we love Him?", "Each person shares their favorite way to connect with God."),
        ("We Are a Team", "Ecclesiastes 4:9-10", "Two are better than one! We are stronger together.", "How does our family work as a team?", "Do a family challenge together (puzzle, game, cooking) as a TEAM."),
        ("God Is Always With Us", "Deuteronomy 31:6", "God will never leave us or forget about us -- EVER!", "Does it comfort you that God is always there?", "Family prayer: Thank God that He is ALWAYS with you. Group hug!"),
    ]

    for i, (theme, verse_ref, teaching, discussion, activity) in enumerate(family_days, 1):
        pdf.start_page()
        pdf.add_text(f"DAY {i}", size=9, bold=True, color=(100, 60, 20))
        pdf.add_chapter_title(f"Day {i}: {theme}")
        pdf.add_text(f"Read Together: {verse_ref}", size=10, bold=True, color=(51, 51, 102))
        pdf.add_space(8)
        pdf.add_text("Today's Teaching:", size=11, bold=True, color=(100, 60, 20))
        pdf.add_wrapped_text(teaching, size=10, indent=5)
        pdf.add_space(8)
        pdf.add_text("Family Discussion:", size=11, bold=True, color=(100, 60, 20))
        pdf.add_wrapped_text(discussion, size=10, italic=True, indent=5)
        pdf.add_space(8)
        pdf.add_text("Family Activity:", size=11, bold=True, color=(100, 60, 20))
        pdf.add_wrapped_text(activity, size=10, indent=5)
        pdf.add_space(8)
        pdf.add_text("Family Prayer:", size=10, bold=True, color=(80, 60, 100))
        pdf.add_lined_space(2, spacing=18)
        pdf.add_text("Memory Verse Check:", size=9, bold=True)
        pdf.add_checkbox(f"We memorized {verse_ref}")
        pdf.end_page()

    # FAMILY PRAYER LIST
    pdf.start_page()
    pdf.add_chapter_title("Our Family Prayer Board")
    pdf.add_text("Prayers from each family member:", size=10, bold=True)
    for member in ["Mom/Parent 1:", "Dad/Parent 2:", "Child 1:", "Child 2:", "Child 3:", "Other:"]:
        pdf.add_text(f"  {member}", size=10, bold=True, indent=5)
        pdf.add_lined_space(2, spacing=18)
        pdf.add_space(3)
    pdf.end_page()

    # CELEBRATION PAGE
    pdf.start_page()
    pdf.add_chapter_title("30 Days Complete! Celebration!")
    pdf.add_wrapped_text("Your family did it! 30 days of growing closer to God and each other!")
    pdf.add_space(10)
    pdf.add_text("Our favorite devotion was Day #: ___", size=10, bold=True)
    pdf.add_space(5)
    pdf.add_text("The most fun activity was:", size=10, bold=True)
    pdf.add_lined_space(2)
    pdf.add_text("We memorized ___ verses!", size=10, bold=True)
    pdf.add_space(5)
    pdf.add_text("How our family grew:", size=10, bold=True)
    pdf.add_lined_space(4)
    pdf.add_text("Family signatures:", size=10, bold=True)
    pdf.add_lined_space(4, spacing=25)
    pdf.end_page()

    pad_to_40_pages(pdf, "Family Devotional Journal")
    return pdf


def create_book_10():
    """Kids Bible Stories Activity Workbook"""
    pdf = PDFEngine()
    pdf.header_text = "Kids Bible Stories Activity Workbook"

    pdf.add_title_page(
        title="Kids Bible Stories Activity Workbook",
        subtitle="50+ Fun Activities, Puzzles, and Crafts Based on Favorite Bible Stories!",
        author="For Kids Ages 5-10",
        extra_lines=["Word searches, mazes, fill-in-the-blanks,", "drawing pages, quizzes, and more!"]
    )

    pdf.start_page()
    pdf.add_chapter_title("Hi, Kids!")
    pdf.add_wrapped_text("Welcome to the most FUN Bible workbook ever! Inside, you will find all kinds of cool activities based on your favorite Bible stories. You can color, draw, solve puzzles, find hidden words, answer quiz questions, and SO much more!")
    pdf.add_space(10)
    pdf.add_text("Activities inside:", size=11, bold=True)
    items = ["Fill in the blank Bible stories", "True or False quizzes",
             "Word scrambles and word searches", "Draw-your-own-scene pages",
             "Match the character to the story", "Put the story in order",
             "Bible verse decoder puzzles", "Spot the differences",
             "Prayer journaling pages for kids", "Memory verse coloring pages"]
    for item in items:
        pdf.add_text(f"  * {item}", size=10, indent=10)
        pdf.add_space(2)
    pdf.end_page()

    # ACTIVITY SECTIONS - Each story gets multiple activity pages
    stories_activities = [
        ("Creation", "Genesis 1-2", [
            ("Fill in the Blank", [
                "On Day 1, God created ___________.",
                "On Day 2, God made the ___________ and ___________.",
                "On Day 3, God made ___________ and ___________.",
                "On Day 4, God made the ___________, ___________, and ___________.",
                "On Day 5, God made ___________ and ___________.",
                "On Day 6, God made ___________ and ___________.",
                "On Day 7, God ___________.",
            ]),
            ("Draw It!", "Draw your favorite thing God created. Make it colorful!"),
            ("True or False", [
                "God created the world in 5 days. (T / F)",
                "God said everything He made was 'very good.' (T / F)",
                "God rested on the 7th day. (T / F)",
                "God made animals before He made people. (T / F)",
                "The first man's name was Noah. (T / F)",
            ]),
        ]),
        ("Noah's Ark", "Genesis 6-9", [
            ("Fill in the Blank", [
                "God told ___________ to build a big ___________.",
                "Noah brought ___________ of every animal on the ark.",
                "It rained for ___________ days and ___________ nights.",
                "After the flood, God put a ___________ in the sky.",
                "The rainbow was God's ___________ to never flood the whole earth again.",
            ]),
            ("Draw It!", "Draw Noah's ark with your favorite animals peeking out!"),
            ("Word Scramble", [
                "KAAR = ___________",
                "NRAI = ___________",
                "ANIRBOW = ___________",
                "HAON = ___________",
                "DLFOO = ___________",
                "SLMAIAN = ___________",
            ]),
        ]),
        ("David and Goliath", "1 Samuel 17", [
            ("Fill in the Blank", [
                "David was a young ___________ boy.",
                "Goliath was a ___________ giant.",
                "David used a ___________ and a ___________.",
                "David said, 'The LORD who saved me from the ___________ and the ___________...'",
                "David won because ___________ was on his side.",
            ]),
            ("Draw It!", "Draw David standing brave before the giant Goliath!"),
            ("True or False", [
                "David was the biggest soldier in the army. (T / F)",
                "Goliath wore heavy armor. (T / F)",
                "David used a sword to defeat Goliath. (T / F)",
                "David trusted God to help him. (T / F)",
                "All the other soldiers were brave too. (T / F)",
            ]),
        ]),
        ("Daniel and the Lions", "Daniel 6", [
            ("Fill in the Blank", [
                "Daniel prayed ___________ times every day.",
                "The king made a law that no one could pray to ___________.",
                "Daniel was thrown into the ___________'s den.",
                "God sent an ___________ to shut the lions' mouths.",
                "Daniel was not ___________!",
            ]),
            ("Draw It!", "Draw Daniel in the lions' den with the angel protecting him!"),
            ("Quiz Time!", [
                "Why was Daniel thrown to the lions? Because he ___________.",
                "How did God protect Daniel? He sent an ___________.",
                "What lesson does this teach? Never stop ___________ to God.",
            ]),
        ]),
        ("Jonah and the Whale", "Jonah 1-4", [
            ("Fill in the Blank", [
                "God told Jonah to go to ___________.",
                "Instead, Jonah got on a ___________ going the other way.",
                "God sent a big ___________ to swallow Jonah.",
                "Jonah was inside the fish for ___________ days.",
                "Jonah prayed and said ___________ to God.",
            ]),
            ("Draw It!", "Draw Jonah inside the big fish! What does it look like in there?"),
            ("Put in Order (number 1-5)", [
                "___ Jonah goes to Nineveh",
                "___ God tells Jonah to go to Nineveh",
                "___ A big fish swallows Jonah",
                "___ Jonah runs away on a boat",
                "___ The fish spits Jonah out",
            ]),
        ]),
        ("Baby Jesus", "Luke 2", [
            ("Fill in the Blank", [
                "Jesus was born in a ___________ in Bethlehem.",
                "Mary laid baby Jesus in a ___________.",
                "The ___________ visited Jesus first.",
                "A bright ___________ appeared in the sky.",
                "___________ sang 'Glory to God!'",
            ]),
            ("Draw It!", "Draw the nativity scene -- baby Jesus, Mary, Joseph, animals, and the star!"),
            ("True or False", [
                "Jesus was born in a fancy palace. (T / F)",
                "Angels appeared to shepherds. (T / F)",
                "A star guided people to Jesus. (T / F)",
                "Jesus was wrapped in expensive clothes. (T / F)",
                "God sent Jesus because He loves us. (T / F)",
            ]),
        ]),
        ("The Good Samaritan", "Luke 10:25-37", [
            ("Fill in the Blank", [
                "A man was walking and ___________ hurt him.",
                "Two people walked ___________ without helping.",
                "A ___________ man stopped to help.",
                "He bandaged the man's ___________ and took care of him.",
                "Jesus said, 'Go and do ___________.'",
            ]),
            ("Draw It!", "Draw the kind Samaritan helping the hurt man on the road."),
            ("Think About It", [
                "Who is your 'neighbor'? ___________",
                "How can you be a Good Samaritan at school? ___________",
                "How can you be a Good Samaritan at home? ___________",
            ]),
        ]),
        ("Jesus Feeds 5,000", "John 6:1-14", [
            ("Fill in the Blank", [
                "A young boy had ___________ loaves and ___________ fish.",
                "___________ thousand people were hungry.",
                "Jesus ___________ God for the food.",
                "Everyone ate until they were ___________.",
                "There were ___________ baskets left over!",
            ]),
            ("Draw It!", "Draw the little boy sharing his lunch with Jesus!"),
            ("Math Challenge!", [
                "5 loaves + 2 fish = ___ items shared",
                "5,000 people fed - 1 small lunch = ___ MIRACLE!",
                "12 baskets left over. 12 x 1 = ___ baskets of leftover blessing!",
            ]),
        ]),
    ]

    for story_name, verse_ref, activities in stories_activities:
        # Story intro page
        pdf.start_page()
        pdf.add_chapter_title(f"{story_name}")
        pdf.add_text(f"Bible Reference: {verse_ref}", size=10, italic=True, color=(100, 100, 100))
        pdf.add_space(10)

        for activity in activities:
            if isinstance(activity, tuple) and len(activity) == 2:
                act_type, act_content = activity
                if act_type == "Draw It!":
                    pdf.add_space(8)
                    pdf.add_text(f"DRAW IT!", size=12, bold=True, color=(0, 120, 0))
                    pdf.add_wrapped_text(act_content, size=10, indent=5)
                    pdf.add_space(5)
                    # Drawing box
                    pdf.add_rect(pdf.margin_left,
                                 pdf.y_position - 120, pdf.content_width, 120,
                                 stroke_color=(0.6, 0.6, 0.6))
                    pdf.y_position -= 130
                elif isinstance(act_content, list):
                    pdf.add_space(8)
                    pdf.add_text(f"{act_type}:", size=12, bold=True, color=(51, 51, 102))
                    pdf.add_space(5)
                    for item in act_content:
                        pdf._check_page_break(18)
                        pdf.add_text(f"  {item}", size=10, indent=10)
                        pdf.add_space(4)
            elif isinstance(activity, tuple) and len(activity) == 3:
                act_type, act_content_list = activity[0], activity[1]
                if isinstance(act_content_list, list):
                    pdf.add_space(8)
                    pdf.add_text(f"{act_type}:", size=12, bold=True, color=(51, 51, 102))
                    pdf.add_space(5)
                    for item in act_content_list:
                        pdf._check_page_break(18)
                        pdf.add_text(f"  {item}", size=10, indent=10)
                        pdf.add_space(4)
        pdf.end_page()

    # Additional drawing pages
    drawing_prompts = [
        "Draw YOUR family praising God!",
        "Draw what heaven might look like!",
        "Draw yourself as a superhero for God!",
        "Draw your favorite Bible story!",
        "Draw God's creation -- the whole world!",
    ]
    for prompt in drawing_prompts:
        pdf.start_page()
        pdf.add_chapter_title("Draw It!")
        pdf.add_text(prompt, size=12, bold=True, color=(0, 120, 0))
        pdf.add_space(10)
        # Large drawing area (blank space)
        pdf.add_rect(55, 100, pdf.content_width, 550, stroke_color=(0.7, 0.7, 0.7))
        pdf.end_page()

    # PRAYER PAGE FOR KIDS
    pdf.start_page()
    pdf.add_chapter_title("My Prayer Page")
    pdf.add_text("Dear God,", size=12, bold=True)
    pdf.add_space(8)
    pdf.add_text("Thank you for:", size=10, bold=True)
    pdf.add_lined_space(3, spacing=22)
    pdf.add_text("Please help:", size=10, bold=True)
    pdf.add_lined_space(3, spacing=22)
    pdf.add_text("I am sorry for:", size=10, bold=True)
    pdf.add_lined_space(3, spacing=22)
    pdf.add_text("I love you because:", size=10, bold=True)
    pdf.add_lined_space(3, spacing=22)
    pdf.add_text("Amen!", size=12, bold=True)
    pdf.end_page()

    # ANSWER KEY (partial)
    pdf.start_page()
    pdf.add_chapter_title("Answer Hints (No peeking!)")
    pdf.add_text("Creation: light, sky/water, land/plants, sun/moon/stars, fish/birds, animals/people, rested", size=8, color=(100, 100, 100))
    pdf.add_space(3)
    pdf.add_text("Noah: Noah, ark, two, 40, 40, rainbow, promise", size=8, color=(100, 100, 100))
    pdf.add_space(3)
    pdf.add_text("David: shepherd, tall/huge, slingshot, stone, lion, bear, God", size=8, color=(100, 100, 100))
    pdf.add_space(3)
    pdf.add_text("Daniel: three, God, lions, angel, hurt", size=8, color=(100, 100, 100))
    pdf.add_space(3)
    pdf.add_text("Jonah: Nineveh, boat, fish, three, sorry", size=8, color=(100, 100, 100))
    pdf.add_space(3)
    pdf.add_text("Baby Jesus: stable, manger, shepherds, star, angels", size=8, color=(100, 100, 100))
    pdf.add_space(3)
    pdf.add_text("Good Samaritan: robbers, past, Samaritan/kind, wounds, likewise", size=8, color=(100, 100, 100))
    pdf.add_space(3)
    pdf.add_text("Feeds 5000: five, two, five, thanked, full, twelve", size=8, color=(100, 100, 100))
    pdf.end_page()

    pad_to_40_pages(pdf, "Kids Bible Activities")
    return pdf


if __name__ == '__main__':
    output_dir = os.path.dirname(os.path.abspath(__file__))

    books = [
        ("06_Christian_Womens_30_Day_Prayer_Journal.pdf", create_book_06),
        ("07_Christian_Mens_Prayer_Purpose_Workbook.pdf", create_book_07),
        ("08_30_Day_Prayer_Purpose_Journal.pdf", create_book_08),
        ("09_Christian_Family_Devotional_30_Days.pdf", create_book_09),
        ("10_Kids_Bible_Stories_Activity_Workbook.pdf", create_book_10),
    ]

    print("=" * 65)
    print("  GENERATING TIER 2 WORKBOOKS - Part 1 (Books 6-10)")
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
    print("  TIER 2 PART 1 COMPLETE!")
    print("=" * 65)
