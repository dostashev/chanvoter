from sqlalchemy import Column, ForeignKey, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker, relationship, backref

Base = declarative_base()

class User(Base):
    __tablename__= 'users'

    id = Column(Integer, primary_key=True)
    public_key = Column(String, unique=True)
    private_key = Column(String, unique=True)
    coins = Column(Integer)


class Transaction(Base):
    __tablename__ = 'transactions'

    id = Column(Integer, primary_key=True)
    sender_id = Column(Integer, ForeignKey('users.id'))
    receiver_id = Column(Integer, ForeignKey('users.id'))
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

    #first_girl = relationship('Girl', back_populates='contests')
    #second_girl = relationship('Girl', back_populates='contests')


class Vote(Base):
    __tablename__ = 'votes'
 
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    contest_id = Column(Integer, ForeignKey('contests.id'))
    winner_id = Column(Integer, ForeignKey('girls.id'))
    looser_id = Column(Integer, ForeignKey('girls.id'))
    
    user = relationship('User')
    contest = relationship('Contest')




