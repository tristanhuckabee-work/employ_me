from app.models import db, User_Site_Role, environment, SCHEMA
from sqlalchemy.sql import text


def seed_usrs():
    usrs = [
        User_Site_Role(site_id=1, user_id=2, role='Manager'),
        User_Site_Role(site_id=1, user_id=3),
        User_Site_Role(site_id=1, user_id=4),
        User_Site_Role(site_id=1, user_id=5),
        User_Site_Role(site_id=2, user_id=3, role='Manager'),
        User_Site_Role(site_id=2, user_id=4),
        User_Site_Role(site_id=2, user_id=5),
        User_Site_Role(site_id=3, user_id=6, role='Manager'),
        User_Site_Role(site_id=3, user_id=7),
        User_Site_Role(site_id=3, user_id=8),
        User_Site_Role(site_id=3, user_id=9),
        User_Site_Role(site_id=4, user_id=10, role='Manager'),
        User_Site_Role(site_id=4, user_id=11),
        User_Site_Role(site_id=4, user_id=2),
        User_Site_Role(site_id=4, user_id=3),
        User_Site_Role(site_id=5, user_id=4, role='Manager'),
        User_Site_Role(site_id=5, user_id=5),
        User_Site_Role(site_id=5, user_id=6),
        User_Site_Role(site_id=6, user_id=8, role='Manager'),
        User_Site_Role(site_id=6, user_id=9),
        User_Site_Role(site_id=6, user_id=10),
        User_Site_Role(site_id=7, user_id=11, role='Manager'),
        User_Site_Role(site_id=7, user_id=5, role='Manager'),
        User_Site_Role(site_id=7, user_id=2),
        User_Site_Role(site_id=7, user_id=4)
    ]
    for usr in usrs:
        db.session.add(usr)
    db.session.commit()


def undo_usrs():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.user_site_roles RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM user_site_roles"))
        
    db.session.commit()
