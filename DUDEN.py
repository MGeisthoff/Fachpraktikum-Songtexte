#pip install duden
# Hilfsseite: https://pypi.org/project/duden/
#Dictionary
result_nomen = {"Nomen": {}}

unknown_nomen = 0
id = 0
for word in distinct_nouns:
        n = duden.get(word)  
        if n is not None: 
                result_nomen['Nomen'][id] = {"WORT": n.name, "ARTIKEL": n.article}
                id += 1
        else:
                unknown_nomen +=1
    
    #pb.update(1)
with open('Nomen.json', 'w') as fp:
      dict_result_nomen=json.dump(result_nomen, fp, indent=4)

#########################################################################NOMEN
## nach m,w,n unterteilen in einzelne JSON Dateien
nomen_m , nomen_w, nomen_n = [],[],[] 
   
for id in result_nomen["Nomen"]: 
    if  result_nomen ["Nomen"][id]["ARTIKEL"]== "der":
        nomen_m.append(result_nomen["Nomen"][id]["WORT"])
    elif result_nomen ["Nomen"][id]["ARTIKEL"]== "die":
        nomen_w.append(result_nomen["Nomen"][id]["WORT"])
    elif result_nomen ["Nomen"][id]["ARTIKEL"]== "das":
        nomen_n.append(result_nomen["Nomen"][id]["WORT"])
    else:
        pass
with open('Nomen_m.json', 'w') as fp:
      dict_result_nomen=json.dump(nomen_m, fp, indent=4)
with open('Nomen_w.json', 'w') as fp:
      dict_result_nomen=json.dump(nomen_w, fp, indent=4)
with open('Nomen_n.json', 'w') as fp:
      dict_result_nomen=json.dump(nomen_n, fp, indent=4)


#########################################################################PRONOMEN
pronomen_m, pronomen_w = [],[]

for word in list_of_pronouns:
    #männlich
    #personal
    if word == "er":
        pronomen_m.append(word)
    elif word == "Er":
        pronomen_m.append(word)
    elif word == "ER":
        pronomen_m.append(word)
    elif word == "ihn":
        pronomen_m.append(word)
    elif word == "Ihn":
        pronomen_m.append(word)
    elif word == "IHN":
        pronomen_m.append(word)
    elif word == "ihm":
        pronomen_m.append(word)
    elif word == "Ihm":
        pronomen_m.append(word)
    elif word == "IHM":
        pronomen_m.append(word)
    #possesiv
    elif word == "sein":
        pronomen_m.append(word)
    elif word == "Sein":
        pronomen_m.append(word)
    elif word == "SEIN":
        pronomen_m.append(word)
    elif word == "seine":
        pronomen_m.append(word)
    elif word == "Seine":
        pronomen_m.append(word)
    elif word == "SEINE":
        pronomen_m.append(word)
    elif word == "Seiner":
        pronomen_m.append(word)
    elif word == "seiner":
        pronomen_m.append(word)
    elif word == "SEINER":
        pronomen_m.append(word)
    elif word == "Seines":
        pronomen_m.append(word)
    elif word == "seines":
        pronomen_m.append(word)
    elif word == "SEINES":
        pronomen_m.append(word)
    elif word == "Seinen":
        pronomen_m.append(word)
    elif word == "seinen":
        pronomen_m.append(word)
    elif word == "SEINEN":
        pronomen_m.append(word)
    elif word == "Seinem":
        pronomen_m.append(word)
    elif word == "seinem":
        pronomen_m.append(word)
    elif word == "SEINEM":
        pronomen_m.append(word)
    #demonstrativ
    elif word == "Der":
        pronomen_m.append(word)
    elif word == "der":
        pronomen_m.append(word)
    elif word == "DER":
        pronomen_m.append(word)
    elif word == "Dieser":
        pronomen_m.append(word)
    elif word == "DIESER":
        pronomen_m.append(word)
    elif word == "dieser":
        pronomen_m.append(word)
    elif word == "Derjenige":
        pronomen_m.append(word)
    elif word == "DERJENIGE":
        pronomen_m.append(word)
    elif word == "derjenige":
        pronomen_m.append(word)
    elif word == "Derselbe":
        pronomen_m.append(word)
    elif word == "DERSELBE":
        pronomen_m.append(word)
    elif word == "derselbe":
        pronomen_m.append(word)
    elif word == "Jener":
        pronomen_m.append(word)
    elif word == "jener":
        pronomen_m.append(word)
    elif word == "JENER":
        pronomen_m.append(word)
    #weiblich
    #personal
    if word == "sie":
        pronomen_w.append(word)
    elif word == "Sie":
        pronomen_w.append(word)
    elif word == "SIE":
        pronomen_w.append(word)
    elif word == "ihr":
        pronomen_w.append(word)
    elif word == "IHR":
        pronomen_w.append(word)
    elif word == "Ihr":
        pronomen_w.append(word)
    #possessiv
    elif word == "Ihre":
        pronomen_w.append(word)
    elif word == "IHRE":
        pronomen_w.append(word)
    elif word == "ihre":
        pronomen_w.append(word)
    elif word == "IHREN":
        pronomen_w.append(word)
    elif word == "Ihren":
        pronomen_w.append(word)
    elif word == "ihren":
        pronomen_w.append(word)
    elif word == "IHREM":
        pronomen_w.append(word)
    elif word == "ihrem":
        pronomen_w.append(word)
    elif word == "Ihrem":
        pronomen_w.append(word)
    #demonstrativ
    elif word == "Die":
        pronomen_w.append(word)
    elif word == "DIE":
        pronomen_w.append(word)
    elif word == "die":
        pronomen_w.append(word)
    elif word == "Diejenige":
        pronomen_w.append(word)
    elif word == "diejenige":
        pronomen_w.append(word)
    elif word == "DIEJENIGE":
        pronomen_w.append(word)
    elif word == "DIESELBE":
        pronomen_w.append(word)
    elif word == "dieselbe":
        pronomen_w.append(word)
    elif word == "Dieselbe":
        pronomen_w.append(word)
    elif word == "DIESE":
        pronomen_w.append(word)
    elif word == "diese":
        pronomen_w.append(word)
    elif word == "Diese":
        pronomen_w.append(word)
    elif word == "Jene":
        pronomen_w.append(word)
    elif word == "JENE":
        pronomen_w.append(word)
    elif word == "jene":
        pronomen_w.append(word)
   
    else:
        pass

print(pronomen_m)
print (pronomen_w)
with open('Pronomen_m.json', 'w') as fp:
      dict_result_nomen=json.dump(pronomen_m, fp, indent=4)
with open('Pronomen_w.json', 'w') as fp:
      dict_result_nomen=json.dump(pronomen_w, fp, indent=4)