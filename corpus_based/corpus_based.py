from sklearn.feature_extraction.text import TfidfTransformer, TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import yaml
import pandas as pd 
import numpy as np
import pickle
from colorama import Fore, Style
import spacy
import re

characters = ["Snape", "Hagrid", "Dumbledore", "Draco"]

nlp = spacy.load("en_core_web_lg")

# Load the contents of the YAML file into a dictionary
with open("config.yml", "r") as f:
    config = yaml.safe_load(f)

# read jsons
data = pd.read_json("corpus_based/data.json")
data.columns = ["questions", "responses"]

data_2 = pd.read_json("corpus_based/data_2.json")
data_2.columns = ["questions", "responses"]

# load the vectors from the file
with open("corpus_based/vectors.pkl", "rb") as f:
    question_vectors = pickle.load(f)

with open("corpus_based/vectors_2.pkl", "rb") as f:
    question_vectors_2 = pickle.load(f)

# Access the values in the configuration
min_df = config["TFIDF"]["min_df"]
max_df = config["TFIDF"]["max_df"]
ngram_range = (config["TFIDF"]["ngram_range_min"], config["TFIDF"]["ngram_range_max"])

# define tfidfs
tfidf = TfidfVectorizer(min_df=min_df, max_df=max_df, ngram_range=ngram_range, stop_words={'english'}, sublinear_tf=True)
tfidf.fit_transform(data.questions + data.responses)

tfidf_2 = TfidfVectorizer(min_df=min_df, max_df=max_df, ngram_range=ngram_range, stop_words={'english'}, sublinear_tf=True)
tfidf_2.fit_transform(data_2.questions + data_2.responses)

def corpusbased_answer(user_input : str, required_similarity : float):
    user_input_tfidf = tfidf.transform([user_input])

    similarities = cosine_similarity(user_input_tfidf, question_vectors)

    idx = np.argsort(similarities)[0][-1]

    question = data.loc[idx, "questions"] 
    response = data.loc[idx, "responses"] 
    similarity = similarities[0][idx]

    response = replace_entities(user_input, response)

    print(Fore.RED + "DEBUG Harry: Question: " + question + "\n Answer: " + response + "\n Similarity: " + str(similarity) + Style.RESET_ALL) #Debugging

    if(similarity < required_similarity):
        return None

    return response

def corpusbased_answer_2(user_input : str, required_similarity : float):
    user_input_tfidf = tfidf_2.transform([user_input])

    similarities = cosine_similarity(user_input_tfidf, question_vectors_2)

    idx = np.argsort(similarities)[0][-1]

    question = data_2.loc[idx, "questions"] 
    response = data_2.loc[idx, "responses"] 
    similarity = similarities[0][idx]

    response = replace_entities(user_input, response)

    print(Fore.RED + "DEBUG GPT: Question: " + question + "\n Answer: " + response + "\n Similarity: " + str(similarity) + Style.RESET_ALL) #Debugging

    if(similarity < required_similarity):
        return None

    return response

def replace_entities(input : str, output : str):
    input_nlp = nlp(input)
    output_nlp = nlp(output)


    person = "wizard"

    for ent in input_nlp.ents:
        if ent.label_ == "PERSON":
            person = ent
        elif ent.label_ == "ORG":
            person = "Bürgerbüro"

    for ent in output_nlp.ents:
        output = replace_entity(output, ent, person, "PERSON")

    output = replace_entity_custom(output, characters, person)

    return output

def replace_entity(output : str, ent, new_ent, label: str):
    if ent.label_ == label:
            output = re.sub(ent.text, new_ent, output)
    return output

def replace_entity_custom(output, list, entity):
    for element in list:
        if element in output:
            output = re.sub(element, entity, output)