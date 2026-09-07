import re

samples = [
    "abc123",
    "abcdef",
    "Passw0rd",
]


def validate_password(text: str) -> str | None:
    match = re.search(r"^(?=.*\d).*$", text)
    return match.group(0) if match else None

results = [validate_password(sample) for sample in samples]
print(results)

''' Note:Lookahead (?=.*\d) checks if at least 1 digit exists anywhere in the string  [^.*$] then matches the entire string from start to finish '''