from app.models import db, Ticket, environment, SCHEMA
from sqlalchemy.sql import text


def seed_tickets():
    tickets = [
        Ticket(owner_id=2, site_id=1, title='', description='', priority=1),
        Ticket(owner_id=3, site_id=1, title='', description='', priority=2),
        Ticket(owner_id=4, site_id=2, title='', description='', priority=3),
        Ticket(owner_id=5, site_id=2, title='', description='', priority=4),
        Ticket(owner_id=6, site_id=3, title='', description='', priority=5),
        Ticket(owner_id=6, site_id=3, title='', description='', priority=4),
        Ticket(owner_id=8, site_id=3, title='', description='', priority=3),
        Ticket(owner_id=2, site_id=4, title='', description='', priority=2),
        Ticket(owner_id=11, site_id=4, title='', description='', priority=3),
        Ticket(owner_id=5, site_id=5, title='', description='', priority=2),
        Ticket(owner_id=9, site_id=6, title='', description='', priority=3),
        Ticket(owner_id=11, site_id=7, title='', description='', priority=4),
    ]
    for ticket in tickets:
        db.session.add(ticket)
    db.session.commit()


def undo_tickets():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.tickets RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM tickets"))
        
    db.session.commit()
