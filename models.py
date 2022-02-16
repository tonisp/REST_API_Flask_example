from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import app

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///example.db'

db = SQLAlchemy(app)

class User(db.Model):
    user = db.Column(db.String(20), primary_key=True)
    country = db.Column(db.String(20))
    birth_date = db.Column(db.Date)
    sex = db.Column(db.String(20))
    currency = db.Column(db.String(20))
    balance = db.Column(db.Integer)

def __init__(self, user, country, birth_date, sex, currency, balance):
    self.user = user
    self.country = country
    self.birth_date = birth_date
    self.sex = sex
    self.currency = currency
    self.balance = balance


if __name__ == '__main__':
    db.create_all()
    app.run(debug = True)