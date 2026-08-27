import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("John was born in Rome and now works at Google, earning $150,000 a year")

for ent in doc.ents:
    print(f"{ent.text} --> {ent.label_} --> {spacy.explain(ent.label_)}")