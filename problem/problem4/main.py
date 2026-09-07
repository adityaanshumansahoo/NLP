import spacy

nlp = spacy.load("en_core_web_sm")
sentences = [
    "Led a team of 5 engineers and increased revenue by 30 percent using automation tools.",
    "Reduced deployment time by 40% after migrating to Docker.",
    "Helped organize weekly meetings.",
    "build a mern stack website and deliver it in 5 days"
]
   
def find_main_verb_and_object(doc):
    candidates = []
    for token in doc:
        if token.dep_ == "ROOT" and token.pos_ == "VERB":
            for child in token.children:
                if child.dep_ == "dobj":
                    candidates.append((token, child))
    for token in doc:
        for child in token.children:
            if child.dep_ == "amod" and child.pos_ == "VERB":
                candidates.append((child, token))
    for token in doc:
        for child in token.children:
            if child.dep_ == "nummod" and child.pos_ == "NUM":
                candidates.append((child,token))
    return candidates


for sentence in sentences:
    doc = nlp(sentence)
    print(f"\nSentence: {sentence}")
    candidates = find_main_verb_and_object(doc)
    for token in doc:
        print(f"  {token.text} -> {token.dep_} ({token.pos_})")
    print(candidates)
