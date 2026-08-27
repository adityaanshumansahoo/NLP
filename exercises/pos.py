import spacy
from spacy.matcher import Matcher

nlp = spacy.load("en_core_web_sm")
doc = nlp("I read a good book. I need to book a flight.")

matcher = Matcher(nlp.vocab)
# Match "book" ONLY when used as a VERB
pattern = [{"LOWER": "book", "POS": "VERB"}]
matcher.add("BOOK_VERB", [pattern])

for match_id, start, end in matcher(doc):
    print(doc[start:end].text)
# Output: book (only matches "book a flight")