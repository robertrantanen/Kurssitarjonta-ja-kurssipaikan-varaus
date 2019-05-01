from application import db
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from application.kurssit import models
from application.auth import models
from application.models import Base
from flask_login import current_user
from sqlalchemy.sql import text


class Varaus(db.Model):
    __tablename__ = 'varaus'
    account_id = Column(Integer, ForeignKey('account.id'), primary_key=True)
    kurssi_id = Column(Integer, ForeignKey('kurssi.id'), primary_key=True)
    maksettu = db.Column(db.String(144))

    account = relationship('User', backref=db.backref('account'))
    kurssi = relationship('Kurssi', backref=db.backref('kurssi'))


    @staticmethod
    def loyda_kayttajan_kurssit():
        stmt = text("SELECT Kurssi.id, Kurssi.nimi, Kurssi.aika, Kurssi.paikka, Varaus.maksettu FROM Kurssi"
                     " LEFT JOIN Varaus ON Varaus.kurssi_id = Kurssi.id"
                     " WHERE (Varaus.account_id = :id)").params(id=current_user.id)
        res = db.engine.execute(stmt)

        return res

    @staticmethod
    def loyda_kaikki_varaukset():
        stmt = text("SELECT Varaus.kurssi_id, Kurssi.nimi AS kurssi, Varaus.account_id, account.username AS user, Varaus.maksettu FROM Varaus"
                     " LEFT JOIN Kurssi ON Varaus.kurssi_id = Kurssi.id"
                     " LEFT JOIN account ON Varaus.account_id = account.id"
                     " ORDER BY kurssi")
        res = db.engine.execute(stmt)

        return res

    @staticmethod
    def loyda_kurssin_varaukset(kurssi=0):
        stmt = text("SELECT * FROM Kurssi"
                     " LEFT JOIN Varaus ON Varaus.kurssi_id = Kurssi.id"
                     " WHERE (Varaus.kurssi_id = :id)").params(id=kurssi)
        res = db.engine.execute(stmt)

        return res


    @staticmethod
    def loyda_onko_varaus_jo_olemassa(kurssi=0):
        stmt = text("SELECT kurssi_id FROM Varaus"
                     " WHERE (Varaus.kurssi_id = :kurssi AND Varaus.account_id = :account)"
        ).params(kurssi=kurssi, account=current_user.id)
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"kurssi_id":row[0]})

        return response






