import spacy

# Load the small English language model
nlp = spacy.load("en_core_web_sm")

text = "The striped bats were hanging upside down while mice ate better cheese."
doc = nlp(text)

print(f"{'Original Word'} | {'POS Tag'} | {'Lemma'}")
print("-" * 42)

for token in doc:
    if not token.is_punct:
        print(f"{token.text:<15} | {token.pos_:<10} | {token.lemma_:<10}")