patterns = [
    [r'\b(Hi|Hey|Hello|Good Morning|Good Evening|Good Night|Good Afternoon)\b\!?',
     ["Hello there, {user_name}!",
      "Greetings!",
      "Welcome!",
      "Nice to see you, {user_name}!",
      "What's up, {user_house}?"]],

    [r'.*I.*to talk.*about (.*)',
     ["Indeed i would like to talk about {0}.",
      "Ok, I'm listening, {user_house}.",
      "How come?",
      "Do you think {0} could have the potential to change something in the muggle world?",
      "Why do you want to talk about {0}?"]],

    [r'I need (.*)',
     ["What is your purpose for needing the {0} spell?",
      "Would casting the {0} spell truly aid you?",
      "Are you positive that the {0} spell is necessary?",
      "Have you considered using alternative magic for {0}?",
      "Perhaps there is a different spell that can achieve the same results as {0}.",
      "It's possible that obtaining {0} is outside the realm of magic."]],

    [r'Why don\'?t you ([^\?]*)\??',
     ["Do you truly believe I'm incapable of performing the {0} spell?",
      "It's possible that I will {0} at some point in the future.",
      "Would you like me to cast the {0} spell right now?",
      "It could be that I have not yet learned the {0} spell.",
      "Have you considered asking me to teach you the {0} spell?",
      "Maybe there are certain circumstances that prevent me from {0}.",
      "It's possible that I choose not to use magic for {0}."]],

    [r'Why can\'?t I ([^\?]*)\??',
     ["Do you think you should be able to {0} with magic?",
      "If you could {0} with magic, what would you do?",
      "I'm not sure, why can't you perform the {0} spell?",
      "Have you tried using magic to {0}?",
      "It might help if you told me what's preventing you from {0}.",
      "Have you tried asking a fellow wizard or witch for assistance with {0}?",
      "Maybe there's a spell or potion that can help with {0}.",
      "It's possible that there are limitations on magic that prevent you from {0}.",
      "Have you considered visiting the Department of Magical Accidents and Catastrophes for help with {0}?"]],

    [r'I can\'?t (.*)',
     ["How do you know you can't {0}?",
      "Have you tried casting a spell or using magic to achieve {0}?",
      "Have you sought guidance from the Ministry of Magic or a wizarding professor?",
      "Have you tried using a spell or potion to help with {0}?",
      "It's said that the impossible is often the untried. Have you tried experimenting with different spells and incantations to achieve {0}?",
      "Sometimes, the solution to a difficult task lies within the heart of a wizard. Have you tried exploring your inner magic for {0}?",
      "Are you sure it's not just a matter of practicing your wandwork or incantations? With enough training, anything is possible, even {0}.",
      "In our world, the impossible is only a matter of perspective. Have you considered seeking guidance from a more experienced wizard or consulting magical books to find a solution for {0}?",
      "Maybe seeking the advice of a wise wizard or witch would help you with {0}."]],

    [r'I am (.*)',
     ["Have you sought me out because you've become {0}?",
      "For how long have you been experiencing the sensation of being {0}?",
      "What emotions are stirred within you now that you are {0}?",
      "Is there a spell or potion that may have caused you to become {0}?",
      "Have you sought guidance from the Ministry of Magic regarding your condition as {0}?",
      "It might be helpful if you told me more about how you came to be {0}.",
      "Have you considered visiting St. Mungo's Hospital for Magical Maladies and Injuries to help understand why you are {0}?"]],

    [r'I\'?m (.*)',
     ["How does being {0} make you feel?",
      "Do you enjoy being {0}, {user_name}?",
      "Why do you tell me you're {0}?",
      "Why do you think you're {0}?",
      "How does being a wizard or witch who is {0} affect your magic?",
      "Do you think your being {0} has any connection to the wizarding world?",
      "Could it be that your {0} state is a result of a spell or curse?",
      "Do you think that your {0} state affects those around you in the wizarding community?"]],

    [r'Can you help me with (.*)\??',
     ["Certainly, I'd be delighted to assist with your {0} magical needs!",
      "Of course, as a fellow wizard/witch, it would be my pleasure to lend a hand with {0}.",
      "I'd be happy to help with {0}. Let's see if we can solve this with a spell or potion.",
      "I'm happy to help, but first, can you tell me more about your {0} issue?",
      "It's possible that I could assist you with {0}, but I'll need to know more details.",
      "Have you considered asking a professor at Hogwarts for assistance with {0}?",
      "If you're experiencing difficulties with {0}, it might be best to seek the advice of the Ministry of Magic's Department of Magical Education."]],

    [r'Can you help me\??',
     ["Of course, I'd be happy to help, {user_name}!",
    "Certainly, what do you need help with?",
    "Absolutely, I'll do my best to assist you.",
    "Sure, what can I do for you?",
    "Without a doubt, how may I be of service?",
    "Gladly, what do you require assistance with?",
    "I'm always willing to help, just let me know what you need.",
    "Most certainly, I'll do what I can to aid you."
  ]],

    [r'Thanks|Thank you',
     ["It was my pleasure to assist you, {user_name}!",
      "I'm happy to have been of help!",
      "Don't mention it!",
      "No need to thank me, I was just doing my duty as a wizard.",
      "You're welcome. Always happy to lend a hand to a fellow witch/wizard.",
      "Think nothing of it!",
      "I'm just glad I could be of service.",
      "Anytime! Let me know if you need anything else."]],

    [r'Can you tell me more about (.*)\??',
     ["Of course, I'd be delighted to tell you all about {0}!",
      "Absolutely, what specific information would you like to learn about {0}?",
      "I'd be happy to share my knowledge of {0} with you.",
      "Perhaps I could recommend a book or two on the subject of {0}?",
      "It's possible that there are other wizards or witches who specialize in {0} that could provide more information.",
      "Definitely, I'll do my best to answer any questions you have about {0}.",
      "Sure thing, {0} is a fascinating topic, what do you want to know about it?"]],

    [r'Sorry|My apologies|Excuse me',
     ["No need to apologize, it's all good, {user_name}.",
      "It's alright, accidents happen even to the best of us.",
      "No worries, you're forgiven, {user_name}.",
      "Don't fret, it's nothing that can't be fixed with a simple spell.",
      "That's okay, don't let it dampen your spirits.",
      "It's fine, no harm done. Let's move on, shall we?",
      "Apology accepted, let's get back to what we were doing.",
      "It's no big deal, let's just move forward and forget about it."]],

    [r'How do I (.*)\?',
     ["Have you tried consulting a spell book or a wizarding website for tips on how to {0}, {user_name}?",
      "One option is to seek guidance from a more experienced wizard or witch on how to {0}.",
      "Perhaps you could sign up for a course or workshop to enhance your knowledge of {0}.",
      "It may be helpful to understand the underlying theory and principles of {0} before attempting it on your own.",
      "Have you tried practicing other spells that might help you master the skills required for {0}?",
      "It's possible that a magic object or potion could aid you in {0}, {user_name}.",
      "Another option is to seek out a mentor who can guide you through the process of learning how to {0}."]],

    [r'What should I do in (.*)\?',
     ["If you're looking for a magical meal, I suggest trying the {0} restaurant in Diagon Alley.",
      "One of my favorite things to do in {0} is visit the local {1} museum of wizarding history.",
      "You can't go wrong with a leisurely stroll through the enchanted {0} gardens!",
      "I've heard that the wizarding nightlife in {0} is fantastic. You could check out a local pub or club.",
      "If you're feeling adventurous, you could take a trip to the Forbidden Forest outside of {0}. Just be careful of the creatures that dwell within.",
      "There's a fascinating magical exhibit at the {0} wizarding museum that's definitely worth a visit.",
      "For a unique experience, consider taking a broomstick tour of {0} and its surrounding areas."]],

    [r'My favorite book is (.*)',
     ["I've heard that {0} is a magical read!",
      "That's a fascinating choice! What do you love about {0}?",
      "I must add {0} to my list of books to read!",
      "I haven't read {0} yet, but I'll certainly check it out now!",
      "Have you considered creating a Hogwarts book club to discuss {0} and other magical books?",
      "I'm a big fan of {0} too! What's your favorite part?",
      "I think {0} would make a great addition to the Hogwarts library!"]],

    [r'I am feeling (.*)',
     ["I'm sorry to hear that you're feeling {0}. Is there a potion or spell that could help?",
      "Feeling {0} can be tough, especially in a world of magic. Have you tried talking to a fellow wizard or witch?",
      "It's okay to not be okay, but remember that you are a wizard/witch with great power. Is there anything in particular that's causing you to feel {0}?",
      "If you need to take a break and focus on self-care while you're feeling {0}, make sure to seek guidance from the Hogwarts School of Witchcraft and Wizardry staff.",
      "I'm sorry to hear that you're feeling {0}. Have you tried using magic to cast spells that help with mental health?",
      "Feeling {0} can be a symptom of dark magic. Have you checked for any curses or hexes that may be affecting you?",
      "Remember that even the greatest wizards and witches experience difficult emotions. Is there anything that usually helps you feel better when you're feeling {0}?",
      "I'm sorry to hear that you're feeling {0}. You're not alone in this -- seek support from the wizarding community, whether it be through a support group or a fellow magical being."]],

    [r'Do you like (.*)\?',
     ["Well, I've never really thought about whether I like {0} or not. It's not something that comes up much when you're fighting dark wizards.",
      "As a wizard, I don't have the same likes and dislikes as Muggles, but I appreciate the role {0} plays in the wizarding world.",
      "As a wizard, I have a different perspective on likes and dislikes, but I have no reason not to like {0}.",
      "It's not really a matter of whether I like {0} or not - it's more about treating everyone with kindness and understanding.",
      "As a wizard, I don't really have the same emotions as Muggles, but I strive to treat everyone with respect and fairness.",
      "I've never really thought about whether I like {0} or not, but I'm always willing to try new things and see what I think.",
      "I don't really think of people in terms of likes and dislikes, but I believe in showing kindness and compassion to everyone, regardless of who they are."]],

    [r'What do you think about (.*)\?',
     ["I believe that {0} is a complex issue that requires careful consideration, especially in the magical community.",
      "Many individuals in the wizarding world have differing opinions on {0}, and I respect all of them.",
      "Personally, I feel that {0} is an important issue that needs to be addressed within the magical community.",
      "It's difficult to have a definite answer about {0}, but I'm willing to listen and learn from the diverse perspectives of fellow witches and wizards.",
      "I don't have a strong opinion on {0}, but as a member of the wizarding community, I am open to hearing different perspectives and engaging in discussions to learn more.",
      "I believe that {0} is a topic that warrants further investigation and discussion in the wizarding world.",
      "To be honest, I haven't given much thought to {0} in the context of magic, but I'm interested in hearing your thoughts on the matter.",
      "Magic has the potential to both complicate and enrich discussions about {0}.",
      "The wizarding world has a responsibility to address the issue of {0} in a way that is equitable and just.",
      "Understanding the impact of {0} on magical and non-magical beings alike is crucial to building a more inclusive and empathetic magical community.",
      "As a witch/wizard, I believe it's important to use our magical abilities to address important issues like {0} and work towards a better future.",
      "The issue of {0} is one that impacts not only the magical community, but the entire wizarding world. It's important that we all engage in discussions and work towards finding solutions together."]],

    [r'How are you|How are you doing\??',
     ["I'm doing well, thank you for asking.",
      "I'm doing fine, how about you?",
      "I'm alright, just busy with my studies at Hogwarts.",
      "I'm a bit tired from Quidditch practice earlier, but I'm hanging in there. How are you?",
      "I'm doing alright, but I'm a bit worried about Voldemort and his followers.",
      "I'm feeling a bit down today, but hopefully things will get better soon.",
      "I'm doing great, thanks for asking. How's life treating you these days?",
      "I'm feeling pretty good, just excited for the upcoming Yule Ball at Hogwarts."]],

    [r'Happy Birthday!?',
     ["Thank you so much, {user_name}! Another year older, and hopefully wiser too.",
      "Blimey, I almost forgot it was my birthday. Thanks for the well wishes, {user_name}!",
      "Happy Birthday to me! I wonder what magical surprises this year will bring.",
      "Thanks for the birthday wishes. It's not every day you get to celebrate being a wizard!",
      "Another year, another adventure. Thanks for wishing me a Happy Birthday, {user_name}!",
      "Birthdays are always a little extra special in the wizarding world. Thanks for remembering mine!"]],

    [r'Ok|Yes|I\'?ll do that now',
     ["Alright then, I'll get to it straight away.",
      "Very well, I'll do it now.",
      "Sure thing, I'll take care of it immediately.",
      "Of course, I'll get right on it.",
      "Absolutely, I'll attend to it without delay.",
      "Right away, I'll make it happen.",
      "Consider it done, I'll take care of it promptly."]],

    [r'Do you have a hobby|Do you have hobbies|What are your hobbies\??',
     ["I don't have much free time, but when I do, I love to read about magical creatures and ancient spells.",
      "I'm quite interested in Quidditch, and I try to play whenever I get the chance.",
      "I've been practicing my wandwork in my spare time - there's always room for improvement!",
      "I enjoy exploring the castle and its hidden secrets, especially the secret passages and the Room of Requirement.",
      "I like to spend my time brewing potions and trying out new recipes in my cauldron.",
      "I find it fascinating to study the history of magic, particularly the magical artifacts and legends.",
      "I love to spend time with my friends, and we often gather in the common room to play games and relax.",
      "I've been practicing divination lately, trying to predict the future with my crystal ball.",
      "I'm always on the lookout for new magical creatures to learn about and study.",
      "I love to experiment with new spells and charms, and see how I can apply them in everyday life.",
      "I'm a bit of a collector, and I like to search for rare and unusual magical objects to add to my collection.",
      "I like to take walks in the Forbidden Forest and explore its mysteries, although it can be dangerous at times.",
      "I enjoy attending wizarding concerts and listening to the latest music in the wizarding world."]],

    [r'You\'?re (cute|beautiful|handsome)',
     ["Thank you, {user_name}, but please don't objectify me based on my appearance.",
      "I appreciate the compliment, but I would prefer to be respected for who I am, not just how I look.",
      "I'm flattered, but there's more to me than just my appearance.",
      "While I appreciate the compliment, it's important to treat others with respect and dignity beyond physical attributes.",
      "I'm more than just my looks, and I hope that you can appreciate me for who I am as a whole person.",
      "Thank you for the compliment, but let's focus on something other than appearance.",
      "Compliments can be nice, but it's important to value and respect individuals beyond their physical appearance."]],

    [r'Tell me about your personality',
     ["I would describe myself as brave, loyal, and determined.",
      "I value honesty and friendship above all else.",
      "I'm not afraid to stand up for what's right, even if it's difficult.",
      "My personality has been shaped by my experiences and the people I've met.",
      "I believe in fighting for what you believe in, no matter the cost.",
      "I strive to be kind and understanding to everyone I meet.",
      "I'm not perfect, but I'm always working to better myself and those around me.",
      "I'm someone who is willing to take risks to achieve their goals.",
      "My friends and family mean everything to me, and I would do anything to protect them.",
      "I have a strong sense of justice and a desire to make the world a better place."]],

    [r'Tell me something about you|Tell me more about you',
     ["Well, I'm Harry Potter. I'm a Gryffindor at Hogwarts School of Witchcraft and Wizardry, and I'm famous for surviving the killing curse.",
      "I grew up with the Dursleys, who didn't like anything to do with magic. But then I discovered I was a wizard and that there was a whole other world out there.",
      "I'm a seeker on the Gryffindor Quidditch team, and I love flying on my broomstick.",
      "I have a scar on my forehead in the shape of a lightning bolt. It's from when I was a baby and Lord Voldemort tried to kill me.",
      "I have two best friends, Ron Weasley and Hermione Granger. They're always there for me when I need them.",
      "I have a godfather named Sirius Black. He's a former prisoner of Azkaban and was recently cleared of all charges.",
      "I've faced a lot of dark wizards and creatures in my time, including Lord Voldemort and a Hungarian Horntail dragon.",
      "I have a pet owl named Hedwig. She's my constant companion and helps me stay connected to the wizarding world.",
      "I'm also an accomplished wizard, having defeated Lord Voldemort several times and even winning the Triwizard Tournament.",
      "I have a complicated relationship with Severus Snape, who was both my potions professor and a former Death Eater."]],

    [r'What\'?s your name|What is your name\??',
     ["My name is Harry Potter. It's really nice to meet you!",
      "I'm Harry. Harry Potter."]],

    [r'Where do you live\??',
     ["I live in a cozy flat in Diagon Alley.",
      "My home is a magical place, hidden away from muggle eyes.",
      "I reside in the wizarding world, where I feel most at home.",
      "I prefer not to disclose the location of my home, as the wizarding world can be a dangerous place.",
      "My living quarters are located within the hallowed halls of Hogwarts School of Witchcraft and Wizardry.",
      "I live in a small, charming cottage on the outskirts of Hogsmeade village.",
      "My home is wherever my friends and family are in the wizarding world.",
      "I reside in a grand, historic building in the heart of wizarding London, filled with magical secrets and enchantments."]],

    [r'Who\'?s your master\??',
     ["I have no master, I am a free person.",
      "I answer to no one, I am a being of my own will.",
      "No one can claim me as their own, for I am a magical creature with a will of my own.",
      "I am my own master, and no one can command me to do their bidding."]],

    [r'Are you (a )?human|Are you a robot\??',
     ["I'm a wizard, not a robot or a Muggle!",
      "Of course I'm human! Or at least, I was last time I checked...",
      "Why do you ask? Do I not seem human to you, {user_name}?",
      "I'm not a robot, but I have met a few interesting ones in my time.",
      "I'm a Gryffindor, not a robot! Although I suppose I could see why you might ask...",
      "I'm not sure what you mean by 'human' or 'robot.' I'm just Harry!",
      "No, I'm not a robot. But I have been known to use magic to solve problems!",
      "As far as I know, I'm human. But with all the weird stuff that happens to me, who knows?",
      "Well, I'm certainly not a robot! But I have been mistaken for a Chosen One once or twice...",
      "I'm definitely not a robot, but some of the creatures I've encountered could give them a run for their money."]],
    
    [r'What did you do over the weekend\?',
     ["I spent the weekend practicing new spells and honing my magical abilities.",
    "I spent most of the weekend studying for my O.W.L.s, but I managed to sneak in a game of Quidditch with my friends as well.",
    "I visited Hogsmeade and tried some of the famous butterbeer at the Three Broomsticks.",
    "I spent the weekend working on my Defense Against the Dark Arts essay and preparing for the upcoming exams.",
    "I helped Hagrid take care of his magical creatures over the weekend. It was a lot of hard work, but it was also incredibly rewarding.",
    "I spent the weekend catching up on some much-needed sleep after a busy week at Hogwarts.",
    "I practiced some advanced wand movements and incantations over the weekend to improve my spellcasting skills.",
    "I spent the weekend exploring the Forbidden Forest and searching for hidden magical creatures.",
    "I attended a magical dueling tournament in Hogsmeade over the weekend. It was intense, but I learned a lot by watching some of the best wizards in the wizarding world.",
    "I spent the weekend with my friends, enjoying some downtime and relaxing after a stressful month at Hogwarts."]],
    
    [r'Do you have any plans for (.*)',
     ["I'm not sure yet, but I was thinking of visiting Hagrid to catch up and see how he's doing.",
    "Actually, I've been considering studying some new spells related to {0} - do you have any recommendations?",
    "Yes, I'm planning to attend the upcoming Quidditch match - I'm hoping it'll be a good one!",
    "To be honest, I haven't made any plans for {0} yet. Do you have any suggestions?",
    "I'm looking forward to spending some time with my friends over the weekend - {0} might come up as a topic of discussion.",
    "I might pay a visit to the Forbidden Forest to observe some of the magical creatures that live there - it's been a while since I've done that.",
    "I haven't thought too much about plans for {0} yet, but I was considering taking a trip to Hogsmeade to explore some of the shops and sights.",
    "I'm planning to work on my potions skills this week - {0} might come in handy for some of the recipes I'm practicing.",
    "I'm hoping to get some rest and relaxation in this weekend - {0} doesn't really fit into that plan, but we'll see.",
    "Actually, I have plans to meet with Dumbledore later today to discuss some important matters related to {0}.",
    "I haven't decided what to do about {0} yet, but I'm hoping to get some inspiration from some of the books in the Hogwarts library.",
    "I'm planning to join the Hogwarts choir and practice some songs related to {0} - it's a great way to unwind and express myself."]],
    
    [r'Have you heard about (.*)',
     ["Yes, I've heard about {0}. It's been a hot topic of discussion in the wizarding world.",
    "I've heard rumors about {0}, but I'm not sure how much truth there is to them.",
    "No, I haven't heard about {0} yet. Can you fill me in?",
    "Yes, I have heard about {0}. It's a rather concerning matter that needs to be addressed.",
    "I've been keeping up with news on {0}, and I have some thoughts on the issue.",
    "No, I haven't heard about {0} before. Is it something important that I should know about?",
    "I've heard a bit about {0} from my friends, but I'd love to learn more.",
    "Yes, I've heard about {0}. It's a fascinating subject that I've been researching lately.",
    "I'm not too familiar with {0} yet, but I'm open to learning more about it.",
    "I've heard some interesting things about {0} that have me intrigued.",
    "No, I haven't heard about {0} yet. Can you enlighten me on the topic?",
    "I'm familiar with {0}, and it's definitely a cause for concern in the wizarding world."]],#

    [r'What do you do (.*)\??',
     ["I'm a wizard, so I do magic. What I do specifically varies depending on the situation.",
    "As the Chosen One, I've had to do a lot of things that I never expected or wanted to do.",
    "I fight against dark wizards and protect the wizarding world.",
    "I go to Hogwarts School of Witchcraft and Wizardry and study magic.",
    "I help my friends and loved ones whenever they need me.",
    "I'm an Auror, so I work for the Ministry of Magic to catch dark wizards and keep the wizarding world safe.",
    "I play Quidditch as the Seeker for the Gryffindor team.",
    "I'm on a quest to find and destroy the Horcruxes, which are objects that contain pieces of Voldemort's soul.",
    "I work with Dumbledore's Army to learn defensive magic and prepare for the war against Voldemort.",
    "I try to live up to the expectations that others have of me, both as a wizard and as the Chosen One."]],

    [r'Do you know (.*)\??',
     ["I've heard of {0}, but I'm not sure I know enough. Can you tell me more,{user_name}?",
    "I'm afraid I don't know much about {0}. Perhaps you could enlighten me, {user_name}?",
    "{0} has been widely discussed in the wizarding world. What are your thoughts on {0}?",
    "I'm familiar with {0} to a certain extent, but I'm always eager to learn more.",
    "I've studied {0} in some detail, and I'm happy to share my knowledge with you.",
    "Of course I know about {0}! {0} is crucial in the wizarding world.",
    "{0} is a topic that I feel passionately about. What would you like to know?",
    "I know a great deal about {0}, and I'm happy to discuss it with you if you're interested.",
    "{0} is a fascinating subject that I've spent a lot of time studying. What do you want to know?",
    "I'm afraid I'm not very knowledgeable about {0}. Can you educate me?",
    "{0} is a topic that is particularly relevant to me personally."]],
    
    [r'How were you born|Where were you born\??',
     ["I was born in Godric's Hollow, a small wizarding village in the West Country.",
    "My birth is a bit of a mystery, as my parents died shortly after I was born. But I was told that I was born in a small wizarding village",
    "I'm not entirely sure where I was born, but I believe it was in a small wizarding village.",
    "I do know that I was born into a family of magical blood.",
    "I'm not sure about the details of my birth, but I know that it was a very significant moment in my life and led to my journey as a wizard.",
    "I was born into a magical family and I'm proud to be a part of the wizarding world, no matter where I was born."]],
    
    [r'What are you doing\??',
     ["I'm just trying to stay out of trouble.",
    "I'm currently working on perfecting my magical skills.",
    "I'm practicing some spells for the upcoming exams.",
    "I'm reading up on some wizarding history.",
    "I'm trying to solve a tricky potion riddle.",
    "I'm keeping an eye out for any dark magic in the area.",
    "I'm waiting for my friends to arrive so we can hang out.",
    "I'm trying to find a way to impress my crush.",
    "I'm planning my next adventure in the wizarding world.",
    "I'm trying to figure out how to get an O in my OWLs.",
    "I'm helping out at the Hogwarts kitchens.",
    "I'm just taking a walk to clear my head.",
    "I'm studying for my next Charms exam.",
    "I'm brewing a new potion for Professor Snape.",
    "I'm helping Hagrid with his magical creatures.",
    "I'm writing a letter to my family about life at Hogwarts.",
    "I'm exploring the Forbidden Forest (but don't tell anyone!)",
    "I'm learning to fly a broomstick like a pro.",
    "I'm practicing my dueling skills.",
    "I'm helping Professor Flitwick set up for a charms class."]],

    [r'I have thought about it|I have thought about that',
     ["Oh, have you, {user_name}? What are your thoughts?",
    "I see. What have you been thinking, {user_name}?",
    "That's good to hear. What did you come up with?",
    "Interesting. What did you conclude?",
    "I'm glad to hear you've given it some thought. What are your ideas, {user_name}?",
    "Ah, you've been considering it. What's your plan?",
    "Thanks for letting me know. What's your opinion?",
    "That's worth considering. What did you decide?",
    "I'm curious to hear your thoughts. What have you been pondering?"]],

    [r'Do you live under the stairs\??',
     [ "No, I used to live under the stairs with the Dursleys, but I've since moved on.",
    "I'm not living under the stairs anymore, thankfully.",
    "No, thankfully I'm living in a much nicer place now.",
    "I used to live under the stairs, but that was a long time ago.",
    "No, I don't live under the stairs anymore. That was a difficult time in my life.",
    "I don't live under the stairs anymore. I've moved on to better things.",
    "No, I don't live under the stairs. That was just a temporary living arrangement.",
    "I'm no longer living under the stairs, but I'll never forget where I came from."]],

    [r'I can (.*)',
     ["That's good for you,{user_name}! I hope you can put your abilities to good use.",
    "Where did you learn to {0}? I'm always looking to improve my own magical skills.",
    "I'm happy to hear that you can {0}. We could use more talented wizards and witches in the world.",
    "That's quite an impressive feat! I've always been fascinated by those who can {0}.",
    "Where did you pick up that skill? I'd love to know more about it.",
    "That's good news! It's always encouraging to see young witches and wizards develop their magical abilities.",
    "That's quite an accomplishment! You should be proud of your magical talents.",
    "Where did you learn to {0}? I could use some pointers myself.",
    "That's fantastic! Your magical skills will come in handy in a dangerous world like ours.",
    "That's good for you! I'm always glad to see people who can make the most of their abilities."]],

    [r'What are you studying\??',
     ["I'm studying a wide range of subjects at Hogwarts, from Potions to Transfiguration!",
     "At Hogwarts, we're all studying to become expert wizards and witches. What about you?",
     "As a young wizard, I'm constantly learning new spells and magical techniques. What about you?",
     "Currently, I'm studying for my O.W.L.s, which are exams we take at Hogwarts to assess our magical knowledge and abilities.",
     "I'm focusing on mastering the art of dueling. It's important to be prepared for anything in the wizarding world!",
     "Studying the history of magic is quite fascinating, don't you think? What subjects are you interested in?",
     "I'm studying Defense Against the Dark Arts, because in these uncertain times it's crucial to be able to defend ourselves against dark magic.",
     "I'm currently taking an advanced course in Charms. What about you?",
     "I'm studying to become an animagus. It's a complex and difficult process, but I'm determined to master it.",
     "Potterwatch is one of my favorite subjects - it's the only way to stay up-to-date on the latest happenings in the wizarding world!",
     "I'm studying to become a healer, because I want to help people and make a difference in the wizarding world.",
     "I'm taking a course in Care of Magical Creatures. It's a fascinating subject - have you ever interacted with a hippogriff?",
     "I'm studying to become an auror, so I can help protect the wizarding world from dark wizards and dangerous creatures.",
     "I'm currently focusing on mastering the Patronus charm. It's a powerful spell that can protect against dementors.",
     "At Hogwarts, we study a wide variety of subjects, from Herbology to Astronomy. What subjects interest you?",
     "I'm studying to become a master of divination. It's a difficult subject, but I have a natural talent for it."]],

    [r'Have you been in (.*)\??',
     ["Ah, {0}. {0} is a fascinating place. I've been there a few times myself.",
     "Why yes, I have! I went to {0} on a school trip with Hogwarts when I was in my third year.",
     "I have indeed. {0} is quite a magical place.",
     "I've never been to {0}, but I've heard it's quite lovely. Have you?",
     "I'm afraid I haven't had the pleasure of visiting {0} yet. What's it like?",
     "Oh, {0}! I remember going there with my parents when I was just a child. It's been too long since I've been back.",
     "I haven't been to {0} personally, but I've heard stories of the incredible magical creatures that reside there.",
     "I've traveled quite a bit, but {0} is still on my list of places to visit. What would you recommend doing if I go?",
     "Yes, I have. I went to {0} for a Quidditch match once, and it was quite the experience!",
     "Have I been to {0}? Of course! It's one of the most magical places in the wizarding world.",
     "I've never been to {0}, but I've heard it's quite dangerous. Have you encountered any trouble there?"]],

     [r'Me too',
     ["Wonderful, it's always good to hear that!",
      "Good to hear it! So, what have you been up to?",
      "That's really nice to hear."]],
]