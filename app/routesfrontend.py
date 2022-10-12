import os.path
from pathlib import Path
import random

from flask import render_template, flash, url_for, request, send_file
from werkzeug.utils import redirect

from app import app, forms, db
from app.RezeptRanking import getRezepteByZutatNamen, getRezepteByZutatIDs
from app.rezept import zutat, rezept, tags, Association
from app.Rezeptsammlung import getRezeptByEigenschaft, Rezeptsammlung, isVegan, isVegetarisch, isEinfach, isFleisch
import logging, time


@app.route('/base')
def index():
    return render_template('base.html', title="base")

#Zutatwahl
choices_array = []
alleZutaten = []

#TODO: irgendwie rezeptranking die rezeptRankings vermitteln, nicht über globale variable
globalRezeptRankings = []


@app.route('/rezeptranking', methods=['GET', 'POST'])
def rezeptranking():

    ausgewZutaten = request.args['zutaten'].split('|')
    #Mach int-Array draus wegen kompatibilität
    #zutatIDs = list(map(int, request.args['ids'].split('|')))

    testRankings = getRezepteByZutatIDs(ausgewZutaten=ausgewZutaten, bewertungsmodus=0)

    form = forms.rezeptranking()
    if request.method == "POST":
        if form.btnSort1.data:
            testRankings = getRezepteByZutatNamen(zutatnamen=ausgewZutaten, bewertungsmodus=1)
        elif form.btnSort2.data:
            testRankings = getRezepteByZutatNamen(zutatnamen=ausgewZutaten, bewertungsmodus=2)

        rezeptSuchbegriff = form.rezeptnamen.data

        if form.btnSuchen.data:
            if rezeptSuchbegriff != "":
                passendesRezept = rezept.query.filter_by(name=rezeptSuchbegriff).first()
                form.rezeptnamen.data = ""
                return redirect(url_for('rezeptsammlung_id', ids=passendesRezept.id))

            if form.rezeptkategorien.data:
                # EIgenschaft aus [vegan, vegetarisch, einfach, fleisch]
                eigenschaft = form.rezeptkategorien.data.lower()

                for ranking in testRankings.copy():
                    rez = rezept.query.get(ranking.rid)

                    bedingung = True
                    if eigenschaft == "vegan":
                        bedingung = isVegan(rez)
                    elif eigenschaft == "vegetarisch":
                        bedingung = isVegetarisch(rez)
                    elif eigenschaft == "fleisch":
                        bedingung = isFleisch(rez)
                    elif eigenschaft == "einfach":
                        bedingung = isEinfach(rez)

                    if not bedingung:
                        testRankings.remove(ranking)

            if form.maxZutaten.data:
                maxZutaten = int(form.maxZutaten.data)

                for ranking in testRankings.copy():
                    rez = rezept.query.get(ranking.rid)

                    if len(rez.zutaten) > maxZutaten:
                        testRankings.remove(ranking)


    return render_template('rezeptranking.html', title="Rezeptranking", rezeptRankings=testRankings, form=form, choices_array=ausgewZutaten)


home_html = "home.html"
alleZutaten = []
try:
    for entry in zutat.query.order_by(zutat.name).all():
        alleZutaten.append(entry.name)
    pass
except Exception as e:
    logging.error(e)

@app.route('/', methods=['GET', 'POST'])
def home():

    """alleTags = []
    alleTagNamen = []
    for rez in rezept.query.all():
        for tag in rez.tags:
            alleTags.append(tag.id)
            if not tag.id in alleTagNamen:
                alleTagNamen.append(tag.id)

    for tag in alleTagNamen:
        vorkommen = alleTags.count(tag)
        print(f"{tag} ist {vorkommen} mal")

    deltags = [64, 65, 66, 67, 20]"""


    form = forms.d_felder()

    global choices_array

    global alleZutaten

    def updateZutatenlisten():
        #form.selected.choices = choices_array.copy()
        verbleibendeZutaten = alleZutaten.copy()
        for entry in choices_array:
            try:
                verbleibendeZutaten.remove(entry)
            except:
                pass


        #form.eingabe.choices = verbleibendeZutaten
        #form.suchfeld.choices = [""] + verbleibendeZutaten

    updateZutatenlisten()

    #print("eingabe",form.eingabe.data)
    #print("selected",form.selected.data)
    if form.errors:
        for error_field, error_message in form.errors.iteritems():
            print(error_field,error_message)

    erstes = True
    '''FÜR ERSTEN AUFRUF IMMER MIT NEUEN SUBMIT BUTTONS ANPASSEN!!!!!'''
    if not  form.submitSuchen.data and not form.sumbitAddSuchbegriff.data:
        #prüfe welche Zutat gedrückt wurde
        for zut in alleZutaten:
            if 'btn%s'%zut in request.form:
                if zut not in choices_array:
                    choices_array.append(zut)
                else:
                    choices_array.remove(zut)
                updateZutatenlisten()
                erstes = False
                break

        # wenn sonst erster Aufruf
        if erstes:
            choices_array = []
            updateZutatenlisten()

    updateZutatenlisten()

    return render_template(home_html, form=form,choices_array=choices_array)


@app.route('/rezept', methods=['GET', 'POST'])
def rezeptanzeige():
    id = request.args['id']
    zutaten = request.args['zutaten'].split('|')
    form = forms.rezeptanzeige()
    thisrezept = rezept.query.get(id)
    #print(thisrezept.zutaten)

    class r_zutat:
        name = ""
        einheit = ""
        menge = ""
        verfuegbar = "❌"

        def __init__(self, _name, _einheit, _menge):
            self.name = _name
            self.einheit = _einheit
            self.menge = _menge
            for zut in zutaten:
                if _name == zut:
                    self.verfuegbar = "✅"


    r_tags = ""
    for tag in thisrezept.tags:
        r_tags += f"{tag.name}, "
    r_tags = r_tags[:-2]

    r_zutaten = []
    for zutat in thisrezept.zutaten:
        zname = zutat.hatzutat.name
        zeineit = zutat.hatzutat.einheit
        zmenge = zutat.menge
        #wenn menge gleich 0 dann daten kaputt -> nix anzeigen
        if zmenge == "0":
            zmenge = ""
        r_z = r_zutat(_name=zname, _einheit=zeineit, _menge=zmenge)
        r_zutaten.append(r_z)


    r_handl = []
    for handlungsschritt in thisrezept.handlungsschritte:
        r_handl.append(handlungsschritt.hatid.text)


    try:
        """ersetze Handlungsschritte temporär durch in Dateien erkannte HS"""
        rezPath = Path(__file__).parent.parent / "webscraper" / "Rezepte" / thisrezept.name
        txtHandl = open(rezPath / "handlungsschritte.txt", "r")
        arr_hs = []
        for line in txtHandl.readlines():
            arr_hs.append(line.replace("\n", ""))

        """ersetze Zutaten temporär mit Daten aus Webscraper, EINKAUFLISTE HAUT DANN NICHT GANZ HIN"""
        """txtZutaten = open(Path(__file__).parent.parent / "webscraper" / "Rezepte" / thisrezept.name / "zutaten.txt")
        arrZutaten =[]
        for line in txtZutaten.readlines():
            zname = line.strip().split("|")[1]
            menge = line.strip().split("|")[0]
            arrZutaten.append(r_zutat(zname, "", menge))"""
    except:
        pass


    """IN ORIGINAL NIMM r_zutaten statt arrZutaten"""
    #r_zutaten = arrZutaten
    # war vorher r_handl statt arr_hs
    # r_handl = arr_hs
    return render_template('rezeptanzeige.html', form=form, rezept=thisrezept, r_tags=r_tags, r_zutaten=r_zutaten,
                           anz_zutaten=len(r_zutaten), r_handl=r_handl, anz_handl=len(r_handl))


@app.route('/rezeptsammlung/<path:ids>', methods=['GET', 'POST'])
def rezeptsammlung_id(ids):
    form = forms.rezeptanzeige()
    thisrezept = rezept.query.get(ids)
    #print(thisrezept.zutaten)

    class r_zutat:
        name = ""
        einheit = ""
        menge = ""
        verfuegbar = ""

        def __init__(self, _name, _einheit, _menge):
            self.name = _name
            self.einheit = _einheit
            self.menge = _menge
            if _name in choices_array:
                self.verfuegbar = ""

    r_tags = ""
    for tag in thisrezept.tags:
        r_tags += f"{tag.name}, "
    r_tags = r_tags[:-2]

    r_zutaten = []
    for zutat in thisrezept.zutaten:
        zname = zutat.hatzutat.name
        zeineit = zutat.hatzutat.einheit
        zmenge = zutat.menge
        #wenn menge gleich 0 dann daten kaputt -> nix anzeigen
        if zmenge == "0":
            zmenge = ""
        r_z = r_zutat(_name=zname, _einheit=zeineit, _menge=zmenge)
        r_zutaten.append(r_z)

    r_handl = []
    for handlungsschritt in thisrezept.handlungsschritte:
        r_handl.append(handlungsschritt.hatid.text)


    """ersetze Handlungsschritte temporär durch in Dateien erkannte HS"""
    """rezPath = Path(__file__).parent.parent / "webscraper" / "Rezepte" / thisrezept.name
    txtHandl = open(rezPath / "handlungsschritte.txt", "r")
    arr_hs = []
    for line in txtHandl.readlines():
        arr_hs.append(line.replace("\n", ""))"""


    # war vorher r_handl statt arr_hs
    #r_handl = arr_hs

    return render_template('rezeptanzeige.html', form=form, rezept=thisrezept, r_tags=r_tags, r_zutaten=r_zutaten,
                           anz_zutaten=len(r_zutaten), r_handl=r_handl, anz_handl=len(r_handl))


@app.route('/rezeptsammlung', methods=['GET', 'POST'])
def rezeptsammlung():
    form=forms.rezeptsammlung()

    class PassendeRezeptliste:
        rezepte = []
        name = ""

        def __init__(self, _name, _rezepte):
            self.name = _name
            self.rezepte = _rezepte

    passendeRezepte = PassendeRezeptliste("", [])

    print("aufgerufen")

    #wenn nicht erster Aufruf:
    if request.method == "POST":
        print("POST")
        print(form.rezeptnamen.data)
        rezeptSuchbegriff = form.rezeptnamen.data
        if rezeptSuchbegriff != "":
            passendesRezept = rezept.query.filter_by(name=rezeptSuchbegriff).first()
            form.rezeptnamen.data = ""
            return redirect(url_for('rezeptsammlung_id', ids=passendesRezept.id))

        if form.btnSuchen.data:
            print("DATA gefunden")
            rezeptSuchbegriff = form.rezeptnamen.data
            if rezeptSuchbegriff != "":
                passendesRezept = rezept.query.filter_by(name=rezeptSuchbegriff).first()
                return redirect(url_for('rezeptsammlung_id', ids=passendesRezept.id))

            if form.rezeptkategorien.data:
                eigenschaft = form.rezeptkategorien.data.lower()
                passendeRezepte = PassendeRezeptliste(form.rezeptkategorien.data, getRezeptByEigenschaft(1000, eigenschaft))

            if form.maxZutaten.data:
                maxZutaten = int(form.maxZutaten.data)
                if form.rezeptkategorien.data:
                    for rez in passendeRezepte.rezepte.copy():
                        if len(rezept.query.get(rez.rid).zutaten) > maxZutaten:
                            passendeRezepte.rezepte.remove( Rezeptsammlung(rez.rid, rez.name, rez.tags, rez.bild) )
                else:
                    for rez in rezept.query.all():
                        if len(rez.zutaten) <= maxZutaten:
                            passendeRezepte.rezepte.append( Rezeptsammlung(rez.id, rez.name, rez.tags, rez.bild) )

            return render_template('rezeptsammlung.html', title="Rezeptsammlung", form=form,
                                   rezeptsammlungen=[passendeRezepte],
                                   anzRezeptvorschlaege=len(passendeRezepte.rezepte))


    #wenn erster Aufruf:

    #genriere iste von zufälligen Rezeptvorschlägen, die Kategorie erfüllen
    """_veganRezeptListe = random.shuffle(getRezeptByEigenschaft(100, "vegan"))
    _fleischRezeptListe = random.shuffle(getRezeptByEigenschaft(100, "fleisch"))
    _einfachRezeptListe = random.shuffle(getRezeptByEigenschaft(100, "einfach"))"""
    veganes = PassendeRezeptliste(_rezepte=getRezeptByEigenschaft(4, "vegan"), _name="Vegane Rezepte")
    fleisch = PassendeRezeptliste(_rezepte=getRezeptByEigenschaft(4, "fleisch"), _name="Rezepte mit Fleisch")
    einfach = PassendeRezeptliste(_rezepte=getRezeptByEigenschaft(4, "einfach"), _name="Einfache Rezepte")
    rezeptsammlungen = [veganes, fleisch, einfach]
    anzRezeptvorschlaege = 0
    for sammlung in rezeptsammlungen:
        anzRezeptvorschlaege += len(sammlung.rezepte)

    form.rezeptnamen.data = ""

    return render_template('rezeptsammlung.html', title="Rezeptsammlung", form=form, rezeptsammlungen=rezeptsammlungen,
                           anzRezeptvorschlaege=anzRezeptvorschlaege)

@app.route('/einkaufliste', methods=['GET', 'POST'])
def einkaufliste():
    zutaten = request.args['zutaten'].split('|')
    rezeptname = request.args['rezeptname']

    print(f"zutatarray in py  {zutaten}")
    temp = f"einkaufliste{random.randint(0, 1000)}"
    filepath = Path(__file__).parent.resolve() / 'einkauflisten' / f"{temp}.txt"
    txtZutatenliste = None
    try:
        txtZutatenliste = open(filepath, 'w')
    except:
        os.mkdir(filepath.parent)
        txtZutatenliste = open(filepath, 'w')


    txtZutatenliste.write("\n".join([f"Einkaufzettel für {rezeptname}:", ""] + zutaten))

    txtZutatenliste.close()

    print(f"current path {filepath}")
    return send_file(filepath, as_attachment=True)

