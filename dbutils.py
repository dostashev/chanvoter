from database.models import *
from database.utils import serialize
import datetime


def get_balance(dbsession, address):
    return dbsession.query(User).filter(User.address == address).first().coins


def get_address(dbsession, private_key):
    user = dbsession.query(User).filter(
        User.private_key == private_key).first()
    return user.address if user != None else ""


def add_coins(dbsession, address, amount):
    dbsession.query(User).filter(
        User.address == address).first().coins += amount


def check_already_voted(dbsession, address, contest_id):
    return len(
        dbsession.query(Vote).filter(Vote.user_addr == address).filter(
            Vote.contest_id == contest_id).all()) != 0


def check_already_bet(dbsession, address, contest_id):
    return len(
        dbsession.query(Bet).filter(Bet.user_addr == address).filter(
            Bet.contest_id == contest_id).all()) != 0


def begin_contest(dbsession, contest_id):
    contest = dbsession.query(Contest).filter(Contest.id == contest_id).first()
    contest.begin = datetime.datetime.now()


def check_contest_active(dbsession, contest_id):
    begin, end = dbsession.query(
        Contest.begin, Contest.end).filter(Contest.id == contest_id).first()
    return begin <= datetime.datetime.today() <= end


def get_contest_girls(dbsession, contest_id):
    contest = dbsession.query(Contest).filter(Contest.id == contest_id).first()
    return {
        'first_girl': serialize(contest.first_girl),
        'second_girl': serialize(contest.second_girl)
    }


def get_active_contests(dbsession):
    cur_time = datetime.datetime.today()
    return list(
        dbsession.query(Contest).filter(Contest.begin <= cur_time).filter(
            Contest.end >= cur_time).filter(Contest.finalized == False).all())


def get_finalizable_contests(dbsession):
    cur_time = datetime.datetime.today()
    return list(
        dbsession.query(Contest).filter(Contest.finalized == False).filter(cur_time >= Contest.begin).all())


def get_bet_contests(dbsession):
    cur_time = datetime.datetime.today()
    return list(
        dbsession.query(Contest).filter(cur_time < Contest.begin).all())


def get_all_girls(dbsession):
    return list(map(serialize, dbsession.query(Girl).all()))


def get_all_girls_mapped(dbsession):
# return dict where key is girl id and value is girl
    res = dict()
    for girl in get_all_girls(dbsession):
        res[girl["id"]] = girl

    return res


def get_all_users(dbsession):
    return list(map(serialize, dbsession.query(User).all()))


def get_contest_votes(dbsession, contest_id):
    girls = dbsession.query(
        Contest.first_girl_id,
        Contest.second_girl_id).filter(Contest.id == contest_id).first()
    return list(
        map(len, (dbsession.query(Vote).filter(
            Vote.contest_id == contest_id).filter(Vote.chosen_id == x).all()
                  for x in girls)))


def get_contest_girls_rating(dbsession, contest_id):
    contest = dbsession.query(Contest).filter(Contest.id == contest_id).first()
    return contest.first_girl.ELO, contest.second_girl.ELO


def get_bet_coeffs(dbsession, contest_id):
    contest = dbsession.query(Contest).filter(Contest.id == contest_id).first()
    contest_bets = dbsession.query(Bet).filter(Bet.contest_id == contest.id)
    first_girl_bets = contest_bets.filter(
        Bet.chosen_id == contest.first_girl.id).all()
    second_girl_bets = contest_bets.filter(
        Bet.chosen_id == contest.second_girl.id).all()

    first_girl_sum = 0
    for bet in first_girl_bets:
        first_girl_sum += bet.coins

    second_girl_sum = 0
    for bet in second_girl_bets:
        second_girl_sum += bet.coins

    ss = first_girl_sum + second_girl_sum
    k1 = '&infin;' if first_girl_sum == 0 else round(ss / first_girl_sum, 2)
    k2 = '&infin;' if second_girl_sum == 0 else round(ss / second_girl_sum, 2)

    return k1, k2

def close_bets(dbsession, contest_id, winner_id):
    """
        close all bets made to this contest.
        If there is a draw `winner_id` have to be `-1`
    """
    bets = dbsession.query(Bet).filter(Bet.contest_id == contest_id).all()

    k1, k2 = get_bet_coeffs(dbsession, contest_id) 

    for bet in list(bets):
        user = dbsession.query(User).filter(User.address == bet.user_addr).first()

        if k1 == '&infin;' or k2 == '&infin;' or winner_id == -1:
            user.coins += bet.coins 
            bet.profit = 0
            continue

        if winner_id == bet.chosen_id:
            if winner_id == bet.contest.first_girl_id:
                user.coins += round(k1  * bet.coins)
                bet.profit = round((k1 - 1) * bet.coins)
            else:
                user.coins += round(k2 * bet.coins)
                bet.profit = round((k2 - 1) * bet.coins)
        else:
            bet.profit = -bet.coins

        bet.finalized = True
        

def get_user_votes(dbsession, user_addr):
    return dbsession.query(Vote).filter(Vote.user_addr == user_addr).all()


def get_user_bets(dbsession, user_addr):
    return dbsession.query(Bet).filter(Bet.user_addr == user_addr).all()


def get_voted_contests(dbsession, user_addr):
    user_votes = dbsession.query(Vote).filter(Vote.user_addr == user_addr).all()
    return list(map(lambda v : v.contest_id, user_votes))


def get_opened_bets(dbsession, user_addr):
    user_bets = dbsession.query(Bet).filter(Bet.user_addr == user_addr).all()
    return list(map(lambda b : b.contest_id, user_bets))

