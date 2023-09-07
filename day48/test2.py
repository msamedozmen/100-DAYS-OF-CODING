from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

option = webdriver.ChromeOptions()
option.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=option)
driver.get("http://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(By.NAME,"fName")
last_name = driver.find_element(By.NAME,"lName")
email = driver.find_element(By.NAME,"email")

first_name.send_keys("Samed")
last_name.send_keys("Özmen")
email.send_keys("sametozmen22@gmail.com")

sign_up = driver.find_element(By.CSS_SELECTOR,"form button")

sign_up.click()