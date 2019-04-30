from application import db
from application.models import Base
from flask_login import current_user


class Aihepiiri(Base):
    
    __tablename__ = "aihepiiri"

    nimi = db.Column(db.String(144), nullable=False)

    def __init__(self, nimi):
        self.nimi = nimi
