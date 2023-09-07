from selenium import webdriver
from selenium.webdriver.common.by import By
options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=options)

# driver.get("https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6")
driver.get("https://www.zara.com/tr/tr/man-from-40-l5443.html?v1=2305698")
# price = driver.find_element(By.CLASS_NAME,"a-price-whole").text
# symbol = driver.find_element(By.CLASS_NAME,"a-price-symbol").text
# decimal = driver.find_element(By.CLASS_NAME,"a-size-base a-color-secondary").text
# price = driver.find_element(By.XPATH, '//*[@id="main"]/article/div[2]/section[1]/ul/li[2]/ul[3]/li[1]/div/div/div[3]/span/span[2]/div/span').text
price = driver.find_element(By.CLASS_NAME,"money-amount__main").text
print(price)

# print(symbol + price + decimal)
# driver.get("https://www.python.org/")

# name = driver.find_element(By.NAME,"q")


# print(name.get_attribute("placeholder"))

driver.quit()