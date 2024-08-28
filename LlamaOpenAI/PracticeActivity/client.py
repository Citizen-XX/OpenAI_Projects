import requests

base_url = "http://127.0.0.1:8000"
endpoint = "/query_data"
query = input("What's you question about Machine Learning?: ")
data = {"text": str(query)}

response = requests.post(url=f"{base_url+endpoint}",json=data)

if response.status_code == 200:
    print("Response: ",response.json()["result"]["response"])
else:
    print("Error: ", response.text)