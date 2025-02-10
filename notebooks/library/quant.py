import pandas as pd
import numpy as np
import nltk
from nltk.corpus import stopwords
nltk.download("stopwords")
nltk.download("punkt")
nltk.download("punkt_tab")
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from collections import Counter
import regex as re


#create function to preprocess data
def preprocessor (data, col):
  #Lower the lettercase
  data[col] = data[col].str.lower()

  #Remove stop words
  stop_words = set(stopwords.words("english"))
  data[col] = data[col].apply(lambda x: " ".join([word for word in str(x).split() if word not in (stop_words)]))

  #Tokenize the word
  data[col] = data[col].apply(word_tokenize)

  #Remove numbers
  data[col] = data[col].apply(lambda x: [word for word in x if not word.isdigit()])

  #remove symbol from comments
  data[col] = data[col].apply(lambda x: [word for word in x if x!=""])

  #remove short word
  data[col] = data[col].apply(lambda x: [word for word in x if len(word)>2])

  #remove symbols
  data[col] = data[col].apply (lambda x: [re.sub(r"[^a-z]", "", word) for word in x])

  #remove stemmers
  stemmer =PorterStemmer()
  data[col] = data[col].apply(lambda x: [stemmer.stem(word)for word in x])
  
  return

def remove_freq_words(data, col, percent):
  #Flatten the list of tokens
  all_tokens = [token for sublist in data[col] for token in sublist]

#calculate word frequencies
  word_freq = Counter(all_tokens)

#Convert it to DF
  word_freq_df = pd.DataFrame(word_freq.items(), columns = ["word","freq"])

#Identify the to 5% most frequent words
  top_5_percent = word_freq_df.nlargest(int(len(word_freq_df)*percent), "freq")["word"]

  filtered_data = []
  for sentence in data[col]:
    filtered_sentence = [word for word in sentence if word not in top_5_percent.values]
    filtered_data.append(" ".join(filtered_sentence))

  return filtered_data
