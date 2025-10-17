import json
import functions_framework

@functions_framework.http
def hba1c_triage(request):
    """HTTP Cloud Function for binary HbA1c classification.
    Normal if < 6.5%, otherwise Abnormal.
    """
    data = request.get_json(silent=True) or {}
    args = request.args or {}
    hba1c = data.get("hba1c", args.get("hba1c"))

    if hba1c is None:
        return (
            json.dumps({"error": "'hba1c' is required."}),
            400,
            {"Content-Type": "application/json"},
        )

    try:
        hba1c_val = float(hba1c)
    except (TypeError, ValueError):
        return (
            json.dumps({"error": "'hba1c' must be a number."}),
            400,
            {"Content-Type": "application/json"},
        )

    # Binary classification for assignment
    if hba1c_val < 6.5:
        status = "normal"
        category = "Normal (<6.5%)"
    else:
        status = "abnormal"
        category = "Abnormal (≥6.5%)"

    payload = {"hba1c": hba1c_val, "status": status, "category": category}

    return json.dumps(payload), 200, {"Content-Type": "application/json"}
