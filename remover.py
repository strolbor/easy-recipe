from app import db
from app.rezept import rezept,Association,zutat

fileWriter = open("neuverknüpfung.txt","w")
fileWriter.write(f"from app import db\n")
fileWriter.write(f"from app.rezept import rezept,Association,zutat\n\n")

while True:
    try:
        print("\nBitte geben Sie die Zutaten ID ein")
        zid = input("ID bitte:")
        zutat0 = zutat.query.get(int(zid))
        print(f"Die Zutat {zutat0.name} hat folgende Verknüpfungen:")
        for entry in zutat0.rezepte:
            print(f"> {entry.rezept.name} ID: {entry.rezept.id}")
        eingabe = input("Wollen Sie das neu verknüpfen?")
        if eingabe == "y":
            rid = input("Bitte geben Sie die ID des Rezepts ein:")
            zid_neu = input("Bitte geben Sie die ID des neuen Zutat ein:")
            fileWriter.write(f"remo=zutat.query.get({zid})\n")
            fileWriter.write(f"db.session.delete(remo)\n")
            fileWriter.write(f"rezept1 = rezept.query.get({rid})\n")
            fileWriter.write(f"zutat_neu = zutat.query.get({zid_neu})\n")
            remo = zutat.query.get(zid)
            fileWriter.write(f"assoc1 = Association(menge={remo.rezepte[0].menge})\n")
            fileWriter.write(f"assoc1.hatzuat = zutat_neu\n")
            fileWriter.write(f"with db.session.no_autoflush:\n")
            fileWriter.write(f"    rezept1.zutaten.append(assoc1)\n")
            fileWriter.write(f"db.session.commit()\n\n")
            fileWriter.flush()
    except ValueError:
        pass

fileWriter.flush()
fileWriter.close()