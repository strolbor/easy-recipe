from app import app, db, forms
from app.rezept import rezept, zutat,handlungsschritt,tags,Association,AssociationRHhat
from app.backend_helper import createFolderIfNotExists, getNewID,createArrayHelper, savepic


import os
from flask import redirect, render_template,request, abort
from flask.helpers import flash, url_for
from sqlalchemy import desc

##############
#   Rezept   #
##############

@app.route('/admin/add/rezept/',methods=['GET','POST'])
def addrezept():
    """Seite um ein neues Rezept anzulegen."""
    form = forms.rezeptanlegen()
    # Alle Tags holen
    form.tags.choices = createArrayHelper(tags.query.all())

    #Formular wird abgesendet
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

        new = rezept(name=form.rezeptname.data,bild=bild_url)
        #new.tags.append(tags.query.get(form.tags.data))
        """ Neues Rezept wurde erstellt."""
        db.session.add(new)
        db.session.commit()
        flash(form.rezeptname.data + " wurde erfolgreich angelegt!")
    return render_template('admin_rezept.html',form=form,titlet="Neues Rezept anlegen")

@app.route('/admin/modify/rezept/<path:ids>',methods=['GET','POST'])
def modifyrezept(ids):
    form = forms.rezeptanlegen()
    form.tags.choices = createArrayHelper(tags.query.all())
    zuRezept = rezept.query.get(ids)

    if form.validate_on_submit():
        # Name speichern
        zuRezept.name = form.rezeptname.data
        if request.method == 'POST':
            # Bild aktualisieren
            picure_url = savepic('bildupload', request.files, f'rezept{ids}')
            if not (picure_url == "A" or picure_url == "B"):
                zuRezept.bild = picure_url
        # Speichern des Eintrages
        db.session.commit()
        flash(f"{zuRezept.name} wurde gespeichert!")
        return redirect(url_for('modifyrezept',ids=ids))

    form.rezeptname.data = zuRezept.name
    form.tags.data = createArrayHelper(zuRezept.tags)
    
    if zuRezept.bild is not None:
         # Diese Aufruf wird gemacht, wenn ein Bild vorhanden ist
        return render_template('admin_rezept.html',form=form,titlet="Rezepts ändern",showbilds=True,showbild=zuRezept.bild) 
    else:
        # Diese Aufruf wird gemacht, wenn kein Bild vorhanden ist
        return render_template('admin_rezept.html',form=form,titlet="Rezepts ändern") 


@app.route('/admin/show/rezepte/')
def showRezepte():
    page = request.args.get('page', 0, type=int)
    liste = rezept.query.paginate(page,app.config['ITEMS_PER_PAGE'], False)
    next_url = url_for('showRezepte', page=liste.next_num)  if liste.has_next else None
    prev_url = url_for('showRezepte', page=liste.prev_num)  if liste.has_prev else None
    return render_template('admin_show.html',liste=liste.items,titlet="Rezepte",next_url=next_url,prev_url=prev_url,showCase=True,page=page)

@app.route('/admin/remove/rezept')
def removeRezept():
    """ Löschen eines Rezeptes"""
    return remover(MODE_REZEPT,rezept,'removeRezept')