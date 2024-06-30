from .db import db, environment, SCHEMA, add_prefix_for_prod
from datetime import datetime
from .user_site_roles import user_site_roles


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
    staff = db.relationship('User', secondary=user_site_roles, back_populates='sites')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'phone_number': self.phone_number,
            'client' : self.client.to_dict(),
        }
