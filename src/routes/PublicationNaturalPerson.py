from flask import Blueprint, render_template,request,flash,redirect, url_for
from flask_login import current_user

from src.services.UsertypeService import UsertypeService
from src.services.TopicService import TopicService
from src.services.ImageService import ImageService
from src.services.paymentoption_adoptioncenterService import Paymentoption_AdoptioncenterService
from src.services.PublicationService import PublicationService

from src.models.Publication import Publication

main = Blueprint('publication_natural_person',__name__)

@main.route('/publication_natural_person', methods = ['GET', 'POST'])
def publicationNaturalPerson():
  if request.method == 'POST':
      photo = request.form['urlImage'] if request.form['urlImage'] != '' else None
      upload_photo = ImageService.upload_image_to_imgbb(photo)
      
      publication_photo = upload_photo['data']['url'] if photo else None
      publication_title = request.form['publication_title'].capitalize() if request.form['publication_title'] != '' else None  
      publication_description = request.form['publication_description'].capitalize() if request.form['publication_description'] != '' else None 
      
      new_publication = Publication(None,None,current_user.access_id,publication_photo,
                                    publication_title,publication_description,None,True)
      PublicationService.addNewPublication(new_publication)
      return redirect(url_for('view_profile_natural_person.viewProfileNaturalPerson', name = current_user.name, id = current_user.get_id()))
  else:
    if current_user.is_authenticated and UsertypeService.verifyUserTypeNatrualPerson(current_user.user_type_id):
      topics = False
      visible = False
      return render_template('publication.html', topics=topics, visible = visible)
    else:
      return render_template('auth/no_authorized.html')