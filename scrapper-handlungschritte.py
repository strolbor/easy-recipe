import os
import pathlib
from turtle import position
from app.rezept import rezept,tags, handlungsschritt,AssociationRHhat
from app import db
import codecs

#Predefined Fkt
def write(file,eintrag):
    file.write(eintrag+"\n")


path = pathlib.Path(__file__).parent.absolute()
path2 = os.path.join(path,"webscraper","Rezepte") 
ldir = os.listdir(path2)

fileWriter = open("handlungschritte-adder.py","w")
write(fileWriter,"from app import db")
write(fileWriter,"import sqlalchemy")
write(fileWriter,"from app.rezept import Association,AssociationRHhat,handlungsschritt, rezept, zutat,tags\n")


#ldir = ["Bauerntopf"]
for rezeptentry in ldir:
    rezaus = rezept.query.filter_by(name=rezeptentry).first()
    print("#",rezeptentry,rezaus)
    inputfile = codecs.open(os.path.join(path2,rezeptentry,"handlungsschritte.txt"),"r", encoding='ISO8859')#ds#ds
    pos = 0
    for line in inputfile:
        if len(line) > 10:
            pos +=1
            # Line ist langgenugt ein eigener Eintrag zu sein
            # um die Leerzeilen rauszufiltern
            line = line.replace("\n","")
            line = line.replace("\r","")
            line = line.replace('"',"")
            #print(">",line.split(" "))

            # Objekt erstellen
            write(fileWriter,f"handob = handlungsschritt(text=\"{line}\")")
            write(fileWriter,"db.session.add(handob)")
            write(fileWriter,"db.session.commit()")
            
            write(fileWriter,f"rezaus = rezept.query.get({rezaus.id})")
            write(fileWriter,f"assoc = AssociationRHhat(position=\"{pos}\")")
            write(fileWriter,"assoc.hatid = handob")
            write(fileWriter,"with db.session.no_autoflush:")
            write(fileWriter,"    rezaus.handlungsschritte.append(assoc)")
            write(fileWriter,"db.session.commit()\n")
            fileWriter.flush()
    inputfile.close()

# Closer
fileWriter.flush()
fileWriter.close()