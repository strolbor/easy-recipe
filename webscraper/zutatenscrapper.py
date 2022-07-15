import os
import pathlib
from Levenshtein import distance
import re

path = pathlib.Path(__file__).parent.absolute()
path2 = os.path.join(path,"Rezepte") 
ldir = os.listdir(path2)

fileout2 = open("add.txt","w")

zutatenarray = []
for entry in ldir:
    file = open(os.path.join(path2,entry,"zutaten.txt"))
    for line in file:
        arraytmp = line.split("|")

        # Zutatennamen filtern
        zutateninhalt = arraytmp[1]
        zutateninhalt = zutateninhalt.split(",")[0]
        zutateninhalt = zutateninhalt.split(" ")[0]
        zutateninhalt = zutateninhalt.replace(" ","")
        zutateninhalt = zutateninhalt.replace('\n',"")
        zutateninhalt = zutateninhalt.split("(")[0]

        # einheit
        mengeRAW = arraytmp[0]
        tmp = re.search("[^0-9]+",mengeRAW)
        if tmp is not None:
            print(tmp)
            tmp3 = tmp.span()
            menge = mengeRAW[tmp3[0]:tmp3[1]]
            if menge.startswith(" "):
                menge = menge[1:]

        
        if zutateninhalt not in zutatenarray:
            zutatenarray.append(zutateninhalt)
            #print("Zutat",zutateninhalt, "im Rezept", entry)
            #addZutat(name="{zutateninhalt}",bild="",einheit="{mengeRAW}")
            fileout2.write(f"addZutat(name=\"{zutateninhalt}\",bild=\"\",einheit=\"{menge}\")\n")

    file.close()
zutatenarray.sort()
fileout = open("sortiert.txt","w")

for entry in zutatenarray:
    fileout.write(entry + "\n")
    
    
fileout.flush()
fileout.close()
fileout2.flush()
fileout2.close()
