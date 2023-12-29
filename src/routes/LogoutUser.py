from flask import Blueprint,redirect, url_for
from flask_login import logout_user

main = Blueprint('logout_user',__name__)

@main.route('/', methods = ['GET', 'POST'])
def logoutUser():
  logout_user()
  return redirect(url_for('home_adoption_center.homeAdoptionCenter'))