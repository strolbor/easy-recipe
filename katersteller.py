from app import db
from app.rezept import zutat, kategorie


zlist = zutat.query.all()
zkat = kategorie.query.all()
i = 0
for entry in zkat:
    print(f"{i}: {entry.name}")
    i += 1

for zuta in zlist:
    if len(zuta.kategorie) != 0:
        print(f"Zutat {zuta.name} hat keine Kategorie.")
        print(f"Bitte geben Sie die den entsprechenden Index ein")
        xin = input("Index:")
        try:
            x = int(xin)
        except ValueError:
            print("Wird nicht gesetzt.")
            continue
        zuta.kategorie = []
        zuta.kategorie.append(zkat[x])
        db.session.commit()