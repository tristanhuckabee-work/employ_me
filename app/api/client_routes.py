from flask import Blueprint, jsonify
from flask_login import current_user, login_required
from app.models import Client

client_routes = Blueprint('clients', __name__)


@client_routes.route('/')
@login_required
def clients():
    """
    Query for all clients and returns a list of client dictionaries
    """
    if current_user.is_admin:
        clients = Client.query.all()
        return [client.to_dict() for client in clients]
    return {'errors' : ['Unauthorized']}