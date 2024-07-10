from flask import Blueprint, jsonify, request
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


@user_routes.route('/<int:id>/edit', methods=['PATCH'])
@login_required
def edit_user(id):
    """
    Query for a user by id, edit that user and return the updated user as a dictionary
    """
    req = request.json
    user = User.query.get(id)

    if not user:
        return {'error' : 'User not found'}, 404
    elif user.id != current_user.id or not current_user.is_admin:
        return {'error' : 'Forbidden'}, 403

    if 'first_name' in req:
        user.first_name = req['first_name']
    if 'last_name' in req:
        user.last_name = req['last_name']
    if 'is_admin' in req:
        user.is_admin = req['is_admin']
    if 'email' in req:
        user.email = req['email']

    db.session.commit()
    return user.to_dict(),


@user_routes.route('/<int:id>/delete', methods=['DELETE'])
@login_required
def del_user(id):
    """
    Query for a user by id and delete that user, return success or failure
    """
    user = User.query.get(int(id))

    if user.id == current_user.id:
        db.session.delete(user)
        db.session.commit()
        return {'message' : 'User Deleted'}, 200
    else:
        return {'error' : 'Forbidden'}, 403
