from app import app, db, forms
from app.rezept import rezept, zutat, handlungsschritt, tags, Association, AssociationRHhat
from app.backend_helper import createFolderIfNotExists, getNewID, createArrayHelper, savepic


import os
from flask import redirect, render_template, request, abort
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


def showclass(classes, sortedby, title, redirect_url):
    """Paginate a section"""
    page = request.args.get('page', 0, type=int)
    liste = classes.query.order_by(sortedby).paginate(
        page, app.config['ITEMS_PER_PAGE'], False)
    next_url = url_for(
        redirect_url, page=liste.next_num) if liste.has_next else None
    prev_url = url_for(
        redirect_url, page=liste.prev_num) if liste.has_prev else None
    return render_template('admin_show.html', liste=liste.items, titlet=title, next_url=next_url, prev_url=prev_url, showCase=True, page=page)






##############
#   generic  #
##############


def entfernerAnzeiger(classes, redirect_url: str, title):
    """Wir wählen zuerst eine Rezept aus um es dann zu bearbeiten"""
    form = forms.rzanlegen()
    form.rezeptpicker.choices = createArrayHelper(
        classes.query.order_by(classes.name).all())
    if form.validate_on_submit():
        return redirect(url_for(redirect_url, ids=form.rezeptpicker.data))
    return render_template('admin_rzpicker.html', form=form, titlet=title)
