# Multi‑Cloud Serverless Function
The purpose of this assignment is to implement the same HTTP serverless function in two clouds: Google Cloud Platform (GCP) and Microsoft Azure. The function accepts JSON input values describing HbA1c levels, applies a simple binary classifier to determine whether the value is normal or abnormal, and returns the result as a structured JSON response.

## Lab Rules (HbA1c)
- Rule: Normal if hba1c < 6.5; otherwise Abnormal.

- Plain English: If HbA1c is below 6.5%, the status is normal; if 6.5% or higher, it’s abnormal.

- Clinical Citation:
    - American Diabetes Association. Standards of Medical Care in Diabetes – 2025. Diabetes Care. 2025;48(Suppl. 1):S1–S157. https://doi.org/10.2337/dc25-S001
    - Centers for Disease Control and Prevention (CDC): https://www.cdc.gov/diabetes/managing/managing-blood-sugar/a1c.html

# Azure 
- Name the file 


# Google Cloud
- Named the file hba1c-triage
- Chose us-central1 for the region
- Selected python 3.13
- Allowed for public access
- Networking, select all
- Endpoint link: https://hba1c-triage-718737153982.us-central1.run.app

## Steps
1. Log into Google Cloud
2. Searched for Cloud run and then selected "create a service"
3. I then selected inline editor to create a function
4. Named the service hba1c-triage and chose the region "us-central1" and selected Python 3.13 for runtime. I selected Allow public access and made billing request based. I then made the maximum number of isntances 1 and changed ingress to All.
5. Click on "create"
6. Changed the key of the entry point to the "main.py" code in the gcp folder.
7. Renamed as hba1c-triage and clicked save and deploy to update the new code.
8. I was able to copy the URL and use it to do a series of tests. 

## Testing

### Post Request
I ran the deployed GCP Cloud Function endpoint directly from VS Code using Python.

![images](gcp/images/gcp_testing.png)

I made a new file labeled ```test_client.py``` where I then ran this using the command ```python3 gcp/test_client.py```

### GET Request
Using the URL of the end point link, I pasted it into the browser and typed in ```?hba1c=6.8``` and it generated a response for me

![images](gcp/images/gcp_get_request.png)

