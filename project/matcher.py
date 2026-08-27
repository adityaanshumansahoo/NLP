import spacy
from spacy.matcher import Matcher

nlp = spacy.load("en_core_web_sm")
doc = nlp("Sundar Pichai announced that Google will invest $10 billion in India by 2027.")

matcher = Matcher(nlp.vocab)
pattern = [
    {"POS": "AUX"},
    {"POS": "VERB"},
]
matcher.add("investPattern", [pattern])

matches = matcher(doc)
for match_id, start, end in matches:
    print(doc[start:end].text)