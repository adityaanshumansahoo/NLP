import spacy
from spacy.tokens import Span
from spacy.matcher import PhraseMatcher
from spacy import displacy
nlp = spacy.load("en_core_web_sm")