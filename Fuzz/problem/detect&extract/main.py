from rapidfuzz import fuzz
import re
text = """
Patient: Rahul Kumar
Hospital: Apollo Hospitl, Bhubaneswr 
Admission: Date: 12-08-2026
Phone: 9835743740
Amount: ₹45000
"""
hospitals = [
    "Apollo Hospital Bhubaneswar",
    "AIIMS Bhubaneswar",
    "KIMS Hospital Bhubaneswar",
    "SUM Ultimate Hospital"
]
def extract_hospital_name(text):
    match = re.search(r"(?<=Hospital:)(.+)", text)
    if match:
        return match.group(1).strip()
    return None
def match_hospital_name(extracted_name, hospitals):
    score_accuracy=0
    hospital_name=None
    for hospital in hospitals:
        score = fuzz.ratio(extracted_name,hospital)
        
        if score > score_accuracy:
            score_accuracy = score
            hospital_name = hospital
    return hospital_name, score_accuracy
matched_hospital, similarity_score = match_hospital_name(extract_hospital_name(text), hospitals)
if similarity_score > 50:
    print(f"Match found: {matched_hospital}, with accuracy_score: {round(similarity_score,2)}%")
else:
    print("Match not found")

