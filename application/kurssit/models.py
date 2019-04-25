from application import db
from application.models import Base
from sqlalchemy.orm import relationship
from application.varaus import models
from flask_login import current_user
from sqlalchemy.sql import text


class Kurssi(Base):
    
    __tablename__ = "kurssi"

    nimi = db.Column(db.String(144), nullable=False)
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
        stmt = text("SELECT Kurssi.id, Kurssi.nimi, Kurssi.aika, Kurssi.paikka, Kurssi.maksimikoko, COUNT(Varaus.kurssi_id) AS maara, Kurssi.taynna FROM Kurssi"
                     " LEFT JOIN Varaus ON Varaus.kurssi_id = Kurssi.id"
                     " GROUP BY Kurssi.id, Kurssi.nimi")
        res = db.engine.execute(stmt)

        return res