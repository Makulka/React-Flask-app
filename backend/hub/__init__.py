from flask import request, jsonify
from flask_api import FlaskAPI
from flask_sqlalchemy import SQLAlchemy 
from flask_marshmallow import Marshmallow 

import os

app = FlaskAPI(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

class NostroSchema(ma.Schema):
  class Meta:
    fields = ('id', 'nostro_name')
    
nostro_schema = NostroSchema()

from hub.ref.api.nostros.model import Nostro

@app.route('/nostro', methods=['GET'])
def get_nostros():
    first_nostro = Nostro.query.first()
    result = nostro_schema.dump(first_nostro)
    return jsonify(result)




