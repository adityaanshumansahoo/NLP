import re

samples = [
    "Diagnosis: Fever",
    "Symptom: Fever",
    "Fever reported by patient",
]


def extract_diagnosis(text):
    match = re.search(r"(?<=Diagnosis:\s)\w+", text)
    return match.group(0) if match else None

results = [extract_diagnosis(sample) for sample in samples]
print(results)