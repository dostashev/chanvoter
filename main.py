from flask import Flask, render_template, request, redirect, url_for, make_response, session

import database
from database import models
import dbutils

app = Flask(__name__)
db_path = 'var/main.db'

@app.route("/", methods = ["GET", "POST"])
def index():
    #отображает текущие, прошедшие и предстоящие матчи и всякую разную инфу
    pass

@app.route("/contest/<int:contestID>", methods = ["GET", "POST"])
def contest():
    #отображает информацию о матче, предлагает проголосовать или сделать ставку
    pass

@app.route("/vote", methods = ["POST"])
def vote():
    #принимает форму, возвращает информацию об успехе
    pass

@app.route("/transactions", methods = ["GET", "POST"])
def transactions():
    #отображает список транзакций и предлагает сделать оную
    pass

@app.route('/new_transaction', methods = ["POST"])
def new_transaction():
    #принимает форму, делает дела, возвращает информацию об успехе
    td = request.form
    scope, _ = database.open_db(db_path)
    with scope() as dbsession:
        sender = dbutils.get_address(dbsession, td['private_key'])
        if sender == "":
            return "error: wrong private key"
        recipient = td['recipient']
        amount = td['amount']
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
def submit_answer():
    #принимает форму, отдает баланс кошелька
    pass
    

if __name__ == "__main__":
    app.secret_key = "loadsecretkey"
    app.run(host="0.0.0.0", port=5000, debug=True)
