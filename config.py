import os

class Config:
    COINS_PER_VOTE = 10_000

    ADMIN_PASS = "admin"

    BASE_DIR = os.path.abspath(os.path.dirname(__file__))

    FLASK_CONFIG = {
                "TESTING" : True, 
                "DEBUG" : True, 
                "SECRET_KEY" : "this_is_realy_secret",
                "SQLALCHEMY_DATABASE_URI" : os.path.join(BASE_DIR, "var", "main.db"),
            }
   
    
