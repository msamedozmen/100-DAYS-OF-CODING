from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from xyz import InternetSpeedTwitterBot


PROMISED_DOWN = 150
PROMISED_UP =20
MY_USERNAME = "y"
MY_PASS = "x."
link =  "https://twitter.com"

speedtest = InternetSpeedTwitterBot()
speedtest.get_internet_speed()

if PROMISED_DOWN > speedtest.down or PROMISED_UP > speedtest.up:
    speedtest.tweet_at_provider(MY_USERNAME,MY_PASS,PROMISED_UP,PROMISED_DOWN)


