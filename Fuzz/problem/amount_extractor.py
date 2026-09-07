import re

amount_samples = [
    "₹45,000",
    "Rs. 45000/-",
    "INR 45,000.00",
    "45000 rupees only",
    "Rs 1,20,000",
    "₹ 999.50",
    "amount: 7500",
    "Total Due: Rs.2,300.75/-",
    "8,00,000 INR",
    "Free",
    "Rs. --",
]


def extract_amount(text):
    # Step A: find where a currency signal starts
    currency_pattern = r"(?:₹|Rs\.?|INR|Amount|Total\s*Due)[:\s]*"
    match = re.search(currency_pattern + r"(\d[\d,]*(?:\.\d+)?)", text, re.IGNORECASE)
    
    if match:
        clean_str = match.group(1).replace(",", "")
        return float(clean_str)
    
    return None


# Run test
results = [extract_amount(sample) for sample in amount_samples]
print(results)