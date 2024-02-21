from bs4 import BeautifulSoup
import lxml
import requests

response = requests.get("https://news.ycombinator.com/")

yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")
nested_tags = soup.find_all(name="span", class_="titleline")

article_texts = []
article_links = []
scores = []

for article_tag in nested_tags:
    article_text = article_tag.getText()
    article_texts.append(article_text)
    article_link = article_tag.find("a").get("href")
    article_links.append(article_link)

score_tags = soup.find_all("span", class_="score")
scores = [int(score_tag.getText().split()[0]) for score_tag in score_tags]

highest_upvote = max(scores)
highest_upvote_index = scores.index(highest_upvote)
highest_upvote_article = article_texts[highest_upvote_index]
highest_upvote_link = article_links[highest_upvote_index]

# print(article_texts)
# print(article_links)
# print(scores)

print(highest_upvote_article)
print(highest_upvote_link)
print(highest_upvote)
