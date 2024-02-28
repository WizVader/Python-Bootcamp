from selenium import webdriver
from selenium.webdriver.common.by import By

LINK = "https://www.python.org/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(LINK)

menu_class_tag = driver.find_element(By.XPATH, value='//*[@id="content"]/div/section/div[2]/div[2]/div/ul')

li_tags = menu_class_tag.find_elements(By.TAG_NAME, "li")
li_tags_text = [tag.text for tag in li_tags]

date_tags = [tag.split("\n")[0] for tag in li_tags_text]
event_tags = [tag.split("\n")[1] for tag in li_tags_text]
print(date_tags, event_tags)

driver.quit()
