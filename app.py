import logging
from logging.handlers import TimedRotatingFileHandler
from flask import Flask
from dotenv import load_dotenv
import os
from routes import register_routes

def create_app():
    # Charger les variables d'environnement
    load_dotenv()

    # Créer l'application Flask
    app = Flask(__name__)

    # Configurer le logging
    log_dir = "log"
    os.makedirs(log_dir, exist_ok=True)
    log_file = os.path.join(log_dir, "app.log")

    handler = TimedRotatingFileHandler(log_file, when="midnight", interval=1)
    handler.suffix = "%Y-%m-%d"
    handler.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    )
    handler.setFormatter(formatter)

    app.logger.addHandler(handler)
    app.logger.setLevel(logging.DEBUG)

    # Enregistrer les routes
    register_routes(app)

    return app
