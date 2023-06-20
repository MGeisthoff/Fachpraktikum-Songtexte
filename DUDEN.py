## DUDEN API

#pip install duden
# Hilfsseite: https://pypi.org/project/duden/
#Dictionary
result_nomen = {"Nomen": {}}

unknown_nomen = 0
id = 0
for word in distinct_nouns:
        n = duden.get(word)  #DUDEN API
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
