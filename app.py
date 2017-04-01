from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
# import os
#
# BASE_DIR = os.path.abspath(os.path.dirname(__file__))
#
# app = Flask(__name__)
#
# app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + BASE_DIR + "/db.db"
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#
# db = SQLAlchemy(app)
#
# class Socks(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(30))
#     description = db.Column(db.String(200))
#     price = db.Column(db.Float)
#     image = db.Column(db.String(100))

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)


class Socks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    description = db.Column(db.String(200))
    price = db.Column(db.Float)
    image = db.Column(db.String(100))


@app.route('/')
def index():
    all_socks = Socks.query.all()
    return render_template('index.html', socks=all_socks)


@app.route('/add')
def add():
    return render_template('add.html')


@app.route('/save', methods=['POST'])
def save():
    name = request.form['sname']
    description = request.form['comment']
    price = request.form['price']
    image = request.form['image']
    new_sock = Socks(name=name, description=description, price=price, image=image)
    db.session.add(new_sock)
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/delete/<idx>')
def delete(idx):
    del_sock = Socks.query.filter_by(id=idx).first()
    db.session.delete(del_sock)
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/show/<idx>')
def show(idx):
    return idx\


@app.route('/update/<idx>')
def update(idx):
    return idx

if __name__ == '__main__':
    app.run(debug=True)

