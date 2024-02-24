from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep chrome open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.amazon.com.au/AOC-24G2SE-165HZ-VESA-Black/dp/B0BMPG2XH8")

price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole").text
price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction").text

print(f"The price of the product is: {price_dollar}.{price_cents}")
driver.quit()
