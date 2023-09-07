import requests
from bs4 import BeautifulSoup
import smtplib


URL = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Accept-Language": "tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7"
}
response = requests.get(url=URL,headers=header)

price_text = response.text

soup= BeautifulSoup(price_text,"lxml")

price = soup.find("span", class_='a-offscreen')
decimal_price = soup.find("span", class_="a-price-fraction").getText()

print(price.text)
# print(price+ decimal_price)

# price = float(price + decimal_price)

# if price <100:
#     my_email = "sametto0603@gmail.com"
#     my_pass ="ulkbhcbvfrnbqjtf"
#     connection = smtplib.SMTP("smtp.gmail.com")
#     connection.starttls()
#     connection.login(user=my_email,password=my_pass)
#     connection.sendmail(from_addr=my_email,to_addrs="sametozo@yahoo.com",msg=f"Subject:LOW PRICE \n\n Your equipment new price: {price}")
#     connection.close()
#     print("mail already sent")