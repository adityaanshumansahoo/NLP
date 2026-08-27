import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("My name is Aditya. I like coding a lot! Do you like Python too?")

for index, sent in enumerate(doc.sents, start=1):
    print(f"Sentence_{index}:{sent.text}")