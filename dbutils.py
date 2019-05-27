from database.models import *
from database.utils import serialize
import datetime

def get_balance(dbsession, address):
    return dbsession.query(User).filter(User.address == address).first().coins

def get_address(dbsession, private_key):
    user = dbsession.query(User).filter(User.private_key == private_key).first()
    return user.adress if user != None else ""

def add_coins(dbsession, address, amount):
    dbsession.query(User).filter(User.address == address).first().coins += amount

def check_already_voted(dbsession, address, contest_id):
    return len(dbsession.query(Vote).filter(Vote.user_addr == address and Vote.contest_id == contest_id).all()) != 0

def check_contest_active(dbsession, contest_id):
    begin, end = dbsession.query(Contest.begin, Contest.end).filter(Contest.id == contest_id)
    return begin <= datetime.datetime.today() <= end

def get_contest_girls(dbsession, contest_id):
    contest = dbsession.query(Contest).filter(Contest.id == contest_id).first()
    return {'first_girl':serialize(contest.first_girl),'second_girl':serialize(contest.second_girl)}

def get_active_contests(dbsession):
    cur_time = datetime.datetime.today()
    return list(dbsession.query(Contest).filter(Contest.begin <= cur_time).filter(Contest.end >= cur_time).all())

def get_all_girls(dbsession):
    return list(map(serialize,dbsession.query(Girl).all()))