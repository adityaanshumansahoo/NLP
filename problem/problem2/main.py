import spacy
from nltk.stem import PorterStemmer
import nltk
from nltk.corpus import stopwords
from collections import Counter

nlp = spacy.load("en_core_web_sm")

nltk.download("stopwords")
stop_words = set(stopwords.words("english"))

stemmer = PorterStemmer()

reviews = [
    "The pasta at Olive Garden was amazing but the waiter, Mike, was rude.",
    "I ordered biryani from Zomato and it arrived cold after 2 hours.",
    "My mom loves this cafe near Bhubaneswar, she visits every Sunday for tea and the tea was bad because the tea was very sweet",
    "Terrible service! Never ordering from Swiggy again.",
]

review_intelligence = {}
all_words = []

for i, review in enumerate(reviews):

    doc = nlp(review)

    # 1. Sentence segmentation
    sentences = [sent.text for sent in doc.sents]

    # 2. Tokenization
    tokens = [token.text for token in doc]

    # 3. Stopword removal
    filtered_words = [
        token.text
        for token in doc
        if token.text.lower() not in stop_words
        and not token.is_punct
    ]

    all_words.extend(filtered_words)

    # 4. Stemming vs Lemmatization
    stem_lemma_pairs = [
        (
            token.text,
            stemmer.stem(token.text),
            token.lemma_
        )
        for token in doc
        if not token.is_punct
    ]

    # 5. POS tagging
    pos_tags = [
        (token.text, token.pos_, token.tag_)
        for token in doc
    ]

    # 6. NER
    entities = {
        "ORG": [],
        "PERSON": [],
        "GPE": [],
        "DATE": []
    }
    for ent in doc.ents:
        if ent.label_ in entities:
            entities[ent.label_].append(ent.text)
    # 8. Noun_chunks
    noun_chunks = [
        chunk.text
        for chunk in doc.noun_chunks
        ]
    # 9. dependency
    dependency_tree = [
        (
            token.text,
            token.head.text,
            token.dep_
        )
        for token in doc
    ]
    # 10.
    adjective_noun_pairs = []

    for token in doc:
        if token.pos_ != "ADJ":
            continue
        if token.dep_ == "amod" and token.head.pos_ in ("NOUN", "PROPN"):
            adjective_noun_pairs.append((token.text, token.head.text))

    # Case 2: predicative — "pasta was amazing" (acomp/attr: adj complements a copula verb)
        elif token.dep_ in ("acomp", "attr"):
            verb = token.head
            for child in verb.children:
                if child.dep_ in ("nsubj", "nsubjpass") and child.pos_ in ("NOUN", "PROPN"):
                    adjective_noun_pairs.append((child.text, token.text))
            
    # Store everything for this review
    review_intelligence[i] = {
        "text": review,
        "sentences": sentences,
        "tokens": tokens,
        "filtered_words": filtered_words,
        "stem_lemma": stem_lemma_pairs,
        "pos_tags": pos_tags,
        "entities": entities,
        "noun_chunks": noun_chunks,
        "dependency_word":dependency_tree,
    }


# 7. Overall word frequency
word_frequency = Counter(
    word.lower()
    for word in all_words
)

review_intelligence["word_frequency"] = word_frequency 




