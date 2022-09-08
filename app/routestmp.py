from app import app, db, forms
from app.rezept import zutat, tags, handlungsschritt
from app.backend_helper import getNewID, savepic, createArrayHelper2, createArrayHelper
from app.routesbackend import remover, MODE_ZUTATEN, showclass

import os
from flask import redirect, render_template, request
from flask.helpers import flash, url_for
from sqlalchemy import desc


@app.route("/tmp/eingabe")
def tmpein():
    form = forms.nutzerein()

    form.tags.choices = createArrayHelper(tags.query.all())
    if form.validate_on_submit():
        pass

    return render_template('nutzer_rezeptanlege.html', form=form)


@app.route("/ctl/post", methods=["POST", "GET"])
def postskill():
    if request.method == 'POST':
        zutaten = request.form.getlist('zutat[]')
        menge = request.form.getlist('menge[]')
        for value in zutaten:
            print(f"Erhalten in Zutaten: {value}")
        for value in menge:
            print(f"Erhalten in Menge: {value}")
        msg = 'New record created successfully'
    return str(msg)
