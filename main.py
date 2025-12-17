from fingerprint import enroll_fingerprint
from api import create_patient


def main():
    print("\n=== CLINIC CLIENT ===")
    print("1. Register new patient")
    choice = input("Select option: ")

    if choice != "1":
        print("Invalid option")
        return

    fingerprint_id = enroll_fingerprint()

    if fingerprint_id is None:
        print("Enrollment failed")
        return

    print("\nEnter patient details")

    name = input("Full name: ")
    age = int(input("Age: "))
    medical_history = input("Medical history: ")
    allergies = input("Allergies: ")
    medications = input("Current medications: ")

    # Match backend PatientCreate schema exactly
    patient_data = {
        "fingerprint_id": str(fingerprint_id),
        "name": name,
        "age": age,
        "medical_history": medical_history,
        "allergies": allergies,
        "medications": medications,
    }

    create_patient(patient_data)


if __name__ == "__main__":
    main()
