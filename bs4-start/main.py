from bs4 import BeautifulSoup
import lxml
import requests

response = requests.get("https://news.ycombinator.com/")

yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")
nested_tags = soup.find_all("span", class_="titleline")
# print(nested_tags)
for tags in nested_tags:
    article_tags = tags.find("a", name="href")
    print(article_tags)

