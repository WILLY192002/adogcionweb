from flask import Blueprint, render_template,request,flash,redirect, url_for
from flask_login import current_user

main = Blueprint('view_profile_natural_person',__name__)

@main.route('/view/profile=<id>/natural_person/<name>', methods = ['GET', 'POST'])

def viewProfileAdoptionCenter(id,name):
  if request.method == 'POST':
    return 'metodo post'
  else:
    return render_template('User_Natural_Person/profile_natural_person.html')