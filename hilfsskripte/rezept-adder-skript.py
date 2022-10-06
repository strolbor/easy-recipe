import os
import pathlib
import shutil

#
## Mit diesen Hilfsskript werden die Rezepte erstellt. und in der "data-rezept-add.py" gespeichert.
# 

path = pathlib.Path(__file__).parent.absolute()
path2 = os.path.join(path,"Rezepte") 
ldir = os.listdir(path2)

fileout2 = open("data-rezept-add.py","w")

rezeptarray = []
zahler = 1
for entry in ldir:
    picpath = f"rezept{zahler}/{entry}.png"
    path3 =  os.path.join(path,"dummy",picpath.split("/")[0])
    zahler = zahler + 1
    if not os.path.exists(path3):
        os.makedirs(path3)
    shutil.copy(os.path.join(path2,entry,entry+".png"),os.path.join(path3,entry+".png"))
    
    try:
        filer = open(os.path.join(path2,entry,"kurzbeschreibung.txt"),"r")
        kurzbeschreibung = filer.readline()
        filer.close()
    except:
        kurzbeschreibung = ""
    fileout2.write(f"addRezept(name='{entry}',bild='{picpath}',kurzbe='{kurzbeschreibung}')\n")

    
fileout2.flush()
fileout2.close()
