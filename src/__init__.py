from flask import Flask

# Routes
from .routes import RegisterAdoptionCenter
from .routes import LoginUser
from .routes import LogoutUser
from .routes import HomeAdoptionCenter
from .routes import RegisterUser
from .routes import RegisterNaturalPerson
from .routes import ProfileAdoptionCenter
from .routes import indexRoute
from .routes import AnimalsAdoptionCenter
from .routes import PublicationAdoptionCenter

from .routes.LoginUser import LoginManagerApp



app = Flask(__name__)

def init_app(config):
    # Configuration
    app.config.from_object(config)
    LoginManagerApp.init_app(app)

    app.register_blueprint(indexRoute.main, url_prefix='/')

    app.register_blueprint(RegisterAdoptionCenter.main, url_prefix='/register/adoption_center/')
    app.register_blueprint(RegisterNaturalPerson.main, url_prefix='/register/natural_person')
    app.register_blueprint(RegisterUser.main, url_prefix='/register')

    app.register_blueprint(LoginUser.main, url_prefix='/login')
    app.register_blueprint(LogoutUser.main, url_prefix='/logout')

    app.register_blueprint(HomeAdoptionCenter.main)
    
    app.register_blueprint(ProfileAdoptionCenter.main)

    app.register_blueprint(AnimalsAdoptionCenter.main)

    app.register_blueprint(PublicationAdoptionCenter.main)


    
    return app
