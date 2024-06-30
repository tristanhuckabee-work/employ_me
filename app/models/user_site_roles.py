from .db import db, environment, SCHEMA, add_prefix_for_prod
from datetime import datetime


user_site_roles = db.Table(
    'user_site_roles',
    db.Model.metadata,
    db.column('user_id', db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')), primary_key=True),
    db.column('site_id', db.Integer, db.ForeignKey(add_prefix_for_prod('sites.id')), primary_key=True),
    db.column('role', db.String, primary_key=True),
)


if environment == "production":
    playlist_songs.schema = SCHEMA