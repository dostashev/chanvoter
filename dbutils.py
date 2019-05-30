from database.models import *
from database.utils import serialize
import datetime

def get_balance(dbsession, address):
    return dbsession.query(User).filter(User.address == address).first().coins

def get_address(dbsession, private_key):
    user = dbsession.query(User).filter(User.private_key == private_key).first()
    return user.address if user != None else ""

def add_coins(dbsession, address, amount):
    dbsession.query(User).filter(User.address == address).first().coins += amount

def check_already_voted(dbsession, address, contest_id):
    return len(dbsession.query(Vote).filter(Vote.user_addr == address).filter(Vote.contest_id == contest_id).all()) != 0

def check_contest_active(dbsession, contest_id):
    begin, end = dbsession.query(Contest.begin, Contest.end).filter(Contest.id == contest_id).first()
    return begin <= datetime.datetime.today() <= end

def get_contest_girls(dbsession, contest_id):
    contest = dbsession.query(Contest).filter(Contest.id == contest_id).first()
    return {'first_girl':serialize(contest.first_girl),'second_girl':serialize(contest.second_girl)}

def get_active_contests(dbsession):
    cur_time = datetime.datetime.today()
    return list(dbsession.query(Contest).filter(Contest.begin <= cur_time).filter(Contest.end >= cur_time).filter(Contest.finalized == False).all())

def get_finalizable_contests(dbsession):
    return list(dbsession.query(Contest).filter(Contest.finalized == False).all())

def get_all_girls(dbsession):
    return list(map(serialize,dbsession.query(Girl).all()))

def get_all_users(dbsession):
    return list(map(serialize,dbsession.query(User).all()))
  
def get_contest_votes(dbsession, contest_id):
    girls = dbsession.query(Contest.first_girl_id, Contest.second_girl_id).filter(Contest.id == contest_id).first()
    return list(map(len,(dbsession.query(Vote).filter(Vote.contest_id == contest_id).filter(Vote.chosen_id == x).all() for x in girls)))

def get_contest_girls_rating(dbsession, contest_id):
    contest = dbsession.query(Contest).filter(Contest.id == contest_id).first()
    return contest.first_girl.ELO, contest.second_girl.ELO

def get_contest_bets(dbsession, contest_id):
    girls = dbsession.query(Contest.first_girl_id, Contest.second_girl_id).filter(Contest.id == contest_id).first()
    return list(map(sum,(dbsession.query(Bet.amount).filter(Bet.contest_id == contest_id).filter(Bet.chosen_id == x).all() for x in girls)))