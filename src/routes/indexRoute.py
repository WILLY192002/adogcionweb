from flask import Blueprint,request,redirect, url_for
from flask_login import logout_user

main = Blueprint('index_route',__name__)


@main.route('/', methods = ['GET'])
def loginUser():
  return redirect(url_for('home_adoption_center.homeAdoptionCenter'))