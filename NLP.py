
import re
#import getlyrics.py
#string = getlyrics.py.song.lyrics
import Übungstext
string = Übungstext.string
#Entfernen von allen Satzzeichen und eckigen Klammern 
string = re.sub("\!|\'|\?|\,|\.|\[|\]", "", string)
print(string) 
#Zerlegt den Text in einzelne Strings
zerteilt = string.split()
print(zerteilt)
