from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID = "fbfe8b36abe24b519baeda2d061719a2"
CLIENT_SECRET = "60122fc50ae34214945e1503a02b6c21"
URL = "https://www.billboard.com/charts/hot-100/"
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:")
username ="sametozmen22"
response = requests.get(url=f"{URL}/{date}")

my_musics = response.text

soup = BeautifulSoup(my_musics,"html.parser")

musics = [music.getText() for music in  soup.find_all("h3", class_="a-no-trucate") ]
for i in range(len(musics)):
    if "\n" in musics[i] or "\t" in musics[i] :
        musics[i] = musics[i].replace("\n","")
        musics[i] = musics[i].replace("\t","")


# with open("hot100.txt","w",encoding="utf-8") as file:
#     for music in musics:
#         file.write(f"{music}\n")


sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://localhost/",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt",
        username="sametozmen22"
    )
)
music_uri = []
year = date[:4]
for music in musics:
    final = sp.search(q=f"track:{musics} year:{year}", type="track")
    # print(final)
    try:
        uri = final["tracks"]["items"][0]["uri"]
        music_uri.append(uri)
    except IndexError:
        pass

playlist = sp.user_playlist_create(user=username, name=f"{date} Billboard 100", public=False)
# print(playlist)

sp.playlist_add_items(playlist_id=playlist["id"], items=music_uri)