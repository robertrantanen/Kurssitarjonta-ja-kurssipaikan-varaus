from application import db
from application.models import Base
from sqlalchemy.orm import relationship
from application.varaus import models
from flask_login import current_user
from sqlalchemy.sql import text


class Kurssi(Base):
    
    __tablename__ = "kurssi"

    nimi = db.Column(db.String(144), nullable=False)
    aihepiiri_id = db.Column(db.Integer, db.ForeignKey('aihepiiri.id'), nullable=False)
    aika = db.Column(db.String(144))
    paikka = db.Column(db.String(144))
    maksimikoko = db.Column(db.Integer)
    taynna = db.Column(db.String(144))

    account = relationship('Varaus', backref=db.backref('varaus.account'))

    def __init__(self, nimi):
        self.nimi = nimi
        self.taynna = "Ei"


    @staticmethod
    def loyda_kaikki_kurssit():
        stmt = text("SELECT Kurssi.id, Kurssi.nimi, Aihepiiri.nimi AS aihepiiri, Kurssi.aika, Kurssi.paikka, Kurssi.maksimikoko, COUNT(Varaus.kurssi_id) AS maara, Kurssi.taynna FROM Kurssi"
                     " LEFT JOIN Varaus ON Varaus.kurssi_id = Kurssi.id"
                     " LEFT JOIN Aihepiiri ON Kurssi.aihepiiri_id = Aihepiiri.id"
                     " GROUP BY Kurssi.id, Kurssi.nimi, Aihepiiri.nimi")
        res = db.engine.execute(stmt)

        return res

    @staticmethod
    def loyda_aihepiirin_kurssit(aihepiiri=0):
        stmt = text("SELECT Kurssi.id, Kurssi.nimi, Kurssi.aika, Kurssi.paikka, Kurssi.maksimikoko, COUNT(Varaus.kurssi_id) AS maara, Kurssi.taynna FROM Kurssi"
                     " LEFT JOIN Varaus ON Varaus.kurssi_id = Kurssi.id"
                     " LEFT JOIN Aihepiiri ON Kurssi.aihepiiri_id = Aihepiiri.id"
                     " WHERE (Aihepiiri.id = :id)"
                     " GROUP BY Kurssi.id, Kurssi.nimi"
                     ).params(id=aihepiiri)
        res = db.engine.execute(stmt)

        return res

    @staticmethod
    def loyda_kurssi(kurssi=0):
        stmt = text("SELECT Kurssi.nimi FROM Kurssi"
                     " WHERE (Kurssi.id = :id)"
                     " LIMIT 1"
                     ).params(id=kurssi)
        res = db.engine.execute(stmt)

        return res

