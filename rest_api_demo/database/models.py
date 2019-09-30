# The examples in this file come from the Flask-SQLAlchemy documentation
# For more information take a look at:
# http://flask-sqlalchemy.pocoo.org/2.1/quickstart/#simple-relationships

from datetime import datetime
from pytz import timezone

from rest_api_demo.database import db

import sqlite3


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    body = db.Column(db.Text)
    pub_date = db.Column(db.DateTime)

    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    category = db.relationship('Category', backref=db.backref('posts', lazy='dynamic'))

    def __init__(self, title, body, category, pub_date=None):
        self.title = title
        self.body = body
        if pub_date is None:
            pub_date = datetime.utcnow()
        self.pub_date = pub_date
        self.category = category

    def __repr__(self):
        return '<Post %r>' % self.title


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Category %r>' % self.name

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    def __init__(self, id, name):
        self.id = id
        self.name = name

    #def insert_user_value_db(self):
    #    print("++++++++id: " + str(self.id))
    #    print("++++++++name: " + str(self.name))
    #    conn = sqlite3.connect('user_db.sqlite')
    #    cur = conn.cursor()
    #    cur.execute('INSERT INTO experiments (id, name) values ("1", "JoelRest")')
    #    conn.commit()
    #    conn.close()

    @classmethod
    def all(cls):
        items = []
        for i in db.session.query(cls).all():
            items.append(i.to_dict())
        print("======: " + str(items))
        return items

    def to_dict(self):
        return dict((k, getattr(self, k))
                    for k in self.__table__.c.keys())

    @classmethod
    def get(cls, key):
        return db.session.query(cls).get(key)

    def update(self):
        db.session.commit()
        return self

