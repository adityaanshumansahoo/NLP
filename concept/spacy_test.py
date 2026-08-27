import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("I can't believe it's already 5pm???")

for index, word in enumerate(doc, start=1):
    print(f"Token_{index}:{word}")