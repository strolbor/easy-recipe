from app import app, db, forms
from app.rezept import zutat
from app.backend_helper import getNewID, savepic
from app.routesbackend import remover,MODE_ZUTATEN,showclass

import os
from flask import redirect, render_template,request
from flask.helpers import flash, url_for
from sqlalchemy import desc

@app.route("/tmp/eingabe")
def tmpein():
    form = forms.nutzerein()

    if form.validate_on_submit():
        pass

    return render_template('nutzer_rezeptanlege.html',form=form)