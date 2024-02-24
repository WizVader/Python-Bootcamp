import requests
import spotipy
import os
from bs4 import BeautifulSoup
from spotipy import SpotifyOAuth

SPOTIFY_CLIENT_ID = os.environ['spotify_client_id']
SPOTIFY_CLIENT_SECRET = os.environ['spotify_client_secret']
SPOTIFY_API_ENDPOINT = "https://api.spotify.com/v1/search"

date = input("Which year do you want to travel to? Type the data in this format YYYY-MM-DD:\n")

URL = f"https://www.billboard.com/charts/hot-100/{date}"
playlist_name = f"Top 100 of {date}"

response = requests.get(URL)
billboard_webpage = response.text

soup = BeautifulSoup(billboard_webpage, "html.parser")

song_tags = soup.select("li ul li h3")
song_names = [tag.text.strip() for tag in song_tags]

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET,
        redirect_uri="http://example.com",
        scope="playlist-modify-private",
        show_dialog=True,
        cache_path="token.txt",
        username="Charan"
    )
)

user_id = sp.current_user()["id"]
year = date.split("-")[0]
track_uris = []

for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        track_uris.append(uri)
    except IndexError:
        print(f"{song} does not exist")

my_playlist = sp.user_playlist_create(user=user_id, name=playlist_name, public=False, collaborative=False,
                                      description=f"A playlist consisting of the top 100 songs from {date}")
playlist_id = my_playlist["id"]
sp.playlist_add_items(playlist_id=playlist_id, items=track_uris, position=None)