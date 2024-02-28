from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

LINK = "https://en.wikipedia.org/wiki/Main_Page"

driver = webdriver.Chrome(options=chrome_options)
driver.get(LINK)

div = driver.find_element(By.ID, value="articlecount")
number_of_articles = div.find_element(By.TAG_NAME, "a").text
print(number_of_articles)

driver.quit()