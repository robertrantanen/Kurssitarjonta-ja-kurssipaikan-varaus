from application import db
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Varaus(Base):
    __tablename__ = 'varaus'
    account_id = Column(Integer, ForeignKey('account.id'), primary_key=True)
    kurssi_id = Column(Integer, ForeignKey('kurssi.id'), primary_key=True)

    account = relationship('User', backref=db.backref('kurssi_varaus'))
    kurssi = relationship('Kurssi', backref=db.backref('account_varaus'))
