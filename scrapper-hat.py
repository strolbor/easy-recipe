import os
import pathlib
import re
import operator
from app import db
from app.rezept import rezept, zutat
import codecs

path = pathlib.Path(__file__).parent.absolute()
path2 = os.path.join(path,"webscraper","Rezepte") 
ldir = os.listdir(path2)

fileout = open("hat-fileout.1.txt","w")
fileAdder = open("hat-add.txt","w")
fileLog = open("hat-scrapper.log","w")
fileWarning = open("hat-warning.log","w")


def write(file,eintrag):
    file.write(eintrag+"\n")


for entry in ldir:
    # = open(os.path.join(path2,entry,"zutaten.txt"))
    file = codecs.open(os.path.join(path2,entry,"zutaten.txt") ,'r', encoding='ISO8859')
    write(fileLog,"Rezeptname: "+entry) # entry => Ordnername 
    rezept_aus = rezept.query.filter_by(name=entry).first()
    write(fileLog,str(rezept_aus))
    for line in file:
        write(fileLog,f"- {line}")
        arr = line.split("|")
        name = arr[1]
        name = name.replace('\n','')
        # TODO: Zutat auswählen
        zutat_aus = zutat.query.filter_by(name=name).all()
        write(fileLog,f"{arr[1]},{zutat_aus}")
        while len(zutat_aus) == 0:
            print(f"Zutat: {name} im Rezept: {entry} wurde nicht gefunden.")
            x = input("Bitte geben Sie den richtigen Namen ein:")
            zutat_aus = zutat.query.filter_by(name=x).all()
            if len(zutat_aus) > 1:
                k = 0
                print("Es wurde folgendes gefunden:")
                for entry in zutat_aus:
                    print(f"{k}: {entry} ")
                auswahl = input("Welcher Eintrag soll genommen werden:")
                zutat_aus = zutat_aus[auswahl]
            print(zutat_aus, "wurde gefunden.")
            

                #write(fileLog,"-- abort")
                #write(fileWarning,f"Aborting at {entry} bei {line}")
        # TODO: Regex für die Zahlen einrichten
        
        # TODO: Appenden und comitten
        







        write(fileAdder,"assoc1 = Association(menge=500,optional=False)")
        write(fileAdder,"zutat = zutat.query.get(73)")
        write(fileAdder,"rezept1 = rezept.query.get(1)")
        write(fileAdder,"assoc1.hatzutat= zutat")
        write(fileAdder,"with db.session.no_autoflush:")
        write(fileAdder,"    rezept1.zutaten.append(assoc1)")
        write(fileAdder,"db.session.commit()\n")

    file.close()



fileout.flush()
fileout.close()
fileAdder.flush()
fileAdder.close()
fileLog.flush()
fileLog.close()
fileWarning.flush()
fileWarning.close()