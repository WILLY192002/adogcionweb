from flask import Blueprint, render_template,request,flash,redirect, url_for
from flask_login import current_user

from src.services.PublicationService import PublicationService
from src.services.NaturalpersonService import NaturalpersonService
from src.services.AccessService import AccessService
from src.services.UsertypeService import UsertypeService
from src.services.ImageService import ImageService

from src.models.NaturalPerson import NaturalPerson

main = Blueprint('view_profile_natural_person',__name__)

@main.route('/view/profile=<id>/natural_person/<name>', methods = ['GET', 'POST'])
def viewProfileNaturalPerson(id,name):
  if request.method == 'POST':
    if current_user.is_authenticated and UsertypeService.verifyUserTypeNatrualPerson(current_user.user_type_id) and current_user.get_id() == id:
      photo = request.form['hiddenField'] if request.form['hiddenField'] != '' else None
      upload_photo = ImageService.upload_image_to_imgbb(photo)
      naturalperson_photo = upload_photo['data']['url'] if photo else None

      naturalperson_description = request.form['naturalperson_description'].capitalize() if request.form['naturalperson_description'] != '' else 'Sin descripción'
      new_natural_person = NaturalPerson(None,None,None,naturalperson_photo,None,naturalperson_description)
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


@main.route('/edit_information/profile=<id>/natural_person/<name>', methods = ['GET', 'POST'])
def editNaturalPersonInformation(id, name):
  if request.method == 'POST':
    if current_user.is_authenticated and UsertypeService.verifyUserTypeAdoptionCenter(current_user.user_type_id): 
      return 'Si hay endponint'
      return redirect(url_for('view_profile_adoption_center.viewProfileAdoptionCenter', name = current_user.name, id = current_user.get_id()))
    else:
      return render_template('auth/no_authorized.html')
  else:
    if current_user.is_authenticated and UsertypeService.verifyUserTypeNaturalPerson(current_user.user_type_id):
      #INFORMATION PROFILE
      user_information = NaturalpersonService.getNaturalPersonById(id)
      access_user_information = AccessService.getAccessById(user_information.access_id)
      user_information.user_type_id = access_user_information.user_type_id
      user_information.email = access_user_information.email
      return render_template('User_Natural_Person/post/edit_information_person.html', user_information = user_information)
    else:
      return render_template('auth/no_authorized.html')