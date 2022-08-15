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

# Anzeiger
def showclass(classes, sortedby,title,redirect_url):
    """Paginate a section"""
    page = request.args.get('page', 0, type=int)
    liste = classes.query.order_by(sortedby).paginate(page,app.config['ITEMS_PER_PAGE'], False)
    next_url = url_for(redirect_url, page=liste.next_num)  if liste.has_next else None
    prev_url = url_for(redirect_url, page=liste.prev_num)  if liste.has_prev else None
    return render_template('admin_show.html',liste=liste.items,titlet=title,next_url=next_url, prev_url=prev_url,showCase=True,page=page)




MODE_ZUTATEN = 0
"""Diese Einstellung ist da um Zutaten zu entfernen"""
MODE_TAGS = 1
"""Diese Einstellung ist da um Tags zu entfernen"""
MODE_REZEPT = 2 # Rezepte entfernen
"""Diese Einstellung ist da um Rezepte zu entfernen"""
MODE_HAND = 3
"""Diese Einstellung ist da um Handlungsschritte zu entfernen"""
MODE_RZHAT = 4
"""Diese Einstellung ist da um Verknüpfungen zw.  Zutat <-> Rezept zu entfernen"""
MODE_TAGver = 5
"""Diese Einstellung ist da um Verknüpfungen zw.  Tags <-> Rezept zu entfernen"""
MODE_HANDver = 6
"""Diese Einstellung ist da um Verknüpfungen zw.  Handlungschritten <-> Rezept zu entfernen"""
MODE_HANDadd = 7
"""Diese Einstellung ist da um Verknüpfungen zw.  Handlungschritten <-> Rezept hinzuzufügen"""
MODE_REZEPTadd = 8
"""Diese Einstellung ist da um Verknüpfungen zw.  Zutat <-> Rezept hinzuzufügen"""


def remover(mode : int,classes, redirect_url: str):
    page = request.args.get('page', 0, type=int)
    liste = classes.query.paginate(page,app.config['ITEMS_PER_PAGE'], False)
    next_url = url_for(redirect_url, page=liste.next_num)  if liste.has_next else None
    prev_url = url_for(redirect_url, page=liste.prev_num)  if liste.has_prev else None
    if mode == MODE_ZUTATEN:
        return render_template('admin_remove.html',inhalt=liste.items,titlet="endgültiger Zutatentferner",targetzutat=True,next_url=next_url,prev_url=prev_url,page=page)
    elif mode == MODE_REZEPT:
        return render_template('admin_remove.html',inhalt=liste.items,titlet="endgültiger Rezeptentferner",targetrezept=True,next_url=next_url,prev_url=prev_url,page=page)
    elif mode == MODE_TAGS:
        return render_template('admin_remove.html',inhalt=liste.items,titlet="endgültiger Tagsentferner",targettags=True,next_url=next_url,prev_url=prev_url,page=page)
    elif mode == MODE_RZHAT:
        return render_template('admin_remove.html',inhalt=liste.items,titlet="Verknüpfungentferner von Zutat <-> Rezept",targerzhat=True,next_url=next_url,prev_url=prev_url,page=page)
    elif mode == MODE_HAND:
        return render_template('admin_remove.html',inhalt=liste.items,titlet="Verknüpfungentferner von Handlungsschritten",handlung=True,next_url=next_url,prev_url=prev_url,page=page)
    elif mode == MODE_TAGver:
        return render_template('admin_remove.html',inhalt=liste.items,titlet="Verknüpfungentferner von Tags <-> Rezept",Tagver=True,next_url=next_url,prev_url=prev_url,page=page)
    elif mode == MODE_HANDver:
        return render_template('admin_remove.html',inhalt=liste.items,titlet="Verknüpfungentferner von Handlungschritten <-> Rezept",HANDver=True,next_url=next_url,prev_url=prev_url,page=page)
    elif mode == MODE_HANDadd:
        return render_template('admin_remove.html',inhalt=liste.items,titlet="Verknüpfungadder von Handlungschritten <-> Rezept",MODE_HANDadd=True,next_url=next_url,prev_url=prev_url,page=page)
    elif mode == MODE_REZEPTadd:
        return(render_template('admin_remove.html',inhalt=liste.items,titlet="Verknüpfungadder von Zutaten <-> Rezept",MODE_REZEPTadd=True,next_url=next_url,prev_url=prev_url,page=page))
    else:
        print("Kein Tamplate gefunden!")
        return "Kein Tamplate gefunden!"



##############
#    rzhat   #
##############


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

