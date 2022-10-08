import imp
import re
from app import app, db, forms
from app.rezept import rezept, zutat, handlungsschritt, tags, Association, AssociationRHhat
from app.backend_helper import createArrayHelper, savepic, createArrayHelper2
from app.routesbackend import showclass

import os
from flask import redirect, render_template, request, abort
from flask.helpers import flash, url_for
from sqlalchemy import desc
import sqlalchemy

##############
#   Rezept   #
##############


@app.route('/rezept/show/')
def showRezepte():
    return showclass(rezept, rezept.name, "Rezepte", "showRezepte")

def newRezept(rname: str, tagarray):
    """Kapselung von Rezepte"""

    # Rezept anlegen
    new = rezept(name=rname)

    # Tags adden
    for entry in tagarray:
        if int(entry) > 0:
            new.tags.append(tags.query.get(entry))

    """ Neues Rezept der Datenbank hinzufügen."""
    db.session.add(new)
    db.session.commit()
    rnew: rezept = rezept.query.filter_by(name=rname).first()
    return rnew.id

@app.route("/rezept/eingabe/", methods=["POST", "GET"])
def nutzerrezeptein():
    """Nutzereingabe Menü"""
    form = forms.nutzerein()
    # Das ist schon so fertig
    if request.method == 'POST' and form.submit.data:
        # Reload der Seite mit dem Flash, der zeigt, dass es gespeichert wruden ist.
        return redirect(url_for('nutzerrezeptein'))
    return render_template('nutzer_rezeptanlege.html', form=form, zutaten=zutat.query.all(), tags=tags.query.all())

@app.route("/rezept/eingabe/ctl/", methods=["POST", "GET"])
def postrezept():
    """AJAX Methode zum Anlegen der Methode.
    AJAX ruft diese Funktion bevor der eigentliche POST-Methode nutzereingabe().
    """
    if request.method == 'POST':
        # Informationen aus Stream abrufen
        zutaten = request.form.getlist('zutat[]')
        menge = request.form.getlist('menge[]')
        rezeptname = request.form.get('rname')
        taglist = request.form.getlist('tags[]')
        handlungsschritttext = request.form.get('handlung')

        # Rezept anlegen
        """ Wenn das Rezept nicht existiert, erstelle es"""
        newRezept(rezeptname, taglist)
        print(f"AJAX hat Rezept {rezeptname} erstellt")
        rnew: rezept = rezept.query.filter_by(name=rezeptname).first()

        #Bild hochladen
        pic_url = savepic('bildupload', request.files, f'rezept{rnew.id}')
        if not (pic_url == "A" or pic_url == "B"):
            rnew.bild = pic_url
        
        # Zutaten verknüpfen
        counter = 0
        for entry in zutaten:
            # Abfrage, ob Verbindung schon da ist
            if Association.query.get((rnew.id,entry)) is None:
                if int(entry) > 0:  # Abfrage, ob es eine gültige Zutat ist. Gültig heißt nicht -1 oder kleiner
                    zuttmp = zutat.query.get(entry)
                    print(f"Erhalte Zutaten zum hinzufügen: {zuttmp.name}")
                    assoc1 = Association(menge=menge[counter], optional=False)
                    assoc1.hatzutat = zuttmp
                    with db.session.no_autoflush:
                        rnew.zutaten.append(assoc1)
                # else: nichts zu tun, weil -1 ungültig ist und für Keine Angabe stehen    
                counter += 1
            else:
                flash(f"Diese Verknüpfung ({rnew.id},{entry}) existiert schon.")

        # Handlungschritt anlegen
        txt = handlungsschritttext
        txtarr = txt.split("\n")
        posArr = 0
        # entry ist ein String
        for entry in txtarr:
            # Wir müssen neue Associations machen
            handNew = handlungsschritt(text=entry)
            assocNew = AssociationRHhat(position=posArr)
            handlung = handNew
            assocNew.hatid = handlung
            with db.session.no_autoflush:
                rnew.handlungsschritte.append(assocNew)
            db.session.commit()
            print("Neue Assoc")
            posArr +=1
                
        db.session.commit()

        # speichern
        flash(f"{rnew.name} ({rnew.id}) wurde gespeichert!")
    return "ok"

@app.route('/rezept/modify/<path:ids>/', methods=['GET', 'POST'])
def modifyrezept(ids):
    form = forms.rezeptaendern()
    zuRezept: rezept = rezept.query.get(ids)
    if zuRezept is None:
        page = int(request.args.get('page', 1))
        return redirect(url_for('showRezepte', page=page))
    if request.method == "POST" and form.submit.data:
        # Rezept bearbeiten
        # Und alles mögliche aus dem Formular abspeichern
        print("Validate")

        # Name speichern
        zuRezept.name = form.rezeptname.data

        # Bild aktualisieren
        picure_url = savepic('bildupload', request.files, f'rezept{ids}')
        if not (picure_url == "A" or picure_url == "B"):
            zuRezept.bild = picure_url

        # Handlungsschritt Text bearbeiten
        txt = form.handlung.data
        txtarr = txt.split("\n")
        assocArr = zuRezept.handlungsschritte

        # Die Position des Array speichern um zu entscheiden, ob wir neue Assocs brauchen oder nicht.

        posArray = 0
        # Für jeden Eintrag im Textarea müssen wir ein Eintrag in der Assoc machen
        for entry in txtarr:
            # Wir können die Handlungschritte überschreiben
            if posArray < len(assocArr):
                zuRezept.handlungsschritte[posArray].hatid.text = txtarr[posArray]
                #print(f"Ändere {txtarr[posArray]}")
            else:
                # Wir müssen neue Associations machen
                handNew = handlungsschritt(text=txtarr[posArray])
                assocNew = AssociationRHhat(position=posArray)
                handlung = handNew
                assocNew.hatid = handlung
                with db.session.no_autoflush:
                    zuRezept.handlungsschritte.append(assocNew)
                db.session.commit()
                #print("Neue Assoc")
            posArray += 1
        #print(assocArr[posArray:])
        for entry in assocArr[posArray:]:
            print(f"lösche {entry.aid}")
            # Handlungsschritt löschen
            rezeptausAssoc = entry.hatid
            db.session.delete(rezeptausAssoc)
            # Association löschen
            try:
                zuRezept.handlungsschritte.remove(entry)
            except ValueError:
                pass
            db.session.commit()

        # Tag speichern
        zuRezept.tags = []
        for tagentry in form.tags.data:
            tmpTag = tags.query.get(tagentry)
            zuRezept.tags.append(tmpTag)

        # Speichern des Eintrages
        db.session.commit()
        flash(f"{zuRezept.name} wurde gespeichert!")
        return redirect(url_for('modifyrezept', ids=ids))

    # Anzeigen der Handlungschritte
    handlarray = []
    for entry in zuRezept.handlungsschritte:
        handlarray.append(entry.hatid.text)
    form.handlung.data = '\n'.join(handlarray)

    form.rezeptname.data = zuRezept.name
    # Tags
    tagarry = []
    tagarry.append(["-1", "Keine Angabe"])
    tmp = createArrayHelper(tags.query.all())
    for entry in tmp:
        tagarry.append(entry)
    form.tags.choices = tagarry
    if zuRezept.tags is not None:
        try:
            form.tags.data = [zuRezept.tags[0].id, zuRezept.tags[0].name]
        except IndexError:
            print("Indexerror bei modifyrezept")

    return render_template('admin_rezept.html', form=form, titlet="Rezepts ändern", rid=ids, rezept=zuRezept)

@app.route("/rezept/zutatenedit/<path:rid>", methods=['GET', 'POST'])
def rezeptver2(rid):
    rezept1 = rezept.query.get(rid)
    if rezept1 is None:
        page = int(request.args.get('page', 1))
        return redirect(url_for('showZutaten', page=page))
    form = forms.rezeptzutatadder()
    # Zutaten auswählbar machen
    form.zutat.choices = createArrayHelper2(zutat.query.all())
    if form.validate_on_submit and request.method == "POST":
        # Wir speichern  das Formular
        assoc1 = Association(menge=int(form.menge.data), optional=False)
        zutat1 = zutat.query.get(int(form.zutat.data))
        assoc1.hatzutat = zutat1
        try:
            with db.session.no_autoflush:
                rezept1.zutaten.append(assoc1)
            db.session.commit()
            flash("Gespeichert!")
            return redirect(url_for('rezeptver2', rid=rid))
        except sqlalchemy.exc.IntegrityError:
            db.session.rollback()
            flash("Fehler: Zutat wurde bereits verknüpft!")

    return render_template('admin_addrzver.html', form=form, rezept1=rezept1)

@app.route('/rezept/delete/<path:ids>')
def deleteRezept(ids):
    """Rezept Objekt entfernen"""
    page = request.args.get('page', 0, type=int)
    repdel = rezept.query.get(ids)
    if repdel is None:
        page = int(request.args.get('page', 1))
        return redirect(url_for('showRezepte', page=page))

    # Handlungsschritte & Verknüpfung löschen
    for entry in repdel.handlungsschritte:
        handdel = handlungsschritt.query.get(entry.hid)
        db.session.delete(handdel)
        db.session.delete(entry)

    # Tags vom Rezept löschen
    repdel.tags = []
    db.session.commit()

    # Rezept löschen
    db.session.delete(repdel)

    db.session.commit()
    return redirect(url_for('showRezepte', page=page))
