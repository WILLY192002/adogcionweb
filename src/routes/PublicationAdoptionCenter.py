from flask import Blueprint, render_template,request,flash,redirect, url_for
from flask_login import current_user
from flask import jsonify

from src.services.UsertypeService import UsertypeService
from src.services.TopicService import TopicService
from src.services.ImageService import ImageService
from src.services.paymentoption_adoptioncenterService import Paymentoption_AdoptioncenterService
from src.services.PublicationService import PublicationService

from src.models.Publication import Publication

main = Blueprint('publication_adoption_center',__name__)

@main.route('/publication_adoption_center', methods = ['GET', 'POST'])
def publicationAdoptionCenter():
  if request.method == 'POST':
      photo = request.form['urlImage'] if request.form['urlImage'] != '' else None
      upload_photo = ImageService.upload_image_to_imgbb(photo)
      publication_photo = upload_photo['data']['url'] if photo else None

      publication_topic = request.form.get('publication_topic')
      publication_title = request.form['publication_title'].capitalize() if request.form['publication_title'] != '' else None  
      publication_description = request.form['publication_description'].capitalize() if request.form['publication_description'] != '' else None 
      add_payment_options = request.form.get('payments_option')


      if add_payment_options != None:
        payments_option = Paymentoption_AdoptioncenterService.getPaymentOptionAdoptionCenter(current_user.get_id())
        publication_description += ("\n\nNos puedes ayudar mediante: ")
        for payment_option in payments_option:
          publication_description += ("\n*. "+payment_option.name_paymentoption+": "+payment_option.number_payment)
      
      new_publication = Publication(None,publication_topic,current_user.access_id,publication_photo,
                                    publication_title,publication_description,None,True)
      PublicationService.addNewPublication(new_publication)
      return redirect(url_for('view_profile_adoption_center.viewProfileAdoptionCenter', name = current_user.name, id = current_user.get_id()))
  else:
    if current_user.is_authenticated and UsertypeService.verifyUserTypeAdoptionCenter(current_user.user_type_id):
      topics = TopicService.getAllTopics()
      visible = True
      return render_template('publication.html', topics=topics, visible = visible)
    else:
      return render_template('auth/no_authorized.html')


@main.route('/delete_publication', methods = ['POST'])
def deletePublication():
  post_id = request.form.get('id')
  return PublicationService.deletePublication(post_id)

@main.route('/report_publication', methods = ['POST'])
def reportPublication():
  post_id = request.form.get('id')
  return PublicationService.reportPublication(post_id)

@main.route('/adoption_center/publication/edit=<string:publication_id>', methods = ['GET','POST'])
def editPublication(publication_id):
  if request.method == 'POST':
    photo = request.form['urlImage'] if request.form['urlImage'] != '' else None
    upload_photo = ImageService.upload_image_to_imgbb(photo)
    publication_photo = upload_photo['data']['url'] if photo else None

    publication_topic = request.form.get('publication_topic')
    publication_title = request.form['publication_title'].capitalize() if request.form['publication_title'] != '' else None  
    publication_description = request.form['publication_description'].capitalize() if request.form['publication_description'] != '' else None 
  
    new_publication = Publication(None,publication_topic,current_user.access_id,publication_photo,
                                  publication_title,publication_description,None,True)
    PublicationService.updatePublication(publication_id,new_publication)
    return redirect(url_for('view_profile_adoption_center.viewProfileAdoptionCenter', name = current_user.name, id = current_user.get_id()))
  else:
    if current_user.is_authenticated and UsertypeService.verifyUserTypeAdoptionCenter(current_user.user_type_id):
      topics = TopicService.getAllTopics()
      publication = PublicationService.getPublicationByid(publication_id)
      visible = True
      if publication.access_id == current_user.access_id:
        return render_template('edit_publication.html', topics=topics, visible = visible, publication = publication)
      else:
        return redirect(url_for('view_profile_adoption_center.viewProfileAdoptionCenter', id = current_user.id, name = current_user.name))
    else:
      return render_template('auth/no_authorized.html')