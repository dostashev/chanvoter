from sqlalchemy import Column, ForeignKey, Integer, String, Float, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker, relationship, backref

Base = declarative_base()

class User(Base):
    __tablename__= 'users'

    id = Column(Integer, primary_key=True)
    address = Column(String, unique=True)
    private_key = Column(String, unique=True)
    coins = Column(Integer)


class Transaction(Base):
    __tablename__ = 'transactions'

    id = Column(Integer, primary_key=True)
    sender_addr = Column(Integer, ForeignKey('users.address'))
    recipient_addr = Column(Integer, ForeignKey('users.address'))
    amount = Column(Integer)


class Girl(Base):
    __tablename__ = 'girls'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    instagram = Column(String)
    ELO = Column(Float)


class Contest(Base):
    __tablename__ = 'contests'

    id = Column(Integer, primary_key=True)
    first_girl_id = Column(Integer, ForeignKey('girls.id'))
    second_girl_id = Column(Integer, ForeignKey('girls.id'))
    begin = Column(DateTime)
    end = Column(DateTime)

    first_girl = relationship('Girl',foreign_keys=[first_girl_id])
    second_girl = relationship('Girl',foreign_keys=[second_girl_id])


class Vote(Base):
    __tablename__ = 'votes'
 
    id = Column(Integer, primary_key=True)
    user_addr = Column(Integer, ForeignKey('users.address'))
    contest_id = Column(Integer, ForeignKey('contests.id'))
    chosen_id = Column(Integer, ForeignKey('girls.id'))
    
    user = relationship('User')
    contest = relationship('Contest')




