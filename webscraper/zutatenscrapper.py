import os
import pathlib
from Levenshtein import distance

path = pathlib.Path(__file__).parent.absolute()
path2 = os.path.join(path,"Rezepte") 
ldir = os.listdir(path2)

zutatenarray = []
for entry in ldir:
    file = open(os.path.join(path2,entry,"zutaten.txt"))
    for line in file:
        zutateninhalt = line.split("|")[1]
        zutateninhalt = zutateninhalt.split(",")[0]
        zutateninhalt = zutateninhalt.split(" ")[0]
        zutateninhalt = zutateninhalt.replace(" ","")
        zutateninhalt = zutateninhalt.replace('\n',"")
        zutateninhalt = zutateninhalt.split("(")[0]
        
        
        if zutateninhalt not in zutatenarray:
            zutatenarray.append(zutateninhalt)
            print("Zutat",zutateninhalt, "im Rezept", entry)
    file.close()
zutatenarray.sort()
fileout = open("sortiert.txt","w")
for entry in zutatenarray:
    fileout.write(entry + "\n")
fileout.flush()
fileout.close()

