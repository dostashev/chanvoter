from .database import db

def init_app(app):
    for ext in (db):
        ext.init_app(app)
