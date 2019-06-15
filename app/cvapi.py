from datetime import datetime

from .database.models import *
from .database.schemas import *


class ChanVoterApi(object):

    dbsession = None


    def __init__(self, dbsession):
        self.dbsession = dbsession


    def get_user(self, address):
        user = self.dbsession.query(User).filter(
            User.address == address).first()
        us = UserSchema()
        return us.dump(user).data


    def get_contest(self, id):
        contest = self.dbsession.query(Contest).filter(Contest.id == id).first()
        cs = ContestSchema()
        return cs.dump(contest).data


    def get_bets(self, user_addr=None, contest_id=None):
        bets = self.dbsession.query(Bet)

        if not user_addr is None:
            bets = bets.filter(Bet.user_addr == user_addr)

        if not contest_id is None:
            bets = bets.filter(Bet.contest_id == contest_id)

        bs = BetSchema(many=True)
        return bs.dump(bets.all()).data


    def get_votes(self, user_addr=None, contest_id=None):
        votes = self.dbsession.query(Vote)

        if not user_addr is None:
            votes = votes.filter(Vote.user_addr == user_addr)

        if not contest_id is None:
            votes = votes.filter(Vote.contest_id == contest_id)

        vs = VoteSchema(many=True)
        return vs.dump(votes.all()).data

    
    def get_contests(self):
        contests = self.dbsession.query(Contest)
        cs = ContestSchema(many=True)
        return cs.dump(contests.all()).data


    def get_user_by_private_key(self, private_key):
        user = self.dbsession.query(User).filter(
            User.private_key == private_key).first()
        us = UserSchema()
        return us.dump(user).data


    def get_balance(self, addr):
        user = self.get_user(addr)
        return user["coins"]

    '''
    def check_already_voted(self, addr, contest_id):
        bets = self.get_bets(user_addr=user_addr, contest_id=contest_id)
        return bet
    '''

    def check_contest_active(self, id):
        contest = self.get_contest(id)
        begin = datetime.fromisoformat(contest["begin"])
        end = datetime.fromisoformat(contest["end"])
        return not contest["finalized"] and begin <= datetime.today() <= end


    def check_contest_finalizable(self, id):
        contest = self.get_contest(id)
        begin = datetime.fromisoformat(contest["begin"])
        return not contest["finalized"] and begin <= datetime.today()


    def check_contest_is_bet(self, id):
        contest = self.get_contest(id)
        begin = datetime.fromisoformat(contest["begin"])
        return datetime.today() <= begin

    def get_bet_coeffs(self, contest_id):
        """ Return how much money will get
        user for this girl win. If it is impossible
        to count coeff then function return '&infin;'
        """
        contest = self.get_contest(contest_id)
        bets = self.get_bets(contest_id=contest_id)
        s1 = 0
        s2 = 0

        for b in bets:
            if b["chosen_id"] == contest["first_girl_id"]:
                s1 += b["coins"]
            if b["chosen_id"] == contest["second_girl_id"]:
                s2 += b["coins"]

        k1 = '&infin;' if s1 == 0 else (s1 + s2) / s1
        k2 = '&infin;' if s2 == 0 else (s1 + s2) / s2
        return k1, k2


    def get_active_contests(self):
        contests = self.get_contests()
        contests = filter(lambda c :
            self.check_contest_active(c["id"]),
            contests)
        return list(contests)


    def get_bet_contests(self, include_coeffs=False):
        """ Return contests from which you can bet.
        If `include_coeffs` flag is set then add
        `k1` and `k2` fields with bet coeffs to every
        contest object
        """
        contests = self.get_contests()
        contests = filter(lambda c :
            self.check_contest_is_bet(c["id"]),
            contests)

        if include_coeffs:
            for c in contests: 
                k1, k2 = self.get_bet_coeffs(c["id"])
                #c.k1 = k1
                #c.k2 = k2

        return list(contests)


    def get_finalizable_contests(self):
        contests = self.get_contests()
        contests = filter(lambda c :
            self.check_contest_finalizable(c["id"]),
            contests)
        return list(contests)


    def get_girls(self, sort_by_elo=False, enum=False):
        """ Return girls. 
        If `sort_by_elo` flag set then girls will ordered by ELO. 
        If `enum` flag set then add field number to every girl object
        """
        girls = self.dbsession.query(Girl).all()

        if sort_by_elo:
            girls = sorted(girls, key=lambda g: g["ELO"])

        if enum:
            for g, i in zip(girls, range(1, len(girls) + 1)):
               #g.number = i 
               pass

        return list(girls)


    def get_girls_mapped(self, **argv):
        """ Return dict where key is id of girl, value
        is girl's object
        """
        girls = self.get_girls(**argv)
        girls_dict = dict()

        for g in girls:
            girls_dict.update({g["id"], g})

        return girls_dict


    def get_users(self):
        return self.dbsession.query(User).all()


    def get_voted_contest_ids(self, user_addr):
        """ Return list of contests ids from whick user 
        make a bit
        """
        votes = self.get_votes(user_addr=user_addr)
        return list(map(lambda v : v["contest_id"], votes)) 


    def get_rated_contest_ids(self, user_addr):
        """ Return list of contest ids from  which the user
        made a bit
        """
        bets = self.get_bets(user_addr=user_addr)
        return list(map(lambda b : b["contest_id"], bets))




