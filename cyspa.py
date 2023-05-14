#Spacy muss gedownloaded werden mit : pip install -U pip setuptools wheel   und    pip install spacy 
import spacy
nlp = spacy.load("de_core_news_sm")
import de_core_news_sm
nlp = de_core_news_sm.load()
doc = nlp("Das ist ein Satz.")
print([(w.text, w.pos_) for w in doc])