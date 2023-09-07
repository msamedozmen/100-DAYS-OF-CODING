import smtplib

#Simple Mail Transfer Protocol
# my_email = "sametto0603@gmail.com"
# my_pass ="ulkbhcbvfrnbqjtf"
# connection = smtplib.SMTP("smtp.gmail.com")
#Transport Layer Security
# connection.starttls() 
#login
# connection.login(user=my_email,password=my_pass)
# connection.sendmail(from_addr=my_email,to_addrs="sametozo@yahoo.com",msg="Subject:Happy Birthday\n\n HELLO.")

# connection.close()

# Second Way

# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls() 
#     connection.login(user=my_email,password=my_pass)
#     connection.sendmail(from_addr=my_email,
#                         to_addrs="sametozo@yahoo.com",  
#                         msg="Subject:Happy Birthday\n\n HELLO.")



import datetime as dt
current_time = dt.datetime.now()
    
year = current_time.year

month = current_time.month

day = current_time.day

hour = current_time.hour

min = current_time.minute

day_of_week = current_time.weekday()

sec = current_time.second
print(day_of_week)
birth = dt.datetime(year=1885,month=11,day=13)
print(birth)