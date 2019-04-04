from application import db
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from application.kurssit import models
from application.auth import models


class Varaus(db.Model):
    __tablename__ = 'varaus'
    account_id = Column(Integer, ForeignKey('account.id'), primary_key=True)
    kurssi_id = Column(Integer, ForeignKey('kurssi.id'), primary_key=True)

    account = relationship('User', backref=db.backref('account'))
    kurssi = relationship('Kurssi', backref=db.backref('kurssi'))

    #def __init__(self):


