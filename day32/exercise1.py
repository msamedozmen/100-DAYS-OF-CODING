import random as rd
import datetime as dt
import smtplib


current_time = dt.datetime.now()

day_of_week =current_time.weekday()

with open("quotes.txt") as file:
    lines = file.readlines()
    
    if day_of_week != 5 or day_of_week!=6:
        message=rd.choice(lines)
        
        my_email = "sametto0603@gmail.com"
        my_pass ="ulkbhcbvfrnbqjtf"
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user=my_email,password=my_pass)
        connection.sendmail(from_addr=my_email,to_addrs="sametozo@yahoo.com",msg=f"Subject:Motivation Message\n\n{message}")
        
        connection.close()
        