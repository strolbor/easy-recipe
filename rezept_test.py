from app import db
from app.rezept import rezept,zutat,  Association

rezept1 = rezept.query.get(1)


# iterate through child objects via association, including association
# attributes
for assoc in rezept1.zutaten:
    print(assoc.menge)
    print(assoc.hatzutat)

ass = Association.query.get((1,1))
print(ass)