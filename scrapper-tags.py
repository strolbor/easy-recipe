import os
import pathlib
from app.rezept import rezept,tags
import codecs

path = pathlib.Path(__file__).parent.absolute()
path2 = os.path.join(path,"webscraper","Rezepte") 
ldir = os.listdir(path2)

#Predefined Fkt
def write(file,eintrag):
    file.write(eintrag+"\n")

print("Init Stage")
# Datenspeicher
arrTags = []
# Logdaten
logWar = open("scrapper-tags.war.log","w")
fileAdder = open("scrapper-tags-add.txt","w")

# File Init
write(fileAdder,"from app import db")
write(fileAdder,"import sqlalchemy")
write(fileAdder,"from app.rezept import Association, rezept, zutat,tags\n")

write(fileAdder,"tags.query.delete()")
# Logik
print("ADD Stage",len(ldir))
for entry in ldir:
    # kurzbeschreibung öffnen
    filePath = os.path.join(path2,entry,"kurzbeschreibung.txt")
    try:
        rezaus = rezept.query.filter_by(name=entry).first()
        kurzbe = codecs.open(filePath,"r", encoding='ISO8859')
        inhalt = kurzbe.readline()
        # Inhalt trennen
        #print(">",inhalt)
        inhaltarray = inhalt.split(", ")
        for tagsein in inhaltarray:
            tagsein = tagsein.replace("ß","ss")
            tagsein = tagsein.replace("ü","ue")
            tagsein = tagsein.replace("ä","ae")
            tagsein = tagsein.replace("ö","oe")
            tagsein = tagsein.replace("\r","")
            tagsein = tagsein.replace("\n","")
            if len(tagsein) < 30:
                if tagsein not in arrTags:
                    arrTags.append(tagsein)
            else:
                write(logWar,f"{entry} hat keine vernüftigen Tags\n")
        #print(inhaltarray)
    except FileNotFoundError:
        write(logWar,f"{entry} hat keine Tags\n")
    
print("-----------")
print("Verknüpfer Stage")
write(fileAdder,f"db.session.rollback()")
write(fileAdder,f"def addTags(name):")
write(fileAdder,f"    new = tags(name=name)")
write(fileAdder,f"    db.session.add(new)")
write(fileAdder,f"    db.session.commit()\n")


write(fileAdder,"db.session.commit()")
for entry in arrTags:
    write(fileAdder,f"addTags(\"{entry}\")")
write(fileAdder,f"\n")

## Verknüpfer
ldir = os.listdir(path2)
print(len(ldir),ldir)
for rezeptname in ldir:
    filePath = os.path.join(path2,rezeptname,"kurzbeschreibung.txt")
    try:
        rezaus = rezept.query.filter_by(name=rezeptname).first()
        kurzbe = codecs.open(filePath,"r", encoding='ISO8859')
        inhalt = kurzbe.readline()
        inhaltarray = inhalt.split(", ")
        for tagsein in inhaltarray:
            tagsein = tagsein.replace("ß","ss")
            tagsein = tagsein.replace("ü","ue")
            tagsein = tagsein.replace("ä","ae")
            tagsein = tagsein.replace("ö","oe")
            tagsein = tagsein.replace("\r","")
            tagsein = tagsein.replace("\n","")
            if len(tagsein) < 30 and not (tagsein.startswith("ergibt") or tagsein.startswith("fuer")):
                write(fileAdder,f"rezaus = rezept.query.get({rezaus.id})")
                write(fileAdder,f"taaus = tags.query.filter_by(name=\"{tagsein}\").first()")
                write(fileAdder,f"rezaus.tags.append(taaus)")
        
    except FileNotFoundError:
        write(logWar,f"{rezeptname} hat keine Tags\n")


write(fileAdder,f"db.session.commit()")
#print(arrTags)
# Daten schließen
logWar.flush()
logWar.close()
fileAdder.flush()
fileAdder.close()