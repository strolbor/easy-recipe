from app import app, db, forms
from app.rezept import rezept, zutat,handlungsschritt,tags,Association,AssociationRHhat
from app.backend_helper import createFolderIfNotExists, getNewID,createArrayHelper, savepic


import os
from flask import redirect, render_template,request, abort
from flask.helpers import flash, url_for
from sqlalchemy import desc

##############
#    tags   #
##############

@app.route('/admin/show/tags/')
def showTags():
    liste = tags.query.order_by(tags.name).all()
    return render_template('admin_show.html',liste=liste,titlet="Tags")

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