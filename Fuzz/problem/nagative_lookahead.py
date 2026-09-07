import re

samples = [
    "Room No: 45",
    "Amount: 45",
    "45₹",
]


def extract_non_rupee_number(text: str) -> str | None:
    match = re.search(r"\d+(?!\s*₹)", text)
    return match.group(0) if match else None

results = [extract_non_rupee_number(sample) for sample in samples]
print(results)
# Matches digits ONLY IF NOT immediately followed by optional spaces and '₹'