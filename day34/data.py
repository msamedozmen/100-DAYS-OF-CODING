import requests
parameters= {
    "amount":10,
    "type": "boolean"
}
get_data = requests.get(url="https://opentdb.com/api.php",params=parameters)

question_data = get_data.json()["results"]
print(question_data)
print(len(question_data))