import pandas as pd 
import spacy
from sklearn.feature_extraction.text import TfidfTransformer, TfidfVectorizer

# read json
data = pd.read_json("data.json")
data.columns = ["questions", "responses"]

# load language model
nlp = spacy.load("en_core_web_lg")

tfidf = TfidfVectorizer(min_df=2, max_df = 0.2, ngram_range=(1, 3))


def get_input():
    input_text = "Is it true?"    
    
    return input_text

def get_response_retrieval_based(input):
    id, similarity = find_matching_question_id(input)
    return data.responses[id], similarity

def find_matching_question_id(input_text):
    input_nlp = nlp(input_text)

    most_similar_question_id = 0
    most_similar_question_similarity = 0

    for id, question in enumerate(data.questions):
        question_nlp = nlp(question)

        if question_nlp.vector_norm:
            similarity = input_nlp.similarity(question_nlp)

            if similarity > most_similar_question_similarity:
                most_similar_question_id = id
                most_similar_question_similarity = similarity
             
    return most_similar_question_id, most_similar_question_similarity

def get_response(user_input):
    rule_based_text, rule_based_similarity = get_response_retrieval_based(user_input)
    if(rule_based_similarity > 0.5):
        return rule_based_text

# MAIN METHOD
if __name__ == '__main__':
    # Get Input
    user_input = input(">>> ")
    while "exit" not in user_input.lower():
        print(get_response(user_input))
        
        user_input = input(">>> ")

    # Get Matching Question
    # print(find_matching_question(input))