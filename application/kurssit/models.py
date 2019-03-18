from application import db

class Kurssi(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nimi = db.Column(db.String(144), nullable=False)
    aika = db.Column(db.DateTime)
    paikka = db.Column(db.String(144))
    maksimikoko = db.Column(db.Integer)

    def __init__(self, nimi):
        self.nimi = nimi
