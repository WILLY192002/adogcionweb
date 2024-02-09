from flask import Blueprint, render_template,request,flash,redirect, url_for
from flask_login import current_user

from src.services.PublicationService import PublicationService
from src.services.NaturalpersonService import NaturalpersonService
from src.services.AccessService import AccessService
from src.services.UsertypeService import UsertypeService
from src.services.ImageService import ImageService
from src.services.PersonService import PersonService

from src.models.NaturalPerson import NaturalPerson
from src.models.Person import Person

main = Blueprint('view_profile_natural_person',__name__)

@main.route('/view/profile=<id>/natural_person/<name>', methods = ['GET', 'POST'])
def viewProfileNaturalPerson(id,name):
  if request.method == 'POST':
    if current_user.is_authenticated and UsertypeService.verifyUserTypeNaturalPerson(current_user.user_type_id) and current_user.get_id() == id:
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
    if current_user.is_authenticated and UsertypeService.verifyUserTypeNaturalPerson(current_user.user_type_id): 
      #PERSON INFORMATION
      person_first_name = request.form['person_first_name'].capitalize()
      person_middle_name = request.form['person_middle_name'].capitalize()
      person_first_surname = request.form['person_first_surname'].capitalize()
      person_second_lastname = request.form['person_second_lastname'].capitalize() 
      person_identification_type = None
      person_identification_number = None
      person_contact = request.form['person_contact']
      person_department = request.form.get('person_department')
      person_city = request.form.get('person_city')

      #NATURAL PERSON INFORMATION
      photo = request.form['hiddenField'] if request.form['hiddenField'] != '' else None
      upload_photo = ImageService.upload_image_to_imgbb(photo)
      naturalPerson_photo = upload_photo['data']['url'] if photo else None

      naturalperson_description = request.form['naturalperson_description'].capitalize()

      naturalPerson_name = person_first_name + " " + person_first_surname

      update_person = Person(None,person_first_name,person_middle_name,person_first_surname,
                            person_second_lastname,person_identification_type,person_identification_number,
                            person_contact,person_city, person_department)
      PersonService.updatePerson(current_user.person_id,update_person)

      update_naturalPerson = NaturalPerson(None,None,None,naturalPerson_photo, naturalPerson_name,naturalperson_description)
      NaturalpersonService.updateNaturalPerson(current_user.id,update_naturalPerson)
      return redirect(url_for('view_profile_natural_person.viewProfileNaturalPerson', name = current_user.name, id = current_user.get_id()))
    else:
      return render_template('auth/no_authorized.html')
  else:
    if current_user.is_authenticated and UsertypeService.verifyUserTypeNaturalPerson(current_user.user_type_id):
      #INFORMATION PROFILE
      user_information = NaturalpersonService.getNaturalPersonById(id)
      access_user_information = AccessService.getAccessById(user_information.access_id)
      user_information.user_type_id = access_user_information.user_type_id
      user_information.email = access_user_information.email

      person_information = PersonService.getPersonById(current_user.person_id)
      return render_template('User_Natural_Person/post/edit_information_person.html', user_information = user_information, person_information = person_information)
    else:
      return render_template('auth/no_authorized.html')