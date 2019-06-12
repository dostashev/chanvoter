import flask
import jinja2
import importlib
from .routes import app as app_blueprint

def make_app(config, **argv):
    app = flask.Flask(__name__)
    app.config.from_object(config)
    app.register_blueprint(app_blueprint)

    templates_loader = jinja2.ChoiceLoader([
        app.jinja_loader, 
        jinja2.FileSystemLoader(config.TEMPLATE_DIR)])
    app.jinja_loader = templates_loader

    return app

