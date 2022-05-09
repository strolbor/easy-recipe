from app import app

@app.route('/admin')
def admin():
    """Dies ist der Admin Hauptindex"""
    return "Hallo Admin!"