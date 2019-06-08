import os
import getpass

class Config:
    COINS_PER_VOTE = 100
    DEFAULT_ELO = 1500

    ADMIN_PASS = "sokolovgay"
    
    USER          = getpass.getuser()
    HOST          = "ochk.tk"
    BASE_DIR      = os.path.abspath(os.path.dirname(__file__))
    RESOURCES_DIR = os.path.join(BASE_DIR, "resources")
    ENV           = os.path.join(os.path.dirname(BASE_DIR), "bin")
    DB_PATH       = os.path.join(BASE_DIR, "var", "main.db")

    FLASK_CONFIG = {
                "TESTING" : True, 
                "DEBUG" : True, 
                "SECRET_KEY" : "this_is_realy_secret",
                "SQLALCHEMY_DATABASE_URI" : DB_PATH,
            }
