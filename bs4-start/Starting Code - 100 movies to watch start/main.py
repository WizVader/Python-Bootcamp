import requests
from bs4 import BeautifulSoup

URL = "https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
webpage = response.text
soup = BeautifulSoup(webpage, "html.parser")
movie_tags = soup.find_all(name="h3", class_="listicleItem_listicle-item__title__BfenH")
movies_text = [(movie_tag.text + '\n') for movie_tag in movie_tags]
movies_text.reverse()

with open("movies.txt", 'w') as file:
    file.writelines(movies_text)

