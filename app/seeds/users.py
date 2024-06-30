from app.models import db, User, environment, SCHEMA
from sqlalchemy.sql import text


def seed_users():
    users = [
        User(first_name='Demo', last_name='Yung', is_admin=True, email='dyung@demo.com', password='password'),
        User(first_name='Marnie', last_name='Smith', is_admin=False, email='msmith@demo.com', password='password'),
        User(first_name='Bobbie', last_name='Boy', is_admin=False, email='bboy@demo.com', password='password'),
        User(first_name='Robert', last_name='Doe', is_admin=False, email='rdoe@demo.com', password='password'),
        User(first_name='Darla', last_name='Smith', is_admin=False, email='dsmith@demo.com', password='password'),
        User(first_name='William', last_name='Smith', is_admin=False, email='wsmith@demo.com', password='password'),
        User(first_name='Greg', last_name='Arby', is_admin=False, email='garby@demo.com', password='password'),
        User(first_name='Halton', last_name='James', is_admin=False, email='hjames@demo.com', password='password'),
        User(first_name='DeMarcus', last_name='LeMarcus', is_admin=False, email='dlemarcus@demo.com', password='password'),
        User(first_name='Ronald', last_name='Dahl', is_admin=False, email='rdahl@demo.com', password='password'),
        User(first_name='Pewter', last_name='Comm', is_admin=False, email='pcomm@demo.com', password='password')
    ]
    for user in users:
        db.session.add(user)
    db.session.commit()


def undo_users():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM users"))
        
    db.session.commit()
