import os
import pathlib
import re
import operator
from app import db
from app.rezept import rezept, zutat
import codecs

#
## Mithilfe diesen Skripts werden Zutaten und Rezepte mit einander verbunden.
#

path = pathlib.Path(__file__).parent.absolute()
path2 = os.path.join(path,"webscraper","Rezepte") 
ldir = os.listdir(path2)

fileAdder = open("hat-add.py","w")
fileLog = open("hat-scrapper.log","w")
bigerror = open("bigerror.txt","w")


def write(file,eintrag):
    file.write(eintrag+"\n")

def info(rezept,line):
    maxs = max(len(rezept.name),len(line)) +len("Rezept:") + 5
    for i in range(0,maxs): print("=",end='')
    print()
    print(f"Rezept: {rezept.name}")
    tmp = line.replace('\n','')
    print(f"Line: {tmp}")
    for i in range(0,maxs): print("=",end='')
    print()

# add-file vorbereiten
write(fileAdder,"from app import db")
write(fileAdder,"import sqlalchemy")
write(fileAdder,"from app.rezept import Association, rezept, zutat\n")


for entry in ldir:
    # = open(os.path.join(path2,entry,"zutaten.txt"))
    file = codecs.open(os.path.join(path2,entry,"zutaten.txt") ,'r', encoding='ISO8859')
    write(fileLog,"Rezeptname: "+entry) # entry => Ordnername 
    rezept_aus = rezept.query.filter_by(name=entry).first()
    for line in file:
        write(fileLog,f"- {line}".replace('\n',''))
        arr = line.split("|")
        
        try:
            name = arr[1]
        except IndexError:
            print("INFO:",entry,line,arr)
            exit()
        name = name.replace('\n','')
        name = name.split("(")[0]
        name = name.split(",")[0]
   
        zutat_aus = zutat.query.filter(zutat.name.like(name+"%")).all()
        
        zutat_wahl  = None
        # Abfrage, ob wir keine Elemente haben
        if len(zutat_aus) == 0 or len(zutat_aus) > 50:
            while (len(zutat_aus) == 0 or len(zutat_aus) > 50):
                info(rezept_aus,line)
                write(fileLog,f"> (W) Bei {name} wurde nichts gefunden.")
                print("Es wurde nichts gefunden.")
                x = input("Bitte geben Sie den richtigen Namen ein:")
                zutat_aus = zutat.query.filter(zutat.name.like(x+"%")).all()
                
        if len(zutat_aus) > 50:
            write(bigerror,f"{rezept_aus} {line}")
        # Haben wir genau 1 Element, so ist es 
        # Und geben es weiter an den Appender
        print("zutat aus:",len(zutat_aus))
        if len(zutat_aus) == 1:
            zutat_wahl = zutat_aus[0]

        # Haben wir mehr als ein Element, so müssen wir wählen
        while len(zutat_aus) > 1:
            write(fileLog,f"> (W) Bei {name} wurden mehrere Zutaten gefunden.")
            info(rezept_aus,line)
            k = 0
            if len(zutat_aus) > 0:
                print(f"Es wurde zur Eingabe mehrere verschiedene Begriffe gefunden:")
                for entry in zutat_aus:
                    print(f"{k}: {entry} ")
                    k += 1
                auswahl = input("Welcher Eintrag soll genommen werden:")

            try:
                zutat_wahl = zutat_aus[int(auswahl)]
                zutat_aus = []
            except IndexError:
                print(f"Ihre Eingabe ({auswahl}) ist außerhalb des Arrays. Bitt erneut versuchen.\n")
            except ValueError:
                write(bigerror,f"{auswahl} war ein ValueEroor.")
            print(zutat_wahl, "wurde gewählt.\n")
        
        write(fileLog,f"> {zutat_wahl.name} wurde genommen.")
        # Die Zahl der Menge holen
        tmp = re.search("[0-9]+",line)
        menge = 0
        if not tmp is None:
            menge = int(line[tmp.span()[0]:tmp.span()[1]])


        
        write(fileLog,f"> wird {zutat_wahl.name} hinzugefügt.")
        write(fileAdder,f"try:")
        write(fileAdder,f"   print('Rezept: {str(rezept_aus.name)} wird {zutat_wahl.name} hinzugefügt.')")
        write(fileAdder,f"   assoc1 = Association(menge={menge},optional=False)")
        write(fileAdder,f"   zutat = zutat.query.get({str(zutat_wahl.id)})")
        write(fileAdder,f"   rezept1 = rezept.query.get({str(rezept_aus.id)})")
        write(fileAdder,f"   assoc1.hatzutat= zutat")
        write(fileAdder,f"   with db.session.no_autoflush:")
        write(fileAdder,f"       rezept1.zutaten.append(assoc1)")
        write(fileAdder,f"   db.session.commit()")
        write(fileAdder,f"except sqlalchemy.exc.IntegrityError:")
        write(fileAdder,f"   print('Fehler: hier über mir')")
        write(fileAdder,f"   db.session.rollback()\n")


    file.close()



fileAdder.flush()
fileAdder.close()
fileLog.flush()
fileLog.close()
bigerror.flush()
bigerror.close()