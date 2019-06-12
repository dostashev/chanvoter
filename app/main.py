from flask import Flask, render_template, request, redirect, url_for, make_response, session, send_from_directory, g

import database
from database import models
import dbutils
import rating
from functools import wraps
from config import Config

app = Flask(__name__, static_url_path='')
app.config.update(Config.FLASK_CONFIG)
db_path = Config.FLASK_CONFIG["SQLALCHEMY_DATABASE_URI"]




if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)

