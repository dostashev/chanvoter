import os
import getpass

class Config:
    COINS_PER_VOTE = 100
    DEFAULT_ELO = 1500

    ADMIN_PASS = "sokolovgay"
    SECRET_KEY = "This realy need to be changed"
    
    USER          = getpass.getuser()
    HOST          = "ochk.tk"
    BASE_DIR      = os.path.abspath(os.path.dirname(__file__))
    STATIC_DIR    = os.path.join(BASE_DIR, "resources")
    TEMPLATE_DIR  = os.path.join(BASE_DIR, "templates")
    DB_PATH       = os.path.join(BASE_DIR, "var", "main.db")
    ENV           = os.path.join(os.path.dirname(BASE_DIR), "bin")

    DEBUG = True
