import spacy
from spacy.matcher import Matcher

nlp = spacy.load('en_core_web_sm')
# set up the Matcher once, outside the loop
matcher = Matcher(nlp.vocab)
pattern = [
    {"POS": "PRON"},
    {"POS": "VERB"},
]
matcher.add("pronVerbPattern", [pattern])

reviews = [
    'I bought this laptop from Amazon last week and it works great!',
    'The delivery from FedEx was terrible, my package arrived broken.',
    'Sarah recommended this phone and I love how fast it charges.'
]
for review in reviews:
    doc = nlp(review)
    print(f"Review: {review}")

    for ent in doc.ents:
        if ent.label_ == "ORG":
            print(f"  ORG found: {ent.text}")

    for token in doc:
        if token.pos_ == "ADJ":
            print(f"  Adjective found: {token.text}")
        if token.dep_ == "ROOT":
            print(f"Root verb found: {token.text}")
    
    matches = matcher(doc)
    for match_id, start, end in matches:
        print(f"  Pronoun+Verb pattern: {doc[start:end].text}")
    print()