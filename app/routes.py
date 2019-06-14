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
        voted_contests=cvapi.get_voted_contest_ids(user.address),
        bet_contests=cvapi.get_bet_contests(),
        rated_contests=cvapi.get_rated_contest_ids(user.address))


@app.route('/contests', methods=['GET'])
@login_required
def contests():
    cvapi = ChanVoterApi(db.session)
    user = cvapi.get_user_by_private_key(session['private_key'])
    return render_template('contests.html.j2', 
        active_contests=cvapi.get_active_contests(),
        voted_contests=cvapi.get_voted_contest_ids(user.address))


@app.route('/bets', methods=['GET'])
@login_required
def bets():
    cvapi = ChanVoterApi(db.session)
    user = cvapi.get_user_by_private_key(session['private_key'])
    print(cvapi.get_bet_contests(include_coeffs=True))
    return render_template('bets.html.j2',
        bet_contests=cvapi.get_bet_contests(include_coeffs=True),
        rated_contests=cvapi.get_rated_contest_ids(user.address))


@app.route("/resources/<path:path>")
def send_resource(path):
   return send_from_directory("/home/deadstone/Projects/chanvoter/chanvoter/resources", path)


from app.database.schemas import * 

@app.route("/test")
def test():
    """
    julia = Girl(name="Iulia")
    inna  = Girl(name="Inna")
    contest = Contest(first_girl=julia, second_girld=inna)
    cs = ContestSchema()
    print(cs.dump(contest).data)
    """
    return "It is OK"
