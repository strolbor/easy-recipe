from random import random

from flask import render_template, flash, url_for, request
from werkzeug.utils import redirect

from app import app, forms
from app.RezeptRanking import getRezepteByZutatNamen
from app.rezept import zutat, rezept
from app.Rezeptsammlung import getRezeptByEigenschaft, Rezeptsammlung



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
@app.route('/', methods=['GET', 'POST'])
def home():
    global choices_array
    form = forms.d_felder()

    global alleZutaten
    alleZutaten = []
    try:
        for entry in zutat.query.order_by(zutat.name).all():
            alleZutaten.append(entry.name)
        pass
    except Exception as e:
        print(e)

    def updateZutatenlisten():
        #global choices_array
        form.selected.choices = choices_array.copy()
        #global alleZutaten
        verbleibendeZutaten = alleZutaten.copy()
        for entry in choices_array:
            try:
                verbleibendeZutaten.remove(entry)
            except:
                pass

        #verbleibendeZutaten = updateMitSuchtext( verbleibendeZutaten=verbleibendeZutaten.copy() ).copy()

        if form.suchtext.data != "" and form.suchtext.data != None :
            uebrigeZutaten = []
            for entry in verbleibendeZutaten.copy():
                if str(form.suchtext.data).lower() in str(entry).lower():
                    uebrigeZutaten.append(entry)
            verbleibendeZutaten = uebrigeZutaten.copy()
            #form.suchtext.data = ""

        form.eingabe.choices = verbleibendeZutaten
        form.suchfeld.choices = [""] + verbleibendeZutaten

    updateZutatenlisten()

    print("eingabe",form.eingabe.data)
    print("selected",form.selected.data)
    if form.errors:
        for error_field, error_message in form.errors.iteritems():
            print(error_field,error_message)



    '''FÜR ERSTEN AUFRUF IMMER MIT NEUEN SUBMIT BUTTONS ANPASSEN!!!!!'''
    if not form.submitAdd.data and not form.submitRm.data and not form.submitSuchen.data and not form.submitLoesen.data \
            and not form.submitSuchtext.data and not form.sumbitAddSuchbegriff.data:
        #prüfe welche Zutat gedrückt wurde
        erstes = True
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


    #TODO: Legacy Ifs aufräumen
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

            # neues Template an Client senden
            form.eingabe.data = []
            form.selected.data = []

            return render_template(home_html, form=form,choices_array=choices_array)

        elif form.submitSuchen.data:
            print("Submit suchen")
            """gibt passende Reihenfolge der passendsten Rezepte für die ausgewählten Zutaten"""
            ausgewZutaten = []
            global globalRezeptRankings
            for entry in form.selected.choices.copy():
                ausgewZutaten.append((entry))
            globalRezeptRankings = getRezepteByZutatNamen(zutatnamen=ausgewZutaten, bewertungsmodus=0)

            updateZutatenlisten()

            return redirect(url_for('rezeptranking'))
            #return render_template("rezeptranking.html", rezeptRankings = _rezeptRankings)

        elif form.submitSuchtext.data:
            updateZutatenlisten()
            return render_template(home_html, form=form,choices_array=choices_array)

        else:
            #flash("Don't hack this!")
            pass


    print("last return")
    updateZutatenlisten()
    return render_template(home_html, form=form,choices_array=choices_array)


@app.route('/rezept/<path:ids>', methods=['GET', 'POST'])
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

    #wenn nicht erster Aufruf:
    if request.method == "POST":
        if form.btnSuchen.data:
            rezeptSuchbegriff = form.rezeptnamen.data
            if rezeptSuchbegriff != "":
                passendesRezept = rezept.query.filter_by(name=rezeptSuchbegriff).first()
                return redirect(url_for('rezeptsammlung_id', ids=passendesRezept.id))

            if form.rezeptkategorien.data:
                eigenschaft = form.rezeptkategorien.data.lower()
                passendeRezepte = PassendeRezeptliste(form.rezeptkategorien.data, getRezeptByEigenschaft(1000, eigenschaft))

            if form.maxZutaten.data:
                maxZutaten = int(form.maxZutaten.data)
                for rez in passendeRezepte.rezepte.copy():
                    if len(rezept.query.get(rez.rid).zutaten) > maxZutaten:
                        passendeRezepte.rezepte.remove( Rezeptsammlung(rez.rid, rez.name, rez.tags, rez.bild) )


            form.rezeptnamen.data = ""
            #form.rezeptkategorien.data = ""
            #form.maxZutaten.data = ""

            return render_template('rezeptsammlung.html', title="Rezeptsammlung", form=form,
                                   rezeptsammlungen=[passendeRezepte],
                                   anzRezeptvorschlaege=len(passendeRezepte.rezepte))


    #wenn erster Aufruf:
    veganes = PassendeRezeptliste(_rezepte=getRezeptByEigenschaft(3, "vegan"), _name="Vegane Rezepte")
    fleisch = PassendeRezeptliste(_rezepte=getRezeptByEigenschaft(3, "fleisch"), _name="Rezepte mit Fleisch")
    einfach = PassendeRezeptliste(_rezepte=getRezeptByEigenschaft(3, "einfach"), _name="Einfache Rezepte")
    rezeptsammlungen = [veganes, fleisch, einfach]
    anzRezeptvorschlaege = 0
    for sammlung in rezeptsammlungen:
        anzRezeptvorschlaege += len(sammlung.rezepte)

    return render_template('rezeptsammlung.html', title="Rezeptsammlung", form=form, rezeptsammlungen=rezeptsammlungen,
                           anzRezeptvorschlaege=anzRezeptvorschlaege)
