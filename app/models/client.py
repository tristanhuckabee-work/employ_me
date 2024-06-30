from .db import db, environment, SCHEMA, add_prefix_for_prod
from datetime import datetime


class Client(db.Model):
    __tablename__ = 'clients'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    phone_number = db.Column(db.String(50), nullable=True, unique=True)
    address = db.Column(db.String(255), nullable=True)
    representative = db.Column(db.String(255), nullable=False)
    image = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, default=datetime.now(), onupdate=datetime.now())

    sites = db.relationship('Site', back_populates='client')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'phone_number': self.phone_number,
            'address' : self.address,
            'representative' : self.representative
        }
