from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

date = input("What year would like to travel to in YYY-MM-DD: ")
billboard = requests.get(f"https://www.billboard.com/charts/hot-100/" + date)
soup = BeautifulSoup(billboard.text, "html.parser")
all_songs = soup.soup.find_all(name="h3", class_="chart-element__information__song")

songs_titles = [song.getText() for song in all_songs]


# Todo: Part 2 - Authentication with Spotify

CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
redirect = os.getenv('redirect')

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri=redirect,
        scope="playlist-modify-private",
        show_dialog=True,
        cache_path="token.txt"))

# Todo 3: Search Spotify for the Songs from Step 1

user_id = sp.current_user()["id"]
date = input("What year would like to travel to in YYY-MM-DD: ")
song_names = ["The list of song", "titles from your", "web scrape"]

song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)

    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")
