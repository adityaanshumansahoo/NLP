from rapidfuzz import fuzz

streets = [
    "Janpath Road",
    "Cuttack Road",
    "Bapuji Nagar Road",
    "Saheed Nagar Road",
    "Rasulgarh Main Road"
]

input_street = "cuttack Rd."

def normalize(text):
    text = text.lower().strip()
    return text

def highest_similarity(input_street, streets):
    highest_score = 0
    best_match = None
    normalized_input = normalize(input_street)

    for street in streets:
        score = fuzz.ratio(normalize(street), normalized_input)
        if score > highest_score:
            highest_score = score
            best_match = street

    return best_match, highest_score

match_street, high_probability = highest_similarity(input_street, streets)
print(f"Matching street: {match_street} || match probability: {high_probability}")