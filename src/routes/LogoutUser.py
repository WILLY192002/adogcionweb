from flask import Blueprint,redirect
from flask_login import logout_user

main = Blueprint('logout_user',__name__)

@main.route('/', methods = ['GET', 'POST'])
def logoutUser():
  logout_user()
  return 'Realizado'