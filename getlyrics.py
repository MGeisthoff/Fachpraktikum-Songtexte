import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import lyricsgenius

# Setzen Sie hier Ihre eigenen API-Schlüssel und Zugangsdaten ein
SPOTIPY_CLIENT_ID = '46da6046625f409cb53ab06bf807861d'
SPOTIPY_CLIENT_SECRET = '00efb0ab68db4f1eaf27ec53a4c1e068'
GENIUS_ACCESS_TOKEN = 'OsBvEsJ_OLKYR42CJoaA_N97GNOS44XXFk4KPPcLtCYnWmDwnnzY2RpcG_SdG25a'

# Erstelle eine Instanz von SpotifyClientCredentials mit Deinen Zugangsdaten
client_credentials_manager = SpotifyClientCredentials(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Erstelle eine Instanz von Genius mit Ihrem Zugangstoken
genius = lyricsgenius.Genius(GENIUS_ACCESS_TOKEN)

# Gebe die ID der Playlist ein, aus der die Songtexte extrahiert werden sollen
playlist_id = '2siI2ILJEPr88yibWLgQQl'  #Playlist: "Deutsche Songs die jeder kennt ;)"

# Hole sich die Tracks aus der Playlist
tracks = sp.playlist_tracks(playlist_id)

# Durchlaufe jeden Track in der Playlist
for track in tracks['items']:
    # Holen Sie sich den Namen des Künstlers und den Titel des Tracks
    artist_name = track['track']['artists'][0]['name']
    track_name = track['track']['name']

    # Suche nach dem Song auf Genius
    song = genius.search_song(track_name, artist_name)

    # Überprüfe, ob ein Song gefunden wurde
    if song:
        # Drucken Sie den Songtext
        print(f"{artist_name} - {track_name}")
        print(song.lyrics)
        print()