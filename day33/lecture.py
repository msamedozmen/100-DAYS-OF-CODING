import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
print(response.json()["iss_position"])

response.raise_for_status()
if response.status_code != 200:
    print("Error")
else:
    print("Everything is good")


