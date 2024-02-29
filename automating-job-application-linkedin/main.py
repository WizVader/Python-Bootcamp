from selenium import webdriver
from selenium.webdriver.common.by import By
import os

URL = ("https://www.linkedin.com/jobs/search/?currentJobId=3823155509&f_AL=true&geoId=102257491&keywords=python"
       "%20developer&location=London%2C%20England%2C%20United%20Kingdom&origin=JOB_SEARCH_PAGE_KEYWORD_AUTOCOMPLETE"
       "&refresh=true&sortBy=R&spellCorrectionEnabled=true")

LINKEDIN_EMAIL = os.environ['LINKEDIN_EMAIL']
LINKEDIN_PASSWORD = os.environ['LINKEDIN_PASSWORD']

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

sign_in_button_tag = driver.find_element(By.CLASS_NAME, value="nav__button-secondary")
print(sign_in_button_tag.text)
sign_in_button_tag.click()

email_input_tag = driver.find_element(By.ID, value="username")
email_input_tag.send_keys(LINKEDIN_EMAIL)

password_input_tag = driver.find_element(By.ID, value="password")
password_input_tag.send_keys(LINKEDIN_PASSWORD)

