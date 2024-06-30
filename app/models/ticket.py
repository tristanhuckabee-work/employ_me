from .db import db, environment, SCHEMA, add_prefix_for_prod
from datetime import datetime


class Ticket(db.Model):
    __tablename__ = 'tickets'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')), nullable=False)
    site_id  = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('sites.id')), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(1000), nullable=False)
    priority = db.Column(db.Integer(), nullable=False, default=3)
    status = db.Column(db.String(), nullable=False, default='active')
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, default=datetime.now(), onupdate=datetime.now())

    site = db.relationship('Site', back_populates='tickets')
    owner= db.relationship('User', back_populates='tickets')
    images = db.relationship('Ticket_Image', back_populates='ticket')

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'priority': self.priority,
            'status': self.status,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'site' : self.site.to_user_dict(),
            'owner': self.owner.to_site_dict(),
            'images': [image.to_dict() for image in self.images]
        }
