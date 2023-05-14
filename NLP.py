
import re
#import getlyrics.py
#string = getlyrics.py.song
string = "[Refrain] Zeiten ändern sich und wir uns gleich mit Du und ich, so jung auf diesem alten Polaroid-Bild Das letzte Mal, als wir uns sah'n, ist viel zu lang her Doch jetzt lachen wir, als wenn du nie weggewesen wärst"
#Entfernen von allen Satzzeichen und eckigen Klammern 
string = re.sub("\!|\'|\?|\,|\.|\[|\]", "", string)
print(string) 
#Zerlegt den Text in einzelne Strings
zerteilt = string.split()
print(zerteilt)
