from flask import Flask, render_template, request, redirect, url_for, make_response, session, send_from_directory, g

import database
from database import models
import dbutils
import rating
from functools import wraps

from config import Config

app = Flask(__name__, static_url_path='')
db_path = 'var/main.db'

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'logged_in' in session.keys():
            return redirect(url_for('login', next = request.url))
        return f(*args, **kwargs)
    return decorated_function

@app.route("/login", methods = ["GET", "POST"])
def login():
    session['logged_in'] = True
    return redirect(next or url_for('index'))

@app.route("/", methods = ["GET", "POST"])
def index():
    #отображает текущие, прошедшие и предстоящие матчи и всякую разную инфу
    scope, _ = database.open_db(db_path)
    with scope() as dbsession:
        active_contests = dbutils.get_active_contests(dbsession)
        return render_template('index.html.j2',active_contests = active_contests)

@app.route("/rating", methods = ["GET", "POST"])
def get_rating():
    #отображает текущую таблицу рейтинга
    scope, _ = database.open_db(db_path)
    with scope() as dbsession:
        girls = sorted(dbutils.get_all_girls(dbsession), key=lambda x : -x["ELO"])
        for i in range(len(girls)):
            girls[i]["rating"] = i + 1
        return render_template('rating.html.j2', girls = girls)

@app.route("/contest/<int:contestID>", methods = ["GET", "POST"])
def contest(contestID):
    #отображает информацию о матче, предлагает проголосовать или сделать ставку
    scope, _ = database.open_db(db_path)
    with scope() as dbsession:
        return render_template('contest.html.j2',**dbutils.get_contest_girls(dbsession,contestID),contest_id=contestID)

@app.route("/vote", methods = ["POST"])
def vote():
    #принимает форму, возвращает информацию об успехе
    fd = request.args
    scope, _ = database.open_db(db_path)
    with scope() as dbsession:
        user_addr = dbutils.get_address(dbsession, fd['private_key'])
        if user_addr == "":
            return "error: invalid private key"
        if dbutils.check_already_voted(dbsession, user_addr, fd['contest_id']):
            return "error: already voted in this contest"
        if not dbutils.check_contest_active(dbsession, fd['contest_id']): return "error: inactive contest"
        if dbutils.get_balance(dbsession, user_addr) >= Config.COINS_PER_VOTE:
            dbutils.add_coins(dbsession, user_addr, -Config.COINS_PER_VOTE)
            dbsession.add(models.Vote(user_addr = user_addr, contest_id = fd['contest_id'], chosen_id = fd['chosen_id']))
    return "success"

@app.route("/transactions", methods = ["GET", "POST"])
def transactions():
    #отображает список транзакций и предлагает сделать оную
    pass

@app.route('/new_transaction', methods = ["POST"])
def new_transaction():
    #принимает форму, делает дела, возвращает информацию об успехе
    fd = request.form
    scope, _ = database.open_db(db_path)
    with scope() as dbsession:
        sender = dbutils.get_address(dbsession, fd['private_key'])
        if sender == "":
            return "error: invalid private key"
        recipient = fd['recipient']
        amount = fd['amount']
        if dbutils.get_balance(dbsession, sender) >= amount:
            dbutils.add_coins(dbsession, sender, -amount)
            dbutils.add_coins(dbsession, recipient, amount)
            dbsession.add(models.Transaction(sender_addr = sender, recipient_addr = recipient, amount = amount))
        else:
            return "error: not enough coins"
    return "success"

@app.route("/new_bet", methods = ["POST"])
def new_bet():
    #принимает форму, делает ставочку, возвращает информацию об успехе
    pass

@app.route("/get_balance", methods = ["GET", "POST"])
def get_balance():
    #принимает форму, отдает баланс кошелька
    fd = request.form
    scope, _ = database.open_db(db_path)
    with scope() as dbsession:
        return str(dbutils.get_balance(dbsession, dbutils.get_address(dbsession, fd['private_key'])))

@app.route("/admin")
@login_required
def send_admin_html():
    scope, _ = database.open_db(db_path)
    with scope() as s: 
        return render_template('admin.html.j2', 
                active_contests = dbutils.get_active_contests(s),
                vote_contests = dbutils.get_vote_contests(s),
                girls = dbutils.get_all_girls(s),
                users = dbutils.get_all_users(s))
                

    return render_template 

@app.route("/finish_contest/<int:contest_id>")
def finish_contest(contest_id):
    #завершает контест и пересчитывает рейтинг
    scope, _ = database.open_db(db_path)
    with scope() as dbsession:
        votes_a, votes_b = dbutils.get_contest_votes(dbsession, contest_id)
        rating_a, rating_b = dbutils.get_contest_girls_rating(dbsession, contest_id)
        bets_a, bets_b = dbutils.get_contest_bets(dbsession, contest_id)
        if votes_a == votes_b:
            
        delta = rating.get_elo_change(rating_a, rating_b, votes_a, votes_b)
        contest = dbsession.query(models.Contest).filter(models.Contest.id == contest_id).first()
        contest.first_girl.ELO += delta
        contest.second_girl.ELO -= delta
        contest.finalized = True

    return "success"

@app.route("/resources/<path:path>")
def send_resource(path):
    return send_from_directory("resources", path)

if __name__ == "__main__":
    app.secret_key = "loadsecretkey"
    app.run(host="0.0.0.0", port=5000, debug=True)
