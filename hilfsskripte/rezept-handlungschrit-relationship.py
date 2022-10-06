#!/usr/bin/python
# -*- coding: ISO8859 -*-

import os
import pathlib
from turtle import position
from app.rezept import rezept,tags, handlungsschritt,AssociationRHhat
from app import db
import codecs

#
## Mithilfe diesen Skriptes werden Die Verknüpfung zwischen Rezept und Handlungsschritte erstellt.
#

#Predefined Fkt
def write(file,eintrag):
    file.write(eintrag+"\n")


path = pathlib.Path(__file__).parent.absolute()
path2 = os.path.join(path,"webscraper","Rezepte") 
ldir = os.listdir(path2)

fileWriter = open("handlungschritte-adder.py","w")
write(fileWriter,"#!/usr/bin/python")
write(fileWriter,"# -*- coding: ISO8859 -*-")
write(fileWriter,"from app import db")
write(fileWriter,"import sqlalchemy")
write(fileWriter,"from app.rezept import Association,AssociationRHhat,handlungsschritt, rezept, zutat,tags\n")


#ldir = ["Bauerntopf"]
for rezeptentry in ldir:
    rezaus = rezept.query.filter_by(name=rezeptentry).first()
    print("#",rezeptentry,rezaus)
    #inputfile = codecs.open(os.path.join(path2,rezeptentry,"handlungsschritte.txt"),"r", encoding='ISO8859')
    #
    inputfile = codecs.open(os.path.join(path2,rezeptentry,"handlungsschritte.txt"),"r")
    pos = 0
    array = inputfile.readlines()
    #print(array)
    try:
        array.remove('\r\n')
        array.remove('\n')
    except ValueError:
        pass
    arr2 = []
    for line in array:
        line = line.replace("\n","")
        line = line.replace("\r","")
        line = line.replace('"',"")#
        line = line.replace('�',"�")
        line= line.replace("ß","ss")
        line= line.replace("ü","ue")
        line= line.replace("ä","ae")
        line= line.replace("ö","oe")
        arr2.append(line)
    pos +=1
    #print(arr2)
    line = ' '.join(arr2)
    
    print(line)
   
    # Objekt erstellen
    write(fileWriter,f"handob = handlungsschritt(text=\"{line}\")")
    write(fileWriter,"db.session.add(handob)")
    write(fileWriter,"db.session.commit()")
    
    write(fileWriter,f"rezaus = rezept.query.get({rezaus.id})")
    write(fileWriter,f"assoc = AssociationRHhat(position=1)")
    write(fileWriter,"assoc.hatid = handob")
    write(fileWriter,"with db.session.no_autoflush:")
    write(fileWriter,"    rezaus.handlungsschritte.append(assoc)")
    write(fileWriter,"db.session.commit()\n")
    fileWriter.flush()
    inputfile.close()

# Closer
fileWriter.flush()
fileWriter.close()