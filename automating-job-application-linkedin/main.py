from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

URL = ("https://www.linkedin.com/jobs/search/?currentJobId=3823155509&f_AL=true&geoId=102257491&keywords=python"
       "%20developer&location=London%2C%20England%2C%20United%20Kingdom&origin=JOB_SEARCH_PAGE_LOCATION_AUTOCOMPLETE"
       "&refresh=true")

LINKEDIN_EMAIL = os.environ['LINKEDIN_EMAIL']
LINKEDIN_PASSWORD = os.environ['LINKEDIN_PASSWORD']

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

time.sleep(2)

# auth_wall_sign_in_button = driver.find_element(By.CSS_SELECTOR, value=".join-form .authwall-join-form__form-toggle--bottom")
# auth_wall_sign_in_button.click()

sign_in_button_tag = driver.find_element(By.CLASS_NAME, value="nav__button-secondary")
print(sign_in_button_tag.text)
sign_in_button_tag.click()

email_input_tag = driver.find_element(By.ID, value="username")
email_input_tag.send_keys(LINKEDIN_EMAIL)

password_input_tag = driver.find_element(By.ID, value="password")
password_input_tag.send_keys(LINKEDIN_PASSWORD)

sign_in_button_tag_login_page = driver.find_element(By.CLASS_NAME, value="btn__primary--large")
sign_in_button_tag_login_page.click()

