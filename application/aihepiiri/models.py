from application import db
from application.models import Base
from flask_login import current_user
from sqlalchemy.sql import text


class Aihepiiri(Base):
    
    __tablename__ = "aihepiiri"

    nimi = db.Column(db.String(144), nullable=False)

    def __init__(self, nimi):
        self.nimi = nimi


    @staticmethod
    def loyda_aihepiirit():
        stmt = text("SELECT Aihepiiri.id, Aihepiiri.nimi, COUNT(Kurssi.id) AS kurssit FROM Aihepiiri"
                     " LEFT JOIN Kurssi ON Kurssi.aihepiiri_id = Aihepiiri.id"
                     " GROUP BY Aihepiiri.id")
        res = db.engine.execute(stmt)

        return res

    @staticmethod
    def loyda_aihepiiri(aihepiiri=0):
        stmt = text("SELECT Aihepiiri.nimi FROM Aihepiiri"
                     " WHERE (Aihepiiri.id = :id)"
                     " LIMIT 1"
                     ).params(id=aihepiiri)
        res = db.engine.execute(stmt)

        return res
