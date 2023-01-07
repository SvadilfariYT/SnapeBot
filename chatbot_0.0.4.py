import pandas as pd 
import spacy
from sklearn.feature_extraction.text import TfidfTransformer, TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle
import numpy as np
import yaml
from reflections import reflect
from text_patterns import patterns
import re
import random
from colorama import Fore, Back, Style

# Load the contents of the YAML file into a dictionary
with open("config.yml", "r") as f:
    config = yaml.safe_load(f)

# Access the values in the configuration
min_df = config["DEFAULT"]["min_df"]
max_df = config["DEFAULT"]["max_df"]
ngram_range = (config["DEFAULT"]["ngram_range_min"], config["DEFAULT"]["ngram_range_max"])

# read json
data = pd.read_json("data.json")
data.columns = ["questions", "responses"]

# load the vectors from the file
with open("vectors.pkl", "rb") as f:
    question_vectors = pickle.load(f)

# load language model
nlp = spacy.load("en_core_web_lg")

# define tfidf
tfidf = TfidfVectorizer(min_df=min_df, max_df=max_df, ngram_range=ngram_range, stop_words={'english'}, sublinear_tf=True)
tfidf.fit_transform(data.questions + data.responses)

def templatebased_answer(user_input : str):
# Test input string for all known text patterns in pychobabble
    for pattern, responses in patterns:
        match = re.search(pattern.lower(), str(user_input).lower().strip())
        if match:
            answer = random.choice(responses)
            return answer.format(*[reflect(g.strip(",.?!")) for g in match.groups()])
    return None

def corpusbased_answer(user_input : str, required_similarity : float):
    user_input_tfidf = tfidf.transform([user_input])

    similarities = cosine_similarity(user_input_tfidf, question_vectors)

    idx = np.argsort(similarities)[0][-1]

    print(Fore.RED + "DEBUG: Question: " + data.loc[idx, "questions"] + ", Similarity: " + str(similarities[0][idx]) + Style.RESET_ALL) #Debugging

    if(similarities[0][idx] < required_similarity):
        return None

    return data.loc[idx, "responses"]

# MAIN METHOD
if __name__ == '__main__':
    user_input = input(">>> ").lower().strip()
    
    while "exit" not in user_input.lower():
        answer = ""
        
        # Eliza-Like-Pattern-Matching
        answer = templatebased_answer(user_input)

        # TFIDF
        if(answer == None):
            answer = corpusbased_answer(user_input, 0.5)

        # Standard Answer
        if(answer == None):
            answer = "I don't know that. Sorry"

        print(Fore.GREEN + answer + Style.RESET_ALL)
        user_input = input(">>> ")  