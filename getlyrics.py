import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import lyricsgenius
from tqdm import tqdm
import json

# Setzen Sie hier Ihre eigenen API-Schlüssel und Zugangsdaten ein
SPOTIPY_CLIENT_ID = '46da6046625f409cb53ab06bf807861d'
SPOTIPY_CLIENT_SECRET = '00efb0ab68db4f1eaf27ec53a4c1e068'
GENIUS_ACCESS_TOKEN = 'OsBvEsJ_OLKYR42CJoaA_N97GNOS44XXFk4KPPcLtCYnWmDwnnzY2RpcG_SdG25a'
# Erstelle eine Instanz von SpotifyClientCredentials mit Deinen Zugangsdaten
client_credentials_manager = SpotifyClientCredentials(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Erstelle eine Instanz von Genius mit Ihrem Zugangstoken
genius = lyricsgenius.Genius(GENIUS_ACCESS_TOKEN)

# Gib die ID der Playlist ein, aus der die Songtexte extrahiert werden sollen
playlist_id = '2siI2ILJEPr88yibWLgQQl'  #Playlist: "Deutsche Songs die jeder kennt ;)"
playlist_id1 = '42VKyjutpBoEEVRjsNc1Es' #Playlist: 90er deutsche Songs
playlist_id2 ='2drfKysR4bfgLpFGNNY9KH' # Playlist: Deutsche Songs 2022

#Hole sich die Tracks aus der Playlist
tracks = sp.playlist_tracks(playlist_id)
tracks1 = sp.playlist_tracks(playlist_id1)
tracks2= sp.playlist_tracks(playlist_id2)

#Dictionary
songs_dict = {"Prototyp": {} , "Songs90er":{}, "Songs22":{}}

#####2022
songs_wout_lyrics_2= 0
id_2 = 0
for track_2 in tqdm(tracks2['items']):
    # Holen Sie sich den Namen des Künstlers und den Titel des Tracks
    artist_name_2 = track_2['track']['artists'][0]['name']
    track_name_2 = track_2['track']['name']

    # Suche nach dem Song auf Genius
    song_2 = genius.search_song(track_name_2, artist_name_2)
    if song_2:
        lyrics_2 = song_2.lyrics
        songs_dict['Songs22'][id_2] = {"artist_name": artist_name_2, "track_name":track_name_2, "lyrics": lyrics_2}
        id_2 += 1
    else:
        songs_wout_lyrics_2 += 1

#####90er
# Durchlaufe jeden Track in der Playlist + ID festsetzen
#pb = tqdm(total=len(tracks["items"]))
songs_wout_lyrics_1= 0
id_1 = 0
for track_1 in tqdm(tracks1['items']):
    # Holen Sie sich den Namen des Künstlers und den Titel des Tracks
    artist_name_1 = track_1['track']['artists'][0]['name']
    track_name_1 = track_1['track']['name']

    # Suche nach dem Song auf Genius
    song_1 = genius.search_song(track_name_1, artist_name_1)
    if song_1:
        lyrics_1= song_1.lyrics
        songs_dict['Songs90er'][id_1] = {"artist_name": artist_name_1, "track_name":track_name_1, "lyrics": lyrics_1}
        id_1 += 1
    else:
        songs_wout_lyrics_1 += 1

#####Beliebte Deutsche Songs
# Durchlaufe jeden Track in der Playlist + ID festsetzen
#pb = tqdm(total=len(tracks["items"]))
songs_wout_lyrics_0= 0
id_0 = 0
for track_0 in tqdm(tracks['items']):
    # Holen Sie sich den Namen des Künstlers und den Titel des Tracks
    artist_name_0 = track_0['track']['artists'][0]['name']
    track_name_0 = track_0['track']['name']

    # Suche nach dem Song auf Genius
    song_0 = genius.search_song(track_name_0, artist_name_0)
    if song_0:
        lyrics_0 = song_0.lyrics
        songs_dict['Prototyp'][id_0] = {"artist_name": artist_name_0, "track_name":track_name_0, "lyrics": lyrics_0}
        id_0 += 1
    else:
        songs_wout_lyrics_0 += 1

    
#####2022
songs_wout_lyrics_2= 0
id_2 = 0
for track_2 in tqdm(tracks['items']):
    # Holen Sie sich den Namen des Künstlers und den Titel des Tracks
    artist_name_2 = track_2['track']['artists'][0]['name']
    track_name_2 = track_2['track']['name']

    # Suche nach dem Song auf Genius
    song_2 = genius.search_song(track_name_2, artist_name_2)
    if song_2:
        lyrics_2 = song_2.lyrics
        songs_dict['Songs22'][id_2] = {"artist_name": artist_name_2, "track_name":track_name_2, "lyrics": lyrics_2}
        id_2 += 1
    else:
        songs_wout_lyrics_2 += 1
    

with open("./all_songs.json", "w") as f:
    json.dump(songs_dict, f, indent=4)

print(songs_wout_lyrics_0, songs_wout_lyrics_1, songs_wout_lyrics_2)