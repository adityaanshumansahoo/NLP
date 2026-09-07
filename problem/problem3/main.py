import spacy
from spacy.matcher import Matcher, PhraseMatcher

# Load the spaCy English model
nlp = spacy.load("en_core_web_sm")

# Add an EntityRuler before the statistical NER pipe
ruler = nlp.add_pipe("entity_ruler", before="ner")

# Define custom entity patterns
ruler_patterns = [
    # Explicit Companies (ORG)
    {"label": "ORG", "pattern": "Netflix"},
    {"label": "ORG", "pattern": "Google"},
    {"label": "ORG", "pattern": "Microsoft"},
    {"label": "PRODUCT", "pattern": "Python"}
]

ruler.add_patterns(ruler_patterns)

resumes = [
    "I worked at Google for 3 years and built scalable backend systems using Python.",
    "Led a team of 5 engineers at Microsoft and helped launch a new product in 2022.",
    "Managed data pipelines at Netflix and improved system performance significantly."
]

# PhraseMatcher for Verb Strengths (Using full nlp() to generate LEMMA)
verb_matcher = PhraseMatcher(nlp.vocab, attr="LEMMA")
strong_verbs = [nlp(v) for v in ["lead", "build", "manage", "improve"]]
weak_verbs = [nlp(v) for v in ["help", "work"]]
verb_matcher.add("STRONG", strong_verbs)
verb_matcher.add("WEAK", weak_verbs)

# Matcher for Skill Patterns
skill_matcher = Matcher(nlp.vocab)
pattern_1 = [{"POS": "VERB"}, {"POS": "ADJ"}, {"POS": "NOUN", "OP": "*"}, {"POS": "NOUN"}]
pattern_2 = [{"POS": {"IN": ["VERB", "NOUN"]}}, {"POS": "DET", "OP": "*"}, {"POS": "NUM", "OP": "*"},{"POS": "ADJ", "OP": "*"},{"POS": "NOUN", "OP": "+"}]
skill_matcher.add("SKILL", [pattern_1, pattern_2])

for resume in resumes:
    doc = nlp(resume)
    print(f"\nResume: {resume}")
    
    # Part 1: Tokens and Lemmas
    print("\nTokens & Lemmas:")
    for token in doc:
        if not token.is_punct:
            print(f"  {token.text} -> {token.lemma_}")
            
    # Part 2: Entities & Root Verb
    companies = [ent.text for ent in doc.ents if ent.label_ == "ORG"]
    durations = [ent.text for ent in doc.ents if ent.label_ == "DATE"]
    root_verb = [token.text for token in doc if token.dep_ == "ROOT"]
    
    # Part 3: Action Verb Strength
    verb_matches = verb_matcher(doc)
    verb_strengths = []
    for match_id, start, end in verb_matches:
        category = nlp.vocab.strings[match_id]
        word = doc[start:end].text
        verb_strengths.append(f"{category.lower()} ({word})")
        
    # Part 4: Skill Phrases
    skill_matches = skill_matcher(doc)
    skills = [doc[start:end].text for match_id, start, end in skill_matches]
    
    # Display Summary
    print("\nExtraction Summary:")
    print(f"  Companies:            {', '.join(companies) if companies else 'None'}")
    print(f"  Durations:            {', '.join(durations) if durations else 'None'}")
    print(f"  Root verb:            {', '.join(root_verb) if root_verb else 'None'}")
    print(f"  Action verb strength: {', '.join(verb_strengths) if verb_strengths else 'None'}")
    print(f"  Skill phrases:        {', '.join(set(skills)) if skills else 'None'}")