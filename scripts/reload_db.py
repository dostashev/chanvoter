#!/bin/python3

import os
from test import fill_db

VAR_DIR = 'var'
DB_FNAME = 'main.db'

if not os.path.exists(VAR_DIR):
    print(f'Create dir {VAR_DIR}')
    os.makedirs(VAR_DIR)

DB_FPATH = os.path.join(VAR_DIR, DB_FNAME)
fill_db(DB_FPATH)
print(f'Fill db {DB_FPATH}')
