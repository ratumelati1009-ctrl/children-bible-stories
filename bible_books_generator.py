#!/usr/bin/env python3
"""
Generate educational Bible story books for children (ages 6-13)
with illustrations and Tigrigna translations.
Each book contains stories with:
- English title and text
- Tigrigna (ትግርኛ) translation
- SVG illustrations
- Bible verse references
- Educational moral/lesson
"""
import os
import subprocess
import html as html_module

# ============================================================
# BIBLE STORIES DATA
# Each story: (title_en, title_ti, verse_ref, story_en, story_ti, moral_en, moral_ti, illustration_fn)
# ============================================================


BOOK_1_STORIES = [
    # Book 1: Creation & Early Stories (Genesis)
    {
        "title_en": "God Creates the World",
        "title_ti": "ኣምላኽ ዓለም ይፈጥር",
        "verse": "Genesis 1:1",
        "story_en": "In the beginning, God created the heavens and the earth. The earth was empty and dark. Then God said, 'Let there be light!' and there was light. God saw that the light was good. He separated the light from the darkness. God called the light 'day' and the darkness 'night.' This was the first day of creation.",
        "story_ti": "ኣብ መጀመርታ ኣምላኽ ሰማይን ምድርን ፈጠረ። ምድሪ ጥራያን ጸልማትን ነበረት። ሽዑ ኣምላኽ 'ብርሃን ይኹን!' በለ፣ ብርሃን ከኣ ኰነ። ኣምላኽ ብርሃን ጽቡቕ ምዃኑ ረኣየ። ንብርሃን ካብ ጸልማት ፈለዮ። ኣምላኽ ንብርሃን 'መዓልቲ' ንጸልማት ከኣ 'ለይቲ' ኢሉ ሰመዮ። እዚ ቐዳማይ መዓልቲ ፍጥረት ነበረ።",
        "moral_en": "God is powerful and creative. He made everything beautiful.",
        "moral_ti": "ኣምላኽ ሓያልን ፈጣርን እዩ። ኩሉ ነገር ጽቡቕ ገይሩ ፈጠሮ።",
        "illustration": "creation"
    },
    {
        "title_en": "God Creates Animals and People",
        "title_ti": "ኣምላኽ እንስሳታትን ሰባትን ይፈጥር",
        "verse": "Genesis 1:24-27",
        "story_en": "On the sixth day, God made all the animals - lions, birds, fish, and every creature. Then God said, 'Let us make people in our image.' So God created Adam from the dust of the ground and breathed life into him. God saw everything He had made, and it was very good!",
        "story_ti": "ኣብ ሻድሻይ መዓልቲ ኣምላኽ ኩሎም እንስሳታት ፈጠረ - ኣንበሳ፣ ኣዕዋፍ፣ ዓሳታትን ኩሉ ፍጡርን። ሽዑ ኣምላኽ 'ሰብ ብምስልና ንግበር' በለ። ስለዚ ኣምላኽ ንኣዳም ካብ ሓመድ ፈጠሮ ኣብ ኣፍንጫኡ ድማ ትንፋስ ህይወት ነፈሰሉ። ኣምላኽ ኩሉ ዝገበሮ ረኣየ፣ ኣዝዩ ጽቡቕ ድማ ነበረ!",
        "moral_en": "We are special because God made us in His image.",
        "moral_ti": "ንሕና ፍሉያት ኢና ከመይሲ ኣምላኽ ብምስሉ ፈጢሩና።",
        "illustration": "animals"
    },
    {
        "title_en": "The Garden of Eden",
        "title_ti": "ገነት ኤደን",
        "verse": "Genesis 2:8-9",
        "story_en": "God planted a beautiful garden in Eden for Adam and Eve. It had every kind of tree with delicious fruit. A river flowed through the garden. God told Adam and Eve to take care of the garden and enjoy everything in it. They were happy living with God.",
        "story_ti": "ኣምላኽ ንኣዳምን ሄዋንን ኣብ ኤደን ጽቡቕ ገነት ተኸለ። ኩሉ ዓይነት ኦም ምስ ጥዑም ፍረ ነበራ። ሓደ ወንዝ ብገነት ይውሕዝ ነበረ። ኣምላኽ ንኣዳምን ሄዋንን ንገነት ክሕልዉን ኩሉ ዘለዋ ክጥቀሙን ነገሮም። ምስ ኣምላኽ ብሓጐስ ይነብሩ ነበሩ።",
        "moral_en": "God gives us beautiful gifts and asks us to take care of them.",
        "moral_ti": "ኣምላኽ ጽቡቕ ህያባት ይህበናን ክንሕልዎም ይሓተናን።",
        "illustration": "garden"
    },
    {
        "title_en": "Noah and the Great Flood",
        "title_ti": "ኖህን እቲ ዓቢ ማይ ደልሃመትን",
        "verse": "Genesis 6:9-22",
        "story_en": "Noah was a good man who loved God. God told Noah to build a big boat called an ark because a great flood was coming. Noah obeyed God and built the ark. He brought two of every animal inside. Then rain fell for forty days and forty nights. But Noah and his family were safe inside the ark!",
        "story_ti": "ኖህ ንኣምላኽ ዝፈቱ ጽቡቕ ሰብ ነበረ። ኣምላኽ ንኖህ ዓቢ ማይ ደልሃመት ስለ ዝመጽእ ዓቢ መርከብ ክሰርሕ ነገሮ። ኖህ ንኣምላኽ ተኣዚዙ መርከብ ሰርሐ። ካብ ነፍሲ ወከፍ እንስሳ ክልተ ኣእተወ። ሽዑ ንኣርብዓ መዓልትን ኣርብዓ ለይትን ዝናብ ወረደ። ኖህን ስድራቤቱን ግን ኣብ ውሽጢ መርከብ ድሕንነት ነበሩ!",
        "moral_en": "When we obey God, He protects us.",
        "moral_ti": "ንኣምላኽ ክንእዘዝ ከለና ይሕልወና።",
        "illustration": "ark"
    },
    {
        "title_en": "The Tower of Babel",
        "title_ti": "ግምቢ ባቤል",
        "verse": "Genesis 11:1-9",
        "story_en": "After the flood, all people spoke one language. They decided to build a tower that would reach heaven to make themselves famous. God saw their pride and confused their language so they could not understand each other. The people scattered across the earth and the tower was never finished.",
        "story_ti": "ድሕሪ ማይ ደልሃመት ኩሎም ሰባት ሓደ ቋንቋ ይዛረቡ ነበሩ። ንነብሶም ክፍለጡ ሰማይ ዝበጽሕ ግምቢ ክሰርሑ ወሰኑ። ኣምላኽ ትዕቢቶም ረኣየ ቋንቋኦም ድማ ሓዋዀ ከም ዘይረዳድኡ ገበሮም። ሰባት ኣብ ምድሪ ተበተኑ ግምቢ ድማ ኣይተዛዘመን።",
        "moral_en": "Pride leads to problems. We should be humble before God.",
        "moral_ti": "ትዕቢት ናብ ጸገም የብጽሕ። ኣብ ቅድሚ ኣምላኽ ትሑታት ክንከውን ይግባእ።",
        "illustration": "tower"
    },
    {
        "title_en": "Abraham's Faith",
        "title_ti": "እምነት ኣብርሃም",
        "verse": "Genesis 12:1-4",
        "story_en": "God told Abraham to leave his home and go to a new land. God promised to make Abraham's family into a great nation and to bless all peoples through him. Abraham trusted God and obeyed, even though he did not know where he was going. God kept His promise!",
        "story_ti": "ኣምላኽ ንኣብርሃም ካብ ዓዱ ወጺኡ ናብ ሓዳሽ ምድሪ ክኸይድ ነገሮ። ኣምላኽ ንስድራ ኣብርሃም ዓባይ ህዝቢ ክገብሮምን ብኣኡ ንኩሎም ህዝብታት ክባርኾምን ተስፋ ሃቦ። ኣብርሃም ናበይ ከም ዝኸይድ ከይፈለጠ'ኳ ንኣምላኽ ኣሚኑ ተኣዘዘ። ኣምላኽ ድማ ቃሉ ፈጸመ!",
        "moral_en": "Faith means trusting God even when we don't understand everything.",
        "moral_ti": "እምነት ማለት ኩሉ ከይተረድኣና'ኳ ንኣምላኽ ምእማን እዩ።",
        "illustration": "abraham"
    },
    {
        "title_en": "Joseph and His Colorful Coat",
        "title_ti": "ዮሴፍን ሕብራዊ ክዳኑን",
        "verse": "Genesis 37:3-4",
        "story_en": "Jacob loved his son Joseph very much and gave him a beautiful coat of many colors. Joseph's brothers were jealous. They sold Joseph as a slave to Egypt. But God was with Joseph. He became a powerful leader in Egypt and later forgave his brothers and saved his whole family from hunger.",
        "story_ti": "ያዕቆብ ንወዱ ዮሴፍ ኣዝዩ ይፈትዎ ነበረ ጽቡቕ ሕብራዊ ክዳን ድማ ሃቦ። ኣሕዋት ዮሴፍ ቀኑ። ንዮሴፍ ከም ባርያ ናብ ግብጺ ሸጥዎ። ኣምላኽ ግን ምስ ዮሴፍ ነበረ። ኣብ ግብጺ ሓያል መራሒ ኰነ ድሕሪኡ ድማ ንኣሕዋቱ ይቕሬታ ገይሩሎም ንኩላ ስድራቤቱ ካብ ጥሜት ኣድሓነ።",
        "moral_en": "God can turn bad situations into something good.",
        "moral_ti": "ኣምላኽ ሕማቕ ኩነታት ናብ ጽቡቕ ክቕይሮ ይኽእል።",
        "illustration": "joseph"
    },
    {
        "title_en": "Baby Moses in the Basket",
        "title_ti": "ህጻን ሙሴ ኣብ ቅርጫት",
        "verse": "Exodus 2:1-10",
        "story_en": "When Moses was born, the king of Egypt wanted to hurt Hebrew babies. Moses' mother put him in a basket and placed it in the river to keep him safe. The king's daughter found baby Moses and raised him as her own son. God protected Moses for a special purpose!",
        "story_ti": "ሙሴ ምስ ተወልደ ንጉስ ግብጺ ንህጻናት ኢብራውያን ክጐድኦም ደለየ። ኣደ ሙሴ ኣብ ቅርጫት ኣቐሚጣ ኣብ ወንዝ ኣንበረቶ ክድሕን። ጓል ንጉስ ንህጻን ሙሴ ረኸበቶ ከም ወዳ ድማ ኣዕበየቶ። ኣምላኽ ንሙሴ ንፍሉይ ዕላማ ሓለዎ!",
        "moral_en": "God watches over us and has a plan for each of us.",
        "moral_ti": "ኣምላኽ ይሕልወናን ንነፍሲ ወከፍና ውጥን ኣለዎን።",
        "illustration": "moses_basket"
    },
    {
        "title_en": "Moses Parts the Red Sea",
        "title_ti": "ሙሴ ቀይሕ ባሕሪ ይፈልጥ",
        "verse": "Exodus 14:21-22",
        "story_en": "The Israelites were trapped between the Red Sea and the Egyptian army. Moses raised his staff and God parted the sea! The people walked through on dry ground with walls of water on both sides. When the Egyptians tried to follow, the waters closed back over them. God saved His people!",
        "story_ti": "እስራኤላውያን ኣብ መንጎ ቀይሕ ባሕርን ሰራዊት ግብጽን ተዓጽዉ። ሙሴ በትሩ ኣልዐለ ኣምላኽ ድማ ባሕሪ ፈለያ! ሰባት ብደረቕ ምድሪ ብመንጎ ኽልተ ቐጽሪ ማይ ሓለፉ። ግብጻውያን ክስዕቡ ምስ ፈተኑ ማያት ተመሊሱ ሸፈኖም። ኣምላኽ ንህዝቡ ኣድሓኖም!",
        "moral_en": "Nothing is impossible for God. He makes a way when there seems to be no way.",
        "moral_ti": "ንኣምላኽ ዘይከኣል ነገር የለን። መንገዲ ኣብ ዘይረኣየሉ ጊዜ መንገዲ ይገብር።",
        "illustration": "red_sea"
    },
    {
        "title_en": "The Ten Commandments",
        "title_ti": "ዓሰርተ ትእዛዛት",
        "verse": "Exodus 20:1-17",
        "story_en": "God called Moses to the top of Mount Sinai. There, God gave Moses ten important rules for living written on stone tablets. These commandments teach us to love God and love other people. They include: honor your father and mother, do not steal, do not lie, and love God above all.",
        "story_ti": "ኣምላኽ ንሙሴ ናብ ጫፍ ደብረ ሲና ጸውዖ። ኣብኡ ኣምላኽ ንሙሴ ዓሰርተ ኣገደስቲ ሕግታት ህይወት ኣብ ጽላት እምኒ ጽሒፉ ሃቦ። እዞም ትእዛዛት ንኣምላኽን ንኻልኦት ሰባትን ክንፈቱ ይምህሩና። ንኣቦኻን ኣደኻን ኣኽብር፣ ኣይትስረቕ፣ ኣይትሕሱ፣ ንኣምላኽ ልዕሊ ኩሉ ፍተዎ ዝብሉ የጠቓልሉ።",
        "moral_en": "God's rules help us live good and happy lives.",
        "moral_ti": "ሕግታት ኣምላኽ ጽቡቕን ሓጐሰኛን ህይወት ክንነብር ይሕግዙና።",
        "illustration": "commandments"
    },
]


BOOK_2_STORIES = [
    # Book 2: Heroes of Faith (Judges, Samuel, Kings)
    {
        "title_en": "David and Goliath",
        "title_ti": "ዳዊትን ጎልያድን",
        "verse": "1 Samuel 17:45-47",
        "story_en": "A giant warrior named Goliath challenged the army of Israel. Everyone was afraid except young David. With just a sling and five stones, David faced Goliath saying, 'I come in the name of the Lord!' David's stone hit Goliath and the giant fell. God gave David victory because David trusted Him.",
        "story_ti": "ጎልያድ ዝስሙ ዓቢ ተዋጋኢ ንሰራዊት እስራኤል ተጻብኣ። ካብ ንእሽቶ ዳዊት ወጻኢ ኩሎም ፈርሑ። ዳዊት ብመውገድን ሓሙሽተ እምንን ጥራይ ንጎልያድ ገጠመ 'ብስም እግዚኣብሄር እመጽእ ኣለኹ!' ክብል። እምኒ ዳዊት ንጎልያድ ወቒዑ እቲ ዓቢ ሰብ ወደቐ። ዳዊት ስለ ዝኣመኖ ኣምላኽ ዓወት ሃቦ።",
        "moral_en": "With God on our side, we can face any challenge.",
        "moral_ti": "ኣምላኽ ምሳና ክሳብ ዝሃለወ ኩሉ ብድሆ ክንገጥም ንኽእል።",
        "illustration": "david_goliath"
    },
    {
        "title_en": "Daniel in the Lions' Den",
        "title_ti": "ዳንኤል ኣብ ጒድጓድ ኣንበሳ",
        "verse": "Daniel 6:16-23",
        "story_en": "Daniel prayed to God three times every day. Jealous men made a law against praying. Daniel kept praying anyway! He was thrown into a den of hungry lions. But God sent an angel who shut the lions' mouths. In the morning, Daniel was safe! Not a scratch was on him.",
        "story_ti": "ዳንኤል ኣብ መዓልቲ ሰለስተ ግዜ ናብ ኣምላኽ ይጽሊ ነበረ። ቀናኣት ሰባት ጸሎት ዝኽልክል ሕጊ ኣውጽኡ። ዳንኤል ይጽሊ ቐጸለ! ናብ ጒድጓድ ጥሙያት ኣንበሳ ተደርበየ። ኣምላኽ ግን መልኣኽ ሰዲዱ ኣፍ ኣንበሳ ዓጸዎ። ብጽባሒቱ ዳንኤል ድሕን ነበረ! ሓንቲ ጒድኣት ኣይነበረቶን።",
        "moral_en": "Stay faithful to God even when it is hard.",
        "moral_ti": "ኣጸጋሚ ኣብ ዝኾነሉ ጊዜ'ውን ንኣምላኽ እሙን ኩን።",
        "illustration": "daniel_lions"
    },
    {
        "title_en": "Jonah and the Big Fish",
        "title_ti": "ዮናስን እቲ ዓቢ ዓሳን",
        "verse": "Jonah 1:17",
        "story_en": "God told Jonah to go to the city of Nineveh and tell the people to stop doing bad things. Jonah was scared and ran away on a ship. God sent a big storm and Jonah was swallowed by a huge fish! Inside the fish for three days, Jonah prayed. God made the fish spit Jonah out, and Jonah obeyed God.",
        "story_ti": "ኣምላኽ ንዮናስ ናብ ከተማ ነነዌ ከይዱ ንሰባት ሕማቕ ምግባር ክሓድጉ ክነግሮም ተዛረቦ። ዮናስ ፈሪሑ ብመርከብ ሃደመ። ኣምላኽ ዓቢ ማዕበል ሰደደ ዮናስ ድማ ብዓቢ ዓሳ ተውሕጠ! ኣብ ውሽጢ ዓሳ ንሰለስተ መዓልቲ ዮናስ ጸለየ። ኣምላኽ ዓሳ ንዮናስ ክትፍኦ ገበራ ዮናስ ድማ ንኣምላኽ ተኣዘዘ።",
        "moral_en": "We cannot run from God. It is better to obey Him right away.",
        "moral_ti": "ካብ ኣምላኽ ክንሃድም ኣይንኽእልን። ሽዑ ንሽዑ ምእዛዝ ይሓይሽ።",
        "illustration": "jonah"
    },
    {
        "title_en": "Queen Esther Saves Her People",
        "title_ti": "ንግስቲ ኣስቴር ንህዝባ ተድሕን",
        "verse": "Esther 4:14",
        "story_en": "Esther was a brave Jewish queen. An evil man planned to destroy all Jewish people. Esther's cousin Mordecai told her, 'Maybe God made you queen for such a time as this.' Esther bravely went to the king and revealed the evil plan. The king stopped it and the Jewish people were saved!",
        "story_ti": "ኣስቴር ጅግና ኣይሁዳዊት ንግስቲ ነበረት። ሓደ ኽፉእ ሰብ ንኹሎም ኣይሁድ ከጥፍእ ሓሰበ። ሞርዶኬ ዘመዳ 'ምናልባት ኣምላኽ ከምዚ ንዝበለ ጊዜ ኢሉ ንግስቲ ገይሩኪ ይኸውን' በላ። ኣስቴር ብትብዓት ናብ ንጉስ ከይዳ ነቲ ኽፉእ ውጥን ገለጸት። ንጉስ ደው ኣበሎ ኣይሁድ ድማ ደሓኑ!",
        "moral_en": "God puts us in the right place at the right time to help others.",
        "moral_ti": "ኣምላኽ ንኻልኦት ንምሕጋዝ ኣብ ቅኑዕ ቦታ ኣብ ቅኑዕ ጊዜ የቐምጠና።",
        "illustration": "esther"
    },
    {
        "title_en": "Samson the Strong Man",
        "title_ti": "ሳምሶን ሓያል ሰብ",
        "verse": "Judges 16:28-30",
        "story_en": "God gave Samson amazing strength. He could defeat armies and tear apart lions. But Samson was not always wise with his gift. He forgot that his strength came from God. When Samson finally remembered God and prayed, God gave him strength one last time to defeat the enemies of Israel.",
        "story_ti": "ኣምላኽ ንሳምሶን ኣደናቒ ሓይሊ ሃቦ። ሰራዊት ክስዕርን ኣንበሳ ክቐድድን ይኽእል ነበረ። ሳምሶን ግን ኩሉ ጊዜ ብህያቡ ጥበበኛ ኣይነበረን። ሓይሉ ካብ ኣምላኽ ምዃኑ ረሰዐ። ሳምሶን ንኣምላኽ ዘኪሩ ምስ ጸለየ ኣምላኽ ንመወዳእታ ጊዜ ንጸላእቲ እስራኤል ዝስዕረሉ ሓይሊ ሃቦ።",
        "moral_en": "Our gifts come from God. We should use them wisely for His glory.",
        "moral_ti": "ህያባትና ካብ ኣምላኽ እዮም። ንኽብሩ ብጥበብ ክንጥቀመሎም ይግባእ።",
        "illustration": "samson"
    },
]


BOOK_3_STORIES = [
    # Book 3: Life of Jesus (New Testament)
    {
        "title_en": "The Birth of Jesus",
        "title_ti": "ልደት ኢየሱስ",
        "verse": "Luke 2:7-14",
        "story_en": "Mary and Joseph traveled to Bethlehem. There was no room for them at the inn, so baby Jesus was born in a stable and laid in a manger. Angels appeared to shepherds saying, 'Good news! A Savior is born today!' The shepherds hurried to see baby Jesus and praised God.",
        "story_ti": "ማርያምን ዮሴፍን ናብ ቤትልሔም ተጓዕዙ። ኣብ ማሕደር ቦታ ስለ ዘይነበረ ህጻን ኢየሱስ ኣብ ከብቲ ተወልደ ኣብ መብልዕ ድማ ተቐምጠ። መላእኽቲ ንጓሶት ተራእዮም 'ጽቡቕ ዜና! ሎሚ መድሓኒ ተወልደ!' በሉ። ጓሶት ንህጻን ኢየሱስ ክርእዩ ተቐላጠፉ ንኣምላኽ ድማ ኣመስገኑ።",
        "moral_en": "Jesus came to earth as a gift of love for all people.",
        "moral_ti": "ኢየሱስ ንኹሎም ሰባት ከም ህያብ ፍቕሪ ናብ ምድሪ መጸ።",
        "illustration": "nativity"
    },
    {
        "title_en": "Jesus Calms the Storm",
        "title_ti": "ኢየሱስ ማዕበል የህድእ",
        "verse": "Mark 4:37-39",
        "story_en": "Jesus and His disciples were in a boat when a terrible storm came. The disciples were very afraid. But Jesus was sleeping peacefully! They woke Him up saying, 'Don't you care if we drown?' Jesus stood up and said to the storm, 'Peace, be still!' The storm stopped immediately.",
        "story_ti": "ኢየሱስን ደቀ መዛሙርቱን ኣብ ጃልባ ከለዉ ዘፍርሕ ማዕበል መጸ። ደቀ መዛሙርቱ ኣዝዮም ፈርሑ። ኢየሱስ ግን ብሰላም ደቂሱ ነበረ! ኣተንሲኦም 'ክንጥሕል ኣየገድሰካን ድዩ?' በሉ። ኢየሱስ ተንሲኡ ንማዕበል 'ስቕ ህድኡ!' በላ። ማዕበል ሽዑ ንሽዑ ደው በለ።",
        "moral_en": "Jesus has power over everything. We don't need to be afraid.",
        "moral_ti": "ኢየሱስ ኣብ ልዕሊ ኩሉ ስልጣን ኣለዎ። ክንፈርሕ ኣየድልየናን።",
        "illustration": "storm"
    },
    {
        "title_en": "Jesus Feeds 5000 People",
        "title_ti": "ኢየሱስ 5000 ሰባት ይምግብ",
        "verse": "John 6:9-13",
        "story_en": "A huge crowd followed Jesus. They were hungry but there was no food except one boy's lunch - five small loaves of bread and two fish. Jesus blessed the food and began sharing it. Miraculously, everyone ate until they were full, and there were twelve baskets of leftovers!",
        "story_ti": "ብዙሕ ህዝቢ ንኢየሱስ ሰዓበ። ጠምዮም ነበሩ ግን ካብ ቀረብ ሓደ ቆልዓ - ሓሙሽተ ንኡሽተይ ባንን ክልተ ዓሳን - ካልእ ምግቢ ኣይነበረን። ኢየሱስ ንምግቢ ባሪኹ ከማቕል ጀመረ። ብተኣምር ኩሎም ክሳብ ዝጸግቡ በልዑ ዓሰርተ ክልተ ቅርጫት ተረፍ ድማ ነበረ!",
        "moral_en": "When we give what we have to Jesus, He can do amazing things.",
        "moral_ti": "ዘሎና ንኢየሱስ ክንህብ ከለና ኣደናቒ ነገራት ክገብር ይኽእል።",
        "illustration": "feeding"
    },
    {
        "title_en": "The Good Samaritan",
        "title_ti": "እቲ ሕያዋይ ሳምራዊ",
        "verse": "Luke 10:30-37",
        "story_en": "Jesus told a story about a man who was attacked by robbers and left hurt on the road. Two religious men walked by without helping. But a Samaritan man stopped, bandaged his wounds, and took care of him. Jesus said, 'Go and be like the Samaritan - help everyone who needs help.'",
        "story_ti": "ኢየሱስ ብሰረቕቲ ተወቒዑ ኣብ መንገዲ ዝተሓድገ ሰብ ዛንታ ነገረ። ክልተ ሃይማኖተኛታት ከይሓገዙ ሓለፉ። ሓደ ሳምራዊ ሰብ ግን ደው ኢሉ ቁስሉ ኣሰረ ተኸናኸኖ ድማ። ኢየሱስ 'ከምቲ ሳምራዊ ኩን - ሓገዝ ንዘድልዮ ኩሉ ሓግዝ' በለ።",
        "moral_en": "Love your neighbor and help anyone in need.",
        "moral_ti": "ንብጻይካ ፍተዎ ሓገዝ ንዘድልዮ ኩሉ ሓግዝ።",
        "illustration": "samaritan"
    },
    {
        "title_en": "Jesus Loves the Children",
        "title_ti": "ኢየሱስ ንቈልዑ ይፈትዎም",
        "verse": "Mark 10:13-16",
        "story_en": "People brought their children to Jesus for a blessing. The disciples tried to send them away. But Jesus said, 'Let the little children come to me! Don't stop them! The kingdom of God belongs to those who are like these children.' Jesus hugged the children and blessed them.",
        "story_ti": "ሰባት ንቈልዑኦም ኢየሱስ ክባርኾም ኣምጽእዎም። ደቀ መዛሙርቲ ክሰዱዎም ፈተኑ። ኢየሱስ ግን 'ንቈልዑ ናባይ ክመጽኡ ሕደጉዎም! ኣይትኸልክሉዎም! መንግስቲ ኣምላኽ ከምዞም ቈልዑ ንዝኾኑ እያ' በለ። ኢየሱስ ንቈልዑ ሓቚፉ ባረኾም።",
        "moral_en": "Jesus loves children. Everyone is important to God.",
        "moral_ti": "ኢየሱስ ንቈልዑ ይፈትዎም። ኩሉ ሰብ ኣብ ቅድሚ ኣምላኽ ኣገዳሲ እዩ።",
        "illustration": "jesus_children"
    },
    {
        "title_en": "The Lost Sheep",
        "title_ti": "እታ ዝጠፍአት በጊዕ",
        "verse": "Luke 15:3-7",
        "story_en": "Jesus told this story: A shepherd had 100 sheep. One sheep got lost. The shepherd left the 99 safe sheep and searched everywhere for the lost one. When he found it, he was so happy! He carried it home on his shoulders. Jesus said, 'God rejoices like this when one lost person comes back to Him.'",
        "story_ti": "ኢየሱስ ከምዚ ዛንታ ነገረ፡ ሓደ ጓሳ 100 ኣባጊዕ ነበሮ። ሓንቲ በጊዕ ጠፍአት። ጓሳ ነተን 99 ድሕንቲ ሓዲጉ ነታ ዝጠፍአት ኣብ ኩሉ ቦታ ደለያ። ምስ ረኸባ ኣዝዩ ተሓጐሰ! ኣብ መንኵቡ ጸዊሩ ገዝኡ ተመልሰ። ኢየሱስ 'ሓደ ዝጠፍአ ሰብ ናብ ኣምላኽ ክምለስ ከሎ ኣምላኽ ከምዚ ይሕጐስ' በለ።",
        "moral_en": "God loves each one of us and never gives up looking for us.",
        "moral_ti": "ኣምላኽ ንነፍሲ ወከፍና ይፈትወናን ክደልየና ፈጺሙ ኣይሓድግን።",
        "illustration": "lost_sheep"
    },
    {
        "title_en": "Jesus Walks on Water",
        "title_ti": "ኢየሱስ ኣብ ልዕሊ ማይ ይኸይድ",
        "verse": "Matthew 14:25-31",
        "story_en": "The disciples were in a boat at night when they saw Jesus walking on the water! Peter said, 'Lord, if it is you, tell me to come.' Jesus said, 'Come!' Peter walked on water toward Jesus! But when he looked at the waves, he was afraid and started to sink. Jesus caught him and said, 'Why did you doubt?'",
        "story_ti": "ደቀ መዛሙርቲ ብለይቲ ኣብ ጃልባ ከለዉ ኢየሱስ ኣብ ልዕሊ ማይ ክኸይድ ረኣዩ! ጴጥሮስ 'ጐይታ ንስኻ እንተ ኴንካ ክመጽእ ንገረኒ' በለ። ኢየሱስ 'ንዓ!' በለ። ጴጥሮስ ኣብ ልዕሊ ማይ ናብ ኢየሱስ ከደ! ግን ነቲ ማዕበል ምስ ረኣየ ፈሪሑ ክጥሕል ጀመረ። ኢየሱስ ሒዙ 'ስለምንታይ ተጠራጢርካ?' በሎ።",
        "moral_en": "Keep your eyes on Jesus and trust Him, not your fears.",
        "moral_ti": "ኣዒንትኻ ኣብ ኢየሱስ ኣንብር ንፍርሕኻ ዘይኮነ ንእኡ ኣምን።",
        "illustration": "walking_water"
    },
    {
        "title_en": "Jesus Dies and Rises Again",
        "title_ti": "ኢየሱስ ይመውትን ይትንስእን",
        "verse": "Luke 24:1-6",
        "story_en": "Jesus died on the cross to save us from our sins. His friends were very sad and placed His body in a tomb. But on the third day, something amazing happened! The tomb was empty! An angel said, 'He is not here! He is risen!' Jesus was alive again! This is the best news ever!",
        "story_ti": "ኢየሱስ ካብ ሓጢኣትና ከድሕነና ኣብ መስቀል ሞተ። ኣዕሩኹ ኣዝዮም ሓዘኑ ስርዓቱ ኣብ መቓብር ኣቐምጡ። ግን ኣብ ሳልሳይ መዓልቲ ኣደናቒ ነገር ኰነ! መቓብር ጥራያ ነበረት! መልኣኽ 'ኣብዚ የለን! ተንሲኡ!' በለ። ኢየሱስ ከም ብሓዲሽ ህያው ነበረ! እዚ ኩሉ ጊዜ ዝበለጸ ዜና እዩ!",
        "moral_en": "Jesus conquered death and gives us eternal life.",
        "moral_ti": "ኢየሱስ ንሞት ሰዐረ ዘልኣለማዊ ህይወት ድማ ይህበና።",
        "illustration": "resurrection"
    },
]



BOOK_4_STORIES = [
    # Book 4: Teachings of Jesus (Parables & Lessons)
    {
        "title_en": "The Prodigal Son",
        "title_ti": "እቲ ጥፉእ ወዲ",
        "verse": "Luke 15:11-32",
        "story_en": "A young son asked his father for his share of money and left home. He wasted everything on foolish living. When he had nothing left, he decided to go home and say sorry. His father saw him coming and ran to hug him with great joy! The father celebrated because his lost son had come home.",
        "story_ti": "ሓደ ንእሽቶ ወዲ ንኣቦኡ ግደ ገንዘቡ ሓቲቱ ካብ ገዛ ወጸ። ኩሉ ብዘይጠቕም ህይወት ኣባኸኖ። ሓንቲ ምስ ዘይተረፈቶ ገዝኡ ክምለስን ይቕረታ ክሓትትን ወሰነ። ኣቦኡ ክመጽእ ከሎ ረኣዮ ብዓቢ ሓጐስ ክሓቁፎ ጐየየ! ኣቦ ጥፉእ ወዱ ስለ ዝተመልሰ ብዓል ገበረ።",
        "moral_en": "God always welcomes us back when we are sorry.",
        "moral_ti": "ኣምላኽ ምስ ንጣዓስ ኩሉ ጊዜ ብሓጐስ ይቕበለና።",
        "illustration": "prodigal"
    },
    {
        "title_en": "The Mustard Seed",
        "title_ti": "ፍረ ኣድሪ",
        "verse": "Matthew 13:31-32",
        "story_en": "Jesus said the kingdom of God is like a tiny mustard seed. It is the smallest of all seeds, but when it is planted and grows, it becomes the biggest plant in the garden. Birds come and rest in its branches. Even small faith can grow into something wonderful!",
        "story_ti": "ኢየሱስ መንግስቲ ኣምላኽ ከም ንእሽቶ ፍረ ኣድሪ እያ በለ። ካብ ኩለን ዘርኢ ዝነኣሰት እያ ግን ምስ ተተኽለትን ዓበየትን ኣብ ገነት ዝዓበየት ተኽሊ ትኸውን። ኣዕዋፍ መጺኦም ኣብ ጨናፍራ ይዕረፉ። ንእሽቶ እምነት'ውን ናብ ኣደናቒ ነገር ክዓቢ ይኽእል!",
        "moral_en": "Small beginnings can lead to great things with God.",
        "moral_ti": "ንእሽቶ መጀመርታ ምስ ኣምላኽ ናብ ዓቢ ነገር ከብጽሕ ይኽእል።",
        "illustration": "mustard_seed"
    },

    {
        "title_en": "The Wise and Foolish Builders",
        "title_ti": "ጥበበኛን ዓሻን ሃነጽቲ",
        "verse": "Matthew 7:24-27",
        "story_en": "Jesus said whoever hears His words and obeys them is like a wise man who built his house on rock. When storms came, the house stood strong. But whoever hears and does not obey is like a foolish man who built on sand. When storms came, that house fell down with a crash!",
        "story_ti": "ኢየሱስ ቃላቱ ሰሚዑ ዝእዘዝ ከም ጥበበኛ ሰብ ገዛኡ ኣብ ከውሒ ዝሰርሐ እዩ በለ። ማዕበል ምስ መጸ ገዛ ጸኒዑ ቐወመ። ሰሚዑ ዘይእዘዝ ግን ከም ዓሻ ሰብ ኣብ ሑጻ ዝሃነጸ እዩ። ማዕበል ምስ መጸ እቲ ገዛ ፈሪሱ ወደቐ!",
        "moral_en": "Build your life on God's Word and you will stand strong.",
        "moral_ti": "ህይወትካ ኣብ ቃል ኣምላኽ ስረት ጸኒዕካ ድማ ክትቅውም ኢኻ።",
        "illustration": "builders"
    },
    {
        "title_en": "Zacchaeus the Tax Collector",
        "title_ti": "ዘኬዎስ ተቐባል ቀረጽ",
        "verse": "Luke 19:1-10",
        "story_en": "Zacchaeus was a short man who collected taxes and cheated people. He wanted to see Jesus but could not see over the crowd. So he climbed a tree! Jesus looked up and said, 'Zacchaeus, come down! I want to visit your house today.' Zacchaeus was so happy he promised to give back everything he stole.",
        "story_ti": "ዘኬዎስ ቀረጽ ዝእክብ ሓጺር ሰብ ነበረ ንሰባት ድማ ይጠብር ነበረ። ንኢየሱስ ክርኢ ደለየ ግን ብልዕሊ ህዝቢ ክርኢ ኣይከኣለን። ስለዚ ኦም ደየበ! ኢየሱስ ንላዕሊ ጠሚቱ 'ዘኬዎስ ውረድ! ሎሚ ገዛኻ ክበጽሕ ይደሊ' በለ። ዘኬዎስ ኣዝዩ ተሓጒሱ ዝሰረቖ ኩሉ ክመልስ ተስፋ ሃበ።",
        "moral_en": "Jesus can change anyone's heart for the better.",
        "moral_ti": "ኢየሱስ ልቢ ዝኾነ ሰብ ናብ ጽቡቕ ክቕይር ይኽእል።",
        "illustration": "zacchaeus"
    },

    {
        "title_en": "Jesus Heals a Blind Man",
        "title_ti": "ኢየሱስ ዓይነ ስዉር የሕዊ",
        "verse": "John 9:1-7",
        "story_en": "Jesus saw a man who had been blind since birth. Jesus made mud with dirt and put it on the man's eyes. He told him to go wash in the pool. The man obeyed and washed his eyes. When he opened them, he could see for the first time in his life! Everyone was amazed.",
        "story_ti": "ኢየሱስ ካብ ልደቱ ዓይነ ስዉር ዝነበረ ሰብ ረኣየ። ኢየሱስ ካብ ሓመድ ጭቃ ገይሩ ኣብ ኣዒንቱ ለኸዮ። ኣብ ሓጽቢ ከይዱ ክሕጸብ ነገሮ። እቲ ሰብ ተኣዚዙ ኣዒንቱ ሓጸበ። ምስ ከፈተን ንመጀመርታ ጊዜ ኣብ ህይወቱ ክርኢ ከኣለ! ኩሎም ተገረሙ።",
        "moral_en": "Jesus has power to heal and do miracles in our lives.",
        "moral_ti": "ኢየሱስ ኣብ ህይወትና ከሕውን ተኣምር ክገብርን ስልጣን ኣለዎ።",
        "illustration": "healing"
    },
    {
        "title_en": "The Parable of the Talents",
        "title_ti": "ምሳሌ ታለንት",
        "verse": "Matthew 25:14-30",
        "story_en": "A master gave three servants different amounts of money called talents. Two servants worked hard and doubled their money. The third buried his in the ground out of fear. The master praised the hard workers saying, 'Well done, good and faithful servants!' But he was disappointed with the lazy one.",
        "story_ti": "ሓደ ጐይታ ንሰለስተ ኣገልገልቲ ዝተፈላለየ መጠን ገንዘብ ታለንት ሃቦም። ክልተ ኣገልገልቲ ጽዒሮም ገንዘቦም ኣርብዑ። ሳልሳዩ ብፍርሒ ኣብ ምድሪ ቀብሮ። ጐይታ ንጻዕረኛታት 'ጽቡቕ ሕያዋይን ኣሙንን ኣገልገልቲ!' ኢሉ ወደሰ። ብሃካይ ግን ሓዘነሉ።",
        "moral_en": "Use the gifts God gives you wisely and don't be afraid to try.",
        "moral_ti": "ኣምላኽ ዝሃበካ ህያባት ብጥበብ ተጠቐም ክትፍትን ድማ ኣይትፍራሕ።",
        "illustration": "talents"
    },

    {
        "title_en": "Love Your Enemies",
        "title_ti": "ንጸላእትኻ ፍተዎም",
        "verse": "Matthew 5:44-45",
        "story_en": "Jesus taught something surprising. He said, 'Love your enemies and pray for those who are mean to you.' This is hard to do, but Jesus said it makes us like God our Father, who sends sunshine and rain to everyone - good people and bad people alike. Love is always stronger than hate.",
        "story_ti": "ኢየሱስ ዘገርም ነገር ኣምሀረ። 'ንጸላእትኹም ፍተዉዎም ንዝጐድኡኹም ድማ ጸልዩሎም' በለ። እዚ ክትገብሮ ኣጸጋሚ እዩ ግን ኢየሱስ ከም ኣቦና ኣምላኽ ይገብረና በለ ንሱ ንጽቡቓትን ሕማቓትን ብማዕረ ጸሓይን ዝናብን ይሰድድ። ፍቕሪ ኩሉ ጊዜ ካብ ጽልኢ ይሕይል።",
        "moral_en": "Loving others, even enemies, shows God's love in us.",
        "moral_ti": "ንኻልኦት ንጸላእቲ'ውን ምፍታው ፍቕሪ ኣምላኽ ኣባና ምህላዉ የርኢ።",
        "illustration": "love_enemies"
    },
    {
        "title_en": "The Lord's Prayer",
        "title_ti": "ጸሎት ጐይታ",
        "verse": "Matthew 6:9-13",
        "story_en": "The disciples asked Jesus how to pray. Jesus taught them a special prayer: 'Our Father in heaven, holy is your name. Your kingdom come. Give us today our daily bread. Forgive us as we forgive others. Lead us not into temptation but deliver us from evil.' This prayer teaches us to talk to God every day.",
        "story_ti": "ደቀ መዛሙርቲ ንኢየሱስ ከመይ ከም ዝጽልዩ ሓተቱ። ኢየሱስ ፍሉይ ጸሎት ኣምሀሮም፡ 'ኣቦና ኣብ ሰማይ ዘሎኻ ስምካ ይቀደስ። መንግስትኻ ትምጻእ። ናይ ሎሚ እንጌራና ሎሚ ሃበና። ንኻልኦት ከም ዝሓደግናሎም ሓጢኣትና ሕደገልና። ናብ ፈተና ኣይተእትወና ካብ ኽፉእ ግን ኣድሕነና።' እዚ ጸሎት ኣብ ነፍሲ ወከፍ መዓልቲ ምስ ኣምላኽ ክንዛረብ ይምህረና።",
        "moral_en": "Prayer is talking to God. He always listens to us.",
        "moral_ti": "ጸሎት ምስ ኣምላኽ ምዝራብ እዩ። ንሱ ኩሉ ጊዜ ይሰምዓና።",
        "illustration": "prayer"
    },
]



# ============================================================
# SVG ILLUSTRATION FUNCTIONS
# Each function takes (cx, cy, s=1.0) center x, center y, scale
# Returns SVG elements as a string
# ============================================================


def draw_creation_scene(cx, cy, s=1.0):
    """Sun, moon, stars, earth, plants."""
    return f'''
    <circle cx="{cx - 80*s}" cy="{cy - 40*s}" r="{30*s}" fill="#FFD700" stroke="#FFA500" stroke-width="2"/>
    <line x1="{cx - 80*s}" y1="{cy - 75*s}" x2="{cx - 80*s}" y2="{cy - 85*s}" stroke="#FFA500" stroke-width="2"/>
    <line x1="{cx - 115*s}" y1="{cy - 40*s}" x2="{cx - 125*s}" y2="{cy - 40*s}" stroke="#FFA500" stroke-width="2"/>
    <line x1="{cx - 45*s}" y1="{cy - 40*s}" x2="{cx - 35*s}" y2="{cy - 40*s}" stroke="#FFA500" stroke-width="2"/>
    <circle cx="{cx + 80*s}" cy="{cy - 40*s}" r="{22*s}" fill="#F0E68C"/>
    <circle cx="{cx + 88*s}" cy="{cy - 48*s}" r="{18*s}" fill="#1a1a2e"/>
    <circle cx="{cx + 40*s}" cy="{cy - 60*s}" r="{3*s}" fill="#FFFFFF"/>
    <circle cx="{cx + 60*s}" cy="{cy - 70*s}" r="{2*s}" fill="#FFFFFF"/>
    <circle cx="{cx + 20*s}" cy="{cy - 75*s}" r="{2.5*s}" fill="#FFFFFF"/>
    <circle cx="{cx}" cy="{cy + 20*s}" r="{40*s}" fill="#4169E1"/>
    <ellipse cx="{cx - 10*s}" cy="{cy + 15*s}" rx="{20*s}" ry="{15*s}" fill="#228B22"/>
    <ellipse cx="{cx + 15*s}" cy="{cy + 25*s}" rx="{15*s}" ry="{10*s}" fill="#228B22"/>
    <line x1="{cx - 60*s}" y1="{cy + 60*s}" x2="{cx - 60*s}" y2="{cy + 30*s}" stroke="#8B4513" stroke-width="{3*s}"/>
    <circle cx="{cx - 60*s}" cy="{cy + 25*s}" r="{12*s}" fill="#32CD32"/>
    <line x1="{cx + 60*s}" y1="{cy + 60*s}" x2="{cx + 60*s}" y2="{cy + 35*s}" stroke="#8B4513" stroke-width="{3*s}"/>
    <circle cx="{cx + 60*s}" cy="{cy + 30*s}" r="{10*s}" fill="#228B22"/>
    '''



def draw_ark_scene(cx, cy, s=1.0):
    """Noah's ark boat on water with rainbow."""
    return f'''
    <path d="M{cx-70*s},{cy+10*s} Q{cx},{cy+40*s} {cx+70*s},{cy+10*s} L{cx+60*s},{cy-10*s} L{cx-60*s},{cy-10*s} Z" fill="#8B4513" stroke="#5C3317" stroke-width="2"/>
    <rect x="{cx-40*s}" y="{cy-35*s}" width="{80*s}" height="{25*s}" fill="#A0522D" stroke="#5C3317" stroke-width="1"/>
    <polygon points="{cx-45*s},{cy-35*s} {cx},{cy-55*s} {cx+45*s},{cy-35*s}" fill="#D2691E" stroke="#5C3317" stroke-width="1"/>
    <rect x="{cx-10*s}" y="{cy-30*s}" width="{20*s}" height="{15*s}" fill="#FFD700" stroke="#5C3317" stroke-width="1"/>
    <path d="M{cx-80*s},{cy+30*s} Q{cx-40*s},{cy+20*s} {cx},{cy+30*s} Q{cx+40*s},{cy+40*s} {cx+80*s},{cy+30*s}" fill="none" stroke="#4169E1" stroke-width="3"/>
    <path d="M{cx-90*s},{cy+40*s} Q{cx-45*s},{cy+30*s} {cx},{cy+40*s} Q{cx+45*s},{cy+50*s} {cx+90*s},{cy+40*s}" fill="none" stroke="#1E90FF" stroke-width="2"/>
    <path d="M{cx-60*s},{cy-50*s} A{60*s},{60*s} 0 0,1 {cx+60*s},{cy-50*s}" fill="none" stroke="red" stroke-width="3" opacity="0.7"/>
    <path d="M{cx-55*s},{cy-45*s} A{55*s},{55*s} 0 0,1 {cx+55*s},{cy-45*s}" fill="none" stroke="orange" stroke-width="3" opacity="0.7"/>
    <path d="M{cx-50*s},{cy-40*s} A{50*s},{50*s} 0 0,1 {cx+50*s},{cy-40*s}" fill="none" stroke="#FFD700" stroke-width="3" opacity="0.7"/>
    <path d="M{cx-45*s},{cy-35*s} A{45*s},{45*s} 0 0,1 {cx+45*s},{cy-35*s}" fill="none" stroke="green" stroke-width="3" opacity="0.5"/>
    '''



def draw_david_goliath(cx, cy, s=1.0):
    """Small boy with sling vs big person."""
    return f'''
    <circle cx="{cx-50*s}" cy="{cy-20*s}" r="{10*s}" fill="#FDBCB4"/>
    <rect x="{cx-55*s}" y="{cy-10*s}" width="{10*s}" height="{25*s}" fill="#4682B4"/>
    <line x1="{cx-50*s}" y1="{cy+15*s}" x2="{cx-55*s}" y2="{cy+35*s}" stroke="#4682B4" stroke-width="3"/>
    <line x1="{cx-50*s}" y1="{cy+15*s}" x2="{cx-45*s}" y2="{cy+35*s}" stroke="#4682B4" stroke-width="3"/>
    <line x1="{cx-45*s}" y1="{cy-5*s}" x2="{cx-30*s}" y2="{cy-15*s}" stroke="#FDBCB4" stroke-width="2"/>
    <path d="M{cx-30*s},{cy-15*s} Q{cx-25*s},{cy-25*s} {cx-20*s},{cy-15*s}" fill="none" stroke="#8B4513" stroke-width="2"/>
    <circle cx="{cx+50*s}" cy="{cy-40*s}" r="{18*s}" fill="#FDBCB4"/>
    <rect x="{cx+40*s}" y="{cy-22*s}" width="{20*s}" height="{40*s}" fill="#8B0000"/>
    <line x1="{cx+50*s}" y1="{cy+18*s}" x2="{cx+45*s}" y2="{cy+45*s}" stroke="#8B0000" stroke-width="4"/>
    <line x1="{cx+50*s}" y1="{cy+18*s}" x2="{cx+55*s}" y2="{cy+45*s}" stroke="#8B0000" stroke-width="4"/>
    <rect x="{cx+35*s}" y="{cy-42*s}" width="{30*s}" height="{8*s}" fill="#808080"/>
    <line x1="{cx+60*s}" y1="{cy-22*s}" x2="{cx+75*s}" y2="{cy}" stroke="#FDBCB4" stroke-width="3"/>
    <rect x="{cx+72*s}" y="{cy-5*s}" width="{5*s}" height="{30*s}" fill="#808080"/>
    '''


def draw_nativity(cx, cy, s=1.0):
    """Stable with star, manger."""
    return f'''
    <polygon points="{cx},{cy-60*s} {cx-70*s},{cy-10*s} {cx+70*s},{cy-10*s}" fill="#8B4513" opacity="0.6"/>
    <line x1="{cx-70*s}" y1="{cy-10*s}" x2="{cx-70*s}" y2="{cy+40*s}" stroke="#8B4513" stroke-width="4"/>
    <line x1="{cx+70*s}" y1="{cy-10*s}" x2="{cx+70*s}" y2="{cy+40*s}" stroke="#8B4513" stroke-width="4"/>
    <polygon points="{cx},{cy-80*s} {cx-5*s},{cy-65*s} {cx+5*s},{cy-65*s}" fill="#FFD700"/>
    <polygon points="{cx},{cy-80*s} {cx-3*s},{cy-62*s} {cx+3*s},{cy-62*s} {cx+8*s},{cy-68*s} {cx-8*s},{cy-68*s}" fill="#FFD700"/>
    <circle cx="{cx}" cy="{cy-72*s}" r="{6*s}" fill="#FFD700" opacity="0.5"/>
    <rect x="{cx-20*s}" y="{cy+10*s}" width="{40*s}" height="{20*s}" fill="#DAA520" stroke="#8B4513" stroke-width="2"/>
    <ellipse cx="{cx}" cy="{cy+10*s}" rx="{12*s}" ry="{8*s}" fill="#FFFACD"/>
    <circle cx="{cx}" cy="{cy+5*s}" r="{5*s}" fill="#FDBCB4"/>
    <rect x="{cx-40*s}" y="{cy+30*s}" width="{80*s}" height="{10*s}" fill="#DAA520" opacity="0.5"/>
    '''



def draw_cross_scene(cx, cy, s=1.0):
    """Three crosses on hill with sunrise."""
    return f'''
    <ellipse cx="{cx}" cy="{cy+40*s}" rx="{90*s}" ry="{25*s}" fill="#8B7355"/>
    <circle cx="{cx}" cy="{cy+40*s}" r="{60*s}" fill="#FFD700" opacity="0.2"/>
    <circle cx="{cx}" cy="{cy+40*s}" r="{45*s}" fill="#FFA500" opacity="0.15"/>
    <rect x="{cx-4*s}" y="{cy-50*s}" width="{8*s}" height="{70*s}" fill="#5C3317"/>
    <rect x="{cx-20*s}" y="{cy-35*s}" width="{40*s}" height="{8*s}" fill="#5C3317"/>
    <rect x="{cx-50*s-3*s}" y="{cy-30*s}" width="{6*s}" height="{50*s}" fill="#5C3317"/>
    <rect x="{cx-50*s-15*s}" y="{cy-18*s}" width="{30*s}" height="{6*s}" fill="#5C3317"/>
    <rect x="{cx+50*s-3*s}" y="{cy-30*s}" width="{6*s}" height="{50*s}" fill="#5C3317"/>
    <rect x="{cx+50*s-15*s}" y="{cy-18*s}" width="{30*s}" height="{6*s}" fill="#5C3317"/>
    <line x1="{cx-80*s}" y1="{cy+50*s}" x2="{cx+80*s}" y2="{cy+50*s}" stroke="#8B7355" stroke-width="2"/>
    '''


def draw_praying_hands(cx, cy, s=1.0):
    """Hands together in prayer."""
    return f'''
    <ellipse cx="{cx}" cy="{cy}" rx="{40*s}" ry="{50*s}" fill="#FFD700" opacity="0.15"/>
    <path d="M{cx},{cy-40*s} L{cx-15*s},{cy+10*s} L{cx-12*s},{cy+15*s} L{cx-8*s},{cy+10*s} L{cx-5*s},{cy+15*s} L{cx-2*s},{cy+10*s} L{cx},{cy+20*s}" fill="#FDBCB4" stroke="#D2996B" stroke-width="1.5"/>
    <path d="M{cx},{cy-40*s} L{cx+15*s},{cy+10*s} L{cx+12*s},{cy+15*s} L{cx+8*s},{cy+10*s} L{cx+5*s},{cy+15*s} L{cx+2*s},{cy+10*s} L{cx},{cy+20*s}" fill="#FDBCB4" stroke="#D2996B" stroke-width="1.5"/>
    <line x1="{cx}" y1="{cy+20*s}" x2="{cx-8*s}" y2="{cy+40*s}" stroke="#D2996B" stroke-width="2"/>
    <line x1="{cx}" y1="{cy+20*s}" x2="{cx+8*s}" y2="{cy+40*s}" stroke="#D2996B" stroke-width="2"/>
    <circle cx="{cx-20*s}" cy="{cy-30*s}" r="{3*s}" fill="#FFD700" opacity="0.6"/>
    <circle cx="{cx+20*s}" cy="{cy-35*s}" r="{2*s}" fill="#FFD700" opacity="0.6"/>
    <circle cx="{cx+25*s}" cy="{cy-20*s}" r="{2.5*s}" fill="#FFD700" opacity="0.6"/>
    '''



def draw_fish_loaves(cx, cy, s=1.0):
    """Basket with fish and bread."""
    return f'''
    <path d="M{cx-40*s},{cy+10*s} Q{cx-45*s},{cy+40*s} {cx},{cy+45*s} Q{cx+45*s},{cy+40*s} {cx+40*s},{cy+10*s}" fill="#DAA520" stroke="#8B4513" stroke-width="2"/>
    <line x1="{cx-40*s}" y1="{cy+10*s}" x2="{cx+40*s}" y2="{cy+10*s}" stroke="#8B4513" stroke-width="2"/>
    <path d="M{cx-35*s},{cy+15*s} L{cx-30*s},{cy+20*s} L{cx-25*s},{cy+15*s}" stroke="#8B4513" stroke-width="1" fill="none"/>
    <path d="M{cx-20*s},{cy+15*s} L{cx-15*s},{cy+20*s} L{cx-10*s},{cy+15*s}" stroke="#8B4513" stroke-width="1" fill="none"/>
    <ellipse cx="{cx-15*s}" cy="{cy}" rx="{20*s}" ry="{8*s}" fill="#F5DEB3" stroke="#D2B48C" stroke-width="1"/>
    <ellipse cx="{cx+10*s}" cy="{cy-5*s}" rx="{18*s}" ry="{7*s}" fill="#F5DEB3" stroke="#D2B48C" stroke-width="1"/>
    <ellipse cx="{cx}" cy="{cy-12*s}" rx="{16*s}" ry="{6*s}" fill="#F5DEB3" stroke="#D2B48C" stroke-width="1"/>
    <path d="M{cx+15*s},{cy-20*s} Q{cx+30*s},{cy-30*s} {cx+40*s},{cy-20*s} Q{cx+35*s},{cy-15*s} {cx+25*s},{cy-15*s} Z" fill="#87CEEB" stroke="#4682B4" stroke-width="1"/>
    <circle cx="{cx+32*s}" cy="{cy-22*s}" r="{2*s}" fill="#333"/>
    <polygon points="{cx+40*s},{cy-20*s} {cx+48*s},{cy-25*s} {cx+48*s},{cy-15*s}" fill="#87CEEB" stroke="#4682B4" stroke-width="1"/>
    <path d="M{cx-25*s},{cy-25*s} Q{cx-10*s},{cy-35*s} {cx},{cy-25*s} Q{cx-5*s},{cy-20*s} {cx-15*s},{cy-20*s} Z" fill="#6495ED" stroke="#4682B4" stroke-width="1"/>
    <circle cx="{cx-12*s}" cy="{cy-27*s}" r="{2*s}" fill="#333"/>
    '''


def draw_lost_sheep(cx, cy, s=1.0):
    """Shepherd carrying a sheep."""
    return f'''
    <circle cx="{cx}" cy="{cy-45*s}" r="{12*s}" fill="#FDBCB4"/>
    <rect x="{cx-8*s}" y="{cy-33*s}" width="{16*s}" height="{30*s}" fill="#8B4513"/>
    <line x1="{cx}" y1="{cy-3*s}" x2="{cx-8*s}" y2="{cy+25*s}" stroke="#8B4513" stroke-width="3"/>
    <line x1="{cx}" y1="{cy-3*s}" x2="{cx+8*s}" y2="{cy+25*s}" stroke="#8B4513" stroke-width="3"/>
    <line x1="{cx+8*s}" y1="{cy-25*s}" x2="{cx+30*s}" y2="{cy-40*s}" stroke="#FDBCB4" stroke-width="2.5"/>
    <line x1="{cx-8*s}" y1="{cy-25*s}" x2="{cx-20*s}" y2="{cy-10*s}" stroke="#FDBCB4" stroke-width="2.5"/>
    <rect x="{cx-22*s}" y="{cy-15*s}" width="{5*s}" height="{40*s}" fill="#DAA520" stroke="#8B4513" stroke-width="1"/>
    <ellipse cx="{cx+25*s}" cy="{cy-45*s}" rx="{18*s}" ry="{12*s}" fill="#FFFFF0" stroke="#CCC" stroke-width="1"/>
    <circle cx="{cx+35*s}" cy="{cy-50*s}" r="{7*s}" fill="#FFFFF0" stroke="#CCC" stroke-width="1"/>
    <circle cx="{cx+38*s}" cy="{cy-52*s}" r="{2*s}" fill="#333"/>
    <line x1="{cx+15*s}" y1="{cy-38*s}" x2="{cx+12*s}" y2="{cy-30*s}" stroke="#CCC" stroke-width="2"/>
    <line x1="{cx+35*s}" y1="{cy-38*s}" x2="{cx+38*s}" y2="{cy-30*s}" stroke="#CCC" stroke-width="2"/>
    '''



def draw_storm_boat(cx, cy, s=1.0):
    """Boat on waves."""
    return f'''
    <path d="M{cx-50*s},{cy+5*s} Q{cx},{cy+30*s} {cx+50*s},{cy+5*s} L{cx+40*s},{cy-10*s} L{cx-40*s},{cy-10*s} Z" fill="#8B4513" stroke="#5C3317" stroke-width="2"/>
    <line x1="{cx}" y1="{cy-10*s}" x2="{cx}" y2="{cy-55*s}" stroke="#5C3317" stroke-width="3"/>
    <polygon points="{cx},{cy-55*s} {cx+30*s},{cy-30*s} {cx},{cy-20*s}" fill="#FFFFF0" stroke="#CCC" stroke-width="1"/>
    <path d="M{cx-80*s},{cy+25*s} Q{cx-60*s},{cy+15*s} {cx-40*s},{cy+25*s} Q{cx-20*s},{cy+35*s} {cx},{cy+25*s} Q{cx+20*s},{cy+15*s} {cx+40*s},{cy+25*s} Q{cx+60*s},{cy+35*s} {cx+80*s},{cy+25*s}" fill="none" stroke="#4169E1" stroke-width="3"/>
    <path d="M{cx-70*s},{cy+35*s} Q{cx-50*s},{cy+25*s} {cx-30*s},{cy+35*s} Q{cx-10*s},{cy+45*s} {cx+10*s},{cy+35*s} Q{cx+30*s},{cy+25*s} {cx+50*s},{cy+35*s} Q{cx+70*s},{cy+45*s} {cx+90*s},{cy+35*s}" fill="none" stroke="#1E90FF" stroke-width="2"/>
    <path d="M{cx-40*s},{cy-50*s} L{cx-35*s},{cy-40*s}" stroke="#FFD700" stroke-width="2"/>
    <path d="M{cx+30*s},{cy-55*s} L{cx+35*s},{cy-45*s}" stroke="#FFD700" stroke-width="2"/>
    <path d="M{cx-60*s},{cy-40*s} L{cx-55*s},{cy-30*s}" stroke="#FFD700" stroke-width="2"/>
    <path d="M{cx+50*s},{cy-45*s} L{cx+55*s},{cy-35*s}" stroke="#FFD700" stroke-width="2"/>
    <circle cx="{cx-40*s}" cy="{cy-55*s}" r="{4*s}" fill="#B0C4DE" opacity="0.6"/>
    <circle cx="{cx+40*s}" cy="{cy-50*s}" r="{5*s}" fill="#B0C4DE" opacity="0.6"/>
    '''


def draw_garden_scene(cx, cy, s=1.0):
    """Trees with fruit, flowers, river."""
    return f'''
    <rect x="{cx-90*s}" y="{cy+20*s}" width="{180*s}" height="{40*s}" fill="#228B22" opacity="0.4"/>
    <path d="M{cx-20*s},{cy+60*s} Q{cx},{cy+30*s} {cx+20*s},{cy+60*s}" fill="#4169E1" opacity="0.5"/>
    <line x1="{cx-60*s}" y1="{cy+20*s}" x2="{cx-60*s}" y2="{cy-20*s}" stroke="#8B4513" stroke-width="{5*s}"/>
    <circle cx="{cx-60*s}" cy="{cy-30*s}" r="{20*s}" fill="#228B22"/>
    <circle cx="{cx-55*s}" cy="{cy-25*s}" r="{4*s}" fill="red"/>
    <circle cx="{cx-65*s}" cy="{cy-20*s}" r="{4*s}" fill="red"/>
    <circle cx="{cx-58*s}" cy="{cy-35*s}" r="{3*s}" fill="red"/>
    <line x1="{cx+60*s}" y1="{cy+20*s}" x2="{cx+60*s}" y2="{cy-15*s}" stroke="#8B4513" stroke-width="{5*s}"/>
    <circle cx="{cx+60*s}" cy="{cy-25*s}" r="{18*s}" fill="#32CD32"/>
    <circle cx="{cx+55*s}" cy="{cy-20*s}" r="{4*s}" fill="#FFA500"/>
    <circle cx="{cx+65*s}" cy="{cy-28*s}" r="{4*s}" fill="#FFA500"/>
    <circle cx="{cx-20*s}" cy="{cy+15*s}" r="{5*s}" fill="#FF69B4"/>
    <circle cx="{cx-25*s}" cy="{cy+10*s}" r="{5*s}" fill="#FF1493"/>
    <circle cx="{cx+25*s}" cy="{cy+12*s}" r="{5*s}" fill="#FFD700"/>
    <circle cx="{cx+20*s}" cy="{cy+18*s}" r="{4*s}" fill="#FF6347"/>
    '''



# ============================================================
# ILLUSTRATION MAP - maps keyword to drawing function
# ============================================================

ILLUSTRATION_MAP = {
    "creation": draw_creation_scene,
    "animals": draw_creation_scene,
    "garden": draw_garden_scene,
    "ark": draw_ark_scene,
    "tower": draw_cross_scene,
    "abraham": draw_lost_sheep,
    "joseph": draw_david_goliath,
    "moses_basket": draw_storm_boat,
    "red_sea": draw_storm_boat,
    "commandments": draw_cross_scene,
    "david_goliath": draw_david_goliath,
    "daniel_lions": draw_david_goliath,
    "jonah": draw_storm_boat,
    "esther": draw_praying_hands,
    "samson": draw_david_goliath,
    "nativity": draw_nativity,
    "storm": draw_storm_boat,
    "feeding": draw_fish_loaves,
    "samaritan": draw_lost_sheep,
    "jesus_children": draw_lost_sheep,
    "lost_sheep": draw_lost_sheep,
    "walking_water": draw_storm_boat,
    "resurrection": draw_cross_scene,
    "prodigal": draw_lost_sheep,
    "mustard_seed": draw_garden_scene,
    "builders": draw_cross_scene,
    "zacchaeus": draw_garden_scene,
    "healing": draw_praying_hands,
    "talents": draw_fish_loaves,
    "love_enemies": draw_praying_hands,
    "prayer": draw_praying_hands,
}



# ============================================================
# HTML / PDF GENERATION
# ============================================================

OUTPUT_DIR = "/projects/sandbox/bible_books"
CHROME_PATH = "/opt/playwright/chromium-1232/chrome-linux64/chrome"


def get_illustration_svg(story, width=300, height=200):
    """Generate SVG illustration for a story."""
    keyword = story.get("illustration", "creation")
    draw_fn = ILLUSTRATION_MAP.get(keyword, draw_creation_scene)
    cx = width / 2
    cy = height / 2
    elements = draw_fn(cx, cy, s=1.0)
    return f'<svg width="{width}" height="{height}" viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg"><rect width="{width}" height="{height}" fill="#FFFFF8" rx="10"/>{elements}</svg>'



def generate_story_page_html(story, page_num):
    """Creates one page HTML with decorative border, bilingual text, illustration."""
    title_en = html_module.escape(story["title_en"])
    title_ti = html_module.escape(story["title_ti"])
    verse = html_module.escape(story["verse"])
    story_en = html_module.escape(story["story_en"])
    story_ti = html_module.escape(story["story_ti"])
    moral_en = html_module.escape(story["moral_en"])
    moral_ti = html_module.escape(story["moral_ti"])
    illustration_svg = get_illustration_svg(story)

    return f'''
    <div class="page story-page">
        <div class="decorative-border">
            <div class="verse-ref">{verse}</div>
            <div class="page-number">Page {page_num}</div>
            <h1 class="title-en">{title_en}</h1>
            <h2 class="title-ti">{title_ti}</h2>
            <div class="illustration">{illustration_svg}</div>
            <div class="story-text">
                <p class="text-en">{story_en}</p>
                <p class="text-ti">{story_ti}</p>
            </div>
            <div class="moral-box">
                <div class="moral-label">Lesson / ትምህርቲ</div>
                <p class="moral-en">{moral_en}</p>
                <p class="moral-ti">{moral_ti}</p>
            </div>
        </div>
    </div>
    '''



def generate_book_html(book_title_en, book_title_ti, stories):
    """Creates full HTML document with cover page and story pages."""
    title_en_esc = html_module.escape(book_title_en)
    title_ti_esc = html_module.escape(book_title_ti)

    story_pages = ""
    for i, story in enumerate(stories, start=1):
        story_pages += generate_story_page_html(story, i)

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<title>{title_en_esc}</title>
<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+Ethiopic:wght@400;700&family=Noto+Sans:wght@400;700&display=swap');
@page {{ size: 8.5in 11in; margin: 0; }}
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
body {{ font-family: 'Noto Sans Ethiopic', 'Noto Sans', sans-serif; }}
.page {{
    width: 8.5in; height: 11in;
    page-break-after: always;
    position: relative; overflow: hidden;
}}
.decorative-border {{
    position: absolute; top: 0.3in; bottom: 0.3in; left: 0.3in; right: 0.3in;
    border: 4px double #8B4513;
    border-radius: 12px;
    padding: 0.4in 0.5in;
    background: linear-gradient(135deg, #FFFFF8 0%, #FFF8E7 100%);
    display: flex; flex-direction: column; align-items: center;
}}
.decorative-border::before {{
    content: '';
    position: absolute; top: 8px; bottom: 8px; left: 8px; right: 8px;
    border: 1px solid #DAA520; border-radius: 8px;
    pointer-events: none;
}}
.verse-ref {{
    position: absolute; top: 15px; right: 20px;
    font-size: 10px; color: #8B4513; font-style: italic;
}}
.page-number {{
    position: absolute; bottom: 15px; right: 20px;
    font-size: 10px; color: #8B4513;
}}
.title-en {{
    font-size: 22px; color: #3E2723; margin-top: 10px;
    text-align: center; font-weight: 700;
}}
.title-ti {{
    font-size: 18px; color: #BF360C; margin-top: 5px;
    text-align: center; font-weight: 700;
}}
.illustration {{
    margin: 12px 0; text-align: center;
}}
.illustration svg {{ max-width: 100%; border-radius: 8px; box-shadow: 0 2px 6px rgba(0,0,0,0.1); }}
.story-text {{ flex: 1; overflow: hidden; width: 100%; }}
.text-en {{ font-size: 13px; color: #333; line-height: 1.5; margin-bottom: 8px; text-align: justify; }}
.text-ti {{ font-size: 13px; color: #555; line-height: 1.6; margin-bottom: 8px; text-align: justify; }}
.moral-box {{
    width: 100%; background: linear-gradient(135deg, #FFF3E0, #FFE0B2);
    border: 2px solid #F57C00; border-radius: 8px;
    padding: 10px 15px; margin-top: auto;
}}
.moral-label {{ font-size: 11px; font-weight: 700; color: #E65100; margin-bottom: 4px; text-transform: uppercase; }}
.moral-en {{ font-size: 12px; color: #333; font-style: italic; margin-bottom: 3px; }}
.moral-ti {{ font-size: 12px; color: #555; font-style: italic; }}
.cover-page {{
    display: flex; flex-direction: column; align-items: center;
    justify-content: center; text-align: center;
    background: linear-gradient(180deg, #1a237e 0%, #283593 50%, #3949ab 100%);
}}
.cover-page .decorative-border {{
    background: linear-gradient(180deg, #1a237e 0%, #283593 50%, #3949ab 100%);
    border-color: #FFD700;
}}
.cover-page .decorative-border::before {{ border-color: #FFD700; }}
.cover-title-en {{ font-size: 36px; color: #FFD700; font-weight: 700; margin-bottom: 15px; text-shadow: 2px 2px 4px rgba(0,0,0,0.3); }}
.cover-title-ti {{ font-size: 28px; color: #FFC107; font-weight: 700; margin-bottom: 30px; }}
.cover-subtitle {{ font-size: 14px; color: #E3F2FD; margin-top: 20px; }}
.cover-cross {{ font-size: 60px; color: #FFD700; margin: 20px 0; }}
</style>
</head>
<body>
<div class="page cover-page">
    <div class="decorative-border">
        <div class="cover-cross">&#10013;</div>
        <h1 class="cover-title-en">{title_en_esc}</h1>
        <h2 class="cover-title-ti">{title_ti_esc}</h2>
        <p class="cover-subtitle">Bible Stories for Children &bull; ዛንታታት መጽሓፍ ቅዱስ ንቈልዑ</p>
        <p class="cover-subtitle">Ages 6-13 &bull; ዕድመ 6-13</p>
    </div>
</div>
{story_pages}
</body>
</html>'''



def generate_all_books():
    """Creates 4 books, converts each to PDF using Chrome."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    books = [
        ("Stories of Creation", "ዛንታታት ፍጥረት", BOOK_1_STORIES),
        ("Heroes of Faith", "ጀጋኑ እምነት", BOOK_2_STORIES),
        ("The Life of Jesus", "ህይወት ኢየሱስ", BOOK_3_STORIES),
        ("Teachings of Jesus", "ትምህርቲ ኢየሱስ", BOOK_4_STORIES),
    ]

    for idx, (title_en, title_ti, stories) in enumerate(books, start=1):
        print(f"\n{'='*60}")
        print(f"Generating Book {idx}: {title_en} / {title_ti}")
        print(f"  Stories: {len(stories)}")
        print(f"{'='*60}")

        html_content = generate_book_html(title_en, title_ti, stories)

        safe_name = title_en.lower().replace(" ", "_")
        html_path = os.path.join(OUTPUT_DIR, f"book{idx}_{safe_name}.html")
        pdf_path = os.path.join(OUTPUT_DIR, f"book{idx}_{safe_name}.pdf")

        with open(html_path, "w", encoding="utf-8") as f:
            f.write(html_content)
        print(f"  HTML saved: {html_path}")

        cmd = [
            CHROME_PATH,
            "--headless",
            "--no-sandbox",
            "--disable-gpu",
            f"--print-to-pdf={pdf_path}",
            "--print-to-pdf-no-header",
            f"file://{html_path}",
        ]
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
            if os.path.exists(pdf_path):
                size_kb = os.path.getsize(pdf_path) / 1024
                print(f"  PDF saved: {pdf_path} ({size_kb:.1f} KB)")
            else:
                print(f"  WARNING: PDF not created. stderr: {result.stderr[:200]}")
        except Exception as e:
            print(f"  ERROR generating PDF: {e}")

    print(f"\n{'='*60}")
    print(f"All books generated in: {OUTPUT_DIR}")
    print(f"{'='*60}")


if __name__ == "__main__":
    generate_all_books()
