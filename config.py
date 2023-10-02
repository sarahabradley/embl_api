from app import app
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+mysqlconnector://root@localhost/rest_api"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)