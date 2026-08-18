#!/usr/bin/env python3
"""
Generate a beautifully formatted PDF of 20 Biblical Stories for Children.
This script generates a PDF from scratch without any external libraries.
It uses raw PDF format specification to create a professional document.
"""

import struct
import zlib
import datetime

# ============================================================
# STORY DATA
# ============================================================

stories = [
    {
        "number": 1,
        "title": "God Creates the World",
        "emoji": "🌍",
        "image_desc": "A breathtaking scene showing the Earth from space surrounded by stars, with golden sunlight breaking through clouds. Colorful flowers bloom below, birds fly in the sky, fish swim in crystal-clear oceans, and a smiling sun watches over everything. A rainbow arcs across the sky.",
        "story": "In the very beginning, there was nothing but darkness. Then God said, \"Let there be light!\" and beautiful light filled everywhere! Day by day, God made amazing things - the blue sky, the sparkling oceans, tall mountains, colorful flowers, funny animals, singing birds, and shining stars. On the sixth day, God made something extra special - people! He made YOU! And when God looked at everything He made, He smiled and said, \"It is VERY good!\"",
        "lesson": "God created ALL things - the trees, the animals, the oceans, and even YOU! Everything God made is special and beautiful.",
        "life_connection": "When you see a butterfly, a flower, or a puppy - remember that God made them with love! Since God created everything, we should take care of nature - don't litter, be kind to animals, water plants, and remember that YOU are God's masterpiece too!"
    },
    {
        "number": 2,
        "title": "Noah and the Big Boat",
        "emoji": "🚢",
        "image_desc": "A huge wooden ark floating on blue water under clearing skies. Pairs of adorable animals peek out from the boat - two giraffes, two elephants, two cute pandas, two colorful parrots. A brilliant rainbow stretches across the sky. Noah stands on deck with his family, arms raised in joy.",
        "story": "Noah was a good man who loved God. God told Noah, \"Build a big boat called an ark!\" People laughed at Noah, but he obeyed God anyway. He brought two of every animal onto the ark - two giraffes, two elephants, two tiny ants, two fluffy bunnies! Then rain came for 40 days and 40 nights. But Noah's family and all the animals were safe inside the ark. When the rain stopped, God put a beautiful rainbow in the sky as a promise that He would always take care of them.",
        "lesson": "When we obey God - even when others laugh at us - God will always protect us and keep His promises.",
        "life_connection": "Sometimes doing the right thing is hard. Maybe your friends want you to be mean to someone, but you know it's wrong. Be like Noah - do what's right even when it's not popular! God will always be with you. And every time you see a rainbow, remember God's promise!"
    },
    {
        "number": 3,
        "title": "Baby Moses in the Basket",
        "emoji": "👶",
        "image_desc": "A cute baby wrapped in a soft blanket, sleeping peacefully in a woven basket floating among tall green reeds on a gentle river. Dragonflies hover nearby, lotus flowers bloom on the water, and a kind princess in a golden dress reaches toward the basket with a loving smile.",
        "story": "Baby Moses was in danger! A mean king wanted to hurt all baby boys. But Moses' mommy loved him SO much. She made a special basket-boat, wrapped baby Moses in a cozy blanket, and placed him gently on the river. His big sister Miriam watched from behind the tall grass. A kind princess found baby Moses and said, \"What a beautiful baby! I will keep him safe!\" God used a brave mommy, a watchful sister, and a kind princess to protect little Moses.",
        "lesson": "God uses people who love us - our family, friends, and teachers - to keep us safe and cared for.",
        "life_connection": "Think about all the people who take care of you - your parents, grandparents, teachers, and friends. They are God's helpers! Say \"thank you\" to someone who takes care of you today. And remember - YOU can be a helper too, just like Miriam watched over her baby brother!"
    },
    {
        "number": 4,
        "title": "David the Brave Shepherd Boy",
        "emoji": "🐑",
        "image_desc": "A small, brave boy with curly hair and a slingshot stands confidently before a HUGE giant in armor. The boy has a peaceful, confident smile. Behind him, sheep graze on green hills. Light shines down from heaven onto the boy. Five smooth stones sit at his feet.",
        "story": "David was just a young boy who took care of sheep. One day, a GIANT named Goliath - taller than a house! - scared everyone. All the grown-up soldiers were afraid. But little David said, \"God is with me! I'm not afraid!\" With just a slingshot and one smooth stone, David defeated the giant! Not because David was big and strong, but because God was on his side.",
        "lesson": "With God's help, even someone small can do BIG things! You don't have to be big or strong - you just need to trust God.",
        "life_connection": "Do you ever feel too small or too young to make a difference? Maybe a test feels like a giant, or starting a new school feels scary. Remember David! With God's help, you can face any \"giant\" in your life. Be brave, trust God, and know that being young doesn't mean you can't do amazing things!"
    },
    {
        "number": 5,
        "title": "Daniel in the Lions' Den",
        "emoji": "🦁",
        "image_desc": "A peaceful man sits calmly in a cave surrounded by big lions. But instead of being scary, the lions are lying down like gentle kittens! One lion rests its head on Daniel's lap. A glowing angel with bright wings stands guard. Warm golden light fills the den.",
        "story": "Daniel loved God and prayed every single day. Some jealous people made a rule: \"No one can pray to God, or they'll be thrown to the lions!\" But Daniel kept praying anyway. He was thrown into a den full of hungry lions! But guess what? God sent an angel who shut the lions' mouths! The lions became gentle as kittens. The next morning, Daniel walked out without a single scratch!",
        "lesson": "When we stay faithful to God and keep doing what's right, God will protect us - even in the scariest situations.",
        "life_connection": "It takes courage to pray or talk about God when others might make fun of you. Maybe someone says, \"That's not cool!\" But like Daniel, never be ashamed to talk to God. You can pray anytime - before meals, before bed, or when you feel scared. God always listens!"
    },
    {
        "number": 6,
        "title": "Jonah and the Big Fish",
        "emoji": "🐋",
        "image_desc": "A massive, friendly-looking whale swims in a deep blue ocean with a surprised man visible inside. Colorful coral, starfish, and tropical fish surround the whale. Bubbles float upward. Sunlight streams through the water from above. The scene is both dramatic and whimsical.",
        "story": "God told Jonah, \"Go tell the people of Nineveh to be kind!\" But Jonah said, \"No way!\" and ran the other direction! He jumped on a boat to sail far away. A huge storm came, and Jonah was thrown into the sea. A GIGANTIC fish swallowed him whole! For three days, Jonah sat inside the fish's belly. He prayed, \"I'm sorry, God! I'll listen now!\" The fish spit Jonah out, and he went to Nineveh like God asked.",
        "lesson": "We can't run from God. When we make mistakes, God gives us second chances if we say sorry and try again.",
        "life_connection": "Have you ever been asked to do something you didn't want to do - like sharing your toys, saying sorry, or cleaning your room? Running away from it only makes things harder! It's always better to obey right away. And if you mess up? It's okay! Say sorry and try again. God always gives second chances!"
    },
    {
        "number": 7,
        "title": "The Birth of Baby Jesus",
        "emoji": "⭐",
        "image_desc": "A warm, glowing stable scene. Baby Jesus lies in a manger filled with soft hay, wrapped in white cloth, with a gentle golden glow around him. Mary and Joseph smile lovingly. Cute sheep, a donkey, and a cow watch peacefully. A brilliant star shines above the stable. Angels sing in the sky.",
        "story": "On the most special night ever, baby Jesus was born! Not in a fancy palace, but in a simple stable with animals. Mary wrapped her baby in soft cloths and laid him in a manger - a feeding box for animals! Angels sang in the sky, \"Joy to the world!\" Shepherds came running to see the baby. A bright star guided everyone to Him. God sent His own Son as a tiny baby to show the whole world how much He loves us!",
        "lesson": "God shows His love in humble, simple ways. You don't need to be rich or fancy to be important - Jesus himself was born in a stable!",
        "life_connection": "Sometimes we think we need expensive toys or fancy clothes to be special. But Jesus was born in the simplest place! What makes you special is God's love inside you - not what you own. You can show love in simple ways too: a hug, a kind word, sharing your lunch. That's what really matters!"
    },
    {
        "number": 8,
        "title": "Jesus Feeds 5,000 People",
        "emoji": "🍞",
        "image_desc": "Jesus stands on a green hillside surrounded by thousands of happy people sitting on the grass. A small boy offers his basket with 5 small loaves of bread and 2 fish. Jesus holds them up with a smile. Baskets overflow with food everywhere. Families laugh and eat together.",
        "story": "Five thousand hungry people came to hear Jesus! The disciples worried, \"We don't have enough food!\" But a little boy came forward with his small lunch - just 5 loaves of bread and 2 fish. \"It's not much,\" the boy said, \"but you can have it!\" Jesus took that tiny lunch, thanked God, and broke the bread. Suddenly there was enough food for EVERYONE - with 12 baskets left over! A small boy's sharing made a big miracle possible!",
        "lesson": "When we share what we have - even if it seems small - God can use it to do amazing, BIG things!",
        "life_connection": "You might think, \"I'm just a kid, what can I share?\" But just like that little boy, YOUR sharing matters! Share your snack with a friend, share your toys, share a smile! When you give what you have with a happy heart, God multiplies it into something beautiful. No gift is too small!"
    },
    {
        "number": 9,
        "title": "The Good Samaritan",
        "emoji": "❤️",
        "image_desc": "A kind man with gentle eyes kneels beside a hurt traveler on a dusty road, carefully bandaging his wounds. A donkey waits patiently nearby. Other people walk by in the distance, looking away. The kind man has water, oil, and clean bandages. Wildflowers grow along the road.",
        "story": "Jesus told this story: A man was walking on a road when robbers hurt him and left him alone. A rich man walked by - but he crossed to the other side and ignored him. A religious leader walked by - he didn't help either! Then a Samaritan man came. People didn't like Samaritans, but this man stopped, knelt down, and helped. He cleaned the man's wounds, put him on his donkey, took him to a safe place, and even paid for his care!",
        "lesson": "Be kind to EVERYONE - not just your friends or people who look like you. A true neighbor is anyone who shows love.",
        "life_connection": "If you see someone sitting alone at lunch, a new kid who looks lost, or someone who dropped their books - be the one who helps! Don't walk past like the first two men. It doesn't matter if they're different from you. Every person deserves kindness. Be the Good Samaritan in your school today!"
    },
    {
        "number": 10,
        "title": "The Lost Sheep",
        "emoji": "🐑",
        "image_desc": "A loving shepherd carries a fluffy little lamb on his shoulders through a moonlit meadow. 99 sheep graze peacefully in the background behind a fence. The shepherd looks relieved and happy, hugging the lamb close. Stars twinkle above.",
        "story": "Jesus told a story about a shepherd who had 100 sheep. One day, he counted them - 97, 98, 99... one was missing! Did the shepherd say, \"Oh well, I still have 99\"? NO! He left the 99 safe sheep and searched everywhere for the one lost lamb. Over rocky mountains, through thorny bushes, in the dark night. When he found the little lamb, he was SO happy! He carried it home on his shoulders and threw a party!",
        "lesson": "You are SO important to God that He will never stop looking for you. You are NEVER too lost for God to find.",
        "life_connection": "Have you ever felt left out or forgotten? Maybe you made a mistake and thought, \"God doesn't love me anymore.\" That's NOT true! God loves you like that shepherd loves his one lost sheep. You are never alone. If you ever feel lost or sad, talk to God - He's already looking for you with open arms!"
    },
    {
        "number": 11,
        "title": "The Prodigal Son Comes Home",
        "emoji": "🏠",
        "image_desc": "An emotional scene: a father running with open arms down a path toward his ragged, dirty son. Tears of joy stream down both their faces. The father's home is beautiful in the background with warm lights glowing. A feast is being prepared.",
        "story": "A young man asked his father for his share of money, then ran away to have \"fun.\" He spent ALL his money on silly things. Soon he had nothing - no food, no friends, no home. He was so hungry he wanted to eat pig food! Finally he said, \"I'll go home and say sorry to my dad.\" But while he was still far away, his father SAW him, RAN to him, HUGGED him, and threw the biggest party ever! \"My son was lost, but now he's found!\"",
        "lesson": "No matter how many mistakes you make, God (like the loving father) is ALWAYS waiting to welcome you back with open arms.",
        "life_connection": "Have you ever done something wrong and felt too embarrassed to say sorry? Maybe you lied, said something mean, or disobeyed your parents. It's never too late to come back and say sorry! Your parents love you like that father - and God loves you even MORE. You'll always be welcomed home."
    },
    {
        "number": 12,
        "title": "Jesus Walks on Water",
        "emoji": "🌊",
        "image_desc": "Jesus walks calmly on stormy ocean waves at night, glowing with soft white light. His hand reaches toward Peter, who is starting to sink in the waves with a worried face. A small boat with other disciples rocks in the background. Lightning flashes in dark clouds.",
        "story": "The disciples were in a boat during a terrible storm! Waves crashed, wind howled, and they were SO scared! Then they saw someone walking on the water! It was Jesus! Peter said, \"Jesus, can I walk to you?\" Jesus said, \"Come!\" Peter stepped out and actually WALKED on water! But when he looked at the scary waves instead of Jesus, he started to sink. \"Help me!\" he cried. Jesus immediately grabbed his hand and saved him.",
        "lesson": "When we keep our eyes on Jesus and trust Him, we can do impossible things. When we focus on fear, we start to sink.",
        "life_connection": "Life has \"storms\" too - a scary test, parents fighting, feeling worried about the future. When those storms come, don't focus on the scary waves. Focus on God! Pray, read your Bible, talk to someone you trust. And if you start to \"sink\" with worry, call out to God. He will ALWAYS reach out and hold you up!"
    },
    {
        "number": 13,
        "title": "Zacchaeus the Short Man in a Tree",
        "emoji": "🌳",
        "image_desc": "A very short, funny-looking man perches high in a big sycamore tree with huge green leaves, peering down with wide, curious eyes. Below, Jesus looks UP at him with a warm smile and an outstretched hand. A crowd of surprised people watches.",
        "story": "Zacchaeus was a VERY short man who took money from people unfairly. Everyone disliked him. When Jesus came to town, Zacchaeus wanted to see Him but was too short to see over the crowd! So he climbed a big tree! Jesus looked up and said, \"Zacchaeus, come down! I want to eat at YOUR house today!\" Zacchaeus was SO happy that Jesus loved him! He changed completely and said, \"I'll give back everything I took - and even more!\"",
        "lesson": "Jesus loves everyone - even people others reject. When we experience God's love, it changes us and makes us WANT to do the right thing.",
        "life_connection": "Is there someone at school that nobody likes? Maybe they did something wrong before. Be like Jesus - show them kindness anyway! Your kindness might help them change. And if YOU have done something wrong, know that Jesus still loves you. His love makes us WANT to be better."
    },
    {
        "number": 14,
        "title": "Ruth and Naomi - Friends Forever",
        "emoji": "👫",
        "image_desc": "Two women walk together on a dusty path through golden wheat fields at sunset. The younger woman holds the older woman's hand lovingly. Both carry small bundles. Their faces show determination and loyalty. Stalks of wheat blow gently in the breeze.",
        "story": "Naomi was sad - her husband and sons had died, and she had to go back to her old home alone. Her daughter-in-law Ruth could have gone back to her own family. But Ruth said the most beautiful words: \"Where you go, I will go. Your people will be my people, and your God will be my God.\" Ruth CHOSE to stay with Naomi, work hard in the fields to feed them both, and never leave her side. God blessed Ruth's loyalty in amazing ways!",
        "lesson": "True friendship means sticking with people even when times are hard. Loyalty and love are more precious than anything.",
        "life_connection": "A real friend doesn't leave when things get hard. If your friend is sad, sick, or going through a tough time - stay by their side! Don't only be friends when things are fun. Also, love your grandparents and older family members - spend time with them, help them, listen to their stories."
    },
    {
        "number": 15,
        "title": "The Fiery Furnace",
        "emoji": "🔥",
        "image_desc": "Three young men stand calmly inside a blazing furnace of orange and red flames, completely unharmed! Their clothes aren't even singed. A fourth glowing figure - an angel - stands with them, arms spread protectively. The king watches through the furnace opening with shock.",
        "story": "A king built a huge golden statue and said, \"Everyone must bow down to it!\" But three brave friends - Shadrach, Meshach, and Abednego - said, \"NO! We only worship God!\" The angry king made a furnace seven times hotter and threw them in! But when he looked inside, he saw FOUR people walking around - the three friends PLUS a shining angel! Not even their hair was burned! The king was amazed and said, \"Their God is the true God!\"",
        "lesson": "When we stand up for what's right together, God stands with us. True courage comes from knowing God is by your side.",
        "life_connection": "Peer pressure is like that king - it says \"Do what everyone else does or you'll be left out!\" But you don't have to follow the crowd! Have brave friends who will stand with you for what's right. Together, you're stronger. And remember - even in the \"fire\" of hard times, God is right there with you!"
    },
    {
        "number": 16,
        "title": "Joseph's Colorful Coat - From Pit to Palace",
        "emoji": "🌾",
        "image_desc": "A young man wearing a stunning coat of many bright colors - red, blue, purple, gold, green - stands before a golden throne in an Egyptian palace. Behind him, a split scene shows his journey: a dark pit, a prison cell, and then the palace. His face shows kindness and forgiveness.",
        "story": "Joseph's dad gave him a beautiful coat of many colors. His brothers were SO jealous that they threw him into a pit and sold him! Joseph became a slave, then was put in prison for something he didn't do! Things looked terrible. But Joseph kept trusting God. God had a plan! Joseph became the SECOND most powerful person in all of Egypt! When his brothers came begging for food, Joseph forgave them and said, \"What you meant for harm, God used for good!\"",
        "lesson": "Bad things might happen, but God can turn ANYTHING into something good. Never give up - God has a plan for your life!",
        "life_connection": "Sometimes bad things happen - maybe someone is mean to you, your parents move, or you lose something important. It's okay to feel sad! But don't give up hope. Like Joseph, God can turn your hard times into something beautiful. Also - when someone hurts you, try to forgive them. Forgiveness sets YOUR heart free!"
    },
    {
        "number": 17,
        "title": "The Parable of the Seeds",
        "emoji": "🌱",
        "image_desc": "A four-panel scene: (1) Seeds falling on a hard road with birds eating them, (2) Seeds on rocky ground with tiny weak sprouts wilting, (3) Seeds among thorny weeds that choke small plants, (4) Seeds in rich dark soil growing into a HUGE, beautiful garden full of colorful fruits and flowers!",
        "story": "Jesus told a story about a farmer who scattered seeds. Some fell on the hard road - birds ate them! Some fell on rocky ground - they grew fast but died in the sun because they had no roots. Some fell among thorns - the weeds choked them. But some seeds fell on GOOD soil - they grew into an amazing garden, 100 times more than what was planted! Jesus said the seeds are like God's words, and the soil is our hearts.",
        "lesson": "When we listen to God's words carefully and let them grow in our hearts, amazing things will bloom in our lives!",
        "life_connection": "Your heart is like soil! When someone teaches you something good - at church, at school, or from your parents - really LISTEN and remember it. Don't just hear it and forget. Let good words grow in your heart like seeds in good soil. Read your Bible, pray, and practice kindness - that's how you make your heart the BEST soil!"
    },
    {
        "number": 18,
        "title": "Queen Esther - Brave and Beautiful",
        "emoji": "👑",
        "image_desc": "A beautiful young queen with a golden crown and flowing purple robes stands bravely before a powerful king on his throne. Her face shows courage mixed with fear. Light shines on her like a spotlight. The throne room is grand with pillars and curtains.",
        "story": "Esther was a young Jewish girl who became QUEEN! But an evil man named Haman wanted to hurt all her people. Esther's uncle told her, \"Maybe God made you queen for THIS moment!\" Esther was scared - going to the king without being called could mean death! But she said the bravest words: \"If I die, I die. But I must try to save my people!\" She went to the king, told the truth, and saved everyone!",
        "lesson": "God puts you exactly where you are for a reason. Sometimes being brave and speaking up can save the day - even if it's scary!",
        "life_connection": "Maybe you're the only one who sees someone being bullied. Maybe you know something wrong is happening. Be like Esther - speak up! Tell a teacher, tell your parents, stand up for others. It might feel scary, but God put you in that moment for a reason. Your voice matters!"
    },
    {
        "number": 19,
        "title": "The Wise and Foolish Builders",
        "emoji": "🏗️",
        "image_desc": "A split scene during a storm: On the LEFT, a house built on sand is crumbling and falling apart as waves crash - the foolish builder watches in panic. On the RIGHT, a strong house built on solid rock stands firm and safe - warm light glows inside, and the wise builder waves happily.",
        "story": "Jesus said: \"A wise man built his house on rock. Rain poured, floods came, winds blew - but the house STOOD STRONG because it was on solid rock! A foolish man built his house on sand. It looked great at first! But when the same storm came - the house crashed down with a BIG SPLAT!\" Jesus said that people who hear His words AND do them are like the wise builder. Those who hear but DON'T obey are like the foolish builder.",
        "lesson": "It's not enough to just HEAR good things - we must DO them! Building our lives on God's truth keeps us strong when hard times come.",
        "life_connection": "What's YOUR \"rock\"? It's the good habits you build! Being honest, being kind, obeying your parents, reading the Bible, and praying - these are like building on rock. When hard times come (and they will!), these good habits will keep you strong. Don't just KNOW what's right - DO what's right!"
    },
    {
        "number": 20,
        "title": "Jesus Loves the Little Children",
        "emoji": "🕊️",
        "image_desc": "Jesus sits in a beautiful garden surrounded by happy children of every skin color! Children sit on his lap, hug him, hold his hands, and play around him. Some bring flowers, one brings a puppy. Jesus laughs with pure joy. Butterflies and doves fly around them. A soft golden glow surrounds the whole scene.",
        "story": "Children came running to see Jesus! But the grown-up disciples said, \"Go away, kids! Jesus is too busy for you!\" Jesus heard this and was NOT happy. He said, \"Let the children come to me! Don't stop them! Heaven belongs to people with hearts like these children!\" Then Jesus hugged the children, put His hands on their heads to bless them, and spent time with every single one. To Jesus, children aren't \"just kids\" - they are the MOST important people in the room!",
        "lesson": "YOU are important to Jesus! You don't have to be a grown-up to be close to God. He loves children with His whole heart.",
        "life_connection": "Never think you're too young or too small for God to care about you. Jesus LOVES you right now - just as you are! You don't have to wait until you're grown up. You can talk to God today, right now! And remember - have a child's heart: be full of wonder, trust easily, love freely, and never stop being curious about God. YOU are His favorite!"
    }
]


# ============================================================
# PDF GENERATION (Pure Python - No External Libraries)
# ============================================================

class SimplePDF:
    """Generate a PDF file using raw PDF format specification."""
    
    def __init__(self):
        self.objects = []
        self.pages = []
        self.current_page_content = []
        self.page_height = 792  # Letter size in points (11 inches)
        self.page_width = 612   # Letter size in points (8.5 inches)
        self.margin_left = 60
        self.margin_right = 60
        self.margin_top = 60
        self.margin_bottom = 60
        self.y_position = self.page_height - self.margin_top
        self.font_size = 11
        self.line_height = 14
        self.content_width = self.page_width - self.margin_left - self.margin_right
        
    def _escape_pdf_string(self, text):
        """Escape special characters in PDF strings."""
        text = text.replace('\\', '\\\\')
        text = text.replace('(', '\\(')
        text = text.replace(')', '\\)')
        # Remove emoji and non-ASCII characters for PDF compatibility
        result = ''
        for char in text:
            if ord(char) < 128:
                result += char
            else:
                result += ' '
        return result
    
    def _wrap_text(self, text, max_chars_per_line=85):
        """Word-wrap text to fit within page width."""
        words = text.split()
        lines = []
        current_line = ''
        
        for word in words:
            if len(current_line) + len(word) + 1 <= max_chars_per_line:
                if current_line:
                    current_line += ' ' + word
                else:
                    current_line = word
            else:
                if current_line:
                    lines.append(current_line)
                current_line = word
        
        if current_line:
            lines.append(current_line)
        
        return lines
    
    def _check_page_break(self, needed_height):
        """Check if we need a new page and create one if necessary."""
        if self.y_position - needed_height < self.margin_bottom:
            self._end_page()
            self._start_page()
    
    def _start_page(self):
        """Start a new page."""
        self.current_page_content = []
        self.y_position = self.page_height - self.margin_top
    
    def _end_page(self):
        """End current page and save its content."""
        self.pages.append(self.current_page_content[:])
        self.current_page_content = []
    
    def _add_text(self, text, font_size=11, bold=False, indent=0, color=(0, 0, 0)):
        """Add text to current page."""
        font = '/F2' if bold else '/F1'
        r, g, b = [c/255.0 for c in color]
        
        x = self.margin_left + indent
        self.current_page_content.append(
            f'BT\n{r:.3f} {g:.3f} {b:.3f} rg\n{font} {font_size} Tf\n{x} {self.y_position:.1f} Td\n({self._escape_pdf_string(text)}) Tj\nET'
        )
        self.y_position -= self.line_height * (font_size / 11.0)
    
    def _add_wrapped_text(self, text, font_size=11, bold=False, indent=0, color=(0, 0, 0), max_chars=85):
        """Add word-wrapped text."""
        adjusted_max = max_chars - int(indent / 6)
        lines = self._wrap_text(text, adjusted_max)
        
        for line in lines:
            self._check_page_break(self.line_height * (font_size / 11.0) + 2)
            self._add_text(line, font_size, bold, indent, color)
    
    def _add_separator(self):
        """Add a horizontal line separator."""
        self._check_page_break(20)
        y = self.y_position
        x1 = self.margin_left
        x2 = self.page_width - self.margin_right
        self.current_page_content.append(
            f'0.7 0.7 0.7 RG\n0.5 w\n{x1} {y} m\n{x2} {y} l\nS'
        )
        self.y_position -= 15
    
    def _add_colored_box(self, x, y, width, height, r, g, b):
        """Add a colored rectangle."""
        self.current_page_content.append(
            f'{r:.3f} {g:.3f} {b:.3f} rg\n{x} {y} {width} {height} re\nf'
        )
    
    def _add_space(self, points=10):
        """Add vertical space."""
        self.y_position -= points
    
    def generate(self, output_path):
        """Generate the complete PDF document."""
        
        # === COVER PAGE ===
        self._start_page()
        
        # Background color box for title area
        self._add_colored_box(0, 400, 612, 392, 0.4, 0.3, 0.65)
        
        # Title
        self.y_position = 700
        self._add_text("20 AMAZING", 28, bold=True, indent=140, color=(255, 255, 255))
        self._add_space(8)
        self._add_text("BIBLE STORIES", 32, bold=True, indent=120, color=(255, 255, 255))
        self._add_space(8)
        self._add_text("FOR KIDS", 28, bold=True, indent=170, color=(255, 255, 255))
        
        self._add_space(30)
        self._add_text("Discover God's Love Through", 14, bold=False, indent=140, color=(255, 230, 180))
        self._add_space(4)
        self._add_text("Amazing Adventures!", 14, bold=False, indent=170, color=(255, 230, 180))
        
        # Subtitle area
        self.y_position = 350
        self._add_text("Each story includes:", 13, bold=True, indent=60, color=(80, 80, 80))
        self._add_space(8)
        self._add_text("* A vivid image description for illustration", 11, indent=80, color=(100, 100, 100))
        self._add_space(4)
        self._add_text("* The Bible story retold for children", 11, indent=80, color=(100, 100, 100))
        self._add_space(4)
        self._add_text("* A key lesson from the story", 11, indent=80, color=(100, 100, 100))
        self._add_space(4)
        self._add_text("* How it relates to YOUR life today", 11, indent=80, color=(100, 100, 100))
        
        self.y_position = 200
        self._add_text("\"I have loved you with an everlasting love.\"", 12, bold=True, indent=120, color=(102, 51, 153))
        self._add_space(4)
        self._add_text("- Jeremiah 31:3", 10, indent=200, color=(102, 51, 153))
        
        self.y_position = 100
        self._add_text("Made with love for God's little ones", 10, indent=180, color=(150, 150, 150))
        
        self._end_page()
        
        # === TABLE OF CONTENTS ===
        self._start_page()
        self.y_position = self.page_height - 80
        self._add_text("TABLE OF CONTENTS", 18, bold=True, indent=140, color=(102, 51, 153))
        self._add_space(20)
        self._add_separator()
        self._add_space(10)
        
        for i, story in enumerate(stories):
            self._check_page_break(20)
            title_text = f"Story {story['number']:2d}: {story['title']}"
            self._add_text(title_text, 11, bold=False, indent=20, color=(60, 60, 60))
            self._add_space(4)
        
        self._end_page()
        
        # === STORY PAGES ===
        for story in stories:
            self._start_page()
            
            # Story header with colored bar
            header_y = self.y_position + 5
            self._add_colored_box(self.margin_left - 10, header_y - 30, self.content_width + 20, 40, 0.4, 0.3, 0.65)
            
            # Story number and title
            title = f"Story {story['number']}: {story['title']}"
            self._add_text(title, 16, bold=True, indent=5, color=(255, 255, 255))
            self._add_space(20)
            
            # Decorative line
            self._add_separator()
            self._add_space(5)
            
            # IMAGE DESCRIPTION SECTION
            self._add_text("[IMAGINE THIS SCENE]", 9, bold=True, indent=0, color=(102, 126, 234))
            self._add_space(4)
            self._add_wrapped_text(story['image_desc'], 10, indent=10, color=(80, 100, 140), max_chars=90)
            self._add_space(12)
            
            # STORY SECTION
            self._add_text("THE STORY", 13, bold=True, indent=0, color=(108, 92, 231))
            self._add_space(6)
            self._add_wrapped_text(story['story'], 11, indent=0, color=(50, 50, 50))
            self._add_space(15)
            
            # LESSON BOX
            self._check_page_break(60)
            box_y = self.y_position - 5
            
            self._add_text("LESSON", 12, bold=True, indent=10, color=(125, 88, 0))
            self._add_space(4)
            self._add_wrapped_text(story['lesson'], 11, bold=False, indent=10, color=(90, 64, 0), max_chars=80)
            self._add_space(15)
            
            # LIFE CONNECTION
            self._check_page_break(60)
            self._add_text("HOW THIS RELATES TO YOUR LIFE", 12, bold=True, indent=10, color=(0, 105, 92))
            self._add_space(4)
            self._add_wrapped_text(story['life_connection'], 11, indent=10, color=(45, 106, 79), max_chars=80)
            self._add_space(10)
            
            # Footer separator
            self._add_separator()
            
            self._end_page()
        
        # === FINAL PAGE ===
        self._start_page()
        self.y_position = 500
        self._add_colored_box(0, 300, 612, 300, 0.4, 0.3, 0.65)
        
        self.y_position = 520
        self._add_text("Thank You for Reading!", 22, bold=True, indent=120, color=(255, 255, 255))
        self._add_space(20)
        self._add_text("Remember: God loves YOU", 16, bold=True, indent=140, color=(255, 230, 180))
        self._add_space(8)
        self._add_text("more than all the stars in the sky!", 16, bold=True, indent=110, color=(255, 230, 180))
        
        self.y_position = 250
        self._add_text("Share these stories with your friends", 12, indent=150, color=(100, 100, 100))
        self._add_space(6)
        self._add_text("and family!", 12, indent=210, color=(100, 100, 100))
        
        self.y_position = 150
        self._add_text("\"For God so loved the world that He gave His", 11, bold=True, indent=100, color=(102, 51, 153))
        self._add_space(3)
        self._add_text("one and only Son, that whoever believes in Him", 11, bold=True, indent=95, color=(102, 51, 153))
        self._add_space(3)
        self._add_text("shall not perish but have eternal life.\"", 11, bold=True, indent=115, color=(102, 51, 153))
        self._add_space(4)
        self._add_text("- John 3:16", 10, indent=225, color=(102, 51, 153))
        
        self._end_page()
        
        # === BUILD PDF FILE ===
        self._build_pdf(output_path)
    
    def _build_pdf(self, output_path):
        """Build the actual PDF file."""
        
        # Object references
        obj_num = 1
        objects = {}
        offsets = {}
        
        # Build content streams for each page
        page_content_objs = []
        for page_content in self.pages:
            stream = '\n'.join(page_content)
            page_content_objs.append(stream)
        
        # Calculate object count:
        # 1: Catalog
        # 2: Pages
        # 3: Font1 (Helvetica)
        # 4: Font2 (Helvetica-Bold)
        # 5..5+n-1: Page objects
        # 5+n..5+2n-1: Content stream objects
        
        num_pages = len(self.pages)
        catalog_obj = 1
        pages_obj = 2
        font1_obj = 3
        font2_obj = 4
        first_page_obj = 5
        first_content_obj = first_page_obj + num_pages
        total_objs = first_content_obj + num_pages
        
        output = []
        
        # PDF Header
        output.append('%PDF-1.4\n%\xe2\xe3\xcf\xd3\n')
        
        # Object 1: Catalog
        offsets[catalog_obj] = sum(len(o.encode('latin-1', errors='replace')) for o in output)
        output.append(f'{catalog_obj} 0 obj\n<< /Type /Catalog /Pages {pages_obj} 0 R >>\nendobj\n\n')
        
        # Object 2: Pages
        page_refs = ' '.join(f'{first_page_obj + i} 0 R' for i in range(num_pages))
        offsets[pages_obj] = sum(len(o.encode('latin-1', errors='replace')) for o in output)
        output.append(f'{pages_obj} 0 obj\n<< /Type /Pages /Kids [{page_refs}] /Count {num_pages} >>\nendobj\n\n')
        
        # Object 3: Font1 (Helvetica)
        offsets[font1_obj] = sum(len(o.encode('latin-1', errors='replace')) for o in output)
        output.append(f'{font1_obj} 0 obj\n<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica /Encoding /WinAnsiEncoding >>\nendobj\n\n')
        
        # Object 4: Font2 (Helvetica-Bold)
        offsets[font2_obj] = sum(len(o.encode('latin-1', errors='replace')) for o in output)
        output.append(f'{font2_obj} 0 obj\n<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Bold /Encoding /WinAnsiEncoding >>\nendobj\n\n')
        
        # Page objects
        for i in range(num_pages):
            page_obj_num = first_page_obj + i
            content_obj_num = first_content_obj + i
            offsets[page_obj_num] = sum(len(o.encode('latin-1', errors='replace')) for o in output)
            output.append(
                f'{page_obj_num} 0 obj\n'
                f'<< /Type /Page /Parent {pages_obj} 0 R '
                f'/MediaBox [0 0 {self.page_width} {self.page_height}] '
                f'/Contents {content_obj_num} 0 R '
                f'/Resources << /Font << /F1 {font1_obj} 0 R /F2 {font2_obj} 0 R >> >> '
                f'>>\nendobj\n\n'
            )
        
        # Content stream objects
        for i in range(num_pages):
            content_obj_num = first_content_obj + i
            stream_data = page_content_objs[i]
            stream_bytes = stream_data.encode('latin-1', errors='replace')
            offsets[content_obj_num] = sum(len(o.encode('latin-1', errors='replace')) for o in output)
            output.append(
                f'{content_obj_num} 0 obj\n'
                f'<< /Length {len(stream_bytes)} >>\n'
                f'stream\n'
                f'{stream_data}\n'
                f'endstream\n'
                f'endobj\n\n'
            )
        
        # Cross-reference table
        xref_offset = sum(len(o.encode('latin-1', errors='replace')) for o in output)
        output.append(f'xref\n0 {total_objs + 1}\n')
        output.append('0000000000 65535 f \n')
        
        for obj_id in range(1, total_objs + 1):
            if obj_id in offsets:
                output.append(f'{offsets[obj_id]:010d} 00000 n \n')
            else:
                output.append(f'0000000000 00000 f \n')
        
        # Trailer
        output.append(
            f'trailer\n'
            f'<< /Size {total_objs + 1} /Root {catalog_obj} 0 R >>\n'
            f'startxref\n{xref_offset}\n%%EOF\n'
        )
        
        # Write file
        with open(output_path, 'wb') as f:
            for part in output:
                f.write(part.encode('latin-1', errors='replace'))
        
        return output_path


# ============================================================
# MAIN
# ============================================================

if __name__ == '__main__':
    import os
    
    output_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(output_dir, '20_Biblical_Stories_for_Children.pdf')
    
    print("=" * 60)
    print("  GENERATING: 20 Amazing Bible Stories for Kids (PDF)")
    print("=" * 60)
    print()
    
    pdf = SimplePDF()
    pdf.generate(output_path)
    
    file_size = os.path.getsize(output_path)
    print(f"  SUCCESS! PDF generated at:")
    print(f"  {output_path}")
    print(f"  File size: {file_size / 1024:.1f} KB")
    print(f"  Pages: {len(pdf.pages)} (Cover + TOC + 20 Stories + Final)")
    print()
    print("=" * 60)
