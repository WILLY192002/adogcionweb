from flask import Blueprint, render_template,request,flash,redirect, url_for
from flask_login import current_user

#Services
from src.services.CategoryService import CategoryService
from src.services.TopicService import TopicService
from src.services.PublicationService import PublicationService
from src.services.UsertypeService import UsertypeService

from src.models.Topic import Topic

main = Blueprint('home_adoption_center',__name__)

@main.route('/home/adoption_center', methods = ['GET', 'POST'])
def homeAdoptionCenter():
  print("Si está entrando endpoint homeadoption")
  if request.method == 'POST':
    filter_category = request.form.get('filter_category') if request.form.get('filter_category') != '' else False 
    filter_topic = request.form.get('filter_topic') if request.form.get('filter_topic') != '' else False
    filter_search = request.form.get('filter_search') if request.form.get('filter_search') != '' else False

    if filter_topic and filter_search:
      return redirect(url_for('home_adoption_center.homeAdoptionCenterAllFilter',category = filter_category, topic = filter_topic, search = filter_search))
    elif not filter_topic and (filter_category and filter_search):
      return redirect(url_for('home_adoption_center.homeAdoptionCenterCategorySearch',category = filter_category, search = filter_search))
    elif not filter_category and filter_search:
      return redirect(url_for('home_adoption_center.homeAdoptionCenterSearch',search = filter_search))
    elif filter_topic and not filter_search:
      return redirect(url_for('home_adoption_center.homeAdoptionCenterTopic',category = filter_category, topic = filter_topic))
    elif filter_category and not (filter_topic and filter_search):
      return redirect(url_for('home_adoption_center.homeAdoptionCenterCategory',category = filter_category))
    else:
      return redirect(request.referrer)
      
  else:
    My_categories = CategoryService.getAllCategories()
    My_topics = TopicService.getAllTopics()
    My_publications = PublicationService.getAllPublicationByAdoptionCenter(None, None, None)
    return render_template('home.html',categories = My_categories,topics = My_topics, publications = My_publications, is_adoptioncenter = True)
  
@main.route('/home/adoption_center/filterby=<string:category>', methods = ['GET'])
def homeAdoptionCenterCategory(category):
  My_categories = CategoryService.getAllCategories()
  My_topics = TopicService.getAllTopicByCategory(category)
  My_publications = PublicationService.getAllPublicationByAdoptionCenter(None, None, My_topics)
  return render_template('home.html',categories = My_categories,topics = My_topics, publications = My_publications, is_adoptioncenter = True)

@main.route('/home/adoption_center/filterby=<string:category>/topic=<string:topic>', methods = ['GET'])
def homeAdoptionCenterTopic(category, topic):
  My_categories = CategoryService.getAllCategories()
  My_topics = TopicService.getAllTopics()
  My_publications = PublicationService.getAllPublicationByAdoptionCenter(None, topic, None)
  return render_template('home.html',categories = My_categories,topics = My_topics, publications = My_publications, is_adoptioncenter = True)

@main.route('/home/adoption_center/<string:search>', methods = ['GET'])
def homeAdoptionCenterSearch(search):
  My_categories = CategoryService.getAllCategories()
  My_topics = TopicService.getAllTopics()
  My_publications = PublicationService.getAllPublicationByAdoptionCenter(search, None, None)
  return render_template('home.html',categories = My_categories,topics = My_topics, publications = My_publications, is_adoptioncenter = True)

@main.route('/home/adoption_center/filterby=<string:category>/<string:search>', methods = ['GET'])
def homeAdoptionCenterCategorySearch(category,search):
  My_categories = CategoryService.getAllCategories()
  My_topics = TopicService.getAllTopicByCategory(category)
  My_publications = PublicationService.getAllPublicationByAdoptionCenter(search, None, My_topics)
  return render_template('home.html',categories = My_categories,topics = My_topics, publications = My_publications, is_adoptioncenter = True)

@main.route('/home/adoption_center/filterby=<string:category>/topic=<string:topic>/<string:search>', methods = ['GET'])
def homeAdoptionCenterAllFilter(category,topic,search):
  My_categories = CategoryService.getAllCategories()
  My_topics = TopicService.getAllTopics()
  My_publications = PublicationService.getAllPublicationByAdoptionCenter(search, topic, None)
  return render_template('home.html',categories = My_categories,topics = My_topics, publications = My_publications, is_adoptioncenter = True)

@main.route('/home/community', methods = ['GET', 'POST'])
def homeCommunity():
  print("Si está entrando endpoint homecommunity")
  if request.method == 'POST':
    filter_search = request.form['filter_search'] if request.form['filter_search'] != '' else None
    
  else:
    My_categories = False
    My_topics = False
    My_publications = PublicationService.getAllPublicationByNaturalPerson()
    return render_template('home.html',categories = My_categories,topics = My_topics, publications = My_publications, is_adoptioncenter = False)