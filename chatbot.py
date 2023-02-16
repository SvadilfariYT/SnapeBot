from corpus_based.corpus_based import corpusbased_answer
from corpus_based.corpus_based import corpusbased_answer_2
from template_based.template_based import templatebased_answer
from template_based.template_based import special_patterns

import random

import phrases

# load language model
#nlp = spacy.load("en_core_web_lg")

memory = {'question 1' : 'answer1'}

def get_greeting():
    return random.choice(phrases.greetings)

def get_fallback():
    return random.choice(phrases.errors)

def get_farewell():
    return random.choice(phrases.farewell)

def get_response(input: str):
    
    answer = special_patterns(input)

    # Check if already asked
    if(answer == None):
        answer = get_modified_answer(input)
        print("Debug:  same question")

    # Corpus-Based-Matching (Tfidf)
    if(answer == None):
        answer = corpusbased_answer(input, 0.58)
        if(answer != None):
            print("Debug:  corpus based (Movie)")

    # Corpus-Based-Matching 2 (Tfidf)
    if(answer == None):
        answer = corpusbased_answer_2(input, 0.58)
        if(answer != None):
            print("Debug:  corpus based (GPT)")

    # Template-Based-Pattern-Matching
    if(answer == None):
        answer = templatebased_answer(input)
        if(answer != None):
            print("Debug:  pattern matching")

    # Standard/Fallback Answer
    if(answer == None):
        answer = get_fallback()
        if(answer != None):
            print("Debug:  fallback")

    # add to memory (history)
    memory[input] = answer
    
    return answer

def get_modified_answer(input : str):
    # TODO check for similar input  instead of exact
    if (input in memory):
        return "You have already asked me that"
    return None