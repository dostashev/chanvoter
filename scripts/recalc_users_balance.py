import sys
import database
from database import models
from config import Config

if len(sys.argv) == 1:
    print("Usage: \npython recalc_users_balance <db-path>")
    exit(1)

scope, _ = database.open_db(sys.argv[1])

with scope() as s:
    users = s.query(models.User).all()

    for user in users:

        user_votes = s.query(
            models.Vote).filter(models.Vote.user_addr == user.address).all()

        user_bets = s.query(
            models.Bet).filter(models.Bet.user_addr == user.address).all()

        user_coins = 3000
        user_coins -= len(user_votes) * Config.COINS_PER_VOTE

        for bet in user_bets:
            if bet.finalized:
                user_coins += bet.profit
            else:
                user_coins -= bet.coins

        user.coins = user_coins
