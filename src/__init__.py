from flask import Flask

# Routes
from .routes import RegisterAdoptionCenter
from .routes import LoginUser
from .routes import LogoutUser
from .routes import HomeAdoptionCenter

from .routes.LoginUser import LoginManagerApp



app = Flask(__name__)

def init_app(config):
    # Configuration
    app.config.from_object(config)
    LoginManagerApp.init_app(app)

    app.register_blueprint(RegisterAdoptionCenter.main, url_prefix='/register/adoption_center/')
    app.register_blueprint(LoginUser.main, url_prefix='/login')
    app.register_blueprint(LogoutUser.main, url_prefix='/logout')
    app.register_blueprint(HomeAdoptionCenter.main, url_prefix='/home/adoption_center')
    return app
