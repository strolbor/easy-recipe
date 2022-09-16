from app import app
import os
from flask import render_template, request
from flask_paginate import Pagination


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


