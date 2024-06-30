from app.models import db, Ticket_Image, environment, SCHEMA
from sqlalchemy.sql import text


def seed_ticket_images():
    ticket_images = [
    ]
    for image in ticket_images:
        db.session.add(image)
    db.session.commit()


def undo_ticket_images():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.ticket_images RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM ticket_images"))
        
    db.session.commit()
