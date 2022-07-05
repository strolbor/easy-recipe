from app import app, db, forms
from app.rezept import rezept, zutat,handlungsschritt,tags,Association,AssociationRHhat
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





MODE_ZUTATEN = 0
MODE_TAGS = 1
MODE_REZEPT = 2
MODE_HAND = 3
MODE_RZHAT = 4
MODE_HANDCHG = 5

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
        return render_template('admin_remove.html',inhalt=liste.items,titlet="Verknüpfung Entferner von Rezept <-> Zutat",targerzhat=True,next_url=next_url,prev_url=prev_url,page=page,showCase=True)
    if mode == MODE_HAND:
        return render_template('admin_remove.html',inhalt=liste.items,titlet="Verknüpfung Entferner von Handlungsschritten",handlung=True,next_url=next_url,prev_url=prev_url,page=page,showCase=True)
    if mode == MODE_HANDCHG:
        return render_template('admin_remove.html',inhalt=liste.items,titlet="Verknüpfung Entferner von Handlungsschritten",handlung=True,next_url=next_url,prev_url=prev_url,page=page,showCase=True)







##############
#    rzhat   #
##############


@app.route('/admin/modify/rzhat',methods=['GET','POST'])
def CHGrzhat():
    return entfernerAnzeiger(rezept,"CHGrzhat2","Verknüpfung anlegen")

@app.route('/admin/modify/rzhat-picker/<path:ids>',methods=['GET','POST'])
def CHGrzhat2(ids):
    return entfernerfuction(ids,zutat,rezept,MODE_ZUTATEN,'CHGrzhat2')


##
@app.route('/admin/modify/rhhat',methods=['GET','POST'])
def CHGrhhat():
    return entfernerAnzeiger(rezept,"CHGrhhat2","Verknüpfung zwischen Rezept und Handlungsschritt anlegen")

@app.route('/admin/modify/rhhat-picker/<path:ids>',methods=['GET','POST'])
def CHGrhhat2(ids):
    return entfernerfuction(ids,handlungsschritt,rezept,MODE_HAND,'CHGrhhat2')

##


@app.route('/admin/remove/rzhat/picker/',methods=['GET','POST'])
def removeRZhat():
    return remover(MODE_RZHAT,rezept,'removeRZhat')    

@app.route('/admin/remove/rzhat/remover/<path:rid>',methods=['GET','POST'])
def removeRZhat2(rid):
    ausrezept = rezept.query.get(rid)
    zutatenliste = ausrezept.zutaten
    for assoc in zutatenliste:
        print(assoc.hatzutat.id)
    return render_template('admin_remove.html',inhalt=zutatenliste,titlet="Verknüpfungs Entferner",rid=rid,targerzhat2=True)


##############
#   generic  #
##############


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
    # Alle Zutaten, die schon verknüpft sind, müssen gelöscht werden
    if classes == handlungsschritt:
        # Handlungsschritt hat keinen .name Attribut
        form.zutaten.choices = createArrayHelper(classes.query.all())
    else:
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
                # auswahl = Klasse von rezept
                # gettingclass = Klasse von Zutat
                a = Association(menge=25,optional=True)
                a.hatzutat = gettingclass
                with db.session.no_autoflush:
                    auswahl.zutaten.append(a)
            if mode == MODE_TAGS:
                """ Zielobjekt ist Klasse Tags """
                auswahl.tags.append(gettingclass)
            if mode == MODE_HAND:
                """Wir fügen Handlungsschritte mit Positionen zu."""
                a = AssociationRHhat(position=1)
                a.hatid = gettingclass
                with db.session.no_autoflush:
                    auswahl.handlungsschritte.append(a)
            db.session.commit()
        flash("Gespeichert!")
        return redirect(url_for(redirect_url,ids=ids))
    if mode == MODE_ZUTATEN:
        return render_template('admin_rzpickerzutat.html',form=form,modus="Zutaten",rezeptnamen=auswahl.name,inhalt=auswahl.zutaten)
    if mode == MODE_TAGS:
        return render_template('admin_rzpickerzutat.html',form=form,modus="Tags",rezeptnamen=auswahl.name,inhalt=auswahl.tags)
    if mode == MODE_HAND:
        return render_template('admin_rzpickerzutat.html',form=form,modus="Handlungsschritte",rezeptnamen=auswahl.name,inhalt=auswahl.handlungsschritte)
    else:
        return "Error! <br />Kein Template gefunden!"





