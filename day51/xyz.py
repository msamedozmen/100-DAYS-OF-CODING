from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

PROMISED_DOWN = 150
PROMISED_UP =20
MY_USERNAME = "x"
MY_PASS = "y."

class InternetSpeedTwitterBot:
    def __init__(self):
        self.option = webdriver.ChromeOptions()
        self.option.add_experimental_option("detach",True)
        self.driver = webdriver.Chrome(options=self.option)
        self.up = 0
        self.down =0
    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(10)
        self.start = self.driver.find_element(By.CLASS_NAME,"start-text")
        self.start.click()
        time.sleep(60)
        self.down = float(self.driver.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text)
        print(self.down)
        
        self.up = float(self.driver.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text)
        print(self.up)
        
    
    def tweet_at_provider(self,email,psw,up,down):
        # self.driver.get("https://www.speedtest.net/")
        # time.sleep(10)
        self.driver.get("https://twitter.com")
        time.sleep(10)
        self.login = self.driver.find_element(By.NAME,"text")
        self.login.send_keys(email)
        self.login.send_keys(Keys.ENTER)
        time.sleep(5)
        self.psw = self.driver.find_element(By.NAME,"password")
        self.psw.send_keys(psw)
        self.psw.send_keys(Keys.ENTER)
        time.sleep(60)
        self.write = self.driver.find_element(By.CSS_SELECTOR,".public-DraftStyleDefault-block")
        self.write.send_keys(f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {up}down/{down}up?")
        self.tweet = self.driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[3]/div/span/span')
        self.tweet.click()    
    
    
