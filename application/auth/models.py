from application import db
from application.models import Base
from sqlalchemy.orm import relationship
from application.varaus import models

class User(Base):

    __tablename__ = "account"

    username = db.Column(db.String(144), nullable=False, unique=True)
    password = db.Column(db.String(144), nullable=False)
    admin = db.Column(db.Boolean, nullable=False)

    kurssi = relationship('Varaus', backref=db.backref('varaus.kurssi'))

    def __init__(self, username, password, admin):
        self.username = username
        self.password = password
        self.admin = admin
  
    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    def roles(self):
        if self.admin is True:
            return ["ADMIN"]
        else:
            return ["NORMAL"]

