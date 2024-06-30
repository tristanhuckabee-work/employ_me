from flask.cli import AppGroup
from .users import seed_users, undo_users
from .clients import seed_clients, undo_clients
from .sites import seed_sites, undo_sites
from .usrs import seed_usrs, undo_usrs
from .tickets import seed_tickets, undo_tickets
from .images import seed_ticket_images, undo_ticket_images
from app.models.db import db, environment, SCHEMA

seed_commands = AppGroup('seed')


# Creates the `flask seed all` command
@seed_commands.command('all')
def seed():
    if environment == 'production':
        undo_users()
        undo_clients()
        undo_sites()
        undo_usrs()
        undo_tickets()
        undo_ticket_images()
    seed_users()
    seed_clients()
    seed_sites()
    seed_usrs()
    seed_tickets()
    seed_ticket_images()


# Creates the `flask seed undo` command
@seed_commands.command('undo')
def undo():
    undo_users()
    undo_clients()
    undo_sites()
    undo_usrs()
    undo_tickets()
    undo_ticket_images()

