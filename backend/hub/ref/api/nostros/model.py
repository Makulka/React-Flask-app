from hub import db

class Nostro(db.Model):
    __tablename__ = "nostro"

    id = db.Column(db.Integer, primary_key=True)
    nostro_name=db.Column(db.String(20), unique=True, nullable=False)

