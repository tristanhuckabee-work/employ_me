from flask import Blueprint, jsonify
from flask_login import current_user, login_required
from app.models import Ticket, Ticket_Image

ticket_routes = Blueprint('tickets', __name__)


@ticket_routes.route('/')
@login_required
def tickets():
    """
    Query for all tickets and returns a list of ticket dictionaries
    """
    if current_user.is_admin:
        tickets = Ticket.query.all()
        return [ticket.to_dict() for ticket in tickets]
    return {'errors' : ['Unauthorized']}