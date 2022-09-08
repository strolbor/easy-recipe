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
    form.zutaten.choices = createArrayHelper2(zutat.query.all())

    form.tags.choices = createArrayHelper(tags.query.all())
    if form.validate_on_submit():
        pass

    return render_template('nutzer_rezeptanlege.html', form=form)


@app.route("/postskill", methods=["POST", "GET"])
def postskill():
    if request.method == 'POST':
        skills = request.form.getlist('zutat[]')
        for value in skills:
            print(f"Erhalten: {value}")

        msg = 'New record created successfully'
    return str(msg)
