#Spacy muss gedownloaded werden mit : pip install -U pip setuptools wheel   und    pip install spacy 
#de_core_news_sm-3.5.0-py3-none-any.whl (muss gedownloaded werden -> https://spacy.io/models/de/)

nlp = spacy.load("de_core_news_sm")

list_of_nouns, list_of_pronouns = [], []

for song_id in tqdm(range(len(songs_dict["Prototyp"]))):

    lyrics_from_song = songs_dict["Prototyp"][str(song_id)]["lyrics"]
    doc = nlp(lyrics_from_song)

    # Ausgabe lediglich von Wörtern, die Nomen und Pronomen sind:
    for token in doc: 
        if token.pos_ == "NOUN":
            list_of_nouns.append(token.text)
        elif token.pos_ == "PRON":
            list_of_pronouns.append(token.text)
        else:
            pass
  
        