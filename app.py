from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + BASE_DIR + "/db.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Socks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    description = db.Column(db.String(200))
    price = db.Column(db.Float)
    image = db.Column(db.String(100))


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/add')
def add():
    return render_template('add.html')

if __name__ == '__main__':
    app.run(debug=True)

