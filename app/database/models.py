'''
from sqlalchemy import db.Column, db.ForeignKey, db.Integer, db.String, db.Float, db.DateTime, db.Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker, db.relationship, backref
'''
from .database import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String, unique=True)
    private_key = db.Column(db.String, unique=True)
    coins = db.Column(db.Integer)


class Transaction(db.Model):
    __tablename__ = 'transactions'

    id = db.Column(db.Integer, primary_key=True)
    sender_addr = db.Column(db.Integer, db.ForeignKey('users.address'))
    recipient_addr = db.Column(db.Integer, db.ForeignKey('users.address'))
    amount = db.Column(db.Integer)


class Girl(db.Model):
    __tablename__ = 'girls'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    instagram = db.Column(db.String)
    photo = db.Column(db.String)
    ELO = db.Column(db.Float)


class Contest(db.Model):
    __tablename__ = 'contests'

    id = db.Column(db.Integer, primary_key=True)
    first_girl_id = db.Column(db.Integer, db.ForeignKey('girls.id'))
    second_girl_id = db.Column(db.Integer, db.ForeignKey('girls.id'))
    first_girl_win_chance = db.Column(db.Float)
    begin = db.Column(db.DateTime)
    end = db.Column(db.DateTime)
    finalized = db.Column(db.Boolean, default=False)

    first_girl = db.relationship('Girl', foreign_keys=[first_girl_id])
    second_girl = db.relationship('Girl', foreign_keys=[second_girl_id])


class Vote(db.Model):
    __tablename__ = 'votes'

    id = db.Column(db.Integer, primary_key=True)
    user_addr = db.Column(db.Integer, db.ForeignKey('users.address'))
    contest_id = db.Column(db.Integer, db.ForeignKey('contests.id'))
    chosen_id = db.Column(db.Integer, db.ForeignKey('girls.id'))

    user = db.relationship('User')
    contest = db.relationship('Contest')


class Bet(db.Model):
    __tablename__ = 'bets'

    id = db.Column(db.Integer, primary_key=True)
    coins = db.Column(db.Integer)
    user_addr = db.Column(db.Integer, db.ForeignKey('users.address'))
    contest_id = db.Column(db.Integer, db.ForeignKey('contests.id'))
    chosen_id = db.Column(db.Integer, db.ForeignKey('girls.id'))
    finalized = db.Column(db.Boolean, default=False)
    profit = db.Column(db.Integer, default=0)

    user = db.relationship('User')
    contest = db.relationship('Contest')
