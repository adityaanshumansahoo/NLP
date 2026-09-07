from rapidfuzz import fuzz

name = input("Enter your hospital name: ")

hospitals = [
    "Apollo Hospital Bhubaneswar",
    "AIIMS Bhubaneswar",
    "KIMS Hospital Bhubaneswar",
    "SUM Ultimate Hospital"
]

best_score = 0
best_hospital = None

for hospital in hospitals:
    score = fuzz.ratio(name, hospital)

    if score > best_score:
        best_score = score
        best_hospital = hospital

if best_score > 80:
    print(f"Match found: {best_hospital} with score: {best_score}")
else:
    print("Match not found")