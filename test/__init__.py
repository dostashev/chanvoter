from test.data import *
from database import open_db, models

def fill_db(db_path):
    make_session, clear_db = open_db(db_path)
    clear_db()

    with make_session() as s:
        for g in girls:
            cur_g = models.Girl(**g) 
            s.add(cur_g)
        for c in contests:
            cur_c = models.Contest(**c)
            s.add(cur_c)