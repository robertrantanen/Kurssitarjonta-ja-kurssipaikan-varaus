from application import db
from application.models import Base
from sqlalchemy.orm import relationship
from application.varaus import models


class Kurssi(Base):
    
    __tablename__ = "kurssi"

    nimi = db.Column(db.String(144), nullable=False)
    aika = db.Column(db.String(144))
    paikka = db.Column(db.String(144))
    maksimikoko = db.Column(db.Integer)
    varattu = db.Column(db.Boolean, nullable=False)

    account = relationship('Varaus', backref=db.backref('varaus.account'))

    def __init__(self, nimi):
        self.nimi = nimi
        self.varattu = False
