from sklearn.feature_extraction.text import TfidfTransformer, TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import yaml
import pandas as pd 
import numpy as np
import pickle
from colorama import Fore, Style

# Load the contents of the YAML file into a dictionary
with open("config.yml", "r") as f:
    config = yaml.safe_load(f)

# read json
data = pd.read_json("corpus_based/data.json")
data.columns = ["questions", "responses"]

# load the vectors from the file
with open("corpus_based/vectors.pkl", "rb") as f:
    question_vectors = pickle.load(f)

# Access the values in the configuration
min_df = config["TFIDF"]["min_df"]
max_df = config["TFIDF"]["max_df"]
ngram_range = (config["TFIDF"]["ngram_range_min"], config["TFIDF"]["ngram_range_max"])

# define tfidf
tfidf = TfidfVectorizer(min_df=min_df, max_df=max_df, ngram_range=ngram_range, stop_words={'english'}, sublinear_tf=True)
tfidf.fit_transform(data.questions + data.responses)

def corpusbased_answer(user_input : str, required_similarity : float):
    user_input_tfidf = tfidf.transform([user_input])

    similarities = cosine_similarity(user_input_tfidf, question_vectors)

    idx = np.argsort(similarities)[0][-1]

    print(Fore.RED + "DEBUG: Question: " + data.loc[idx, "questions"] + ", Similarity: " + str(similarities[0][idx]) + Style.RESET_ALL) #Debugging

    if(similarities[0][idx] < required_similarity):
        return None

    return data.loc[idx, "responses"]