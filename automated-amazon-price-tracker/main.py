import requests
from bs4 import BeautifulSoup
import lxml
import smtplib
import os

EMAIL = os.environ["my_email"]
EMAIL_PASSWORD = os.environ["my_email_password"]

amazon_link = "https://www.amazon.com.au/AOC-24G2SE-165HZ-VESA-Black/dp/B0BMPG2XH8"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 "
                  "Safari/537.36",
    "Accept-Language": "en-US,en;q=0.5"
}

response = requests.get(amazon_link, headers=headers)
amazon_webpage = response.text

soup = BeautifulSoup(amazon_webpage, "lxml")
div_tags = soup.find_all("div", class_="a-section a-spacing-micro")
price_tag = [(tag.find("span", class_="a-price aok-align-center")).find("span", class_="a-offscreen") for tag in
             div_tags]

price = float((price_tag[0].text.split("$"))[1])

if price <= 160:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=EMAIL_PASSWORD)
        connection.sendmail(from_addr=EMAIL, to_addrs="svcharanjeet@yahoo.com", msg="Subject: Amazon Price Alert!\n\n"
                                                                                    "The price of the montior has "
                                                                                    f"gone down. Here is the link: "
                                                                                    f"{amazon_link}")
