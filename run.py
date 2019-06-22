import os
import argparse
import importlib

from app import make_app
from config import Config

parser = argparse.ArgumentParser()
parser.add_argument('--host', default="0.0.0.0", type=str)
parser.add_argument('--port', default=80, type=int)
parser.add_argument('--config', default="config", type=str, dest="config_name")

if __name__ == "__main__":
    args = parser.parse_args()
    config = importlib.import_module(args.config_name).Config()

    os.chdir(config.BASE_DIR)
    app = make_app(config=config)
    app.run(host=args.host, port=args.port)
