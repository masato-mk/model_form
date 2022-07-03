#dbの構築

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app import app

#インスタンス作成
db = SQLAlchemy(app)
#migrateするDBの設定
migrate = Migrate(app, db)

#sqlite_databaseのひな型
class Member(db.Model):

    __tablename__ = 'members'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    age = db.Column(db.Integer)
    comment = db.Column(db.Text)

    def __init__(self, name , age, comment):
        self.name = name
        self.age = age
        self.comment = comment