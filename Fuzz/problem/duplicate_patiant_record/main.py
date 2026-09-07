from rapidfuzz import fuzz
from storage import patients
def normalize(text):
    text = text.lower().strip()
    return text


def find_duplicate_patients(patients):
    clusters = []

    for patient in patients:
        matched = False

        for cluster in clusters:
            current_patient = cluster["representative"]

            name_score = fuzz.ratio(
                normalize(patient["name"]),
                normalize(current_patient["name"])
            )

            phone_match = patient["phone"] == current_patient["phone"]
            age_match = patient["age"] == current_patient["age"]

            if name_score > 60 and phone_match and age_match:
                cluster["ids"].append(patient["id"])
                matched = True
                break

        if matched == False:
            clusters.append({
                "ids": [patient["id"]],
                "representative": patient
            })

    # Print results
    for cluster in clusters:
        if len(cluster["ids"]) > 1:
            print("Duplicate group:", cluster["ids"])
        else:
            print("Unique patient:", cluster["ids"])

    return clusters
print(find_duplicate_patients(patients))