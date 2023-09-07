import requests
import datetime as dt
import smtplib
import time
def time_sleep(x):
    time.sleep(x)
    
def sent_mail():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()

        connection.login(user=my_email,password=my_pass)
        connection.sendmail(from_addr=my_email,to_addrs="sametozo@yahoo.com",msg="Subject:ISS Location\n\n Look UP go go go")
        connection.close()
        

my_email = "sametto0603@gmail.com"
my_pass ="ulkbhcbvfrnbqjtf"
d_time = dt.datetime.now()
hour = d_time.hour
my_lat = 36.64389
my_log =33.43885
parameters = {
    "lat" : my_lat,
    "log" : my_log,
    "formatted": 0,
}   
def get_sunrise_sunset():
    response = requests.get(url="https://api.sunrise-sunset.org/json",params=parameters)

    print(response.json()["results"]["sunrise"])
    sunrise = response.json()["results"]["sunrise"].split("T")[1].split(":")[0]
    sunset = response.json()["results"]["sunset"].split("T")[1].split(":")[0]
    sun_rise = int(sunrise)
    sun_set = int(sunset)
    return sun_rise,sun_set


def iss_location():
    response_iss = requests.get(url="http://api.open-notify.org/iss-now.json")
    iss_log= float(response_iss.json()["iss_position"]["longitude"])
    iss_lat= float(response_iss.json()["iss_position"]["latitude"])
    return  iss_lat,iss_log




while True:
    iss_lat,iss_log = iss_location()
    print(iss_lat)
    sun_rise,sun_set = get_sunrise_sunset()
    print(sun_rise,sun_set)
    if my_lat+5> iss_lat<my_lat-5 and my_log+5> iss_log<my_log-5 and hour>sun_set or hour<sun_rise:
        sent_mail()
    print("No found")
    time_sleep(5)