# Fachpraktikum-Songtexte
 
 
 1. Spotify and LyricGenius API: 
 - Im Terminal ausführen: pip install spotipy and pip install lyricsgenius


 NLP.py  -> Segmentation (aktuell nur zum Teilen von text in einzelne Textbausteine) -> kann wahrscheinlich durch cyspa ersetzt werden 
 cyspa.py -> Segmentation and Tokenization and POS Tagging (nur Nomen und Pronomen herausfiltern)


 #Probleme: Doppelte Bedeutung von manchen Deutschen Wörtern (Mal: Muttermal und Mal sehen wie es wird) -> zwei verschiedene Wortarten -> idee: spacy trainiert mit regeln und dadurch fehler 

 all_songs_json -> hier gibt es auch Lieder mit Quatschtext!!! (kann nur manuell herausgenommen werden, wenn nötig!) (ist als weißer Text sichtbar)
