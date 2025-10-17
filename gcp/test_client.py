# test_client.py
import requests, json, sys

url = "https://hba1c-triage-718737153982.us-central1.run.app"

def test(payload):
    try:
        print(f"\n→ Sending: {payload}")
        r = requests.post(url, json=payload, timeout=10)
        print("Status code:", r.status_code)
        print("Response:", r.text)
        try:
            print("JSON:", json.dumps(r.json(), indent=2, ensure_ascii=False))
        except Exception:
            pass
    except Exception as e:
        print("Error:", e)
        sys.exit(1)

if __name__ == "__main__":
    test({"hba1c": 6.3})  # normal
    test({"hba1c": 6.8})  # abnormal
