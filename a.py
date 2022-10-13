from app.rezept import zutat

z = zutat.query.all()

for e in z:
    print(f"{e.id}: {e.name}")