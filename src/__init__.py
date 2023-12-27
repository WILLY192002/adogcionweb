from flask import Flask

# Routes
from .routes import RegisterAdoptionCenter
from .routes import LoginUser

app = Flask(__name__)

def init_app(config):
    # Configuration
    app.config.from_object(config)
    return app
