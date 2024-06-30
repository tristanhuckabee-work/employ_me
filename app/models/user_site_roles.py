from .db import db, environment, SCHEMA, add_prefix_for_prod
from datetime import datetime


class User_Site_Role(db.Model):
    __tablename__ = 'user_site_roles'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String(50), nullable=False, default='Base')
    site_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('sites.id')), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')), nullable=False)

    site = db.relationship('Site', back_populates='staff')
    user = db.relationship('User', back_populates='sites')

    def to_user_dict(self):
        return {
            'id': self.id,
            'role': self.role,
            'site': self.site.to_user_dict()
        }
    def to_site_dict(self):
        return {
            'id': self.id,
            'role': self.role,
            'user': self.user.to_site_dict()
        }
