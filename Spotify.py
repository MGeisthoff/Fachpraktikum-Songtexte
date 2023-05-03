
#pip install spotipy and pip install lyricsgenius  (in Terminal)
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="ID eingeben",

                                                           client_secret="ID eingeben"))

results = sp.search(q='Lea', limit=10)
for idx, track in enumerate(results['tracks']['items']):
    print(idx, track['name'])