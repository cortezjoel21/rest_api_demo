from rest_api_demo.database import db
from rest_api_demo.database.models import User
#from rest_api_demo.database.db_conn import db_conn

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_client_user(data):
    name = data.get('name')
    user_id = data.get('id')
    user = User(user_id, name)
    #user.insert_user_value_db()
    #db_conn.insert_user_value_db(user)
    db.session.add(user)
    db.session.commit()

def update_user(user_id, data):
    user = User.get(user_id)
    user.name = data.get('name')
    User.update()
    #db.session.add(user)
    db.session.commit()

def delete_user(user_id):
    user = User.query.filter(User.id == user_id).one()
    db.session.delete(user)
    db.session.commit()

