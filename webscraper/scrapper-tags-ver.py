import os
import pathlib
from app.rezept import rezept,tags

path = pathlib.Path(__file__).parent.absolute()
path2 = os.path.join(path,"webscraper","Rezepte") 
ldir = os.listdir(path2)

#Predefined Fkt
def write(file,eintrag):
    file.write(eintrag+"\n")


# Datenspeicher
arrTags = []
# Logdaten
logWar = open("scrapper-tags.war.log","w")
fileAdder = open("scrapper-tags-add.txt","w")
for entry in ldir:
    # kurzbeschreibung öffnen
    filePath = os.path.join(path2,entry,"kurzbeschreibung.txt")
    try:
        rezaus = rezept.query.filter_by(name=entry).first()
        kurzbe = open(filePath,"r")
        inhalt = kurzbe.readline()
        # Inhalt trennen
        print(">",inhalt)
        inhaltarray = inhalt.split(", ")
        for tagsein in inhaltarray:
            if len(tagsein) < 30:
                if tagsein not in arrTags:
                    arrTags.append(tagsein)
            else:
                logWar.write(f"{entry} hat keine vernüftigen Tags\n")
        print(inhaltarray)
    except FileNotFoundError:
        logWar.write(f"{entry} hat keine Tags\n")