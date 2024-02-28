from selenium import webdriver
from selenium.webdriver.common.by import By
import time

URL = "https://orteil.dashnet.org/experiments/cookie/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

cookie = driver.find_element(By.ID, "cookie")

start_time = time.time()

while True:
    time.sleep(0.1)  # Done to reduce CPU usage
    cookie.click()
    current_time = time.time()
    money = int(driver.find_element(By.ID, value="money").text.replace(',', ''))
    condition = (current_time - start_time) >= 5
    if condition:
        start_time = current_time
        store_div = driver.find_element(By.ID, value="store")
        items_divs = store_div.find_elements(By.TAG_NAME, value="div")
        prices_texts = [(item.find_element(By.CSS_SELECTOR, value="#store b")).text for item in items_divs[:8]]
        price = [int(((prices_text.split('-')[1].split())[0]).replace(',', '')) for prices_text in prices_texts]

        for i in price[len(price)::-1]:
            if money >= i:
                print("Buying")
                price_index = price.index(i)
                items_divs[price_index].click()