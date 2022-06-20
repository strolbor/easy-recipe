from app import app, db, forms
from app.rezept import rezept, zutat,handlungsschritt,tags
from app.backend_helper import createFolderIfNotExists, getNewID,createArrayHelper, savepic


import os
from flask import redirect, render_template,request, abort
from flask.helpers import flash, url_for
from sqlalchemy import desc


##############
# Startseite #
##############

@app.route('/admin/')
def admin():
    """Dies ist der Admin Hauptindex"""
    return render_template('admin_index.html')


##############
#   Rezept   #
##############

@app.route('/admin/add/rezept/',methods=['GET','POST'])
def addrezept():
    """Seite um ein neues Rezept anzulegen."""
    form = forms.rezeptanlegen()
    form.tags.choices = createArrayHelper(tags.query.all())
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
                # TODO: Absprache mmit Tom, wie wir das Bild abrufen.
        new = rezept(name=form.rezeptname.data,bild=bild_url)
        new.tags.append(tags.query.get(form.tags.data))
        """ Neues Rezept wurde erstellt."""
        db.session.add(new)
        db.session.commit()
        flash(form.rezeptname.data + " wurde erfolgreich angelegt!")
    return render_template('admin_rezept.html',form=form,titlet="Neues Rezept anlegen")

@app.route('/admin/modify/rezept/<path:ids>',methods=['GET','POST'])
def modifyrezept(ids):
    form = forms.rezeptanlegen()
    zuRezept = rezept.query.get(ids)
    if form.validate_on_submit():
        pass
    form.rezeptname.data = zuRezept.name
    print(zuRezept.tags,tags.query.all())
    #form.tags.data = createArrayHelper(zuRezept.tags)
    form.tags.choices = createArrayHelper(tags.query.all())
    if zuRezept.bild != "":
         # Diese Aufruf wird gemacht, wenn ein Bild vorhanden ist
        return render_template('admin_rezept.html',form=form,titlet="Rezepts ändern",showbilds=True,showbild=zuRezept.bild) 
    else:
        # Diese Aufruf wird gemacht, wenn kein Bild vorhanden ist
        return render_template('admin_rezept.html',form=form,titlet="Rezepts ändern") 


@app.route('/admin/show/rezepte/')
def showRezepte():
    liste = rezept.query.order_by(rezept.name).all()
    return render_template('admin_show.html',inhalt=liste,titlet="Rezepte")

@app.route('/admin/remove/rezept')
def removeRezept():
    """ Löschen eines Rezeptes"""
    return remover(MODE_REZEPT,rezept,'removeRezept')


MODE_ZUTATEN = 0
MODE_TAGS = 1
MODE_REZEPT = 2
MODE_HAND = 3
MODE_RZHAT = 4

def remover(mode : int,classes, redirect_url: str):
    page = request.args.get('page', 0, type=int)
    liste = classes.query.paginate(page,app.config['ITEMS_PER_PAGE'], False)
    next_url = url_for(redirect_url, page=liste.next_num)  if liste.has_next else None
    prev_url = url_for(redirect_url, page=liste.prev_num)  if liste.has_prev else None
    if mode == MODE_ZUTATEN:
        return render_template('admin_remove.html',inhalt=liste.items,titlet="Zutat Entferner",targetzutat=True,next_url=next_url,prev_url=prev_url,page=page,showCase=True)
    if mode == MODE_REZEPT:
        return render_template('admin_remove.html',inhalt=liste.items,titlet="Rezept Entferner",targetrezept=True,next_url=next_url,prev_url=prev_url,page=page,showCase=True)
    if mode == MODE_TAGS:
        return render_template('admin_remove.html',inhalt=liste.items,titlet="Tags Entferner",targettags=True,next_url=next_url,prev_url=prev_url,page=page,showCase=True)
    if mode == MODE_RZHAT:
        return render_template('admin_remove.html',inhalt=liste.items,titlet="Verknüpfung Entferner",targerzhat=True,next_url=next_url,prev_url=prev_url,page=page,showCase=True)
    if mode == MODE_HAND:
        return render_template('admin_remove.html',inhalt=liste.items,titlet="Verknüpfung Entferner",handlung=True,next_url=next_url,prev_url=prev_url,page=page,showCase=True)


##############
#    Zutat   #
##############
@app.route('/admin/add/Zutat/',methods=['GET','POST'])
def addzutat():
    """Hiermit wird eine neue Zutat angelegt."""
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
    return render_template('admin_zutat.html',form=form)

@app.route('/admin/show/zutat/')
def showZutaten():
    liste = zutat.query.order_by(zutat.name).all()
    return render_template('admin_show.html',inhalt=liste,titlet="Zutaten")

@app.route('/admin/remove/zutat')
def removeZutat():
    """Hiermit wird eine Zutat entfernt"""
    return remover(MODE_ZUTATEN,zutat,'removeZutat')

@app.route('/admin/modify/zutat/<path:ids>',methods=['GET','POST'])
def modifyZutat(ids):
    """Hiermit wird eine Zutat modifiziert."""
    form = forms.zutatanlegen()
    modifyZutat = zutat.query.get(ids)

    if form.validate_on_submit():
        modifyZutat.name = form.name.data
        modifyZutat.einheit = form.einheit.data
        if request.method == 'POST': 
            picure_url = savepic('bildupload', request.files, f'zutat{modifyZutat.id}')
            if not (picure_url == "A" or picure_url == "B"):
                """Bild wurde gefunden und benutzt.
                Bei den Statusrückgaben von A oder B wird kein Bild hochgeladen."""
                modifyZutat.bild = picure_url
                print("Bild neu gesetzt")
        db.session.commit()
        flash("Gespeichert")
        return redirect(url_for('modifyZutat',ids=ids))

    form.name.data = modifyZutat.name
    form.einheit.data = modifyZutat.einheit
    print("Bild",modifyZutat.bild)
    if modifyZutat.bild == "None":
        return render_template('admin_zutat.html',form=form,titlet="Zutat Eigenschaften ändern")
    else:
        return render_template('admin_zutat.html',form=form,titlet="Zutat Eigenschaften ändern",showbild=modifyZutat.bild,showbilds=True)
       



##############
#  Handlung  #
##############

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
    return render_template('admin_hand.html',form=form,titlet="Neuen Handlungsschritt anlegen")

@app.route('/admin/modify/handlungsschritt/<path:ids>',methods=['GET','POST'])
def modifyHandlung(ids):
    """Hiermit wird eine Zutat modifiziert."""
    form = forms.handlungschrittanlegen()
    modifyHand = handlungsschritt.query.get(ids)

    if form.validate_on_submit():
        modifyHand.text = form.beschreibung.data
        if request.method == 'POST': 
            picure_url = savepic('bildupload1', request.files, f'hand{ids}')
            if not (picure_url == "A" or picure_url == "B"):
                """Bild wurde gefunden und benutzt.
                Bei den Statusrückgaben von A oder B wird kein Bild hochgeladen."""
                modifyHand.bild = picure_url
                print("Bild neu gesetzt")
            picure_url = savepic('bildupload2', request.files, f'hand{ids}')
            if not (picure_url == "A" or picure_url == "B"):
                """Bild wurde gefunden und benutzt.
                Bei den Statusrückgaben von A oder B wird kein Bild hochgeladen."""
                modifyHand.bild2 = picure_url
                print("Bild neu gesetzt")

        db.session.commit()
        flash(f"{modifyHand.text} wurde gespeichert")
        return redirect(url_for('modifyHandlung',ids=ids))
    array_pic =[]
    print(modifyHand.bild,modifyHand.bild2,modifyHand.id)
    if modifyHand.bild != "":
        array_pic.append(modifyHand.bild)
    if modifyHand.bild2 != "":
        array_pic.append(modifyHand.bild2)
    print(array_pic)
    form.beschreibung.data = modifyHand.text
    if len(array_pic) == 0:
        return render_template('admin_hand.html',form=form,id=modifyHand.id,titlet="Handlungsschritt ändern")
    else:
        return render_template('admin_hand.html',form=form,id=modifyHand.id,array_pic=array_pic,showbilds=True,titlet="Handlungsschritt ändern")

@app.route('/admin/remove/removehandlungsschritt')
def removehandlungsschritt():
    """Hiermit wird ein Handlungsschritt entfernt"""
    return remover(MODE_HAND,handlungsschritt,"Handlungsschritt Entferner")


@app.route('/admin/show/handlungsschritt/')
def showhandlungsschritt():
    liste = handlungsschritt.query.all()
    return render_template('admin_show.html',inhalt=liste,titlet="Handlungsschritte")

##############
#    rzhat   #
##############


@app.route('/admin/modify/rzhat',methods=['GET','POST'])
def CHGrzhat():
    return entfernerAnzeiger(rezept,"CHGrzhat2","Verknüpfung anlegen")

@app.route('/admin/modify/rzhat-picker/<path:ids>',methods=['GET','POST'])
def CHGrzhat2(ids):
    return entfernerfuction(ids,zutat,rezept,MODE_ZUTATEN,'CHGrzhat2')

@app.route('/admin/remove/rzhat/picker/',methods=['GET','POST'])
def removeRZhat():
    return remover(MODE_RZHAT,rezept,'removeRZhat')    

@app.route('/admin/remove/rzhat/remover/<path:rid>',methods=['GET','POST'])
def removeRZhat2(rid):
    ausrezept = rezept.query.get(rid)
    zutatenliste = ausrezept.zutaten
    return render_template('admin_remove.html',inhalt=zutatenliste,titlet="Verknüpfungs Entferner",rid=rid,targerzhat2=True)






def entfernerAnzeiger(classes,redirect_url : str,title):
    """Wir wählen zuerst eine Rezept aus um es dann zu bearbeiten"""
    form = forms.rzanlegen()
    form.rezeptpicker.choices = createArrayHelper(classes.query.order_by(classes.name).all())
    if form.validate_on_submit():
        return redirect(url_for(redirect_url,ids=form.rezeptpicker.data))
    return render_template('admin_rzpicker.html',form=form,titlet=title)

def entfernerfuction(ids,classes,ursprung_class,mode,redirect_url):
    """Wir wählen, die Zutaten aus, die wir zum rezept speichern wollen."""
    form = forms.verknupfungsanleger()
    
    form.zutaten.choices = createArrayHelper(classes.query.order_by(classes.name).all())
    auswahl = ursprung_class.query.get(ids)
    if auswahl is None:
        abort(404) 

    if form.validate_on_submit() or form.submit.data:
        """ Hier funktioniert validate on submit nicht"""
        
        ausgewählte = form.zutaten.data
        """Alle Zutaten, die man ausgewählt holen"""
        for entry in ausgewählte:
            gettingclass = classes.query.get(entry)
            """ Zielobjekt aus der entsprechen Klasse zum Adden hinzufügen holen"""
            if mode == MODE_ZUTATEN:
                """ Zielobjekt ist Zutat"""
                auswahl.zutaten.append(gettingclass)
            if mode == MODE_TAGS:
                """ Zielobjekt ist Klasse Tags """
                auswahl.tags.append(gettingclass)
        db.session.commit()
        flash("Gespeichert!")
        return redirect(url_for(redirect_url,ids=ids))
    if mode == MODE_ZUTATEN:
        return render_template('admin_rzpickerzutat.html',form=form,modus="Zutaten",rezeptnamen=auswahl.name,inhalt=auswahl.zutaten)
    if mode == MODE_TAGS:
        return render_template('admin_rzpickerzutat.html',form=form,modus="Tags",rezeptnamen=auswahl.name,inhalt=auswahl.tags)
    else:
        return "Error!"




##############
#    tags   #
##############

@app.route('/admin/show/tags/')
def showTags():
    liste = tags.query.order_by(tags.name).all()
    return render_template('admin_show.html',inhalt=liste,titlet="Tags")

@app.route("/admin/add/tag",methods=['GET','POST'])
def addTags():
    form = forms.taganlegen()
    if form.validate_on_submit():
        newtag = tags(name=form.name.data)
        db.session.add(newtag)
        db.session.commit()
        flash(f'Tag <{form.name.data}> wurde erfolgreich angelegt.')
        return redirect(url_for('addTags'))

    return render_template('admin_tag.html',form=form)

@app.route("/admin/modify/tag/<path:ids>",methods=['GET','POST'])
def modifyTags(ids):
    form = forms.taganlegen()
    zuTag = tags.query.get(ids)
    if form.validate_on_submit():
        zuTag.name = form.name.data
        db.session.commit()
        flash(f"{zuTag.name} wurde gespeichert!")
        return redirect(url_for('modifyTags',ids=ids))
    form.name.data = zuTag.name
    return render_template('admin_tag.html',form=form,titlet="Tag ändern")


@app.route('/admin/modify/rthat',methods=['GET','POST'])
def CHGrthat():
    return entfernerAnzeiger(rezept,"CHGrthat2","Verknüpfung anlegen")

@app.route('/admin/modify/rthat-picker/<path:ids>',methods=['GET','POST'])
def CHGrthat2(ids):
    return entfernerfuction(ids,tags,rezept,MODE_TAGS,'CHGrthat')

@app.route('/admin/remove/tags')
def removeTags():
    return remover(MODE_TAGS,tags,'removeTags')
