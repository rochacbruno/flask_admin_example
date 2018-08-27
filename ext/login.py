from flask_simplelogin import SimpleLogin


def configure(app):
    """Initialize the login extension"""
    SimpleLogin(app)
    # this function will be useful to customize simplelogin extension
