from flask import Blueprint, render_template,request,flash,redirect, url_for
from flask_login import current_user

from src.services.PublicationService import PublicationService
from src.services.NaturalpersonService import NaturalpersonService
from src.services.AccessService import AccessService

main = Blueprint('view_profile_natural_person',__name__)

@main.route('/view/profile=<id>/natural_person/<name>', methods = ['GET', 'POST'])

def viewProfileAdoptionCenter(id,name):
  if request.method == 'POST':
    return 'metodo post'
  else:
    #INFORMATION PROFILE
    user_information = NaturalpersonService.getNaturalPersonById(id)
    access_user_information = AccessService.getAccessById(user_information.access_id)
    user_information.user_type_id = access_user_information.user_type_id
    user_information.email = access_user_information.email

    publications = PublicationService.getAllPublicationByAccessId(user_information.access_id)
    return render_template('User_Natural_Person/profile_natural_person.html', publications = publications)