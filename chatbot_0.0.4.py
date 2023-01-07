from corpus_based.corpus_based import corpusbased_answer
from template_based.template_based import templatebased_answer

from colorama import Fore, Style

# load language model
#nlp = spacy.load("en_core_web_lg")

def getModifiedAnswer(user_input : str):
    # TODO check for similar user_input  instead of exact
    if (user_input in memory):
        return "You have already asked me that"
    return None

# MAIN METHOD
if __name__ == '__main__':
    user_input = input(">>> ").lower().strip()
    memory = {'question 1' : 'answer1'}
    
    while "exit" not in user_input.lower():
        
        # Check if already asked
        answer = getModifiedAnswer(user_input)
            

        # Template-Based-Pattern-Matching
        if(answer == None):
            answer = templatebased_answer(user_input)

        # Corpus-Based-Matching (Tfidf)
        if(answer == None):
            answer = corpusbased_answer(user_input, 0.5)

        # Standard/Fallback Answer
        if(answer == None):
            answer = "I don't know that. Sorry"

        memory[user_input] = answer

        print(Fore.GREEN + answer + Style.RESET_ALL)
        user_input = input(">>> ")  