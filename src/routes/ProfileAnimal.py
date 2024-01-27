#libraries
from flask import Blueprint, render_template,request,flash,redirect, url_for
from flask_login import current_user

# Service
from src.services.AnimalService import AnimalService
from src.services.BreedService import BreedService
from src.services.OperationService import OperationService
from src.services.operation_animalService import Operation_AnimalService
from src.services.DiseaseService import DiseaseService
from src.services.disease_animalService import Disease_AnimalService
from src.services.VaccineService import VaccineService
from src.services.vaccine_animalService import Vaccine_AnimalService
from src.services.AnimalbreedcommentService import AnimalbreedcommentService

from src.models.AnimalBreedComment import AnimalBreedComment 



main = Blueprint('view_profile_animal',__name__)

@main.route('/view/profile=<fund_id>/animal=<animal_id>/<name>', methods = ['GET', 'POST'])
def viewProfileAnimal(fund_id, animal_id, name):
    profile_name = name
    # animal info
    animal_info = AnimalService.getAnimalById(animal_id, fund_id)
    breedAndSpecie = BreedService.getBreedsAndSpecieName(animal_info.breed_id)
    
    # animal Operations
    operations_recorded = Operation_AnimalService.getOperationByAnimalId(animal_id)

    #animal diseases
    diseases_recorded = Disease_AnimalService.getDiseaseByAnimalId(animal_id)

    #animal vaccine
    vaccines_recorded = Vaccine_AnimalService.getVaccineByAnimalId(animal_id)
    return render_template('Profile_Animal/profile_animal_photos.html',
                           prId = animal_id, 
                           prName = profile_name,
                           fund_id = fund_id,
                           animal = animal_info,
                           breedAndSpecie = breedAndSpecie
                           )

@main.route('/view/profile=<fund_id>/animal=<animal_id>/comments', methods = ['GET', 'POST'])
def profilecomments(fund_id, animal_id):
    if request.method == 'POST':
        animal = AnimalService.getAnimalById(animal_id,fund_id)
        animal_breed_comment = request.form['animal_breed_comment'].capitalized()
        new_comment = AnimalBreedComment(None, int(current_user.access_id),animal.breed_id,animal_breed_comment,None,True)
        AnimalbreedcommentService.addNewAnimalBreedComment(new_comment)
        return redirect(request.referrer)
    else:
        # animal info
        animal_info = AnimalService.getAnimalById(animal_id, fund_id)
        breedAndSpecie = BreedService.getBreedsAndSpecieName(animal_info.breed_id)
        
        # animal Operations
        operations_recorded = Operation_AnimalService.getOperationByAnimalId(animal_id)

        #animal diseases
        diseases_recorded = Disease_AnimalService.getDiseaseByAnimalId(animal_id)

        #animal vaccine
        vaccines_recorded = Vaccine_AnimalService.getVaccineByAnimalId(animal_id)
        return render_template('Profile_Animal/animal_breed_comment.html',
                            prId = animal_id, 
                            prName = animal_info.name,
                            fund_id = fund_id,
                            animal = animal_info,
                            breedAndSpecie = breedAndSpecie)


