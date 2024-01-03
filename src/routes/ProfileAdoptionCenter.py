#libraries
from flask import Blueprint, render_template,request,flash,redirect, url_for
from flask_login import current_user

#services
from src.services.AdoptioncenterService import AdoptioncenterService
from src.services.CategoryService import CategoryService
from src.services.PublicationService import PublicationService
from src.services.paymentoption_adoptioncenterService import Paymentoption_AdoptioncenterService
from src.services.AccessService import AccessService
from src.services.ImageService import ImageService

#models
from src.models.Adoptioncenter import AdoptionCenter

main = Blueprint('view_profile_adoption_center',__name__)

@main.route('/view/profile=<id>/adoption_center=<name>', methods = ['GET', 'POST'])
def viewProfileAdoptionCenter(name, id):
  if request.method == 'POST':
    if current_user.is_authenticated:
      adoption_center_name = request.form['name'].capitalize() if request.form['name'] != '' else None
      adoption_center_description = request.form['description'].capitalize() if request.form['description'] != '' else None
      adoption_center_department = request.form['department'].capitalize() if request.form['department'] != '' else None
      adoption_center_city = request.form['city'].capitalize() if request.form['city'] != '' else None
      adoption_center_contact = request.form['contact'] if request.form['contact'] != '' else None
      
      photo = request.form['hiddenField']
      upload_photo = ImageService.upload_image_to_imgbb(photo)
      adoption_center_photo = upload_photo['data']['url'] if photo != '' else None

      #Model adoption center with update fields
      update_adoption_center = AdoptionCenter(None, None, None, adoption_center_photo,adoption_center_name,
                                              adoption_center_description,None,adoption_center_contact,
                                              None,None,adoption_center_city,adoption_center_department,None, None, None)
      AdoptioncenterService.updateAdoptionCenter(current_user.get_id(),update_adoption_center)
      return redirect(url_for('view_profile_adoption_center.viewProfileAdoptionCenter', name = current_user.name, id = current_user.get_id()))
    else:
      return redirect(url_for('view_profile_adoption_center.viewProfileAdoptionCenter', name = name, id = id))
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