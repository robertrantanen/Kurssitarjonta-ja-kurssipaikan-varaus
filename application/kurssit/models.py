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

    account = relationship('Varaus', backref=db.backref('varaus.account'))

    def __init__(self, nimi):
        self.nimi = nimi

    @staticmethod
    def loyda_kayttajan_kurssit():
        stmt = text("SELECT Kurssi.nimi, Kurssi.aika, Kurssi.paikka FROM Kurssi"
                     " LEFT JOIN Varaus ON Varaus.kurssi_id = Kurssi.id"
                     " WHERE (Varaus.account_id = :id)").params(id=current_user.id)
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"nimi":row[0], "aika":row[1], "paikka":row[2]})

        return response
