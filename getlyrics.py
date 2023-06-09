##Spotify and LyricsGenius API
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import lyricsgenius
from tqdm import tqdm
import json
from datetime import datetime



# Setzen Sie hier Ihre eigenen API-Schlüssel und Zugangsdaten ein
SPOTIPY_CLIENT_ID = '46da6046625f409cb53ab06bf807861d'
SPOTIPY_CLIENT_SECRET = '00efb0ab68db4f1eaf27ec53a4c1e068'
GENIUS_ACCESS_TOKEN = 'OsBvEsJ_OLKYR42CJoaA_N97GNOS44XXFk4KPPcLtCYnWmDwnnzY2RpcG_SdG25a'
# Erstelle eine Instanz von SpotifyClientCredentials mit Deinen Zugangsdaten
client_credentials_manager = SpotifyClientCredentials(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)



# Gib die ID der Playlist ein, aus der die Songtexte extrahiert werden sollen
playlist_id ='75hKxWLF6z1rDdO5gFSCd2' # Playlist: Fachpraktikum Sprachentechnologie

# die Spotify API lässt nur 100 Songs zu, daher die Schleife, um alle Songs zu bekommen
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




#Dictionary anlegen, um eine Datei mit mehreren Playlisten zu erhalten
songs_dict = {"Spotify": {}}

# Durchlaufe jeden Track in der Playlist + ID festsetzen
songs_wout_lyrics_0= 0
id_0 = 0
date_0 = 0
year_0 = 0
playlist = "Spotify"
# Erstelle eine Instanz von Genius mit Ihrem Zugangstoken
genius = lyricsgenius.Genius(GENIUS_ACCESS_TOKEN)

for track_0 in tqdm(all_tracks):

    # Holen Sie sich den Namen des Künstlers und den Titel des Tracks
    artist_name_0 = track_0['track']['artists'][0]['name']
    track_name_0 = track_0['track']['name']
    date_name_0 = track_0['track']['album']['release_date']
    year_name_0 = int(date_name_0[:4]) # extract year
    popularity_0 = track_0['track']['popularity']


    # Suche nach dem Song auf Genius
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