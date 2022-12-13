# Import the TfidfVectorizer and spaCy lemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from spacy.lemmatizer import Lemmatizer
from spacy.lang.en import LEMMA_INDEX, LEMMA_EXC, LEMMA_RULES

# Define a custom preprocessing function that uses the spaCy lemmatizer
def preprocess(text):
    # Create a spaCy lemmatizer
    lemmatizer = Lemmatizer(LEMMA_INDEX, LEMMA_EXC, LEMMA_RULES)

    # Lemmatize the text using spaCy
    lemmas = lemmatizer(text)

    # Return the lemmatized text
    return " ".join([lemma[0] for lemma in lemmas])

# Define a custom tokenization function that uses the spaCy lemmatizer
def tokenize(text):
    # Create a spaCy lemmatizer
    lemmatizer = Lemmatizer(LEMMA_INDEX, LEMMA_EXC, LEMMA_RULES)

    # Tokenize the text using spaCy
    tokens = nlp(text)

    # Lemmatize the tokens using spaCy
    lemmas = [token.lemma_ for token in tokens]

    # Return the lemmatized tokens
    return lemmas

# Create a TfidfVectorizer object with the custom preprocessing and tokenization functions
tfidf_vector = TfidfVectorizer(preprocessor=preprocess, tokenizer=tokenize)

# Fit the TfidfVectorizer to the documents
tfidf_vector.fit(documents)
