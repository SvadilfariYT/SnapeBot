patterns = [
    [r'.*I.*to talk.*about (.*)',
     ["Indeed i would like to talk about {0}.",
      "Ok, I'm listening.",
      "How come?",
      "Do you think {0} could have the potential to change something in the muggle world?",
      "Why do you want to talk about {0}?"]],

    [r'I need (.*)',
     ["Why do you need {0}?",
      "Would it really help you to get {0}?",
      "Are you sure you need {0}?"]],

    [r'Why don\'?t you ([^\?]*)\??',
     ["Do you really think I don't {0}?",
      "Perhaps eventually I will {0}.",
      "Do you really want me to {0}?"]],

    [r'Why can\'?t I ([^\?]*)\??',
     ["Do you think you should be able to {0}?",
      "If you could {0}, what would you do?",
      "I don't know -- why can't you {0}?",
      "Have you tried?"]],

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
     ["Did you come to me because you are {0}?",
      "How long have you been {0}?",
      "How do you feel about being {0}?"]],

    [r'I\'?m (.*)',
     ["How does being {0} make you feel?",
      "Do you enjoy being {0}?",
      "Why do you tell me you're {0}?",
      "Why do you think you're {0}?"]]
]
