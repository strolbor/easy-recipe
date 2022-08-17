import app
from app.rezept import zutat, rezept

class RezeptRanking:
    rid = -1
    name = ""
    """speichere Arrays wie Tags,vorhandene/fehlendeZutatenNamen als String, damit auf Website schöner angezeigt wird"""
    tags = "Keine Tags"
    bild = ""
    vorhandeneZutatenNamen = ""
    fehlendeZutatenNamen = ""
    """Bewertung 0 bis 1, 1 ist gut und 0 schlecht = 1 - fehlendeZutaten/zutatenGesamtNötig"""
    bewertung = 0

    def __init__(self, _rid, _name, _tags, _bild, _vorhandeneZutatenNamen, _fehlendeZutatenNamen):
        if (len(_fehlendeZutatenNamen) + len(_vorhandeneZutatenNamen)) > 0:
            self.bewertung = 1 - len(_fehlendeZutatenNamen) / (len(_fehlendeZutatenNamen) + len(_vorhandeneZutatenNamen))
        self.rid=_rid
        self.name = _name
        if len(_tags) > 0:
            self.tags = _tags
        self.bild = _bild
        if len(_vorhandeneZutatenNamen) > 0:
            for zname in _vorhandeneZutatenNamen:
                self.vorhandeneZutatenNamen += f"{zname}{', '}"
            self.vorhandeneZutatenNamen = self.vorhandeneZutatenNamen[:-2]
        else:
            self.vorhandeneZutatenNamen = "Keine"
        if len(_fehlendeZutatenNamen) > 0:
            for zname in _fehlendeZutatenNamen:
                self.fehlendeZutatenNamen += f"{zname}{', '}"
            self.fehlendeZutatenNamen = self.fehlendeZutatenNamen[:-2]
        else:
            self.fehlendeZutatenNamen = "Keine"


    def __repr__(self):
        return 'Rezept {} mit ID:{} Tags:{} Bild-URL:{} vorhandenen Zutaten {} fehlenden Zutaten {} Bewertung:{}'.format(
            self.name,self.rid,self.tags,self.bild,self.vorhandeneZutatenNamen,self.fehlendeZutatenNamen,self.bewertung
        )

    """compare"""
    def __lt__(self,other):
        return self.bewertung < other.bewertung

    def __eq__(self, other):
        return self.rid == other.rid


def getRezepteByZutatNamen(zutatnamen):
    #zutatnamen = ["Salz", "Apfel", "Ei", "Mehl", "Kartoffeln"]
    """speichere Zutaten und mögliche Rezepte ab"""
    zutatIDList = []
    rezeptIDList = []
    """Trage ZutatIDs die der Nutzer hat zusammen und RezeptIDs von rezepten, die mit jeder Zutat in Frage kommen"""
    for zutatname in zutatnamen:
        zutatid = -1
        """finde Zutat-ID zum Zutatenname"""
        for entry in zutat.query.filter_by(name=zutatname):
            zutatid = entry.id
            if not zutatid in zutatIDList:
                zutatIDList.append(zutatid)
        """finde Rezepte, die diese Zutat beinhalten"""
        for entry in zutat.query.get(zutatid).rezepte:
            """entry sind Association-Object (siehe rezept.py)"""
            if not entry.rid in rezeptIDList:
                rezeptIDList.append(entry.rid)

    """Rückgabewert: diese Liste, wird von rezeptanzeige.html interpretiert und genutzt"""
    rezeptRankings = []
    for rid in rezeptIDList:
        vorhandeneZutatenNamen = []
        fehlendeZutatenNamen = []
        _rezept = rezept.query.get(rid)
        for entryZutat in _rezept.zutaten:
            """entryZutat ist Association"""
            if entryZutat.zid in zutatIDList:
                vorhandeneZutatenNamen.append(entryZutat.hatzutat.name)
            else:
                fehlendeZutatenNamen.append(entryZutat.hatzutat.name)

        strTags = ""
        if _rezept.tags != None:
            for tag in _rezept.tags:
                strTags += f"{tag}{', '}"
            strTags = strTags[:-2]
        rezeptRanking = RezeptRanking(_rezept.id, _rezept.name, strTags, _rezept.bild, vorhandeneZutatenNamen, fehlendeZutatenNamen)
        if not rezeptRanking in rezeptRankings:
            rezeptRankings.append(rezeptRanking)

    """Sortiere Liste anhand der Bewertungen der Elemente absteigend:"""
    rezeptRankings.sort(reverse=True)
    rezeptRankings = rezeptRankings[0:app.Config.REZEPTRANKINGS_PER_PAGE]
    return rezeptRankings

    #TODO: Tags beachten, Mengen beachten