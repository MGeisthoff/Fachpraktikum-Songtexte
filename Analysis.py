
## Datei mit den Songtexten öffnen, um hiermit zu arbeiten:
with open("./all_songs_neu2.json") as f:
    songs_dict = json.load(f)

encoded= json.dumps (songs_dict, ensure_ascii=True)
songs_dict_0 =json.loads (encoded)


## Spacy 
nlp2 = spacy.load ("de_core_news_lg")
playlist="Spotify"
song_id=0

with open ('Nomen_csv.csv','w', newline ='') as nomen_file:
    writer = csv.writer(nomen_file, delimiter=';', lineterminator='\n')
    writer.writerow (["ID","Noun", "Gender", "Year", "Artist","Popularity"])    

    for song_id in tqdm(range(len(songs_dict_0[playlist]))):

        lyrics_from_song = songs_dict_0[playlist][str(song_id)]["lyrics"] #hier wird aus dem der Datei mit allen Songtexten nur das Lyrics abgefragt
        year_from_song = songs_dict_0[playlist][str(song_id)]["release_year"]
        artist_song=songs_dict_0[playlist][str(song_id)]["artist_name"]
        popularity_song=songs_dict_0[playlist][str(song_id)]["popularity"]
        doc3 = nlp2 (lyrics_from_song)

        for token in doc3: 
            if token.pos_ == "NOUN":
                    try:
                        row= ([song_id, token.text,token.morph.get('Gender'), year_from_song, artist_song, popularity_song])
                        writer.writerow(row)
                    except:
                        print(f"Error at Song {song_id} with word {token.text}.")
                        pass
            else:
                pass

scrape_data = False # decide, whether to scrape full data again or read an exisiting json file.

### Abfrage Genderneutrale Nomen:
import pandas as pd

complete_df = pd.DataFrame(columns=['Noun', 'Year', 'Artist', 'Popularity'])

gender_neu = pd.read_csv("./gender_neu_Nomen.csv",sep=";",header=None,encoding="utf8")
gender_neu = gender_neu.iloc[:, 0]

df = pd.read_csv(r"Nomen_csv.csv", encoding='ISO-8859-1', sep=';')



for idx, wort in tqdm(df.iterrows()):
    for gender in list(gender_neu):
        if wort["Noun"] == gender:
            complete_df.loc[len(complete_df)] = [wort["Noun"], wort["Year"], wort["Artist"], wort['Popularity']]

complete_df.to_csv("./Nomen_gender.csv")    

##Nomen singualisieren
##Packet ist nicht so gut in der deutschen Sprache
from pattern.text.de import singularize

df = pd.read_csv(r"Nomen_csv.csv", encoding='ISO-8859-1', sep=';')
df["Noun"] = [noun.capitalize() for noun in df["Noun"]]
nouns = list(df["Noun"])

singles =[singularize(noun) for noun in nouns]

### Abfrage Mann/Frau:
##Vergleich mit Singularisierung -> 1993 Ergebnisse
### ohne Singularisierung -> 4646 Ergebnisse 
##--> keine Verwendung von Singularisierung

mf_df = pd.DataFrame(columns=['Noun', 'Männlich','Year', 'Artist','Popularity'])

mf_neu = pd.read_csv("./Mann_Frau.csv",sep=";",header=None,encoding="ISO-8859-1")
mf_neu_m= mf_neu.iloc[:,1]
mf_neu_f= mf_neu.iloc[:,0]

df = pd.read_csv(r"Nomen_csv.csv", encoding='ISO-8859-1', sep=';')


for idx, wort in df.iterrows():
    ## männliche Worte
    for mf in list(mf_neu_m):
        if wort["Noun"] == mf:
            mf_df.loc[len(mf_df)] = [wort["Noun"], True,  wort["Year"], wort["Artist"], wort['Popularity']]
            
     ## weiblich Worte       
     
    for mf in list(mf_neu_f):
        
        if wort["Noun"] == mf:
            
            mf_df.loc[len(mf_df)] = [wort["Noun"], False,  wort["Year"], wort["Artist"],wort['Popularity']]
            

mf_df.to_csv("./Nomen_mf.csv")

## Abfrage Ausdrücke:

aus_df = pd.DataFrame(columns=['Noun','Year', 'Artist','Popularity'])

aus_neu_0 = pd.read_csv("./ausdruecke.csv",sep=";",header=None,encoding="ISO-8859-1")
aus_neu = aus_neu_0.iloc[:, 0]
aus_g = aus_neu_0.iloc[:,1]

df = pd.read_csv(r"Nomen_csv.csv", encoding='ISO-8859-1', sep=';')



for idx, wort in df.iterrows():
    for aus in list(aus_neu):
        if wort["Noun"] == aus:
            aus_df.loc[len(aus_df)] = [wort["Noun"], wort["Year"], wort["Artist"],wort['Popularity']]

aus_df.to_csv("./Nomen_ausdruecke.csv")  