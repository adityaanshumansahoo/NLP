import re
samples = [
    "Quantity: 50 items",
    "Price: $50",
    "Total: ₹50",
    "Count: 50",
]
def extract_non_rupee_number(text: str) -> str | None:
    match = re.search(r"(?<![$₹])\b\d+\b", text)    
    return match.group(0) if match else None

results = [extract_non_rupee_number(sample) for sample in samples]
print(results)