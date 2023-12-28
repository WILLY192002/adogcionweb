#libraries
from flask import Blueprint, render_template,request,flash,redirect, url_for
from flask_login import LoginManager, login_user, current_user

#Table model's
from src.models.Access import Access

#services
from src.services.AccessService import AccessService
from src.services.UsertypeService import UsertypeService
from src.services.AdoptioncenterService import AdoptioncenterService
from src.services.NaturalpersonService import NaturalpersonService

main = Blueprint('login_user',__name__)

LoginManagerApp = LoginManager()

@LoginManagerApp.user_loader
def load_user(access_id):
  new_access = AccessService.getAccessById(access_id)
  id_adoption_center = UsertypeService.getUserTypeByName("UT-ADOPTION_CENTER").id
  id_natural_person = UsertypeService.getUserTypeByName("UT-NATURAL_PERSON").id
  if new_access.user_type_id == id_adoption_center:
    return AdoptioncenterService.getAdoptionCenterByAccessId(new_access.id)
  elif new_access.user_type_id == id_natural_person:
    return NaturalpersonService.getNaturalPersonByAccessId(new_access.id)

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
        id_adoption_center = UsertypeService.getUserTypeByName("UT-ADOPTION_CENTER").id
        id_natural_person = UsertypeService.getUserTypeByName("UT-NATURAL_PERSON").id
        if new_access.user_type_id == id_adoption_center:
          login_user(AdoptioncenterService.getAdoptionCenterByAccessId(new_access.id))
          
        elif new_access.user_type_id == id_natural_person:
          login_user(NaturalpersonService.getNaturalPersonByAccessId(new_access.id))
        else:
          flash("Ha ocurrido un error al iniciar sesion, vuelva a intentarlo mas tarde...")
          return redirect(request.referrer)
        return redirect(url_for('home_adoption_center.homeAdoptionCenter'))
      
    else:
      flash("Error en la contraseña o el usuario")
      return redirect(request.referrer)
  else:
    return render_template('auth/login_user.html')