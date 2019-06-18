import flask
import jinja2
import importlib
from .database import db
from .routes import app as app_blueprint
from .routes_admin import app as admin_blueprint

def make_app(config, **argv):
    app = flask.Flask(__name__)
    app.config.from_object(config)
    app.register_blueprint(app_blueprint)
    app.register_blueprint(admin_blueprint)

    db.init_app(app) 

    # Make cutson jinja2 search parameters
    templates_loader = jinja2.ChoiceLoader([
        app.jinja_loader, 
        jinja2.FileSystemLoader(config.TEMPLATE_DIR)])
    app.jinja_loader = templates_loader

    @app.route("/resources/<path:path>", methods = ["GET"])
    def resources(path):
        return flask.send_from_directory(app.config['STATIC_DIR'],path)

    return app

