from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

LINK = "https://secure-retreat-92358.herokuapp.com/"

driver = webdriver.Chrome(options=chrome_options)
driver.get(LINK)

first_name = driver.find_element(By.NAME, value="fName")
first_name.send_keys("Charanjeet")

last_name = driver.find_element(By.NAME, value="lName")
last_name.send_keys("Viswanathan")

email = driver.find_element(By.NAME, value="email")
email.send_keys("svcharanjeet@gmail.com")

sign_up_button = driver.find_element(By.TAG_NAME, value="button")
sign_up_button.click()

driver.quit()