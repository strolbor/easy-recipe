from app import app, db, forms
from app.rezept import rezept, zutat,handlungsschritt
from werkzeug.utils import secure_filename
import os
from flask import redirect, render_template,request
from flask.helpers import flash, url_for
from sqlalchemy import desc

from app.backend_helper import createFolderIfNotExists, getNewID


@app.route('/admin/')
def admin():
    """Dies ist der Admin Hauptindex"""
    return render_template('admin_index.html')


@app.route('/admin/add/rezept/',methods=['GET','POST'])
def addrezept():
    """Seite um ein neues Rezept anzulegen."""
    form = forms.rezeptanlegen()
    if form.validate_on_submit():
        # Daten des Uploads holen
        bild_url=""
        if request.method == 'POST':
            """ Die Post Methode wird aufgerufen, wenn wir ein Bild hochladen möchten und verarbeiten wollen."""
            idneu = getNewID(rezept)
            """ Wir suchen die nächste ID"""

            picure_url = savepic('bildupload', request.files, f'rezept{idneu}')
            if not (picure_url == "A" or picure_url == "B"):
                """ Bild wurde gefunden und hochgeladen"""
                bild_url = picure_url
        new = rezept(name=form.rezeptname.data,bild=bild_url,tags=form.tags.data)
        """ Neues Rezept wurde erstellt."""
        db.session.add(new)
        db.session.commit()
        flash(form.rezeptname.data + " wurde erfolgreich angelegt!")
    return render_template('admin_newrezept.html',form=form)

@app.route('/admin/add/Zutat/',methods=['GET','POST'])
def addzutat():
    """Hiermit wird eine neue Zutat angelegt.
    """
    form = forms.zutatanlegen()
    if form.validate_on_submit():
        # Daten des Uploads holen
        bild_url=""
        if request.method == 'POST':
            idneu = getNewID(zutat)
            picure_url = savepic('bildupload', request.files, f'zutat{idneu}')
            if not (picure_url == "A" or picure_url == "B"):
                """Bild wurde gefunden und benutzt.
                Bei den Statusrückgaben von A oder B wird kein Bild hochgeladen."""
                bild_url = picure_url
        newzutat = zutat(name=form.name.data,einheit=form.einheit.data,bild=bild_url)
        db.session.add(newzutat)
        db.session.commit()
        flash(f'{form.name.data} wurde erfolgreich angelegt!')
    return render_template('admin_newzutat.html',form=form)

def savepic(feldname, rfiles ,ordner) -> str:
    if feldname not in rfiles:
        """ Bild wurde garnicht erst hochgeladen"""
        return "A"
    file = rfiles[feldname]
    if file.filename == '':
        """ Es wurde kein Bild genommen."""
        return "B"
    if file:
        """ Bild ist vorhanden"""
        file = request.files[feldname]
        filename = secure_filename(file.filename)
        createFolderIfNotExists(os.path.join(app.instance_path,ordner))
        path = os.path.join(app.instance_path,ordner,filename)
        bild_url=filename
        file.save(path)
        print("Bild gespeichert")
        return bild_url


@app.route('/admin/add/handlungsschritt/',methods=['GET','POST'])
def addhandlung():
    """Dies ist der Admin Hauptindex"""
    form = forms.handlungschrittanlegen()
    if form.validate_on_submit():
        if request.method == 'POST':
            bild_url = ""
            bild_url2 = ""
            idneu = getNewID(handlungsschritt)
            picure_url = savepic('bildupload1', request.files, f'hand{idneu}')
            print(picure_url)
            if not (picure_url == "A" or picure_url == "B"):
                """Bild wurde gefunden und benutzt.
                Bei den Statusrückgaben von A oder B wird kein Bild hochgeladen."""
                bild_url = picure_url
            # Zweites Handlungsbild
            picure_url = savepic('bildupload2', request.files, f'hand{idneu}')
            if not (picure_url == "A" or picure_url == "B"):
                """Bild wurde gefunden und benutzt.
                Bei den Statusrückgaben von A oder B wird kein Bild hochgeladen."""
                bild_url2 = picure_url
            newhand = handlungsschritt(bild=bild_url,bild2=bild_url2,text=form.beschreibung.data)
            print(newhand)
            db.session.add(newhand)
            db.session.commit()
            flash(f'Handlungsschritt wurde erfolgreich angelegt!')
    return render_template('admin_newhand.html',form=form)

@app.route('/admin/modify/RZ',methods=['GET','POST'])
def CHGverknupfung():
    """Wir wählen zuerst eine Rezept aus um es dann zu bearbeiten"""
    form = forms.rzanlegen()
    if form.validate_on_submit():
        flash('Test')
        return redirect(url_for('CHGver2',ids=form.rezeptpicker.data))
    return render_template('admin_rzpicker.html',form=form)

@app.route('/admin/modify/RZzutat/<path:ids>',methods=['GET','POST'])
def CHGver2(ids):
    """Wir wählen, die Zutaten aus, die wir zum rezept speichern wollen."""
    form = forms.rzzutaten()
    auswahl = rezept.query.get(ids)
    print("Rezept Zutaten:",auswahl.zutaten[0].id)

    zumarkieren =[]
    for entry in auswahl.zutaten:
        zumarkieren.append([entry.id,entry.name])


    if form.validate_on_submit() or form.submit.data:
        """ Hier funktioniert validate on submit nicht"""
        ausgewählte = form.zutaten.data
        """Alle Zutaten, die man ausgewählt holen"""
        for entry in ausgewählte:
            zutate = zutat.query.get(entry)
            """ Zutat zum Adden hinzufügen als Objekt holen"""
            auswahl.zutaten.append(zutate)
        db.session.commit()
        flash("Gespeichert!")
        return redirect(url_for('CHGver2',ids=ids))
    return render_template('admin_rzpickerzutat.html',form=form,rezeptnamen=auswahl.name,inhalt=auswahl.zutaten)








@app.route('/admin/show/rezepte/')
def showRezepte():
    liste = rezept.query.all()
    return render_template('admin_show.html',inhalt=liste)


@app.route('/admin/show/zutat/')
def showZutaten():
    liste = zutat.query.all()
    return render_template('admin_show.html',inhalt=liste)



