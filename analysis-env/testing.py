import spotipy
import pandas as pd
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials


scope = "user-top-read"  # Make sure this scope is included for accessing top tracks

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
top_tracks = []

for offset in range(0, 200, 50):
    results = sp.current_user_top_tracks(limit=50, offset=offset, time_range="medium_term")
    top_tracks += results['items']


# Print the details of the top tracks
for idx, track in enumerate(top_tracks):
    artists = ', '.join([artist['name'] for artist in track['artists']])
    print(idx, artists, " – ", track['name'])



