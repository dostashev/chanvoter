from os import path
from jinja2 import Environment, FileSystemLoader
from config import Config 

if __name__ == "__main__":
    deploy_dir    = path.join(Config.BASE_DIR, "deploy")
    deploy_meta   = path.join(deploy_dir, "meta") 
    
    templates_enviroment = Environment(loader=FileSystemLoader(deploy_meta))

    nginxt = templates_enviroment.get_template('chanvoter.conf.j2')
    uwsgit = templates_enviroment.get_template('uwsgi.ini.j2')
    systemdt = templates_enviroment.get_template('chanvoter.service.j2')
    
    with open(path.join(deploy_dir, "chanvoter.conf"), "w") as of:
        of.write(nginxt.render(
            HOST=Config.HOST,
            RESOURCES_DIR=Config.RESOURCES_DIR))

    with open(path.join(deploy_dir, "uwsgi.ini"), "w") as of:
        of.write(uwsgit.render(
            BASE_DIR=Config.BASE_DIR,
            ENV=Config.ENV))

    with open(path.join(deploy_dir, "chanvoter.service"), "w") as of:
        of.write(systemdt.render(
            USER=Config.USER,
            BASE_DIR=Config.BASE_DIR,
            ENV=Config.ENV))

