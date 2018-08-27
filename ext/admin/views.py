from flask import flash
from flask_admin.contrib import sqla
from flask_admin.contrib.sqla import filters
from flask_admin.actions import action
from wtforms import validators
from .models import UserInfo, User, Post, Tag


def format_user(self, request, obj, fieldname, *args, **kwargs):
    """Return user name in upper case"""
    return getattr(obj, fieldname).upper()


# Customized User model admin
class UserAdmin(sqla.ModelView):
    inline_models = (UserInfo,)
    column_formatters = {'first_name': format_user}

    @action(
        'notify',
        'Notify users',
        'Are you sure you want to notify the selected users?'
    )
    def action_notify_users(self, ids):
        for _id in ids:
            print(f"Notifying user {_id} ....")

        flash(f'{len(ids)} users notified.', 'success')


class PostAdmin(sqla.ModelView):
    # Visible columns in the list view
    column_exclude_list = ['text']

    # List of columns that can be sorted.
    # For 'user' column, use User.username asa column.
    column_sortable_list = ('title', ('user', 'user.username'), 'date')

    # Rename 'title' columns to 'Post Title' in list view
    column_labels = dict(title='Post Title')

    column_searchable_list = ('title', User.username, 'tags.name')

    column_filters = (
        'user',
        'title',
        'date',
        'tags',
        filters.FilterLike(
            Post.title,
            'Fixed Title',
            options=(('test1', 'Test 1'), ('test2', 'Test 2'))
        )
    )

    # Pass arguments to WTForms. In this case, change label for text field to
    # be 'Big Text' and add required() validator.
    form_args = dict(
        text=dict(label='Big Text', validators=[validators.required()])
    )

    form_ajax_refs = {
        'user': {
            'fields': (User.username, User.email)
        },
        'tags': {
            'fields': (Tag.name,)
        }
    }

    def __init__(self, session):
        # Just call parent class with predefined model.
        super(PostAdmin, self).__init__(Post, session)
