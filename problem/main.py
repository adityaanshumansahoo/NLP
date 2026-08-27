import spacy
from spacy.matcher import PhraseMatcher
from spacy.tokens import Span

nlp = spacy.load("en_core_web_sm")

headlines = [
    "Sundar Pichai announced that Google will invest $10 billion in India by 2027.",
    "Tim Cook confirmed Apple plans to open a new office in Bangalore next year.",
    "Elon Musk said Tesla will build a factory in Germany worth $5 billion by 2026."
]

# known people we want to force-tag as PERSON
known_people = ["Sundar Pichai", "Tim Cook", "Elon Musk"]
person_matcher = PhraseMatcher(nlp.vocab)
person_patterns = [nlp.make_doc(name) for name in known_people]
person_matcher.add("KNOWN_PERSON", person_patterns)

for headline in headlines:
    doc = nlp(headline)

    # find any known-person matches
    matches = person_matcher(doc)

    # remove any existing entities that overlap with a known-person match
    # (so we don't get duplicate/conflicting spans, e.g. ORG + PERSON on same words)
    new_ents = []
    for ent in doc.ents:
        overlaps = any(start < ent.end and end > ent.start for _, start, end in matches)
        if not overlaps:
            new_ents.append(ent)

    # add the corrected PERSON entities
    for match_id, start, end in matches:
        new_ents.append(Span(doc, start, end, label="PERSON"))

    doc.ents = sorted(new_ents, key=lambda e: e.start)

    print(f"Headline: {headline}")
    for ent in doc.ents:
        print(f"  {ent.text}: {ent.label_}")
    print(new_ents)