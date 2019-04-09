from application import db
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from application.kurssit import models
from application.auth import models
from application.models import Base
from flask_login import current_user
from sqlalchemy.sql import text


class Varaus(Base):
    __tablename__ = 'varaus'
    account_id = Column(Integer, ForeignKey('account.id'))
    kurssi_id = Column(Integer, ForeignKey('kurssi.id'))

    account = relationship('User', backref=db.backref('account'))
    kurssi = relationship('Kurssi', backref=db.backref('kurssi'))

    #def __init__(self):


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




