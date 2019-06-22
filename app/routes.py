from flask import Flask, render_template, request, redirect, url_for, make_response, session, send_from_directory, Blueprint

from functools import wraps

from .database import db
from .cvapi import ChanVoterApi

app = Blueprint("app", __name__)


def login_required(f):
    @wraps(f)
    def decorated_f(*args, **kwargs):
        if not session.get("private_key"):
            return redirect('login')
        return f(*args, **kwargs)

    return decorated_f


@app.route("/auth", methods=['POST'])
def auth():
    cvapi = ChanVoterApi(db.session)
    private_key = request.args.get("private_key")
    user = cvapi.get_user_by_private_key(private_key) 
    if not user:
        return "denied"

    session["private_key"] = private_key
    return "success"


@app.route("/login")
def login():
    if session.get("private_key"):
        return redirect('/')
    else:
        return render_template("login.html.j2")


@app.route("/logout")
@login_required
def logout():
    del session['private_key']
    return redirect('/login')


@app.route('/', methods=['GET'])
@login_required
def index():
    cvapi = ChanVoterApi(db.session)
    user = cvapi.get_user_by_private_key(session['private_key'])
    return render_template('index.html.j2',
        active_contests=cvapi.get_active_contests(),
        voted_contests=cvapi.get_voted_contest_ids(user["address"]),
        bet_contests=cvapi.get_bet_contests(),
        rated_contests=cvapi.get_rated_contest_ids(user["address"]))


@app.route('/contests', methods=['GET'])
@login_required
def contests():
    cvapi = ChanVoterApi(db.session)
    user = cvapi.get_user_by_private_key(session['private_key'])
    return render_template('contests.html.j2', 
        active_contests=cvapi.get_active_contests(),
        voted_contests=cvapi.get_voted_contest_ids(user["address"]))


@app.route('/bets', methods=['GET'])
@login_required
def bets():
    cvapi = ChanVoterApi(db.session)
    user = cvapi.get_user_by_private_key(session['private_key'])
    return render_template('bets.html.j2',
        bet_contests=cvapi.get_bet_contests(include_coeffs=True),
        rated_contests=cvapi.get_rated_contest_ids(user["address"]))


@app.route('/contest/<int:id>', methods=["GET"])
@login_required
def contest(id):
   cvapi = ChanVoterApi(db.session)
   contest = cvapi.get_contest(id, include_amounts=True)
   user = cvapi.get_user_by_private_key(session["private_key"])
   return render_template('contest.html.j2', contest=contest, user=user)


@app.route("/vote", methods=["POST"])
@login_required
def vote():
    args = request.args
    cvapi = ChanVoterApi(db.session)
    return cvapi.vote(args["private_key"],
        args["contest_id"],
        args["chosen_id"],
        args["coins"])


@app.route("/bet/<int:id>", methods=["GET"])
@login_required
def bet(id):
   cvapi = ChanVoterApi(db.session)
   contest = cvapi.get_bet_contest(id)
   user = cvapi.get_user_by_private_key(session["private_key"])
   return render_template('bet.html.j2', contest=contest, user=user)


@app.route("/bet", methods=["POST"])
@login_required
def rate():
    args = request.args
    cvapi = ChanVoterApi(db.session)
    return cvapi.bet(args["private_key"],
        args["contest_id"],
        args["chosen_id"],
        args["coins"])


@app.route("/rating", methods=["GET"])
@login_required
def rating():
    cvapi = ChanVoterApi(db.session)
    return render_template("rating.html.j2", 
        girls=cvapi.get_girls(sort_by_elo=True, enum=True))


@app.route("/profile", methods=["GET"])
@login_required
def profile(): 
    cvapi = ChanVoterApi(db.session)
    user = cvapi.get_user_by_private_key(session["private_key"])
    bets = cvapi.get_bets(user_addr=user["address"])
    votes = cvapi.get_votes(user_addr=user["address"])
    bets = list(reversed(bets))[:10]
    votes = list(reversed(votes))[:10]
    return render_template("profile.html.j2", 
        user=user,
        votes=votes,
        bets=bets)
