#libraries
from flask import Blueprint, render_template,request,flash,redirect, url_for

#services
from src.services.AdoptioncenterService import AdoptioncenterService
from src.services.CategoryService import CategoryService
from src.services.TopicService import TopicService

main = Blueprint('view_profile_adoption_center',__name__)

@main.route('/view/profile=<id>/adoption_center=<name>', methods = ['GET', 'POST'])
def viewProfileAdoptionCenter(name, id):
  if request.method == 'POST':
    return 'FALTA PONER LOS POST EN PERFIL'
  else:
    user_information = AdoptioncenterService.getAdoptionCenterById(id)
    publications = []
    categories = CategoryService.getAllCategories()
    topics = []
    actuallySeccion = "General"
    PaymentOptions = []
    topic_adopted_id = 0
    return render_template('User_Adoption_Center/post/profile_adoption_center.html',
                           user_information=user_information, 
                           publications = publications, 
                           categories = categories, 
                           topics = topics, 
                           actuallySeccion = actuallySeccion, 
                           PaymentOptions = PaymentOptions, 
                           topic_adopted_id = topic_adopted_id)