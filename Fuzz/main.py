from rapidfuzz import fuzz

score = fuzz.ratio("Apollo Hospital", "Apollo Hospitl")

print(score)