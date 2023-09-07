from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time as t
import re
option = webdriver.ChromeOptions()
option.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=option)
driver.get("http://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element(By.ID,"cookie")


five_mins = t.time() + 60*5
store_checking = t.time() +5

name_list = []
names = driver.find_elements(By.CSS_SELECTOR,"#store b")
for name in names:
    name = name.text
    new_name = name.split("-")[0]
    print(new_name)
    name_list.append(new_name)
name_list = name_list[:-1]
a=-1
while True:
    price_list = []
    total_dict={}
    cookie.click()
    if store_checking<t.time():
        #Check How Many Cookies
        my_cookies = int(driver.find_element(By.ID,"money").text)
        #Checking Upgrade Prices
        prices = driver.find_elements(By.CSS_SELECTOR,"#store b")
        for price in prices[:-1]:
            price = price.text
            new_price = re.sub("[^0-9]","",price)
            if int(new_price)<my_cookies:
                price_list.append(int(new_price))
            

        #Create Price and Name Dict
        for i in range(len(price_list)):
        
            total_dict[name_list[i]] = price_list[i]
        
        
        # print(type(max(total_dict)))
        # print(total_dict)
        # print(total_dict.items())
        print(total_dict)
        y = list(total_dict.keys())[list(total_dict.values()).index(max(total_dict.values()))]
        y = y.strip()
        print(y)
        # high_upgrade = max(total_dict)
        # x=max(total_dict)      
        max_purchase = driver.find_element(By.ID,f"buy{y}")
        max_purchase.click()
        # a=1

        store_checking = t.time() +5
        # for i in range(len(price_list)):
        #     while my_cookies > price_list[i]:
                

