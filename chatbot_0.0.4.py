from corpus_based.corpus_based import corpusbased_answer
from template_based.template_based import templatebased_answer

from colorama import Fore, Style

# load language model
#nlp = spacy.load("en_core_web_lg")

# MAIN METHOD
if __name__ == '__main__':
    user_input = input(">>> ").lower().strip()
    
    while "exit" not in user_input.lower():
        #get user_input
        #save user_input in variable (as key-value pairs with answer?)
        #check if user_input = / similar to variable
        #if true
            #change answer
        #if false
            #...

        # Template-Based-Pattern-Matching
        answer = templatebased_answer(user_input)

        # Corpus-Based-Matching (Tfidf)
        if(answer == None):
            answer = corpusbased_answer(user_input, 0.5)

        # Standard/Fallback Answer
        if(answer == None):
            answer = "I don't know that. Sorry"

        print(Fore.GREEN + answer + Style.RESET_ALL)
        user_input = input(">>> ")  