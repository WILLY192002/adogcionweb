#libraries
from flask import Blueprint, render_template,request,flash,redirect, url_for

#Table model's
from src.models.Access import Access
from src.models.Person import Person
from src.models.NaturalPerson import NaturalPerson

#services
from src.services.PersonService import PersonService
from src.services.AccessService import AccessService
from src.services.UsertypeService import UsertypeService
from src.services.NaturalpersonService import NaturalpersonService



main = Blueprint('register_natural_person',__name__)

@main.route('/', methods = ['GET', 'POST'])
def registerNaturalPerson():
  if request.method == 'POST':
    #ACCESS INFORMATION
    access_id = None
    access_email = request.form['access_email'].lower()
    access_password = request.form['access_password']
    access_user_type_id = UsertypeService.getUserTypeByName('UT-NATURAL_PERSON').id
    access_status = True
    
    
    #PERSON INFORMATION
    person_id = None #PENDIENTE
    person_first_name = request.form['first_name'].capitalize()
    person_middle_name = request.form['middle_name'].capitalize() if request.form['middle_name'] != '' else None
    person_first_surname = request.form['first_surname'].capitalize()
    person_second_lastname = request.form['second_lastname'].capitalize() if request.form['second_lastname'] != '' else None
    person_identification_type = request.form.get('identification_type')
    person_identification_number = request.form['identification_number']
    person_contact = request.form['contact'] if request.form['contact'] != '' else None
    person_city = request.form.get('person_city') if request.form.get('person_city') != '' else None
    person_department = request.form.get('person_department') if request.form.get('person_department') != '' else None
    
    #NATURAL PERSON INFORMATION
    naturalPerson_id = None
    naturalPerson_access_id = None
    naturalPerson_person_id = None
    naturalPerson_photo = None
    naturalPerson_name = person_first_name + " " +person_first_surname

    new_access = Access(access_id, access_email, access_password, access_user_type_id, access_status)
    new_person = Person(person_id, person_first_name, person_middle_name, person_first_surname, 
                        person_second_lastname,person_identification_type, person_identification_number, person_contact,
                        person_city,person_department)
    new_natural_person = NaturalPerson(naturalPerson_id, naturalPerson_person_id,naturalPerson_access_id, naturalPerson_photo,naturalPerson_name, None)
    
    
    #INSERT NEW ACCESS IN DATA BASE
    if not AccessService.getAccessByEmail(new_access.email):
      AccessService.addNewAccess(new_access)
      new_natural_person.access_id = AccessService.getAccessByEmail(new_access.email).id
    else:
      flash("Este correo electrónico ya ha sido registrado")
      return redirect(request.referrer)
    
    #INSERT NEW PERSON IN DATA BASE
    if not PersonService.getPersonByIdentificationNumber(new_person.identification_number):
      PersonService.addNewPerson(new_person)
      new_natural_person.person_id = PersonService.getPersonByIdentificationNumber(new_person.identification_number).id
    else:
      person_recorded = PersonService.getPersonByIdentificationNumber(new_person.identification_number)
      new_natural_person.person_id = person_recorded.id
      new_natural_person.name = person_recorded.first_name + " " + person_recorded.first_surname
    #INSERT NEW ADOPTION CENTER IN DATA BASE
    NaturalpersonService.addNewNaturalPerson(new_natural_person)

    return redirect(url_for('login_user.loginUser'))

  else:
    return render_template('auth/register_natural_person.html')