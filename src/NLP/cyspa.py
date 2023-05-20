#NEU #Spacy muss gedownloaded werden mit : pip install -U pip setuptools wheel   und    pip install spacy 
#de_core_news_sm-3.5.0-py3-none-any.whl (muss gedownloaded werden -> https://spacy.io/models/de/) + Dateo öffnen
#de_core_news_lg-3.5.0-py3-none-any.whl
#de_dep_news_trf-3.5.0-py3-none-any.whl
import spacy 
from tqdm import tqdm


nlp = spacy.load("de_core_news_sm")
#nlp1 = spacy.load ("de_dep_news_trf")
nlp2 = spacy.load ("de_core_news_lg")

list_of_nouns, list_of_pronouns = [], []

def spacify_with_coref(lyrics_from_song):
    doc3 = nlp2(lyrics_from_song)
    doc = nlp(lyrics_from_song)

    doc._.coref_chains = doc3._.coref_chains

    return doc

for song_id in tqdm(range(len(songs_dict["Prototyp"]))):

    lyrics_from_song = songs_dict["Prototyp"][str(song_id)]["lyrics"]
    doc = nlp(lyrics_from_song)
    #doc2 = nlp1 (lyrics_from_song)
    doc3 = nlp2 (lyrics_from_song)

    # Ausgabe lediglich von Wörtern, die Nomen und Pronomen sind:
    for token in doc: 
        if token.pos_ == "NOUN":
            list_of_nouns.append(token.text)
        elif token.pos_ == "PRON":
            list_of_pronouns.append(token.text)
        else:
            pass


  
        