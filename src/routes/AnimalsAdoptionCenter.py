from flask import Blueprint, render_template,request,flash,redirect, url_for
from flask_login import current_user

from src.services.AnimalService import AnimalService
from src.services.SpeciesService import SpeciesService
from src.services.BreedService import BreedService
from src.services.UsertypeService import UsertypeService
from src.services.ImageService import ImageService
from src.services.OperationService import OperationService
from src.services.operation_animalService import Operation_AnimalService
from src.services.DiseaseService import DiseaseService
from src.services.disease_animalService import Disease_AnimalService
from src.services.VaccineService import VaccineService
from src.services.vaccine_animalService import Vaccine_AnimalService
from src.services.AdoptioncenterService import AdoptioncenterService


from src.models.Animal import Animal

from src.utils.generate_report import generar_reporte

main = Blueprint('animals_adoption_center',__name__)

@main.route('/view/animals', methods = ['GET', 'POST'])
def animalsAdoptionCenter():
  if request.method == 'POST':
    if current_user.is_authenticated and UsertypeService.verifyUserTypeAdoptionCenter(current_user.user_type_id):
      animal_id = request.form['animalid']
      animal_is_adopted = int(request.form.get('animal_is_adopted'))
      update_animal = Animal(animal_id, None, None, None,None, None, None, None, None, None, None, bool(animal_is_adopted))
      AnimalService.updateAnimalInformation(animal_id,update_animal)
      return redirect(request.referrer)
    else:
      return render_template('auth/no_authorized.html')
  else:
    if current_user.is_authenticated and UsertypeService.verifyUserTypeAdoptionCenter(current_user.user_type_id):
      user_information = AdoptioncenterService.getAdoptionCenterById(current_user.get_id())
      species = SpeciesService.getAllSpecies()
      noAdoptedAnimals = AnimalService.getNoAdoptedAnimals(current_user.get_id())
      AdoptedAnimals = AnimalService.getAdoptedAnimals(current_user.get_id())
      return render_template('User_Adoption_Center/post/animals.html', noAdoptedAnimals = noAdoptedAnimals,
                            AdoptedAnimals = AdoptedAnimals,species = species ,user_information = user_information)
    else:
      return render_template('auth/no_authorized.html')
  
@main.route('/view/animals/filter', methods = ['GET', 'POST'])
def viewAnimalsFilter():
  if request.method == 'POST':
    filter_search = request.form.get('filter_search') if request.form.get('filter_search') != '' else None
    filter_specie = request.form.get('filter_specie') if request.form.get('filter_specie') != '' else None
    filter_sex = request.form.get('filter_sex') if request.form.get('filter_sex') != '' else None
    filter_size = request.form.get('filter_size') if request.form.get('filter_size') != '' else None
    filter_age = request.form.get('filter_age') if request.form.get('filter_age') != '' else None

    user_information = AdoptioncenterService.getAdoptionCenterById(current_user.get_id())
    species = SpeciesService.getAllSpecies()
    noAdoptedAnimals = AnimalService.getNoAdoptedAnimalsFilter(current_user.get_id(),filter_search,filter_specie,filter_sex,filter_size,filter_age)
    AdoptedAnimals = AnimalService.getAdoptedAnimalsFilter(current_user.get_id(),filter_search,filter_specie,filter_sex,filter_size,filter_age)
    return render_template('User_Adoption_Center/post/animals.html', noAdoptedAnimals = noAdoptedAnimals,
                            AdoptedAnimals = AdoptedAnimals, species = species,user_information = user_information)
  else:
    if current_user.is_authenticated and UsertypeService.verifyUserTypeAdoptionCenter(current_user.user_type_id):
      user_information = AdoptioncenterService.getAdoptionCenterById(current_user.get_id())
      species = SpeciesService.getAllSpecies()
      noAdoptedAnimals = AnimalService.getNoAdoptedAnimals(current_user.get_id())
      AdoptedAnimals = AnimalService.getAdoptedAnimals(current_user.get_id())
      return render_template('User_Adoption_Center/post/animals.html', noAdoptedAnimals = noAdoptedAnimals,
                            AdoptedAnimals = AdoptedAnimals , species = species,user_information = user_information)
    else:
      return render_template('auth/no_authorized.html')

  
@main.route('/upload_animal', methods = ['GET', 'POST'])
def uploadAnimalAdoptionCenter():
  if request.method == 'POST':
    if current_user.is_authenticated and UsertypeService.verifyUserTypeAdoptionCenter(current_user.user_type_id):
      photo = request.form['urlImage'] if request.form['urlImage'] != '' else None
      upload_photo = ImageService.upload_image_to_imgbb(photo)
      Animal_photo = upload_photo['data']['url'] if photo else None
      
      animal_name = request.form['animal_name'].capitalize() if request.form['animal_name'] != '' else None
      animal_age = request.form['animal_age'] if request.form['animal_age'] != '' else None
      animal_breed = request.form.get('animal_breed')
      animal_sex = request.form.get('animal_sex')
      animal_size = request.form.get('animal_size')
      animal_weight = request.form['animal_weight'] if request.form['animal_weight'] != '' else None
      animal_observation = request.form['animal_observation'].capitalize() if request.form['animal_observation'] != '' else None
      animal_is_adopted = False

      new_animal = Animal(None, current_user.get_id(), Animal_photo, animal_name,animal_breed, 
                          animal_sex, animal_age, animal_size, animal_weight,animal_observation,None,animal_is_adopted)
      AnimalService.addNewAnimal(new_animal)
      new_animal.id = AnimalService.getLastAnimalAddedByName(animal_name, current_user.get_id()).id

      #Animal Operations Selected
      operations = request.form.getlist('operation_id')
      Operation_AnimalService.addNewOperation_Animal(new_animal.id,operations)

      #Animal Disease Selected
      diseases = request.form.getlist('disease_id')
      Disease_AnimalService.addNewDisease_Animal(new_animal.id,diseases)

      #Animal Vaccine Selected
      vaccines = request.form.getlist('vaccine_id')
      Vaccine_AnimalService.addNewVaccine_Animal(new_animal.id,vaccines)
      return redirect(url_for('animals_adoption_center.animalsAdoptionCenter'))
    else:
      return render_template('auth/no_authorized.html')
  else:
    if current_user.is_authenticated and UsertypeService.verifyUserTypeAdoptionCenter(current_user.user_type_id):
      breeds = BreedService.getAllBreeds()
      species = SpeciesService.getAllSpecies()
      operations = OperationService.getAllOperations()
      diseases = DiseaseService.getAllDiseases()
      vaccines = VaccineService.getAllVaccine()
      return render_template('User_Adoption_Center/post/upload_animal.html',
                            breeds = breeds,
                            species = species,
                            operations = operations,
                            diseases = diseases,
                            vaccines = vaccines)
    else:
      return render_template('auth/no_authorized.html')
    
@main.route('/editAnimal/<string:animal_id>', methods = ['GET', 'POST'])
def editAnimalAdoptionCenter(animal_id):
  if request.method == 'POST':
    if current_user.is_authenticated and UsertypeService.verifyUserTypeAdoptionCenter(current_user.user_type_id):
      photo = request.form['urlImage'] if request.form['urlImage'] != '' else None
      upload_photo = ImageService.upload_image_to_imgbb(photo)
      Animal_photo = upload_photo['data']['url'] if photo else None
      
      animal_name = request.form['animal_name'].capitalize() if request.form['animal_name'] != '' else None
      animal_age = request.form['animal_age'] if request.form['animal_age'] != '' else None
      animal_breed = request.form.get('animal_breed')
      animal_sex = request.form.get('animal_sex')
      animal_size = request.form.get('animal_size')
      animal_weight = request.form['animal_weight'] if request.form['animal_weight'] != '' else None
      animal_observation = request.form['animal_observation'].capitalize() if request.form['animal_observation'] != '' else None
      animal_is_adopted = request.form.get('animal_is_adopted') if request.form.get('animal_is_adopted') != '' else None
      new_animal = Animal(None, None, Animal_photo, animal_name,animal_breed, 
                            animal_sex, animal_age, animal_size, animal_weight,animal_observation,None,animal_is_adopted)
      
      AnimalService.updateAnimalInformation(animal_id,new_animal)
      #Animal Operations added
      operationsAdded = request.form.getlist('operation_id')
      Operation_AnimalService.addNewOperation_Animal(animal_id,operationsAdded)

      #Animal Operations deleted
      operationsDelete = request.form.getlist('deleted_operation')
      Operation_AnimalService.deleteOperation_Animal(animal_id,operationsDelete)

      #Animal Disease Selected
      diseasesAdded = request.form.getlist('disease_id')
      Disease_AnimalService.addNewDisease_Animal(animal_id,diseasesAdded)
      
      #Animal disease deleted
      diseasesDelete = request.form.getlist('deleted_disease')
      Disease_AnimalService.deleteDisease_Animal(animal_id,diseasesDelete)

      #Animal Vaccine Selected
      vaccinesAdded = request.form.getlist('vaccine_id')
      Vaccine_AnimalService.addNewVaccine_Animal(animal_id, vaccinesAdded)
      
      #Animal vaccine deleted
      vaccinesDelete = request.form.getlist('deleted_vaccine')
      Vaccine_AnimalService.deleteVaccine_Animal(animal_id,vaccinesDelete)

      return redirect(url_for('animals_adoption_center.animalsAdoptionCenter'))
    
    else:
      return render_template('auth/no_authorized.html')
  else:
    if current_user.is_authenticated and UsertypeService.verifyUserTypeAdoptionCenter(current_user.user_type_id):
      breeds = BreedService.getAllBreeds()
      species = SpeciesService.getAllSpecies()
      operations = OperationService.getAllOperations()
      diseases = DiseaseService.getAllDiseases()
      vaccines = VaccineService.getAllVaccine()
      animal_edit = AnimalService.getAnimalById(animal_id, current_user.get_id())

      # animal Operations
      operations_recorded = Operation_AnimalService.getOperationByAnimalId(animal_id)

      #animal diseases
      diseases_recorded = Disease_AnimalService.getDiseaseByAnimalId(animal_id)

      #animal vaccine
      vaccines_recorded = Vaccine_AnimalService.getVaccineByAnimalId(animal_id)
      return render_template('User_Adoption_Center/post/edit_animal.html', 
                            animal = animal_edit,
                            breeds = breeds,
                            species = species,
                            operations = operations,
                            diseases = diseases,
                            vaccines = vaccines,
                            operations_recorded = operations_recorded,
                            diseases_recorded = diseases_recorded,
                            vaccines_recorded = vaccines_recorded)
    else:
      return render_template('auth/no_authorized.html')

@main.route('/view/animals/generate_report/id=<fund_id>', methods = ['POST'])
def generate_report(fund_id):
  animal_id = request.form['animal_id']
  fund_id = fund_id
  # animal info
  animal_edit = AnimalService.getAnimalById(animal_id, fund_id)
  breedAndSpecie = BreedService.getBreedsAndSpecieName(animal_edit.breed_id)
  
  # animal Operations
  operations_recorded = Operation_AnimalService.getOperationByAnimalId(animal_id)

  #animal diseases
  diseases_recorded = Disease_AnimalService.getDiseaseByAnimalId(animal_id)

  #animal vaccine
  vaccines_recorded = Vaccine_AnimalService.getVaccineByAnimalId(animal_id)

  generar_reporte(animal_edit, operations_recorded, diseases_recorded, vaccines_recorded, breedAndSpecie)

  flash("Reporte generado")
  return redirect(request.referrer)
