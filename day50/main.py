from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException

option = webdriver.ChromeOptions()
option.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=option)
driver.get("https://tinder.com/")
time.sleep
log_in = driver.find_element(By.LINK_TEXT,"Oturum aç")
log_in.click()
time.sleep(5)
# google = driver.find_element(By.LINK_TEXT,"Google ile devam edin")//*[@id="container"]/div/div[2]/span[1]
facebook = driver.find_element(By.XPATH,'//*[@id="u-1238065328"]/main/div[1]/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button/div[2]/div[2]/div/div')
time.sleep(5)
facebook.click()

time.sleep(10)
#Swtich Windows 
main_window = driver.window_handles[0]
fb_window = driver.window_handles[1]
driver.switch_to.window(fb_window)
# user_name = ""
mail = driver.find_element(By.ID,"email")
password = driver.find_element(By.ID,"pass")

mail.send_keys("sametto585@gmail.com")
password.send_keys("060316Msr.")
password.send_keys(Keys.ENTER)

time.sleep(5)
# continue_with = driver.find_element(By.XPATH,'//*[@id="mount_0_0_bV"]/div/div/div/div/div/div/div/div[1]/div[3]/div/div/div/div/div/div/div[2]/div/div/div[1]/div/div/div/div[1]/div/div/div/div/div/div[1]/div/span/span')

# continue_with.click()
driver.switch_to.window(main_window)
time.sleep(10)
allow = driver.find_element(By.XPATH,'//*[@id="u-1238065328"]/main/div[1]/div/div/div[3]/button[1]/div[2]/div[2]')
allow.click()
time.sleep(10)
noti = driver.find_element(By.XPATH,'//*[@id="u-1238065328"]/main/div[1]/div/div/div[3]/button[2]/div[2]/div[2]')
noti.click()


cookies = driver.find_element(By.XPATH,'//*[@id="content"]/div/div[2]/div/div/div[1]/button')
cookies.click()

for n in range(100):
    time.sleep(1)
    try:
        print("called")
        like_button = driver.find_element(By.XPATH,'//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like_button.click()
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element(By.CSS_SELECTOR,".itsAMatch a")
            match_popup.click()
        except NoSuchElementException:
            time.sleep(2)

driver.quit()