import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("Sundar Pichai announced that Google will invest $10 billion in India by 2027.")

for index, word in enumerate(doc, start=1):
    print(f"Token_{index}:{word}")