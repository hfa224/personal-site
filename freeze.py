"""Freezes the personal site app to static files"""
from flask_frozen import Freezer
from app import app


freezer = Freezer(app)

if __name__ == '__main__':
    freezer.freeze()
