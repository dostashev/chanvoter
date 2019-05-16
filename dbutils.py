from database.models import *

def get_balance(dbsession, address):
    return dbsession.query(User.address).filter(User.address == address).first().coins

def get_address(dbsession, private_key):
    return dbsession.query(User.private_key).filter(User.private_key == private_key).first().address

def add_coins(dbsession, address, amount):
    dbsession.query(User.address).filter(User.address == address).first().coins += amount

def check_already_voted(dbsession, address, contest_id):
    return len(dbsession.query(Vote.user_addr, Vote.contest_id).filter(Vote.user_addr == address and Vote.contest_id == contest_id).all()) != 0