from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException
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
        item_ids = ["buyCursor", "buyGrandma", "buyFactory", "buyMine", "buyShipment", "buyAlchemy lab", "buyPortal",
                    "buyTime machine"]
        items_divs = store_div.find_elements(By.TAG_NAME, value="div")
        print("Entering trying")
        all_prices = driver.find_elements(By.CSS_SELECTOR, value="#store b")
        prices_texts = [tag.text for tag in all_prices]
        print("Error")
        #  int(((prices_text.split('-')[1].split())[0]).replace(',', '')) for prices_text in prices_texts
        price = []
        for prices_text in prices_texts:
            if prices_text != "":
                price.append(int(((prices_text.split('-')[1].split())[0]).replace(',', '')))

        for i in price[len(price)::-1]:
            if money >= i:
                print("Buying")
                price_index = price.index(i)
                try:
                    items_divs[price_index].click()
                except StaleElementReferenceException:
                    pass
