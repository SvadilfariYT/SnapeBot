from corpus_based.corpus_based import corpusbased_answer
from corpus_based.corpus_based import corpusbased_answer_2
from template_based.template_based import templatebased_answer

# load language model
#nlp = spacy.load("en_core_web_lg")

memory = {'question 1' : 'answer1'}

def get_response(input: str):
    # Check if already asked
    answer = get_modified_answer(input)
    if(answer != None):
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
        answer = "I don't know that. Sorry"
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