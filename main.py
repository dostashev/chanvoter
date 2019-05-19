from flask import Flask, render_template, request, redirect, url_for, make_response, session, send_from_directory

import database
from database import models
import dbutils

from config import Config

app = Flask(__name__, static_url_path='')
db_path = 'var/main.db'

@app.route("/", methods = ["GET", "POST"])
def index():
    #отображает текущие, прошедшие и предстоящие матчи и всякую разную инфу
    pass

@app.route("/contest/<int:contestID>", methods = ["GET", "POST"])
def contest(contestID):
    #отображает информацию о матче, предлагает проголосовать или сделать ставку
    scope, _ = database.open_db(db_path)
    with scope() as dbsession:
        return render_template('contest.html',**dbutils.get_contest_girls(dbsession,contestID),contest_id=contestID)

@app.route("/vote", methods = ["POST"])
def vote():
    #принимает форму, возвращает информацию об успехе
    fd = request.form
    scope, _ = database.open_db(db_path)
    with scope() as dbsession:
        user_addr = dbutils.get_address(dbsession, fd['private_key'])
        if user_addr == "":
            return "error: invalid private key"
        if dbutils.check_already_voted(dbsession, user_addr, fd['contest_id']):
            return "error: already voted in this contest"
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

@app.route("/get_balance", methods = ["POST"])
def get_balance():
    #принимает форму, отдает баланс кошелька
    fd = request.form
    scope, _ = database.open_db(db_path)
    with scope() as dbsession:
        return str(dbutils.get_balance(dbsession, dbutils.get_address(dbsession, fd['private_key'])))
    
@app.route("/resources/<path:path>")
def send_resource(path):
    return send_from_directory("resources", path)

if __name__ == "__main__":
    app.secret_key = "loadsecretkey"
    app.run(host="0.0.0.0", port=5000, debug=True)
