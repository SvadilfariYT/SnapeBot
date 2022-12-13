import pandas as pd 
import spacy
from sklearn.feature_extraction.text import TfidfTransformer, TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle
import numpy as np
import yaml

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

# MAIN METHOD
if __name__ == '__main__':
    user_input = input(">>> ")
    
    while "exit" not in user_input.lower():
        user_input_tfidf = tfidf.transform([user_input])

        similarities = cosine_similarity(user_input_tfidf, question_vectors)

        idx = np.argsort(similarities)[0][-1]
        print(data.loc[idx, "responses"])
        user_input = input(">>> ")
