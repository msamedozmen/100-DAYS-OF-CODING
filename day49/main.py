from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

option = webdriver.ChromeOptions()
option.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=option)

driver.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0")
sign_in = driver.find_element(By.LINK_TEXT,"Oturum aç")

sign_in.click()

time.sleep(5)


username = driver.find_element(By.ID,"username")
password = driver.find_element(By.ID,"password")

username.send_keys("sametto060316@gmail.com")
password.send_keys("793684520SA")
password.send_keys(Keys.ENTER)
time.sleep(20)

apply_button= driver.find_element(By.CLASS_NAME,"jobs-apply-button--top-card")
apply_button.click()
time.sleep(5)

phone = driver.find_element(By.ID,"single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3641811861-2775101385419551749-phoneNumber-nationalNumber")
summary = driver.find_element(By.ID,"multiline-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3641811861-5995137204034275356-text")
next_button = driver.find_element(By.CSS_SELECTOR,".artdeco-button")
phone.send_keys("5333333333")
summary.send_keys("multiline-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3641811861-5995137204034275356-text")
next_button.click()
