import os
import pathlib
from Levenshtein import distance
import re

path = pathlib.Path(__file__).parent.absolute()
path2 = os.path.join(path,"Rezepte") 
ldir = os.listdir(path2)

fileout2 = open("zutaten-add.txt","w")

zutatenarray = []
zutatenclasar = []

class zutatinhalt():
    def __init__(self,name,einheit):
        self.name = name
        self.einheit = einheit
        
for entry in ldir:
    file = open(os.path.join(path2,entry,"zutaten.txt"))
    print("Rezeptname:",entry)
    for line in file:
        arraytmp = line.split("|")

        # Zutatennamen filtern
        zutateninhalt = arraytmp[1]
        tmpanz = []
        
        zutateninhalt = zutateninhalt.split(",")[0]
        zutateninhalt = zutateninhalt.replace('\n','')
        zutateninhalt = zutateninhalt.split("(")[0]

        tmpanz.append(zutateninhalt)
        print("> Zutatnamen:",tmpanz)
        
        # einheit
        mengeRAW = arraytmp[0]
        
        tmp = re.search("[^0-9]+",mengeRAW)
        if tmp is not None:
            print(">",tmp)
            tmp3 = tmp.span()
            menge = mengeRAW[tmp3[0]:tmp3[1]]
            if menge.startswith(" "):
                menge = menge[1:]

        
        if zutateninhalt not in zutatenarray:
            zutatenarray.append(zutateninhalt)
            
            #print("Zutat",zutateninhalt, "im Rezept", entry)
            #addZutat(name="{zutateninhalt}",bild="",einheit="{mengeRAW}")
            zutateninhalt = zutateninhalt.replace('\n','')
            menge = menge.replace('\n','')
            menge = menge.replace('/n','(n)')#/e
            menge = menge.replace('/e','(e)')#/e
            menge = menge.replace('½','1/2')
            menge = menge.replace('¼','1/4')
            
            zwischenspeicher = zutatinhalt(name=zutateninhalt,einheit=menge)
            zutatenclasar.append(zwischenspeicher)
            towrite = f"addZutat(name=\"{zutateninhalt}\",bild=\"\",einheit=\"{menge}\")\n"
            print(towrite)
            fileout2.write(towrite)
            

    file.close()
zutatenarray.sort()
fileout = open("zutaten-sortiert.txt","w")

for entry in zutatenarray:
    fileout.write(entry + "\n")


for entry in zutatenclasar:
    towrite = f"addZutat(name=\"{entry.name}\",bild=\"\",einheit=\"{entry.einheit}\")\n"
    fileout2.write(towrite)
    
fileout.flush()
fileout.close()
fileout2.flush()
fileout2.close()
