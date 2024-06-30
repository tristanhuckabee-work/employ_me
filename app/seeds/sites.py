from app.models import db, Site, environment, SCHEMA
from sqlalchemy.sql import text


def seed_sites():
    sites = [
        Site(client_id=1, name='Site A1', phone_number='000-000-0001', address='1000 Site Address, Big City, The State, USA'),
        Site(client_id=1, name='Site A2', phone_number='111-111-1112', address='2000 Site Address, Big City, The State, USA'),
        Site(client_id=2, name='Site B1', phone_number='222-222-2223', address='3000 Site Address, Big City, The State, USA'),
        Site(client_id=3, name='Site C1', phone_number='333-333-3334', address='4000 Site Address, Big City, The State, USA'),
        Site(client_id=4, name='Site D1', phone_number='444-444-4445', address='5000 Site Address, Big City, The State, USA'),
        Site(client_id=5, name='Site E1', phone_number='555-555-5556', address='6000 Site Address, Big City, The State, USA'),
        Site(client_id=6, name='Site F1', phone_number='666-666-6667', address='7000 Site Address, Big City, The State, USA')
    ]
    for site in sites:
        db.session.add(site)
    db.session.commit()


def undo_sites():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.sites RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM sites"))
        
    db.session.commit()