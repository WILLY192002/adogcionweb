from flask import Blueprint, render_template,request,flash,redirect, url_for
from flask_login import current_user

from src.services.PublicationService import PublicationService
from src.services.NaturalpersonService import NaturalpersonService
from src.services.AccessService import AccessService
from src.services.UsertypeService import UsertypeService

from src.models.NaturalPerson import NaturalPerson

main = Blueprint('view_profile_natural_person',__name__)

@main.route('/view/profile=<id>/natural_person/<name>', methods = ['GET', 'POST'])

def viewProfileNaturalPerson(id,name):
  if request.method == 'POST':
    if current_user.is_authenticated and UsertypeService.verifyUserTypeNatrualPerson(current_user.user_type_id) and current_user.get_id() == id:
      naturalperson_description = request.form['naturalperson_description'].capitalize() if request.form['naturalperson_description'] != '' else 'Sin descripción'
      new_natural_person = NaturalPerson(None,None,None,None,None,naturalperson_description)
      NaturalpersonService.updateNaturalPerson(current_user.get_id(), new_natural_person)
      return redirect(request.referrer)
    else:
      return render_template('auth/no_authorized.html')
  else:
    #INFORMATION PROFILE
    user_information = NaturalpersonService.getNaturalPersonById(id)
    access_user_information = AccessService.getAccessById(user_information.access_id)
    user_information.user_type_id = access_user_information.user_type_id
    user_information.email = access_user_information.email

    publications = PublicationService.getAllPublicationByAccessId(user_information.access_id)
    return render_template('User_Natural_Person/profile_natural_person.html', user_information=user_information, publications = publications)