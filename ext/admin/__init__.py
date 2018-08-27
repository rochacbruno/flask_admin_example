from flask_admin import Admin
from flask_admin.contrib import sqla
from .models import User, Tag
from .views import UserAdmin, PostAdmin
from ..db import db


# Proteger o admin com login via Monkey Patch
from flask_admin.base import AdminIndexView
from flask_simplelogin import login_required


# Applying decorators w/o the `@` syntax sugar
AdminIndexView._handle_view = login_required(AdminIndexView._handle_view)
sqla.ModelView._handle_view = login_required(sqla.ModelView._handle_view)


def configure(app):
    # Create admin
    admin = Admin(app, name='Example: SQLAlchemy',
                  template_mode='bootstrap3')

    # Add views
    admin.add_view(UserAdmin(User, db.session))
    admin.add_view(sqla.ModelView(Tag, db.session))
    admin.add_view(PostAdmin(db.session))
