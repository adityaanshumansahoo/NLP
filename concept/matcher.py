import spacy
from spacy.matcher import Matcher
from spacy.tokens import Span
from spacy import displacy

# 1. Load model and create Matcher
nlp = spacy.load("en_core_web_sm")
matcher = Matcher(nlp.vocab)

pattern = [
    {"LOWER": "good"},
    {"LOWER": "morning"},
    {"IS_PUNCT": True},
]
matcher.add("monrningGreeting", [pattern])

# 2. Process text into a Doc object FIRST
doc = nlp("Good morning, My name is Marcello Politi!")
matches = matcher(doc)

# 3. Collect matching Spans
spans = []
for match_id, start, end in matches:
    spans.append(Span(doc, start, end, label=match_id))

# 4. Save spans under the SpanCategorizer key "sc"
doc.spans["sc"] = spans

# 5. Render at the VERY END (pass the "sc" key option)
displacy.render(doc, style="span", options={"spans_key": "sc"})
print(spans)