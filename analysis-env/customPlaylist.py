import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials

scope = "user-library-read playlist-modify-private"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

offset = 0
songs = []
items = []
ids = []
while True: #API can only extract 50 songs at a time, looping saved tracks by 50 songs
    results = sp.current_user_saved_tracks(limit=50, offset=offset)
    songs += results['items']
    if results['next'] is not None:
        offset += 50
    else:
        break

for idx, item in enumerate(songs): #loops through songs list and prints song details
    track = item['track']
    print(idx, track['artists'][0]['name'], " – ", track['name'])



