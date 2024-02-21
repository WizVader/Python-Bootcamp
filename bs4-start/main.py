from bs4 import BeautifulSoup
import lxml
import requests

response = requests.get("https://news.ycombinator.com/")

yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")
nested_tags = soup.find("span", class_="titleline")
article_link = nested_tags.find("a").get("href")

print(nested_tags)
print(article_link)