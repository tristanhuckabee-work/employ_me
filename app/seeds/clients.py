from app.models import db, Client, environment, SCHEMA
from sqlalchemy.sql import text


def seed_clients():
    clients = [
        Client(name='Client A', email='clienta@corpo.com', phone_number='000-000-0000', address='123 Client A, Big City, The State, USA', representative='Corpo McCorpo'),
        Client(name='Client B', email='clientb@corpo.com', phone_number='111-111-1111', address='123 Client B, Big City, The State, USA', representative='Corpo McCorpo'),
        Client(name='Client C', email='clientc@corpo.com', phone_number='222-222-2222', address='123 Client C, Big City, The State, USA', representative='Corpo McCorpo'),
        Client(name='Client D', email='clientd@corpo.com', phone_number='333-333-3333', address='123 Client D, Big City, The State, USA', representative='Corpo McCorpo'),
        Client(name='Client E', email='cliente@corpo.com', phone_number='444-444-4444', address='123 Client E, Big City, The State, USA', representative='Corpo McCorpo'),
        Client(name='Client F', email='clientf@corpo.com', phone_number='555-555-5555', address='123 Client F, Big City, The State, USA', representative='Corpo McCorpo')
    ]
    for client in clients:
        db.session.add(client)
    db.session.commit()


def undo_clients():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.clients RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM clients"))
        
    db.session.commit()
