import spacy

nlp = spacy.load("en_core_web_sm")

# Notice 'quick' is lowercase here
doc = nlp("The quick red fox jumps.")

for token in doc:
    print(f"{token.text:<8} -> {token.dep_:<8} (head: {token.head.text})")