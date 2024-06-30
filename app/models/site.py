from .db import db, environment, SCHEMA, add_prefix_for_prod
from datetime import datetime


class Site(db.Model):
    __tablename__ = 'sites'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('clients.id')), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    phone_number = db.Column(db.String(50), nullable=True, unique=True)
    address = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, default=datetime.now(), onupdate=datetime.now())

    client = db.relationship('Client', back_populates='sites')
    tickets = db.relationship('Ticket', back_populates='site')
    staff = db.relationship('User_Site_Role', back_populates='site')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'phone_number': self.phone_number,
            'client' : self.client.to_dict(),
            'staff'  : [user.to_site_dict() for user in self.staff]
        }
    def to_user_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'client' : self.client.to_dict()
        }
