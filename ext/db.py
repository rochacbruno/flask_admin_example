from flask_sqlalchemy import SQLAlchemy
# Other modules will import this before initialization
db = SQLAlchemy()


def configure(app):
    """initialize db"""
    db.init_app(app)
