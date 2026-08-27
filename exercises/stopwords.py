import spacy
import nltk
from nltk.corpus import stopwords

nltk.download("stopwords")          
nlp = spacy.load("en_core_web_sm")
doc = nlp("I don't like cooking, I prefer eating!!!")
stop_words = set(stopwords.words("english"))

result = []
for word in doc:
    if word.text.lower() not in stop_words:   # compare .text, not the token object
        result.append(word.text)
print(result)