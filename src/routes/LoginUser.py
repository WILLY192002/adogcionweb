#libraries
from flask import Blueprint, render_template,request,flash,redirect, url_for
from flask_login import LoginManager, login_user

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
  id_adoption_center = UsertypeService.getUserTypeByName("UT-ADOPTION_CENTER")
  id_natural_person = UsertypeService.getUserTypeByName("UT-NATURAL_PERSON")
  if new_access.user_type_id == id_adoption_center.id:
    Access_adoptionCenter = AdoptioncenterService.getAdoptionCenterByAccessId(new_access.id)
    Access_adoptionCenter.user_type_id = id_adoption_center.id
    Access_adoptionCenter.user_type_name = id_adoption_center.name
    Access_adoptionCenter.email = new_access.email
    return Access_adoptionCenter
  elif new_access.user_type_id == id_natural_person.id:
    Access_NaturalPerson = NaturalpersonService.getNaturalPersonByAccessId(new_access.id)
    Access_NaturalPerson.user_type_id = id_natural_person.id
    Access_NaturalPerson.user_type_name = id_natural_person.name
    Access_NaturalPerson.email = new_access.email
    return Access_NaturalPerson

@main.route('/', methods = ['GET', 'POST'])
def loginUser():
  if request.method == 'POST':
    id = None 
    email = request.form['email']
    password = request.form['password']
    user_type_id = None
    status = None
    new_access = Access(id, email, password, user_type_id, status)

    #Verify user
    if AccessService.verifyUser(new_access):
      if not new_access.status:
        flash("Este usuario se encuentra inactivo")
        return redirect(request.referrer)
      else:
        login_user(AccessService.getAccessById(new_access.id))
        return redirect(url_for('home_adoption_center.homeAdoptionCenter'))
    else:
      flash("Error en la contraseña o el usuario")
      return redirect(request.referrer)
  else:
    return render_template('auth/login_user.html')