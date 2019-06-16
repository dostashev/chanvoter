from flask import Flask, render_template, request, redirect, url_for, make_response, session, send_from_directory, Blueprint

from functools import wraps

from .database import db
from .cvapi import ChanVoterApi

app = Blueprint("admin", __name__)


def admin_login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get("admin"):
            return redirect(url_for('admin.admin_login', next=request.url))
        return f(*args, **kwargs)

    return decorated_function


@app.route("/admin_login", methods=["GET"])
def admin_login():
    return render_template("admin_login.html.j2")


@app.route("/admin_auth", methods=["POST"])
def admin_auth():
    cvapi = ChanVoterApi(db.session)
    if cvapi.check_if_admin(request.args["key"]):
        session["admin"] = True
        return "success"
    else:
        return "denied"


@app.route("/admin", methods=["GET"])
@admin_login_required
def admin():
    cvapi = ChanVoterApi(db.session)
    return render_template("admin.html.j2", finalizable_contests=cvapi.get_finalizable_contests(),
        bet_contests=cvapi.get_bet_contests(),
        girls=cvapi.get_girls(),
        users=cvapi.get_users())


@app.route("/begin_contest/<int:id>", methods=["GET"])
@admin_login_required
def begin_contest(id):
    cvapi = ChanVoterApi(db.session)
    cvapi.begin_contest(id)
    return redirect('/admin')


@app.route("/finish_contest/<int:id>", methods=["GET"])
@admin_login_required 
def finish_contest(id):
    cvapi = ChanVoterApi(db.session)
    cvapi.finish_contest(id)
    return redirect('/admin')
