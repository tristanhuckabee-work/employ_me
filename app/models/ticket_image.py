from .db import db, environment, SCHEMA, add_prefix_for_prod
from datetime import datetime


class Site(db.Model):
    __tablename__ = 'sites'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    ticket_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('tickets.id')), nullable=False)
    url = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, default=datetime.now(), onupdate=datetime.now())

    ticket = db.relationship('Ticket', back_populates='images')

    def to_dict(self):
        return {
            'id': self.id,
            'ticket_id': self.ticket_id,
            'url': self.url,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
