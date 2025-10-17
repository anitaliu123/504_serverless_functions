import json
import logging
import azure.functions as func

app = func.FunctionApp()

@app.function_name(name="hba1c_classifier")
@app.route(route="hba1c", methods=["GET", "POST", "OPTIONS"], auth_level=func.AuthLevel.ANONYMOUS)
def hba1c_classifier(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Processing HbA1c request")

    # CORS preflight
    if req.method == "OPTIONS":
        return func.HttpResponse(status_code=204, headers={
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
            "Access-Control-Allow-Headers": "Content-Type",
        })

    # Parse input (JSON first, then query)
    try:
        data = req.get_json()
    except ValueError:
        data = {}

    hba1c = data.get("hba1c") or req.params.get("hba1c")
    if hba1c is None:
        return func.HttpResponse(json.dumps({"error": "'hba1c' is required."}),
                                 status_code=400, mimetype="application/json",
                                 headers={"Access-Control-Allow-Origin": "*"})

    try:
        val = float(hba1c)
    except (TypeError, ValueError):
        return func.HttpResponse(json.dumps({"error": "'hba1c' must be a number."}),
                                 status_code=400, mimetype="application/json",
                                 headers={"Access-Control-Allow-Origin": "*"})

    # Binary status for grading
    status = "normal" if val < 6.5 else "abnormal"

    # ADA category tiers for context
    if val < 5.7:
        category = "Normal (<5.7%)"
    elif val < 6.5:
        category = "Prediabetes (5.7–6.4%)"
    else:
        category = "Diabetes (≥6.5%)"

    return func.HttpResponse(
        json.dumps({"hba1c": val, "status": status, "category": category}),
        status_code=200, mimetype="application/json",
        headers={"Access-Control-Allow-Origin": "*"},
    )
