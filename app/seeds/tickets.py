from app.models import db, Ticket, environment, SCHEMA
from sqlalchemy.sql import text


def seed_tickets():
    tickets = [
        Ticket(owner_id=2, site_id=1, title='ticket21', description='description...', priority=1),
        Ticket(owner_id=3, site_id=1, title='ticket31', description='description...', priority=2),
        Ticket(owner_id=4, site_id=2, title='ticket42', description='description...', priority=3),
        Ticket(owner_id=5, site_id=2, title='ticket52', description='description...', priority=4),
        Ticket(owner_id=6, site_id=3, title='ticket63', description='description...', priority=5),
        Ticket(owner_id=6, site_id=3, title='ticket63b', description='description...', priority=4),
        Ticket(owner_id=8, site_id=3, title='ticket83', description='description...', priority=3),
        Ticket(owner_id=2, site_id=4, title='ticket24', description='description...', priority=2),
        Ticket(owner_id=11, site_id=4, title='ticket114', description='description...', priority=3),
        Ticket(owner_id=5, site_id=5, title='ticket55', description='description...', priority=2),
        Ticket(owner_id=9, site_id=6, title='ticket96', description='description...', priority=3),
        Ticket(owner_id=11, site_id=7, title='ticket117', description='description...', priority=4),
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
