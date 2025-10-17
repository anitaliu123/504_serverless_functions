import requests, json

URL = "https://hba1c-1-hcdmhreya7cmatc8.northcentralus-01.azurewebsites.net/api/hba1c_classifier"

for ex in ({"hba1c": 6.3}, {"hba1c": 6.8}):
    r = requests.post(URL, json=ex, timeout=15)
    print("\n→ Sent:", ex)
    print("← Status:", r.status_code)
    print("← Body  :", r.text)
    try:
        print("← JSON  :", json.dumps(r.json(), indent=2, ensure_ascii=False))
    except Exception:
        pass
