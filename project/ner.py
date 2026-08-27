import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("Sundar Pichai announced that Google will invest $10 billion in India by 2027.")

for ent in doc.ents:
    print(f"{ent.text} --> {ent.label_} --> {spacy.explain(ent.label_)}")