from app import app

@app.route('/admin')
def admin():
    return "Hallo Admin!"