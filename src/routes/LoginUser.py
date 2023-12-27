#libraries
from flask import Blueprint, render_template,request,flash,redirect, url_for

#Table model's
from src.models.Access import Access

#services
from src.services.AccessService import AccessService

main = Blueprint('login_user',__name__)

@main.route('/', methods = ['GET', 'POST'])
def loginUser():
  if request.method == 'POST':
    id = None 
    email = request.form['email']
    password = request.form['password']
    user_type_id = None
    is_activate = None
    new_access = Access(id, email, password, user_type_id, is_activate)

    #Verify user
    if AccessService.verifyUser(new_access):
      if not new_access.is_activate:
        flash("Este usuario se encuentra inactivo")
        return redirect(request.referrer)
      else:
        return redirect(url_for('home_adoption_center.homeAdoptionCenter'))
      
    else:
      flash("Error en la contraseña o el usuario")
      return redirect(request.referrer)
  else:
    return render_template('auth/login_user.html')