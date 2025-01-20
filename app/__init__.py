# app/__init__.py

from flask import Flask
from .api import api
from .config import Config

def create_app():
    app = Flask(__name__)
    
    # Load configuration settings
    app.config.from_object(Config)
    
    # Register blueprints (API)
    app.register_blueprint(api, url_prefix="/api")
    
    return app