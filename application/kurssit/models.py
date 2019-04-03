from application import db

class Kurssi(db.Model):
    __tablename__ = "kurssi"
    id = db.Column(db.Integer, primary_key=True)
    nimi = db.Column(db.String(144), nullable=False)
    aika = db.Column(db.String(144))
    paikka = db.Column(db.String(144))
    maksimikoko = db.Column(db.Integer)
    varattu = db.Column(db.Boolean, nullable=False)

    def __init__(self, nimi):
        self.nimi = nimi
        self.varattu = False
