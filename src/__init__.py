from flask import Flask

# Routes
from .routes import RegisterAdoptionCenter
from .routes import LoginUser

from .routes.LoginUser import LoginManagerApp



app = Flask(__name__)

def init_app(config):
    # Configuration
    app.config.from_object(config)
    LoginManagerApp.init_app(app)

    app.register_blueprint(RegisterAdoptionCenter.main, url_prefix='/register/adoption_center/')
    app.register_blueprint(LoginUser.main, url_prefix='/login')
    return app
