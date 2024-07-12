from flask import Blueprint, jsonify
from flask_login import current_user, login_required
from app.models import Ticket, Ticket_Image

ticket_routes = Blueprint('tickets', __name__)


@ticket_routes.route('/all')
@login_required
def tickets_all():
    """
    Query for all tickets and returns a list of ticket dictionaries
    """
    if current_user.is_admin:
        tickets = Ticket.query.all()
        return [ticket.to_dict() for ticket in tickets]
    return {'errors' : ['Unauthorized']}


@ticket_routes.route('/<int:id>')
@login_required
def tickets_by_id(id):
    """
    Query for a ticket by id and returns that ticket as a dictionary
    """
    if current_user.is_admin:
        ticket = Ticket.query.get(id)
        return [ticket.to_dict()]
    return {'errors' : ['Unauthorized']}


@ticket_routes.route('/by-site/<int:id>')
@login_required
def tickets_by_site(id):
    """
    Query for tickets by site id and returns a list of tickets dictionaries
    """
    tickets = Ticket.query.filter(Ticket.site_id == id).all()
    return {'tickets': [ticket.to_dict() for ticket in tickets]}


@ticket_routes.route('/<int:id>')
@login_required
def tickets_by_status(id):
    """
    Query for a ticket by id and returns that ticket as a dictionary
    """
    if current_user.is_admin:
        tickets = Ticket.query.all()
        return [ticket.to_dict() for ticket in tickets]
    return {'errors' : ['Unauthorized']}