from flask import Blueprint, jsonify
from flask_login import current_user, login_required
from app.models import User

user_routes = Blueprint('users', __name__)


@user_routes.route('/')
@login_required
def users():
    """
    Query for all users and returns a list of user dictionaries
    """
    if current_user.is_admin:
        users = User.query.all()
        return [user.to_dict() for user in users]
    return {'errors': ['Unauthorized']}


@user_routes.route('/<int:id>')
@login_required
def user(id):
    """
    Query for a user by id and returns that user as a dictionary
    """
    user = User.query.get(id)
    return user.to_dict()
