import spacy
from spacy import displacy

sentence = "Led a team of 5 engineers and increased revenue by 30 percent using automation tools."

nlp = spacy.load("en_core_web_sm")
doc = nlp(sentence)

html = displacy.render(doc, style="dep", jupyter=False)

with open("dependency_parse.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Saved to dependency_parse.html — open it in a browser to view.")