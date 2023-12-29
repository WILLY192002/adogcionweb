from flask import Blueprint, render_template,request,flash,redirect, url_for
from flask_login import current_user

main = Blueprint('home_adoption_center',__name__)

@main.route('/', methods = ['GET', 'POST'])
def homeAdoptionCenter():
  print("Si está entrando endpoint homeadoption")
  if request.method == 'POST':
    return 'FALTA PONER LOS POST'
  else:
    My_categories = None
    My_topics = None
    My_publications = None
    return render_template('Adoption_Center_User/post/home_adoption_center.html',)