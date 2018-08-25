from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

def configure(app):
    """initialize db"""
    db.init_app(app)
