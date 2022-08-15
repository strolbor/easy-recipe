from random import random

from flask import render_template, flash, url_for
from werkzeug.utils import redirect

from app import app, forms
from app.RezeptRanking import getRezepteByZutatNamen
from app.rezept import zutat, rezept


@app.route('/base')
def index():
    return render_template('base.html', title="base")

#TODO: irgendwie rezeptranking die rezeptRankings vermitteln, nicht über globale variable
globalRezeptRankings = []
@app.route('/rezeptranking', methods=['GET', 'POST'])
def rezeptranking():
    return render_template('rezeptranking.html', title="Rezeptranking", rezeptRankings=globalRezeptRankings)

choices_array = []
alleZutaten = []

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
        global choices_array
        form.selected.choices = choices_array.copy()
        global alleZutaten
        verbleibendeZutaten = alleZutaten.copy()
        for entry in choices_array:
            try:
                verbleibendeZutaten.remove(entry)
            except:
                no = "thing"

        #verbleibendeZutaten = updateMitSuchtext( verbleibendeZutaten=verbleibendeZutaten.copy() ).copy()

        if form.suchtext.data != "" and form.suchtext.data != None :
            uebrigeZutaten = []
            for entry in verbleibendeZutaten.copy():
                if str(form.suchtext.data).lower() in str(entry).lower():
                    uebrigeZutaten.append(entry)
            verbleibendeZutaten = uebrigeZutaten.copy()
            #form.suchtext.data = ""

        form.eingabe.choices = verbleibendeZutaten

    updateZutatenlisten()

    print("eingabe",form.eingabe.data)
    print("selected",form.selected.data)
    if form.errors:
        for error_field, error_message in form.errors.iteritems():
            print(error_field,error_message)
    if form.validate_on_submit():
        print("validate")

        if form.submitAdd.data:
            print("submitAdd")
            # Item soll hinzugefügt werden
            # Neue ausgewählte Elemente werden kopiert
            # und hinzugefügt
            for entry in form.eingabe.data.copy():
                if not choices_array.__contains__(entry):
                    choices_array.append(entry)
            
            # Neue List wird kopiert in die Liste
            updateZutatenlisten()
            
            if len(form.eingabe.data) == 0:
                flash("Input error")
            else:
                flash("Success")
            # neues Template an Client senden
            form.eingabe.data = []
            form.selected.data = []
            
            return render_template(home_html,form=form)
        
        if form.submitRm.data:
            print("submitRm")
            # Item soll aus choices entfernt werden

            # Aktuelle Auswahl kopieren
            #form.selected.choices = choices_array.copy()
            array = choices_array.copy()
            print(array)
            # Was wir entfernen wollen, kopieren
            to_delete = form.selected.data.copy()
            print(to_delete)
            try:
                for entry in to_delete:
                    array.remove(entry)
            except ValueError:
                pass
            print(array)
            #form.selected.choices = array.copy()
            choices_array = array.copy()

            updateZutatenlisten()

            if len(form.selected.data) == 0:
                flash("Input error")
            else:
                flash("Success")

            
            form.eingabe.data = []
            form.selected.data = []
            return render_template(home_html,form=form)
        if form.submitLoesen.data:
            form.eingabe.data = []
            form.selected.data = []
            form.selected.choices = choices_array
            return render_template(home_html,form=form)
        if form.submitSuchen.data:
            print("Submit suchen")
            """gibt passende Reihenfolge der passendsten Rezepte für die ausgewählten Zutaten"""
            ausgewZutaten = []
            global globalRezeptRankings
            for entry in form.selected.choices.copy():
                ausgewZutaten.append((entry))
            globalRezeptRankings = getRezepteByZutatNamen(ausgewZutaten)

            updateZutatenlisten()

            return redirect(url_for('rezeptranking'))
            #return render_template("rezeptranking.html", rezeptRankings = _rezeptRankings)

        if form.submitSuchtext.data:
            updateZutatenlisten()
            return render_template(home_html, form=form)
        else:
            flash("Don't hack this!")


    if form.submitAdd.data == False and form.submitRm.data == False and form.submitSuchen.data == False:
        #erster Aufruf
        print("first")
        choices_array = []
        updateZutatenlisten()

    print("last return")
    updateZutatenlisten()
    return render_template(home_html, form=form)


@app.route('/rezept/<path:ids>', methods=['GET', 'POST'])
def rezeptanzeige(ids):
    form = forms.rezeptanzeige()
    thisrezept = rezept.query.get(ids)
    print(thisrezept.zutaten)

    for entry in thisrezept.zutaten:
        print(entry.hatzutat.name)

    r_tags = ""
    for tag in thisrezept.tags:
        r_tags += f"{tag}, "

    flash(r_tags)

    r_zutaten = ""
    for zutat in thisrezept.zutaten:
        r_zutaten += f"{zutat.hatzutat.name}, "
    flash(r_zutaten)

    # Ich hatte dir mal die aktuelle Datenstruktur erklärt, oder?
    # Wir können nicht direkt auf die Zutat zugreifen. Wir müssen ein Umweg über die Association machen.
    # Das bedeutet wir rufen das Rezept -> Association -> Zutat auf
    # Du hast allerdings noch ds allte Schema: Rezept -> Zutat versucht. Das klappt ja nicht.
    # Du hast permanent auf die Assoc. zugegriffen und es als Zutat behandelt.
    # Das war der Fehler ;)
    # Naja, ich hätte es dir anscheinend nochmal in Erinnerung rufen sollten.
    


    return render_template('rezeptanzeige.html', form=form, rezept=thisrezept, r_tags=r_tags, r_zutaten=r_zutaten)
