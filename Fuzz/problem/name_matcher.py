from rapidfuzz import fuzz

names = [
    "Aditya Ansuman Sahoo",
    "Rahul Kumar",
    "Amit Sharma",
    "Priya Das"
]
input_name = input("Enter your name: ")

accuracy = 0
correct_name = None

for name in names:
    score = fuzz.ratio(name, input_name)
    if score > accuracy:
        accuracy = score
        correct_name = name

if accuracy > 80:
    print(f"Match found: {correct_name} with accuracy: {accuracy}")
else:
    print(f"No good match found. Closest: {correct_name} with accuracy: {accuracy}")