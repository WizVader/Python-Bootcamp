from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep chrome open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.python.org")

time_tags = driver.find_elements(By.TAG_NAME, value="time")
time_text_full = [time_tag.text for time_tag in time_tags]
time_text = time_text_full[4:]


driver.quit()
