from hub import db, ma

class Nostro(db.Model):
    __tablename__ = "nostro"

    id = db.Column(db.Integer, primary_key=True)
    nostro_name=db.Column(db.String(20), unique=True, nullable=False)

class NostroSchema(ma.Schema):
  class Meta:
    fields = ('id', 'nostro_name')

# Init schema
nostro_schema = NostroSchema()

class User3(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)