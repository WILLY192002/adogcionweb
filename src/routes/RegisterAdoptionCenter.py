#libraries
from flask import Blueprint, render_template,request,flash,redirect

#Table model's
from src.models.Access import Access
from src.models.Person import Person
from src.models.Adoptioncenter import AdoptionCenter

#services
from src.services.PersonService import PersonService
from src.services.AdoptioncenterService import AdoptioncenterService
from src.services.AccessService import AccessService
from src.services.UsertypeService import UsertypeService



main = Blueprint('register_adoption_center',__name__)

@main.route('/', methods = ['GET', 'POST'])
def registerAdoptionCenter():
  if request.method == 'POST':
    #ACCESS INFORMATION
    access_id = None
    access_email = request.form['access_email'].lower()
    access_password = request.form['access_password']
    access_user_type_id = UsertypeService.getUserTypeByName('UT-ADOPTION_CENTER').id
    access_is_activate = True
    
    
    #PERSON INFORMATION
    person_id = None #PENDIENTE
    person_first_name = request.form['first_name'].capitalize()
    person_middle_name = request.form['middle_name'].capitalize() if request.form['middle_name'] != '' else None
    person_first_surname = request.form['first_surname'].capitalize()
    person_second_lastname = request.form['second_lastname'].capitalize() if request.form['second_lastname'] != '' else None
    person_identification_type = request.form.get('identification_type')
    person_identification_number = request.form['identification_number']
    person_contact = request.form['contact'] if request.form['contact'] != '' else None
    person_city = request.form['city'].capitalize() if request.form['city'] != '' else None
    person_department = request.form['department'].capitalize() if request.form['department'] != '' else None
    

    #ADOPTION CENTER INFORMATION
    adoptionCenter_id = 0 #PENDIENTE
    adoptionCenter_person_id = None #PENDIENTE
    adoptionCenter_access_id = None #PENDIENTE
    adoptionCenter_photo = None
    adoptionCenter_name = request.form['adoptionCenter_name'].capitalize()
    adoptionCenter_description = None
    adoptionCenter_nit = request.form['adoptionCenter_nit'] 
    adoptionCenter_contact = request.form['adoptionCenter_contact'] 
    adoptionCenter_address = None 
    adoptionCenter_city = request.form['adoptionCenter_city'].capitalize() 
    adoptionCenter_department = request.form['adoptionCenter_department'].capitalize()

    new_access = Access(access_id, access_email, access_password, access_user_type_id, access_is_activate)
    new_person = Person(person_id, person_first_name, person_middle_name, person_first_surname, 
                        person_second_lastname,person_identification_type, person_identification_number, person_contact,
                        person_city,person_department)
    new_adoption_center = AdoptionCenter(adoptionCenter_id,adoptionCenter_person_id,adoptionCenter_access_id,
                                        adoptionCenter_photo,adoptionCenter_name,adoptionCenter_description,adoptionCenter_nit,
                                        adoptionCenter_contact,adoptionCenter_address,adoptionCenter_city,adoptionCenter_department)
    
    #INSERT NEW ACCESS IN DATA BASE
    if not AccessService.getAccessByEmail(new_access.email):
      AccessService.addNewAccess(new_access)
      new_adoption_center.access_id = AccessService.getAccessByEmail(new_access.email).id
    else:
      flash("Este correo electrónico ya ha sido registrado")
      return redirect(request.referrer)
    
    #INSERT NEW PERSON IN DATA BASE
    if not PersonService.getPersonByIdentificationNumber(new_person.identification_number):
      PersonService.addNewPerson(new_person)
      new_adoption_center.person_id = PersonService.getPersonByIdentificationNumber(new_person.identification_number).id
    else:
      new_adoption_center.person_id = PersonService.getPersonByIdentificationNumber(new_person.identification_number).id
    
    #INSERT NEW ADOPTION CENTER IN DATA BASE
    AdoptioncenterService.addNewAdoptionCenter(new_adoption_center)

    return 'XD'

  else:

    return render_template('auth/register_adoption_center.html')

