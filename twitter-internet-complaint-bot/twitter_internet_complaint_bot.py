import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

PROMISED_DOWN = 150
PROMISED_UP = 10
TWITTER_USERNAME = os.environ['TWITTER_USERNAME']
TWITTER_PASSWORD = os.environ['TWITTER_PASSWORD']

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


class InternetSpeedTwitterBot:

    def __init__(self):
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get("https://www.speedtest.net/")
        self.down = PROMISED_DOWN
        self.up = PROMISED_UP
        self.calculated_download = None
        self.calculated_upload = None

    def get_internet_speed(self):
        go_button = self.driver.find_element(By.CLASS_NAME, value="start-text")
        go_button.click()
        time.sleep(60)
        close_button = self.driver.find_element(By.XPATH,
                                                value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[8]/div/div/p[2]/button')
        close_button.click()
        self.calculated_download = (self.driver.find_element(By.XPATH,
                                                             value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')).text
        self.calculated_upload = (self.driver.find_element(By.XPATH,
                                                           value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')).text
        print(self.calculated_download)
        print(self.calculated_upload)
        self.driver.quit()

    def tweet_at_provider(self):
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get("https://twitter.com/i/flow/login")
        time.sleep(5)
        email_input = self.driver.find_element(By.XPATH,
                                               value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        email_input.send_keys(TWITTER_USERNAME)
        time.sleep(5)
        next_button = self.driver.find_element(By.XPATH,
                                               value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div')
        next_button.click()
        time.sleep(5)
        password_input_div = self.driver.find_element(By.XPATH,
                                                  value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]')
        password_input_box = password_input_div.find_element(By.TAG_NAME, value="input")
        password_input_box.send_keys(TWITTER_PASSWORD)
        time.sleep(5)
        login_button = self.driver.find_element(By.XPATH,
                                                value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div')
        login_button.click()
        time.sleep(5)
        tweet_input_div = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
        tweet_input_div.send_keys(f"This is an automated tweet as part of a project. The internet download speed is {self.calculated_download}, upload speed is {self.calculated_download}")
        post_button = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/div[3]')
        post_button.click()
