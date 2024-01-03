#libraries
from flask import Blueprint, render_template,request,flash,redirect, url_for

#services
from src.services.AdoptioncenterService import AdoptioncenterService
from src.services.CategoryService import CategoryService
from src.services.PublicationService import PublicationService
from src.services.paymentoption_adoptioncenterService import Paymentoption_AdoptioncenterService
from src.services.AccessService import AccessService

main = Blueprint('view_profile_adoption_center',__name__)

@main.route('/view/profile=<id>/adoption_center=<name>', methods = ['GET', 'POST'])
def viewProfileAdoptionCenter(name, id):
  if request.method == 'POST':
    return 'FALTA PONER LOS POST EN PERFIL'
  else:
    #INFORMATION PROFILE
    user_information = AdoptioncenterService.getAdoptionCenterById(id)
    access_user_information = AccessService.getAccessById(user_information.access_id)
    user_information.user_type_id = access_user_information.user_type_id
    user_information.email = access_user_information.email

    #PUBLICATIONS, CATEGORIES, ACTUALLY SECCION
    publications = PublicationService.getAllPublicationByAccessId(user_information.access_id)
    categories = CategoryService.getAllCategories()
    topics = False
    actuallySeccion = "General"
    PaymentOptions = Paymentoption_AdoptioncenterService.getPaymentOptionAdoptionCenter(id)
    topic_adopted_id = 0
    return render_template('User_Adoption_Center/profile_adoption_center.html',
                           user_information=user_information, 
                           publications = publications, 
                           categories = categories, 
                           topics = topics, 
                           actuallySeccion = actuallySeccion, 
                           PaymentOptions = PaymentOptions, 
                           topic_adopted_id = topic_adopted_id)