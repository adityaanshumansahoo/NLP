from sklearn.feature_extraction.text import CountVectorizer

sentences = [
    "I love Python",
    "I love Java",
    "Python is easy"
]

vectorizer = CountVectorizer()

result = vectorizer.fit_transform(sentences)

print(vectorizer.get_feature_names_out())
print(result.toarray())