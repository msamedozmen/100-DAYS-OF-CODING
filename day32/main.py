##################### Extra Hard Starting Project ######################
import datetime as dt
import smtplib
import pandas as pd
import random as rd
# 1. Update the birthdays.csv

file = pd.read_csv("birthdays.csv")

birthday_dict={(row["month"],row["day"]): row for (key,row) in file.iterrows()}

# 2. Check if today matches a birthday in the birthdays.csv
bd_day = dt.datetime.now()



day= bd_day.day
month =bd_day.month
bd_person = (month,day)

if bd_person in birthday_dict:
        my_email = "sametto0603@gmail.com"
        my_pass ="ulkbhcbvfrnbqjtf"
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user=my_email,password=my_pass)
        
        # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
        rd_num = rd.randint(1,3)
        letter = open(f"letter_templates\letter_{rd_num}.txt")
        selected_letter =letter.read()
        bd_pers = birthday_dict[bd_person]
        selected_letter= selected_letter.replace("[NAME]",bd_pers["name"])
        
        connection.sendmail(from_addr=my_email,to_addrs=bd_pers["email"],msg=f"Subject:Happy Birthday\n\n{selected_letter}")
        connection.close()
# 4. Send the letter generated in step 3 to that person's email address.





my_mail = "xxxx"
my_pass ="tttt"

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_mail,password=my_pass)
connection.sendmail(from_addr=,to_addrs=,msg=)


