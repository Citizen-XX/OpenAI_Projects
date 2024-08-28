import requests

base_url = "http://127.0.0.1:8000"
endpoint = "/query_data"
data_1 = {"text": "Please tell me what Deep Learning is used for"}
data_2 = {"text": "Please tell me what Unsupervised Learning is used for"}
data_3 = {"text": "Please tell me what Unsupervised Learning's applications are"}

response = requests.post(url=f"{base_url+endpoint}",json=data_3)

if response.status_code == 200:
    print("Response: ",response.json()["result"]["response"])
else:
    print("Error: ", response.text)