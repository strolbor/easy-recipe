from random import random

from flask import render_template, flash, url_for, request
from werkzeug.utils import redirect

from app import app, forms
from app.RezeptRanking import getRezepteByZutatNamen
from app.rezept import zutat, rezept
from app.Rezeptsammlung import getRezeptByEigenschaft, Rezeptsammlung
import logging



@app.route('/base')
def index():
    return render_template('base.html', title="base")

#Zutatwahl
choices_array = []
alleZutaten = []

#TODO: irgendwie rezeptranking die rezeptRankings vermitteln, nicht über globale variable
globalRezeptRankings = []

@app.route('/update_choices_array/<path:jsarray>', methods=['GET', 'POST'])
def update_choices_array(jsarray):
    # jsarray ist array mit | abgetrennt
    global choices_array, globalRezeptRankings
    choices_array = jsarray.split("|")
    globalRezeptRankings = globalRezeptRankings = getRezepteByZutatNamen(zutatnamen=choices_array, bewertungsmodus=0)
    return redirect(url_for('rezeptranking'))

@app.route('/rezeptranking', methods=['GET', 'POST'])
def rezeptranking():
    global globalRezeptRankings, choices_array
    form = forms.rezeptranking()
    if request.method == "POST":
        if form.btnSort0.data:
            globalRezeptRankings = getRezepteByZutatNamen(zutatnamen=choices_array, bewertungsmodus=0)
        elif form.btnSort1.data:
            globalRezeptRankings = getRezepteByZutatNamen(zutatnamen=choices_array, bewertungsmodus=1)
        elif form.btnSort2.data:
            globalRezeptRankings = getRezepteByZutatNamen(zutatnamen=choices_array, bewertungsmodus=2)

    return render_template('rezeptranking.html', title="Rezeptranking", rezeptRankings=globalRezeptRankings, form=form)


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
    global choices_array
    form = forms.d_felder()

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
            print("first")
            choices_array = []
            updateZutatenlisten()


    if form.validate_on_submit():
        print("validate")

        if form.sumbitAddSuchbegriff.data and len(form.suchfeld.choices) != 0 and form.suchfeld.data!="":
            # Item soll hinzugefügt werden
            # Neue ausgewählte Elemente werden kopiert
            # und hinzugefügt
            #print(str(form.suchfeld.choices) + " zutaten links übrig")
            entry = form.suchfeld.data
            if not choices_array.__contains__(entry):
                choices_array.append(entry)

            # Neue List wird kopiert in die Liste
            updateZutatenlisten()

            return render_template(home_html, form=form,choices_array=choices_array)

        elif 1== 0 and form.submitSuchen.data:
            print("Submit suchen")
            """gibt passende Reihenfolge der passendsten Rezepte für die ausgewählten Zutaten"""
            ausgewZutaten = []
            global globalRezeptRankings
            for entry in choices_array:
                ausgewZutaten.append(entry)
            globalRezeptRankings = getRezepteByZutatNamen(zutatnamen=ausgewZutaten, bewertungsmodus=0)

            updateZutatenlisten()

            choices_array.sort()
            zNamen = [str(choice) for choice in choices_array]
            return redirect(url_for('rezeptranking')) #zNamen=",".join(zNamen)))

        else:
            #flash("Don't hack this!")
            pass


    updateZutatenlisten()

    return render_template(home_html, form=form,choices_array=choices_array)


@app.route('/rezept/<ids>/', methods=['GET', 'POST'])
def rezeptanzeige(ids):
    form = forms.rezeptanzeige()
    thisrezept = rezept.query.get(ids)
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
            if _name in choices_array:
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
