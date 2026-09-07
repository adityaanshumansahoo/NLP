import re

samples = [
    "Weight: 70kg",
    "Weight: 70 kg",
    "Distance: 70km",
    "Height: 170cm",
]

def extract_kg(text):
    match = re.search(r"\d+(?=\s*kg)", text)
    return match.group(0) if match else None

results = [extract_kg(sample) for sample in samples]
print(results)