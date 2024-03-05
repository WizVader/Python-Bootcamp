from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
SIMILAR_ACCOUNT = "cristiano"
INSTAGRAM_USERNAME = "bootcamp.contacts"
INSTAGRAM_PASSWORD = "Scak1234"


class InstagramBot:

    def __init__(self):
        self.driver = webdriver.Chrome(options=chrome_options)

    def login(self):
        self.driver.get("https://www.instagram.com/")
        time.sleep(2)
        username_input = self.driver.find_element(By.XPATH, value='//*[@id="loginForm"]/div/div[1]/div/label/input')
        username_input.send_keys(INSTAGRAM_USERNAME)
        password_input = self.driver.find_element(By.XPATH, value='//*[@id="loginForm"]/div/div[2]/div/label/input')
        password_input.send_keys(INSTAGRAM_PASSWORD)
        login_button = self.driver.find_element(By.XPATH, value='//*[@id="loginForm"]/div/div[3]/button')
        login_button.click()
        time.sleep(10)

    def search_user(self):
        self.driver.get("https://www.instagram.com/cristiano/following/")

