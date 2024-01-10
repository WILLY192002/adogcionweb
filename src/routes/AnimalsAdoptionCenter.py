from flask import Blueprint, render_template,request,flash,redirect, url_for
from flask_login import current_user

from src.services.AnimalService import AnimalService
from src.services.SpeciesService import SpeciesService
from src.services.BreedService import BreedService
from src.services.UsertypeService import UsertypeService
from src.services.ImageService import ImageService
from src.services.OperationService import OperationService
from src.services.operation_animalService import Operation_AnimalService


from src.models.Animal import Animal

main = Blueprint('animals_adoption_center',__name__)

@main.route('/view/animals', methods = ['GET', 'POST'])
def animalsAdoptionCenter():
  if request.method == 'POST':
    return 'Hay que poner post en view animals'
  else:
    if current_user.is_authenticated and UsertypeService.verifyUserTypeAdoptionCenter(current_user.user_type_id):
      noAdoptedAnimals = AnimalService.getNoAdoptedAnimals(current_user.get_id())
      AdoptedAnimals = AnimalService.getAdoptedAnimals(current_user.get_id())
      return render_template('User_Adoption_Center/post/animals.html', noAdoptedAnimals = noAdoptedAnimals,
                            AdoptedAnimals = AdoptedAnimals)
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
      animal_diet = None
      animal_is_adopted = False

      new_animal = Animal(None, current_user.get_id(), Animal_photo, animal_name,animal_breed, 
                          animal_sex, animal_age, animal_size, animal_weight,animal_diet,None,animal_is_adopted)
      AnimalService.addNewAnimal(new_animal)
      new_animal.id = AnimalService.getLastAnimalAddedByName(animal_name, current_user.get_id()).id


      operaciones = request.form.getlist('operation_id')
      Operation_AnimalService.addNewOperation_Animal(new_animal.id,operaciones)
      return redirect(url_for('animals_adoption_center.animalsAdoptionCenter'))
    else:
      return render_template('auth/no_authorized.html')
  else:
    if current_user.is_authenticated and UsertypeService.verifyUserTypeAdoptionCenter(current_user.user_type_id):
      titlename = 'Nuevo animal'
      breeds = BreedService.getAllBreeds()
      species = SpeciesService.getAllSpecies()
      operations = OperationService.getAllOperations()
      return render_template('User_Adoption_Center/post/animal_information.html', 
                            title = titlename,
                            breeds = breeds,
                            species = species,
                            operations = operations)
    else:
      return render_template('auth/no_authorized.html')