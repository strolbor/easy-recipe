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


@app.route('/admin/show/rezepte/')
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


@app.route("/nutzer/rezept/eingabe", methods=["POST", "GET"])
def nutzerrezeptein():
    """Nutzereingabe Menü"""
    form = forms.nutzerein()
    # Das ist schon so fertig
    if request.method == 'POST' and form.submit.data:
        # Reload der Seite mit dem Flash, der zeigt, dass es gespeichert wruden ist.
        return redirect(url_for('nutzerrezeptein'))
    return render_template('nutzer_rezeptanlege.html', form=form, zutaten=zutat.query.all(), tags=tags.query.all())


@app.route("/ctl/nutzer/rezept/post", methods=["POST", "GET"])
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
        handlung = handlungsschritt(
            bild="", bild2="", text=handlungsschritttext)
        db.session.add(handlung)
        
        # Handlungsschritt verknüpfen
        nhand = handlungsschritt.query.filter_by(
            text=handlungsschritttext).first()
        assoc1 = AssociationRHhat(position=1)
        assoc1.hatid = nhand
        with db.session.no_autoflush:
            rnew.handlungsschritte.append(assoc1)
        
        db.session.commit()

        # speichern
        flash(f"{rnew.name} ({rnew.id}) wurde gespeichert!")
    return "ok"


@app.route('/admin/modify/rezept/<path:ids>', methods=['GET', 'POST'])
def modifyrezept(ids):
    form = forms.rezeptaendern()
    zuRezept: rezept = rezept.query.get(ids)
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
        zuRezept.handlungsschritte[0].hatid.text = form.handlung.data


        # Tag speichern
        zuRezept.tags = []
        for tagentry in form.tags.data:
            tmpTag = tags.query.get(tagentry)
            zuRezept.tags.append(tmpTag)

        # Speichern des Eintrages
        db.session.commit()
        flash(f"{zuRezept.name} wurde gespeichert!")
        return redirect(url_for('modifyrezept', ids=ids))

    form.handlung.data = zuRezept.handlungsschritte[0].hatid.text

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


@app.route("/admin/rezept/rezeptver1")
def rezeptver1():
    """Funktion um Einträge zu entfernen. Generische Funktion.
    mode: Was soll gelöscht werden
    classes: typ der Klasse zum abfragen
    redirect_url: Selbstverweis auf aufrufende Funktion der URL"""
    page = request.args.get('page', 0, type=int)
    liste = rezept.query.paginate(page, app.config['ITEMS_PER_PAGE'], False)
    rid = request.args.get('rid', 0, type=int)
    next_url = url_for('rezeptver1', page=liste.next_num,
                       rid=rid) if liste.has_next else None
    prev_url = url_for('rezeptver1', page=liste.prev_num,
                       rid=rid) if liste.has_prev else None

    return (render_template('admin_remove.html', inhalt=liste.items, titlet="Zutaten ändern", next_url=next_url, prev_url=prev_url, page=page))

@app.route("/admin/rezept/rezeptver2/<path:rid>", methods=['GET', 'POST'])
def rezeptver2(rid):
    rezept1 = rezept.query.get(rid)
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


@app.route('/adminctl/delete/rezept/<path:ids>')
def deleteRezept(ids):
    """Rezept Objekt entfernen"""
    page = request.args.get('page', 0, type=int)
    repdel = rezept.query.get(ids)

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
