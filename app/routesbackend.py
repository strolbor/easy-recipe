from app import app, db, forms
from app.rezept import rezept, zutat, handlungsschritt, tags, Association, AssociationRHhat
from app.backend_helper import createFolderIfNotExists, getNewID, createArrayHelper, savepic


import os
from flask import redirect, render_template, request, abort
from flask.helpers import flash, url_for
from sqlalchemy import desc

from flask_paginate import Pagination, get_page_args


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
    page = int(request.args.get('page', 1))
    per_page = app.config['ITEMS_PER_PAGE']
    offset = (page - 1) * per_page

    files = classes.query.order_by(sortedby)
    files_for_render = files.limit(per_page).offset(offset)

    search = False

    pagination = Pagination(page=page, per_page=per_page, offset=offset,
                            total=files.count(), css_framework='bootstrap3',
                            search=search)
    return render_template('admin_show.html', liste=files_for_render, pagination=pagination, titlet=title, page=page, redirect_url=redirect_url)






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
