import os
import pathlib
import re
import operator

#
## Mit dieses Hilfskript werden die Zutaten normalisiert und in die Datenbank eingespeichert
#

path = pathlib.Path(__file__).parent.absolute()
path2 = os.path.join(path,"Rezepte") 
ldir = os.listdir(path2)

fileout = open("zutaten-sortiert.txt","w")
fileout2 = open("zutaten-add.txt","w")
fileout3 = open("scrapper-zutat.log","w")

zutatenarray = []
zutatenclasar = []

class zutatinhalt():
    name : str
    def getname(self) -> str:
        return self.name
    def __init__(self,name : str,einheit):
        self.name = name
        self.einheit = einheit


def write(file,eintrag):
    file.write(eintrag+"\n")

for entry in ldir:
    file = open(os.path.join(path2,entry,"zutaten.txt"))
    fileout3.write("Rezeptname: "+entry+"\n")
    for line in file:
        arraytmp = line.split("|")

        # Zutatennamen filtern
        zutateninhalt = arraytmp[1]
        
        zutateninhalt = zutateninhalt.split(",")[0]
        zutateninhalt = zutateninhalt.replace('\n','')
        zutateninhalt = zutateninhalt.split("(")[0]
        if zutateninhalt.endswith(" "):
            zutateninhalt = zutateninhalt[:len(zutateninhalt)-1]

        fileout3.write("> Zutatnamen:" + zutateninhalt + "\n")
        
        # einheit
        mengeRAW = arraytmp[0]
        
        tmp = re.search("[^0-9]+",mengeRAW)
        if tmp is not None:
            fileout3.write("> Match: " + tmp.string + "\n") 
            tmp3 = tmp.span()
            menge = mengeRAW[tmp3[0]:tmp3[1]]
            if menge.startswith(" "):
                menge = menge[1:]

        
        if zutateninhalt not in zutatenarray:
            zutatenarray.append(zutateninhalt)
            
            zutateninhalt = zutateninhalt.replace('\n','')
            menge = menge.replace('\n','')
            menge = menge.replace('/n','(n)')#/e
            menge = menge.replace('/e','(e)')#/e
            menge = menge.replace('½','1/2')
            menge = menge.replace('¼','1/4')
            
            zwischenspeicher = zutatinhalt(name=zutateninhalt,einheit=menge)
            zutatenclasar.append(zwischenspeicher)
            towrite = f"addZutat(name=\"{zutateninhalt}\",bild=\"\",einheit=\"{menge}\")\n"
            fileout3.write(towrite)
            fileout2.write(towrite)
            

    file.close()
#zutatenclasar.sort(key=operator.attrgetter('name'))

# Ab hier erst verändern #


for entry in zutatenclasar:
    tmpar = entry.getname().split(" ")
    write(fileout3,entry.getname() + " gab es Probleme" + "\n" )
    if len(tmpar) >= 2:
        print("Beim ITEM:", entry.getname())
        print("Mehrere Leerzeichen erkannt.")
        print("Wollen Sie das Item behalten?")
        eingabe = input("[y/N]")
        if eingabe == "y" or eingabe == "Y":
            print("-> genommen")
            write(fileout,entry.name)#Fileout ist -sortet.txt
            towrite = f"addZutat(name=\"{entry.name}\",bild=\"\",einheit=\"{entry.einheit}\")"
            write(fileout2,towrite)
        else:
            print("->verworfen")
            write(fileout3,"->verworfen")
            # Ich will es nicht übernehmen, also nichts tun

    else:
        write(fileout,entry.name)#Fileout ist -sortet.txt
        towrite = f"addZutat(name=\"{entry.name}\",bild=\"\",einheit=\"{entry.einheit}\")"
        write(fileout2,towrite)




fileout.flush()
fileout.close()
fileout2.flush()
fileout2.close()
fileout3.flush()
fileout3.close()