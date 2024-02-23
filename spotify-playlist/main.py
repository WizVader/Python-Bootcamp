from bs4 import BeautifulSoup
import requests

date = input("Which year do you want to travel to? Type the data in this format YYYY-MM-DD:\n")

URL = f"https://www.billboard.com/charts/hot-100/{date}"

response = requests.get(URL)
billboard_webpage = response.text

soup = BeautifulSoup(billboard_webpage, "html.parser")

song_tags = soup.select("li ul li h3")
song_names = [tag.text.strip() for tag in song_tags]
print(song_names)
