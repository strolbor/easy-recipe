from flask import render_template, flash
from app import app, forms


@app.route('/')
@app.route('/index')
def index():
    return render_template('base.html', title="Test")


choices_array = []
home_html = "home.html"
@app.route('/home', methods=['GET', 'POST'])
def home():
    global choices_array
    form = forms.d_felder()
    return render_template(home_html, title="Suche", form=form)
