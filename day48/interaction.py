from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import re
option = webdriver.ChromeOptions()
option.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=option)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

count = driver.find_element(By.CSS_SELECTOR,"#articlecount a")

# print(count.split(" ")[0])
print(count.text)
# count.click()
# driver.quit()

all_portals = driver.find_element(By.ID,"vector-page-tools-dropdown-checkbox")
# all_portals.click()

button = driver.find_element(By.CSS_SELECTOR,"#p-search a")
button.click()
search = driver.find_element(By.NAME,"search")


search.send_keys("Astronomy")
search.send_keys(Keys.ENTER)