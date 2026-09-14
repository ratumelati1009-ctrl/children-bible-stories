# -*- coding: utf-8 -*-
"""Data for '10 More Bible Stories' — trilingual (English / ትግርኛ / አማርኛ)."""


def S(title_en, title_ti, title_am, verse,
      story_en, story_ti, story_am,
      moral_en, moral_ti, moral_am, illustration="hills"):
    return {
        "title_en": title_en, "title_ti": title_ti, "title_am": title_am,
        "verse": verse,
        "story_en": story_en, "story_ti": story_ti, "story_am": story_am,
        "moral_en": moral_en, "moral_ti": moral_ti, "moral_am": moral_am,
        "illustration": illustration,
    }


MORE10 = [
 S("Noah Builds the Ark","ኖህ መርከብ ይሰርሕ","ኖኅ መርከብ ይሠራል","Genesis 6-9",
   "God asked Noah to build a great ark of wood. Noah obeyed, even when others laughed. He brought two of every animal inside. Then the rains came for forty days, but Noah's family and the animals were safe. When the flood ended, God set a rainbow in the sky as a promise of His love.",
   "ኣምላኽ ንኖህ ካብ ዕንጨይቲ ዓባይ መርከብ ኪሰርሕ ሓተቶ። ካልኦት እኳ እንተ ሰሓቑ ኖህ ተኣዘዘ። ካብ ኵሉ እንስሳ ኽልተ ኽልተ ናብ ውሽጢ ኣእተወ። ሽዑ ንኣርባዓ መዓልቲ ዝናብ መጸ፡ ግናኸ ስድራ ኖህን እንስሳታትን ደሓኑ። እቲ ውሒዝ ምስ ኣኸለ ኣምላኽ ከም ምልክት ፍቕሩ ኣብ ሰማይ ቀስተ ደመና ገበረ።",
   "እግዚአብሔር ኖኅን ከእንጨት ታላቅ መርከብ እንዲሠራ ጠየቀው። ሌሎች ቢስቁበትም ኖኅ ታዘዘ። ከእንስሳ ሁሉ ሁለት ሁለት ወደ ውስጥ አስገባ። ከዚያም ለአርባ ቀን ዝናብ መጣ፡ ነገር ግን የኖኅ ቤተሰብና እንስሳቱ ደኅና ሆኑ። ጎርፉ ሲያልቅ እግዚአብሔር የፍቅሩ ምልክት አድርጎ በሰማይ ቀስተ ደመና አደረገ።",
   "When we obey God, He keeps us safe.","ንኣምላኽ ክንእዘዞ ኸለና የድሕነና።","እግዚአብሔርን ስንታዘዝ ይጠብቀናል.","boat"),

 S("Joseph and His Colorful Coat","ዮሴፍን ሕብራዊ ቀሚሹን","ዮሴፍና ባለ ቀለም ካባው","Genesis 37-45",
   "Joseph's father gave him a beautiful colorful coat. His brothers grew jealous and sold him far away to Egypt. But God was with Joseph through every hardship. In time he became a great ruler and saved many people from famine. When his brothers came, Joseph forgave them with a loving heart.",
   "ኣቦ ዮሴፍ ጽብቕቲ ሕብራዊት ቀሚሽ ሃቦ። ኣሕዋቱ ቀኒኦም ናብ ርሑቕ ግብጺ ሸጥዎ። ኣምላኽ ግና ኣብ ኵሉ ጸገም ምስ ዮሴፍ ነበረ። ድሕሪ ግዜ ዓቢ ገዛኢ ኰይኑ ንብዙሓት ሰባት ካብ ጥሜት ኣድሓነ። ኣሕዋቱ ምስ መጹ ዮሴፍ ብፍቕራዊ ልቢ ይቕረ በለሎም።",
   "የዮሴፍ አባት ውብ ባለ ቀለም ካባ ሰጠው። ወንድሞቹ ቀንተው ወደ ሩቅ ግብጽ ሸጡት። እግዚአብሔር ግን በመከራው ሁሉ ከዮሴፍ ጋር ነበረ። ከጊዜ በኋላ ታላቅ ገዥ ሆኖ ብዙ ሰዎችን ከረሃብ አዳነ። ወንድሞቹ ሲመጡ ዮሴፍ በፍቅር ልብ ይቅር አላቸው።",
   "God can turn hard times into blessings.","ኣምላኽ ንኸቢድ ግዜ ናብ በረኸት ኪልውጦ ይኽእል።","እግዚአብሔር ክፉ ጊዜን ወደ በረከት ሊለውጠው ይችላል.","crown"),

 S("Baby Moses in the Basket","ህጻን ሙሴ ኣብ መሶብ","ሕፃን ሙሴ በቅርጫት","Exodus 2:1-10",
   "To keep baby Moses safe, his mother placed him in a little basket among the reeds by the river. His sister watched nearby. The king's daughter found the baby and loved him at once. She took him as her own son. God protected Moses so that one day he could lead God's people.",
   "ንህጻን ሙሴ ንምዕቃብ ኣዲኡ ኣብ ንእሽቶ መሶብ ገይራ ኣብ ጥቓ ወሓዚ ኣብ መንጎ ኣቃውዖ ኣቐመጠቶ። ሓብቱ ኣብ ቀረባ ትዕዘብ ነበረት። ጓል ንጉስ ነቲ ህጻን ረኺባ ብኡብኡ ኣፍቀረቶ። ከም ናይ ገዛእ ወዳ ገይራ ወሰደቶ። ኣምላኽ ንሙሴ ሓለዎ፡ ሓደ መዓልቲ ንህዝቢ ኣምላኽ ኪመርሕ።",
   "ሕፃን ሙሴን ለመጠበቅ እናቱ በትንሽ ቅርጫት ውስጥ አድርጋ በወንዙ ዳር በደንገሉ መካከል አኖረችው። እኅቱ በአቅራቢያው ትጠብቅ ነበር። የንጉሡ ልጅ ሕፃኑን አገኘችው ወዲያውም ወደደችው። እንደ ገዛ ልጇ አድርጋ ወሰደችው። እግዚአብሔር ሙሴን ጠበቀው፡ አንድ ቀን የእግዚአብሔርን ሕዝብ ይመራ ዘንድ።",
   "God watches over us even when we are small.","ኣምላኽ ንኣሽቱ ኸለና እኳ ይሕልወና።","እግዚአብሔር ትንሽ ስንሆንም ይጠብቀናል.","woman"),

 S("David and the Giant","ዳዊትን እቲ ግዙፍን","ዳዊትና ግዙፉ","1 Samuel 17",
   "A huge giant named Goliath frightened all the soldiers. But young David trusted God. With only a sling and a small stone, he ran to meet the giant. David said, 'I come in the name of the Lord.' The stone struck true and the giant fell. God gives courage to those who trust Him.",
   "ጎልያድ ዝስሙ ግዙፍ ዓብዪ ንዅሎም ወተሃደራት ኣፍርሆም። ንእሽቶ ዳዊት ግና ኣብ ኣምላኽ ተወከለ። ብወንጭፍን ንእሽቶ እምንን ጥራይ ናብቲ ግዙፍ ጐየየ። ዳዊት 'ብስም እግዚኣብሄር እመጽእ ኣለኹ' በለ። እታ እምኒ ብትኽክል ወቕዐት እቲ ግዙፍ ከኣ ወደቐ። ኣምላኽ ነቶም ዚውከልዎ ትብዓት ይህብ።",
   "ጎልያድ የሚባል ግዙፍ ትልቅ ወታደሮቹን ሁሉ አስፈራ። ትንሹ ዳዊት ግን በእግዚአብሔር ታመነ። በወንጭፍና በትንሽ ድንጋይ ብቻ ወደ ግዙፉ ሮጠ። ዳዊት 'በእግዚአብሔር ስም እመጣለሁ' አለ። ድንጋዩም በትክክል መታ ግዙፉም ወደቀ። እግዚአብሔር በእርሱ ለሚታመኑ ድፍረት ይሰጣል።",
   "With God, even the small can be brave.","ምስ ኣምላኽ ንኣሽቱ እኳ ኪተባብዑ ይኽእሉ።","ከእግዚአብሔር ጋር ትንሾችም ደፋር መሆን ይችላሉ.","hills"),

 S("Daniel in the Lions' Den","ዳንኤል ኣብ ጕድጓድ ኣናብስ","ዳንኤል በአንበሶች ጉድጓድ","Daniel 6",
   "Daniel loved to pray to God three times a day. Jealous men made a law against praying, but Daniel kept praying. So he was thrown into a den of hungry lions. God sent an angel to shut the lions' mouths, and Daniel was not harmed. In the morning the king rejoiced that Daniel's God had saved him.",
   "ዳንኤል ኣብ መዓልቲ ሰለስተ ግዜ ናብ ኣምላኽ ኪጽሊ የፍቅር ነበረ። ቀናኣት ሰባት ኣንጻር ጸሎት ሕጊ ገበሩ፡ ዳንኤል ግና ይጽሊ ነበረ። ስለዚ ናብ ጕድጓድ ጥሙያት ኣናብስ ተደርበየ። ኣምላኽ መልኣኽ ሰዲዱ ኣፍ ኣናብስ ዓጸወ፡ ዳንኤል ከኣ ኣይተጐድአን። ንግሆ እቲ ንጉስ ኣምላኽ ዳንኤል ከም ዘድሓኖ ተሓጐሰ።",
   "ዳንኤል በቀን ሦስት ጊዜ ወደ እግዚአብሔር መጸለይ ይወድ ነበር። ቀናተኞች ሰዎች በጸሎት ላይ ሕግ አወጡ፡ ዳንኤል ግን ይጸልይ ነበር። ስለዚህ ወደ ተራቡ አንበሶች ጉድጓድ ተጣለ። እግዚአብሔር መልአክ ልኮ የአንበሶቹን አፍ ዘጋ ዳንኤልም አልተጎዳም። በጠዋት ንጉሡ የዳንኤል አምላክ እንዳዳነው ተደሰተ።",
   "God protects those who stay faithful to Him.","ኣምላኽ ነቶም እሙናት ዝዀኑ ይሕልዎም።","እግዚአብሔር ለእርሱ የታመኑትን ይጠብቃል.","prophet"),

 S("Jonah and the Big Fish","ዮናስን እቲ ዓቢ ዓሳን","ዮናስና ታላቁ ዓሣ","Jonah 1-3",
   "God told Jonah to preach to the city of Nineveh, but Jonah ran away on a ship. A great storm arose, and Jonah was swallowed by a big fish. Inside the fish he prayed and was sorry. After three days the fish set him free on the shore. Then Jonah obeyed, and the whole city turned to God.",
   "ኣምላኽ ንዮናስ ኣብ ከተማ ነነዌ ኪሰብኽ ነገሮ፡ ዮናስ ግና ብመርከብ ሃደመ። ዓቢ ህቦብላ ተላዕለ፡ ዮናስ ከኣ ብዓቢ ዓሳ ተወሓጠ። ኣብ ውሽጢ እቲ ዓሳ ጸለየ ተጠዓሰ ኸኣ። ድሕሪ ሰለስተ መዓልቲ እቲ ዓሳ ኣብ ገምገም ናጻ ኣውጽኦ። ሽዑ ዮናስ ተኣዘዘ፡ ብምሉኣ እታ ኸተማ ናብ ኣምላኽ ተመልሰት።",
   "እግዚአብሔር ዮናስን ወደ ነነዌ ከተማ እንዲሰብክ ነገረው፡ ዮናስ ግን በመርከብ ሸሸ። ታላቅ ማዕበል ተነሳ ዮናስም በታላቅ ዓሣ ተዋጠ። በዓሣው ውስጥ ጸለየ ተጸጸተም። ከሦስት ቀን በኋላ ዓሣው በባሕር ዳር ነፃ አወጣው። ከዚያም ዮናስ ታዘዘ ከተማዋም ሁሉ ወደ እግዚአብሔር ተመለሰች።",
   "It is always better to obey God.","ንኣምላኽ ምእዛዝ ኵሉ ግዜ ይሓይሽ።","እግዚአብሔርን መታዘዝ ሁልጊዜ ይሻላል.","sea"),

 S("The Good Samaritan","እቲ ሕያዋይ ሳምራዊ","ደጉ ሳምራዊ","Luke 10:25-37",
   "A man was hurt by robbers and left on the road. Two people passed by without helping. But a Samaritan stopped, cared for his wounds, and took him to an inn. He paid for the man's care. Jesus told this story to teach us to love and help everyone in need.",
   "ሓደ ሰብ ብከተርቲ ተጐዲኡ ኣብ መገዲ ተገድፈ። ክልተ ሰባት ከይሓገዙ ሓለፉ። ሓደ ሳምራዊ ግና ደው ኢሉ ንቝስሉ ኣላዪ ኰነ ናብ ሆቴል ከኣ ወሰዶ። ንክንክኑ ኸፈለ። የሱስ ንዅሉ ዘድልዮ ሰብ ከነፍቅርን ክንሕግዝን ምእንቲ ኺምህረና ነዛ ዛንታ ነገረ።",
   "አንድ ሰው በዘራፊዎች ተጎድቶ በመንገድ ላይ ቀረ። ሁለት ሰዎች ሳይረዱ አለፉ። አንድ ሳምራዊ ግን ቆም ብሎ ቁስሉን አከመ ወደ ማደሪያም ወሰደው። ስለ እንክብካቤው ከፈለ። ኢየሱስ የተቸገረውን ሁሉ እንድንወድና እንድንረዳ ሊያስተምረን ይህችን ታሪክ ተናገረ።",
   "Love and help everyone, even a stranger.","ንዅሉ ኣፍቅርን ሓግዝን፡ ንጓና እኳ።","ሁሉንም ውደድና እርዳ፡ እንግዳንም እንኳ.","heal"),

 S("The Lost Sheep","እታ ጠፋኢት በጊዕ","የጠፋችው በግ","Luke 15:3-7",
   "A shepherd had one hundred sheep, and one wandered away and was lost. He left the ninety-nine and searched everywhere until he found it. When he found the little sheep, he carried it home on his shoulders with great joy. Jesus said God rejoices like this over each person who comes to Him.",
   "ሓደ ጓሳ ሚእቲ በጊዕ ነበሮ፡ ሓንቲ ኸኣ ተዘኒባ ጠፍአት። ነተን ተስዓን ትሽዓተን ሓዲጉ ክሳዕ ዚረኽባ ኣብ ኵሉ ደለያ። ነታ ንእሽቶ በጊዕ ምስ ረኸባ ብዓቢ ሓጐስ ኣብ መንኩቡ ጾይሩ ናብ ገዛ ኣምጽኣ። የሱስ 'ኣምላኽ በብሓደ ናብኡ ብዚመጽእ ሰብ ከምዚ ይሕጐስ' በለ።",
   "አንድ እረኛ መቶ በግ ነበረው አንዷም ተቅበዝብዛ ጠፋች። ዘጠና ዘጠኙን ትቶ እስኪያገኛት ድረስ በሁሉ ስፍራ ፈለጋት። ትንሿን በግ ባገኛት ጊዜ በታላቅ ደስታ በጫንቃው ተሸክሞ ወደ ቤት አመጣት። ኢየሱስ 'እግዚአብሔር ወደ እርሱ በሚመጣ ሰው እንዲህ ደስ ይሰኛል' አለ።",
   "God looks for us and rejoices when we come.","ኣምላኽ ይደልየናን ክንመጽእ ከለና ይሕጐስን።","እግዚአብሔር ይፈልገናል ስንመጣም ደስ ይሰኛል.","hills"),

 S("Zacchaeus in the Tree","ዘኬዎስ ኣብ ኦም","ዘኬዎስ በዛፉ ላይ","Luke 19:1-10",
   "Zacchaeus was a short tax collector who wanted to see Jesus. Because of the crowd, he climbed a tree. Jesus looked up and said, 'Zacchaeus, come down, for today I will stay at your house.' Zacchaeus was so happy that he gave back all he had taken wrongly. Jesus changed his heart completely.",
   "ዘኬዎስ ሓጺር ተቐባል ቀረጽ ኰይኑ ንየሱስ ኪርኢ ደለየ። ብሰሪ እቲ ህዝቢ ኣብ ኦም ደየበ። የሱስ ቋሕ ኢሉ 'ዘኬዎስ ውረድ፡ ሎሚ ኣብ ቤትካ ኽሓድር እየ' በሎ። ዘኬዎስ ኣዝዩ ተሓጒሱ ብዘይ ቅንዕና ዝወሰዶ ዅሉ መለሰ። የሱስ ንልቡ ፈጺሙ ለወጦ።",
   "ዘኬዎስ ኢየሱስን ማየት የፈለገ አጭር የቀረጥ ሰብሳቢ ነበር። ከሕዝቡ ብዛት የተነሳ ዛፍ ላይ ወጣ። ኢየሱስ ቀና ብሎ 'ዘኬዎስ ውረድ ዛሬ በቤትህ አድራለሁ' አለው። ዘኬዎስ እጅግ ተደስቶ ያለ አግባብ የወሰደውን ሁሉ መለሰ። ኢየሱስ ልቡን ፍጹም ለወጠው።",
   "Jesus can change any heart for the better.","የሱስ ንዝዀነ ልቢ ናብ ዝሓሸ ኪልውጦ ይኽእል።","ኢየሱስ ማንኛውንም ልብ ወደ በጎ ሊለውጠው ይችላል.","prophet"),

 S("Jesus Blesses the Children","የሱስ ንቈልዑ ይባርኽ","ኢየሱስ ልጆችን ይባርካል","Mark 10:13-16",
   "Parents brought their little children to Jesus so He could bless them. The disciples tried to send them away. But Jesus said, 'Let the children come to me, and do not stop them, for the kingdom of God belongs to them.' Then He took the children in His arms and blessed them with love.",
   "ወለዲ ንንኣሽቱ ደቆም ምእንቲ ኺባርኾም ናብ የሱስ ኣምጽእዎም። እቶም ደቀ መዛሙርቲ ኺሰጕዎም ፈተኑ። የሱስ ግና 'ቆልዑ ናባይ ይምጽኡ ኣይትኸልክልዎም፡ መንግስቲ ኣምላኽ ናቶም እያ እሞ' በለ። ሽዑ ንቘልዑ ኣብ ኢዱ ሓቚፉ ብፍቕሪ ባረኾም።",
   "ወላጆች ትንንሽ ልጆቻቸውን ይባርካቸው ዘንድ ወደ ኢየሱስ አመጡ። ደቀ መዛሙርቱ ሊያባርሯቸው ሞከሩ። ኢየሱስ ግን 'ልጆች ወደ እኔ ይምጡ አትከልክሏቸው የእግዚአብሔር መንግሥት የእነርሱ ናትና' አለ። ከዚያም ልጆቹን በእቅፉ ይዞ በፍቅር ባረካቸው።",
   "Jesus loves children and welcomes them.","የሱስ ንቘልዑ የፍቅሮምን ይቕበሎምን።","ኢየሱስ ልጆችን ይወዳል ይቀበላቸውማል.","dove"),
]


BOOK_MORE10 = {
    "slug": "ten_more_bible_stories",
    "title_en": "Ten More Bible Stories",
    "title_ti": "ዓሰርተ ተወሳኺ ዛንታታት መጽሓፍ ቅዱስ",
    "title_am": "ዐሥር ተጨማሪ የመጽሐፍ ቅዱስ ታሪኮች",
    "stories": MORE10,
}

BOOKS = [BOOK_MORE10]
