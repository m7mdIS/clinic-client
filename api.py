import requests

BASE_URL = "http://127.0.0.1:8000"


def create_patient(data):
    try:
        # Backend route is POST /patient/add (see FastAPI router prefix)
        response = requests.post(f"{BASE_URL}/patient/add", json=data)

        if response.status_code in (200, 201):
            print("✅ Patient saved successfully")
        else:
            print("❌ Backend error:", response.text)

    except Exception as e:
        print("❌ API connection failed:", e)
