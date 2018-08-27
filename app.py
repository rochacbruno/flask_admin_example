from flask import Flask
from .ext import db
from .ext import login
from .ext import admin


def create_app():
    """Application Factory"""
    app = Flask(__name__)

    # Create dummy secrey key
    app.config['SECRET_KEY'] = '123456790'
    # Set sqlite database location
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sample_db.sqlite'
    # Set Flask admin theme
    app.config['FLASK_ADMIN_SWATCH'] = 'cosmo'

    # extensions
    db.configure(app)
    login.configure(app)
    admin.configure(app)

    return app
