import os
from database import open_db, models
import random
from string import ascii_letters
from config import Config
import datetime

VAR_DIR = 'var'
DB_FNAME = 'main.db'

if not os.path.exists(VAR_DIR):
    print(f'Create dir {VAR_DIR}')
    os.makedirs(VAR_DIR)

DB_FPATH = os.path.join(VAR_DIR, DB_FNAME)

def add_user(address, coins = 2000):
    private_key = ''.join(random.choices(ascii_letters, k = 10))
    scope, _ = open_db(DB_FPATH)
    with scope() as s:
        s.add(models.User(address=address,private_key=private_key,coins=coins))
    print(f"Private key: {private_key}")

def add_coins(address, coins):
    scope, _ = open_db(DB_FPATH)
    with scope() as s:
        user = s.query(models.User).filter(models.User.address == address).first()
        user.coins += coins
        print(f"User {address} now has {user.coins} coins")

def add_girl(name, instagram, photo):
    scope, _ = open_db(DB_FPATH)
    with scope() as s:
        s.add(models.Girl(name=name,instagram=instagram,ELO=Config.DEFAULT_ELO,photo=photo))

def add_contest(g1, g2, begin, end):
    scope, _ = open_db(DB_FPATH)
    with scope() as s:
        s.add(models.Contest(first_girl_id=g1, second_girl_id=g2, begin=begin, end=end))

