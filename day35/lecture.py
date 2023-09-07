import requests
from twilio.rest import Client
import os

api_key = 
api_key = "1ec8e337ad12098add68f47d8afa3e39"
account_sdi = "AC98a59cb71967516aaa0bcdf41d23cc61"
auth_token = "79c041398e3ddafbaf58373a272511eb"
client = Client(account_sdi,auth_token)
my_log = 39.476219
my_lat = -6.370860
rainy =[]
parameters={
    "lat": my_lat,
    "lon": my_log,
    "appid": api_key,
    "exclude": "daily,minutely,alerts,current"
}
response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall",params=parameters)
print(response.json())

weather_dat = response.json()
only_hourly=weather_dat["hourly"][12:]
print(weather_dat)
for weather in only_hourly:
    
    print(weather["wheather"][0]["id"])
    if int(weather_dat["wheather"][0]["id"])< 700:
        
        rainy.append[weather_dat["wheather"][0]["id"]]
        
if len(rainy) >=1:
    client = Client(account_sdi,auth_token)
    message = client.messages.create(
    body="this gonna be rainy",
    from_="++12534652303",
    to="+905317435406"
    )
    print(message.status)
    
