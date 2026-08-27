import spacy
from spacy.symbols import ORTH
nlp = spacy.load("en_core_web_sm")

special_case = [{ORTH: "Adi"}, {ORTH: "tya"}]
nlp.tokenizer.add_special_case("Aditya", special_case)
doc = nlp("Aditya is learning spaCy")

for index,word in enumerate(doc,start=1):
    print(f"Token_{index}:{word}")