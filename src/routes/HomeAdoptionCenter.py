from flask import Blueprint, render_template,request,flash,redirect, url_for
from flask_login import current_user

#Services
from src.services.CategoryService import CategoryService
from src.services.TopicService import TopicService
from src.services.PublicationService import PublicationService
from src.services.UsertypeService import UsertypeService

main = Blueprint('home_adoption_center',__name__)

@main.route('/', methods = ['GET', 'POST'])
def homeAdoptionCenter():
  print("Si está entrando endpoint homeadoption")
  if request.method == 'POST':
    return 'FALTA PONER LOS POST'
  else:
    My_categories = CategoryService.getAllCategories()
    My_topics = TopicService.getAllTopics()
    id_adoption_center = UsertypeService.getUserTypeByName("UT-ADOPTION_CENTER").id
    My_publications = PublicationService.getAllPublicationByUserType(id_adoption_center)
    return render_template('Adoption_Center_User/post/home_adoption_center.html',categories = My_categories,topics = My_topics, publications = My_publications)