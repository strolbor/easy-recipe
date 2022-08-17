import os
import pathlib
from app.rezept import rezept,tags, handlungsschritt

#Predefined Fkt
def write(file,eintrag):
    file.write(eintrag+"\n")

path = pathlib.Path(__file__).parent.absolute()
path2 = os.path.join(path,"webscraper","Rezepte") 
ldir = os.listdir(path2)

fileWriter = open("handlungschritte-adder.py","w")

for rezeptentry in ldir:
    print("#",rezeptentry)
    inputfile = open(os.path.join(path2,rezeptentry,"handlungsschritte.txt"),"r")
    for line in inputfile:
        if len(line) > 10:
            # Line ist langgenugt ein eigener Eintrag zu sein
            # um die Leerzeilen rauszufiltern
            line = line.replace("\n","")
            print(">",line)
    inputfile.close()

# Closer
fileWriter.flush()
fileWriter.close()