import re
import spacy
import nltk
from nltk.corpus import stopwords

# Load English NLP model
nlp = spacy.load("en_core_web_sm")

# Download NLTK stopwords if not available
nltk.download('stopwords')
STOPWORDS = set(stopwords.words('english'))

def clean_text(text):
    """Removes special characters, numbers, and extra spaces."""
    text = re.sub(r"[^a-zA-Z\s]", "", text)  # Keep only letters and spaces
    text = re.sub(r"\s+", " ", text).strip()  # Remove extra spaces
    return text.lower()

def remove_stopwords(text):
    """Removes stopwords using NLTK."""
    return " ".join([word for word in text.split() if word not in STOPWORDS])

def lemmatize_text(text):
    """Lemmatizes text using spaCy."""
    doc = nlp(text)
    return " ".join([token.lemma_ for token in doc if token.is_alpha])

def preprocess_pipeline(text):
    """Applies full text preprocessing pipeline: cleaning, stopword removal, and lemmatization."""
    text = clean_text(text)
    text = remove_stopwords(text)
    text = lemmatize_text(text)
    return text
