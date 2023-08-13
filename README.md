# Fachpraktikum-Songtexte
 
 - Im File Packages.py sind alle Packages enthalten, die für dieses Projekt geladenen werden müssen, um das gesamte Projekt auszuführen. 
 
 1. Spotify and LyricGenius API: (getlyrics.py)
Um diese Datei ausführen zu können muss ein Konto bei Spotify sowie LyricsGenius erstellt werden. 
Mit dieser Datei werden die Spotifysongs oder -playlisten ausgesucht und die entsprechenden Songtexte, Artists, Erscheinungsdatum sowie -jahre und die Popularität (eEigenwert bei Spotify) herausgefiltert. 
Dann wird eine Datei all_songs_neu2.json erstellt, welche die zuvor genannten Daten enthält in einem Dictonary Spotify. Hier können auch mehrere Dictonaries für verschiedene Playlisten angelegt werden. 

2. Analyse der Songs: (Analysis.py)
Zur Unterstützung der Ausführung der Datei wurden drei CSV Dateien erstellt 
- ausdruecke.csv (Quelle: https://de.wikipedia.org/wiki/Kategorie:Schimpfwort_(Person))
- Mann_Frau.csv 
- gender_neu_Nomen.csv (Quelle: https://geschicktgendern.de/ , Stand 06/2023)

Nun wird auf die Datei aus 1. das Spacy Framework de_core_news_lg-3.5.0-py3-none-any.whl (Quelle: https://spacy.io/models/de/) ausgeführt. Dieses dient 



 NLP.py  -> Segmentation (aktuell nur zum Teilen von text in einzelne Textbausteine) -> kann wahrscheinlich durch cyspa ersetzt werden 
 cyspa.py -> Segmentation and Tokenization and POS Tagging (nur Nomen und Pronomen herausfiltern)


 #Probleme: Doppelte Bedeutung von manchen Deutschen Wörtern (Mal: Muttermal und Mal sehen wie es wird) -> zwei verschiedene Wortarten -> idee: spacy trainiert mit regeln und dadurch fehler 

 all_songs_json -> hier gibt es auch Lieder mit Quatschtext!!! (kann nur manuell herausgenommen werden, wenn nötig!) (ist als weißer Text sichtbar)
