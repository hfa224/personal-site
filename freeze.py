"""Freezes the personal site app to static files"""
from flask_frozen import Freezer
from app import app, bp


app.register_blueprint(bp, url_prefix="/serene-lake")
freezer = Freezer(app)

if __name__ == '__main__':
    freezer.freeze()
