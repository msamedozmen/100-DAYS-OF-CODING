import requests
import datetime as dt
import html
from twilio.rest import Client
import smtplib

time_now = dt.datetime.now()
day=time_now.day
month = time_now.month
year =time_now.year
last_three_days = day -3
from_time =f"{year}-0{month}-0{last_three_days}"
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
# print(from_time)
stock_api_key="RZNP32U4ZHCPHZSE"

stocks_url="https://www.alphavantage.co/query"
stock_param = {
    "function":"TIME_SERIES_DAILY_ADJUSTED",
    "symbol":STOCK,
    "apikey":stock_api_key
    
}
#STEP1 GET STOCK VALUES
stock_response = requests.get(url=stocks_url,params=stock_param)
# print(stock_response)
# print(stock_response.json())
stock_name =stock_response.json()["Meta Data"]["2. Symbol"]
stock_data =stock_response.json()["Time Series (Daily)"]

days = list(stock_data)[1:3]
close =[]
for day in days:
    close_value=(stock_data[day]["4. close"])
    close.append(close_value)

close_dif =float(close[0])-float(close[1])
# print(close_dif)
close_diff_perc =float(float(close[0])/float(close[1]))*100-100
# print(round(close_diff_perc,3),"%")

#STEP2 NEWS

news_api_key ="7a81142e61f7432d870b8504e39f0a96"
news_url="https://newsapi.org/v2/everything"

news_parameters = {
    "q": "tesla",
    "from":from_time,
    "sortBy":"publishedAt",
    "apiKey": news_api_key
}


news_response = requests.get(url=news_url,params=news_parameters)
news_data = news_response.json()["articles"]
# print(news_data)
heads =[]
briefs=[]
for i in range(3):
    headline = news_data[i]["title"]
    headline=html.escape(headline)
    heads.append(headline)
    brief = news_data[i]["description"]
    brief=html.escape(brief)
    briefs.append(brief)
    
# print(briefs)
print(heads)

nl = '\n'
b="🔺"
#STEP 3 SEND MESSAGES
account_sid = "AC98a59cb71967516aaa0bcdf41d23cc61"
auth_token = "79c041398e3ddafbaf58373a272511eb"
client = Client(account_sid, auth_token)
message = client.messages.create(
  body=f"{STOCK}: 🔺{close_diff_perc} {nl}Headline: {heads[0]} {nl} Brief: {briefs[0]} {nl}Headline: {heads[1]} {nl} Brief: {briefs[1]} {nl}Headline: {heads[2]} {nl} Brief: {briefs[2]} ",
  from_="+12534652303",
  to="+905317435406"
)
print(message.sid)
a =f"Subject:Today's Tesle Stock Value{nl}{nl}{STOCK}: {close_diff_perc}{nl}Headline: {heads[0]}{nl}Brief: {briefs[0]}{nl}Headline: {heads[1]}{nl}Brief: {briefs[1]}{nl}Headline: {heads[2]}{nl}Brief: {briefs[2]}"
# a.encode("utf-8")
print(f"Subject:Today's Tesle Stock Value{nl}{nl}{STOCK}: '🔺'{close_diff_perc}{nl}Headline: {heads[0]}{nl} Brief: {briefs[0]} {nl}Headline: {heads[1]} {nl} Brief: {briefs[1]} {nl}Headline: {heads[2]} {nl} Brief: {briefs[2]} ")
my_email = "sametto0603@gmail.com"
my_pass ="ulkbhcbvfrnbqjtf"
connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email,password=my_pass)
connection.sendmail(from_addr=my_email,to_addrs="sametozo@yahoo.com",msg=a.encode("utf-8"))
connection.close()
print(f"{heads[0]}")

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 




# """
# TSLA: 🔺2%
# Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
# Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
# or
# "TSLA: 🔻5%
# Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
# Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
# """

