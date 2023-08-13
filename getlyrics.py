# Setzen Sie hier Ihre eigenen API-Schlüssel und Zugangsdaten ein
SPOTIPY_CLIENT_ID = '' 
SPOTIPY_CLIENT_SECRET = ''
GENIUS_ACCESS_TOKEN = ''

client_credentials_manager = SpotifyClientCredentials(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)



# Playlist-ID eingeben:
playlist_id ='' # in diesem Projekt: 75hKxWLF6z1rDdO5gFSCd2 Playlist: Fachpraktikum Sprachentechnologie

# Da die Spotify API nur 100 Songs zulässt, kommt hier eine Schleife, um alle Songs zu bekommen
offset=0
tracks_alt = sp.playlist_tracks(playlist_id, offset= offset)
all_tracks = []
# die Spotify API lässt nur 100 Songs zu, daher die Schleife, um alle Songs zu bekommen

while True:
    tracks_neu = sp.playlist_tracks(playlist_id, offset=offset)
    all_tracks += tracks_neu["items"]
    
    if len(tracks_neu['items'])==0:
        break
    offset += len(tracks_neu['items'])


# Instanz von Genius mit Zugangstoken
genius = lyricsgenius.Genius(GENIUS_ACCESS_TOKEN)

#Dictionary anlegen, um eine Datei mit mehreren Playlisten zu erhalten
songs_dict = {"Spotify": {}}

# Durchlaufe jeden Track in der Playlist + ID festsetzen
songs_wout_lyrics_0= 0
id_0 = 0
date_0 = 0
year_0 = 0
playlist = "Spotify"


for track_0 in tqdm(all_tracks):

    # Holen Sie sich den Künstlernamen, Tracknamen, Erscheinungsdatum/Jahr, Popularität
    artist_name_0 = track_0['track']['artists'][0]['name']
    track_name_0 = track_0['track']['name']
    date_name_0 = track_0['track']['album']['release_date']
    year_name_0 = int(date_name_0[:4]) 
    popularity_0 = track_0['track']['popularity']


    # Suche Song auf Genius
    try:
        song_0 = genius.search_song(track_name_0, artist_name_0)
        if song_0:
            lyrics_0 = song_0.lyrics
            songs_dict[playlist][id_0]= {"artist_name": artist_name_0, "track_name":track_name_0, "release_date": date_name_0, "release_year": year_name_0, "popularity": popularity_0, "lyrics": lyrics_0}
            id_0 += 1
        else:
            songs_wout_lyrics_0 += 1
    except:
        pass
   

with open("./all_songs_neu2.json", "w") as f:
    json.dump(songs_dict, f, indent=4)

print(songs_wout_lyrics_0)