import requests

url = "http://127.0.0.1:8000/sum"
data = {"number1":5,"number2":7}

response = requests.post(url,json=data)

if response.status_code == 200:
    print("Response: ",response.json())
else:
    print("Error: ", response.text)