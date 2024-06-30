from flask import Blueprint, jsonify
from flask_login import current_user, login_required
from app.models import Site

site_routes = Blueprint('sites', __name__)


@site_routes.route('/')
@login_required
def sites():
    """
    Query for all sites and returns a list of site dictionaries
    """
    if current_user.is_admin:
        sites = Site.query.all()
        return [site.to_dict() for site in sites]
    return {'errors' : ['Unauthorized']}

@site_routes.route('/<int:id>')
@login_required
def site(id):
    """
    Query for a site by id and returns that site as a dictionary
    """
    site = Site.query.get(id)
    return site.to_dict()