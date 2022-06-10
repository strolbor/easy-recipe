from app import app, db, forms
from app.rezept import rezept, zutat
from werkzeug.utils import secure_filename
import os
from flask import redirect, render_template,request
from flask.helpers import flash, url_for

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
            a = savepic('bildupload', request.files)
            if a == "A":
                return  redirect(url_for('addrezept'))
            elif a == "B":
                return redirect(request.url)
            else:
                bild_url = a
        new = rezept(name=form.rezeptname.data,bild=bild_url,tags=form.tags.data)
        print(new)
        db.session.add(new)
        db.session.commit()
        flash(form.rezeptname.data + " wurde erfolgreich angelegt!")
    return render_template('admin_newrezept.html',form=form)

@app.route('/admin/add/Zutat/',methods=['GET','POST'])
def addzutat():
    """Dies ist der Admin Hauptindex"""
    form = forms.zutatanlegen()
    if form.validate_on_submit():
        # Daten des Uploads holen
        bild_url=""
        if request.method == 'POST':
            a = savepic('bildupload', request.files)
            if a == "A":
                return  redirect(url_for('addzutat'))
            elif a == "B":
                return redirect(request.url)
            else:
                bild_url = a
        print(bild_url)
        newzutat = zutat(name=form.name.data,einheit=form.einheit.data,bild=bild_url)
        db.session.add(newzutat)
        db.session.commit()
        flash(f'{form.name.data} wurde erfolgreich angelegt!')
    return render_template('admin_newzutat.html',form=form)

def savepic(feldname, rfiles ) -> str:
    if feldname not in rfiles:
        flash("Kein Bild gefunden!")
        return "A"
    file = rfiles[feldname]
    if file.filename == '':
        flash('Kein Bild wurde ausgewählt.')
        return "B"
    if file:
        file = request.files[feldname]
        filename = secure_filename(file.filename)
        path = os.path.join(
            app.instance_path,'fotos',filename
        )
        print(path,filename)
        bild_url=filename
        file.save(path)
        return bild_url


@app.route('/admin/add/handlungsschritt/',methods=['GET','POST'])
def addhandlung():
    """Dies ist der Admin Hauptindex"""
    form = forms.handlungschrittanlegen()
    if form.validate_on_submit():
        if request.method == 'POST':
            # Erstes Handlungsbild
            a = savepic('bildupload', request.files)
            if a == "A":
                return  redirect(url_for('addrezept'))
            elif a == "B":
                return redirect(request.url)
            else:
                bild_url = a
            # Zweites Handlungsbild
            a = savepic('bildupload2', request.files)
            if a == "A":
                return  redirect(url_for('addrezept'))
            elif a == "B":
                return redirect(request.url)
            else:
                bild_url = a
    return render_template('admin_newhand.html',form=form)

@app.route('/admin/modify/RZ')
def CHGverknupfung():
    """Dies ist der Admin Hauptindex"""
    form = forms.rzanlegen()
    return render_template('admin_rzpicker.html',form=form)







@app.route('/admin/show/rezepte/')
def showRezepte():
    liste = rezept.query.all()
    return render_template('admin_show.html',inhalt=liste)


@app.route('/admin/show/zutat/')
def showZutaten():
    liste = zutat.query.all()
    return render_template('admin_show.html',inhalt=liste)

""" Löschen """
@app.route('/admin/remove/rezept')
def removeRezept():
    liste = rezept.query.all()
    return render_template('admin_remove.html',inhalt=liste,title="Rezept Entferner",targetrezept=True)

@app.route('/admin/remove/zutat')
def removeZutat():
    liste = zutat.query.all()
    return render_template('admin_remove.html',inhalt=liste,title="Zutaten Entferner",targetzutat=True)

"""Controll Section"""
@app.route('/admin/delete/zutat/<path:ids>')
def deleteZutat(ids):
    db.session.delete(zutat.query.get(ids))
    db.session.commit()
    return redirect(url_for('removeZutat'))
    

@app.route('/admin/delete/rezept/<path:ids>')
def deleteRezept(ids):
    db.session.delete(rezept.query.get(ids))
    db.session.commit()
    return redirect(url_for('removeRezept'))

