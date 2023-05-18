#Spacy muss gedownloaded werden mit : pip install -U pip setuptools wheel   und    pip install spacy 
# 	de_core_news_sm-3.5.0-py3-none-any.whl (muss gedownloaded werden -> https://spacy.io/models/de/)
import spacy
#from spacy.lang.de.examples import sentences 
nlp = spacy.load("de_core_news_sm")
import Übungstext
string = Übungstext.string
doc = nlp(string)
print(doc.text)
# Ausgabe jedes Wortes mit entsprechender Wortart:
for token in doc:
    print(token.text, token.pos__)
# Ausgabe lediglich von Wörtern, die Nomen und Pronomen sind:
for token in doc: 
    if token.pos_ == "NOUN" or token.pos_ == "PRON":
         print (token.text, token.pos_)
  
        