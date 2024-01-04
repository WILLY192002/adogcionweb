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
from src.services.PaymentoptionService import PaymentoptionService

#models
from src.models.Adoptioncenter import AdoptionCenter
from src.models.Paymentoption_Adoptioncenter import PaymentOptionAdoptionCenter

main = Blueprint('view_profile_adoption_center',__name__)

@main.route('/view/profile=<id>/adoption_center=<name>', methods = ['GET', 'POST'])
def viewProfileAdoptionCenter(id,name):
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


@main.route('/edit_information/profile=<id>/adoption_center=<name>', methods = ['GET', 'POST'])
def editProfileAdoptionCenter(id, name):
  if request.method == 'POST':
      #Adoption Center information
      adoption_center_name = request.form['name'].capitalize() if request.form['name'] != '' else None
      adoption_center_description = request.form['description'].capitalize() if request.form['description'] != '' else None
      adoption_center_department = request.form['department'].capitalize() if request.form['department'] != '' else None
      adoption_center_city = request.form['city'].capitalize() if request.form['city'] != '' else None
      adoption_center_contact = request.form['contact'] if request.form['contact'] != '' else None

      photo = request.form['hiddenField']
      upload_photo = ImageService.upload_image_to_imgbb(photo)
      adoption_center_photo = upload_photo['data']['url'] if photo != '' else None

      checkAddress = request.form.get('checkAddress')
      check_generate_link = request.form.get('check-generate-link')
      adoption_center_address = None
      adoption_center_googlemaps = None

      #Address information
      if checkAddress == '1':
        type_via = request.form.get('tipo-via')
        number_via = request.form['number-via']
        complement_via = request.form['complement-via']
        start_block = request.form['start-block']
        end_block = request.form['end-block']
        adoption_center_address = type_via +" "+ number_via
        if complement_via != '':
          adoption_center_address += " "+complement_via
        if start_block != '' and end_block != '':
          adoption_center_address += " # "+start_block+"-"+end_block
      
      if check_generate_link == '1':
        adoption_center_googlemaps = request.form['input_link_alternativo']
        if adoption_center_googlemaps == '':
          adoption_center_googlemaps = request.form['input_link_ubicacion']
      
      #UPDATE adoption center information
      update_adoption_center = AdoptionCenter(None, None, None, adoption_center_photo,adoption_center_name,
                                              adoption_center_description,None,adoption_center_contact,
                                              adoption_center_address,adoption_center_googlemaps,
                                              adoption_center_city,adoption_center_department,None, None, None)
      AdoptioncenterService.updateAdoptionCenter(current_user.get_id(),update_adoption_center)
      
      #Payment options information 
      paymentOptions_registered_selected = request.form.getlist('paymentOptions_registered_id')
      number_paymentOptions_registered_selected = request.form.getlist('paymentOptions_registered_number')

      paymentOptions_Noregistered_selected = request.form.getlist('paymentOptions_NoRegistered_id')
      number_paymentOptions_Noregistered_selected = request.form.getlist('paymentOptions_NoRegistered_number')

      #SEPARAR LOS MEDIOS DE PAGO QUE SERÁN ELIMINADOS DE LOS QUE SERÁN ACTUALIZADOS / INSERTADOS
      Insert_paymentOption = []
      Delete_paymentOption = []
      Update_paymentOption = []
      
      for i in range(len(paymentOptions_registered_selected)):
        if number_paymentOptions_registered_selected[i] == '':
          # Delete_paymentOption.append(Alb_MedPago(0,current_user.get_id(),paymentOptions_registered_selected[i],"",""))
          # Paymentoption_AdoptioncenterService.eliminarMedioPagoAlb(db,current_user.get_id(),paymentOptions_registered_selected[i])
          Paymentoption_AdoptioncenterService.deletePaymentOptionAdoptionCenter(current_user.get_id(),int(paymentOptions_registered_selected[i]))
        else:
          # Update_paymentOption.append(Alb_MedPago(0,current_user.get_id(),paymentOptions_registered_selected[i],number_paymentOptions_registered_selected[i],""))
          # Paymentoption_AdoptioncenterService.actualizarMedPagosAlb(db,current_user.get_id(),paymentOptions_registered_selected[i],number_paymentOptions_registered_selected[i])
          Paymentoption_AdoptioncenterService.updatePaymentOptionAdoptionCenter(current_user.get_id(),int(paymentOptions_registered_selected[i]),number_paymentOptions_registered_selected[i])

      for i in range(len(paymentOptions_Noregistered_selected)):
        # Insert_paymentOption.append(Alb_MedPago(0,current_user.get_id(),paymentOptions_Noregistered_selected[i],number_paymentOptions_Noregistered_selected[i],""))
        new_PaymentOptionAdoptionCenter = PaymentOptionAdoptionCenter(None, int(paymentOptions_Noregistered_selected[i]),int(current_user.get_id()),number_paymentOptions_Noregistered_selected[i])
        # Paymentoption_AdoptioncenterService.insertarMedPagosAlb(db,current_user.get_id(),paymentOptions_Noregistered_selected[i],number_paymentOptions_Noregistered_selected[i])
        Paymentoption_AdoptioncenterService.insertPaymentOptionAdoptionCenter(new_PaymentOptionAdoptionCenter)
      
      return redirect(url_for('view_profile_adoption_center.viewProfileAdoptionCenter', name = current_user.name, id = current_user.get_id()))
  else:
    user_information = AdoptioncenterService.getAdoptionCenterById(current_user.get_id())
    access_user_information = AccessService.getAccessById(user_information.access_id)
    user_information.user_type_id = access_user_information.user_type_id
    user_information.email = access_user_information.email

    paymentOptions_registered = Paymentoption_AdoptioncenterService.getPaymentOptionAdoptionCenter(current_user.get_id())
    paymentOptions_NoRegistered = PaymentoptionService.getNoPaymentOptionAdoptionCenter(current_user.get_id())
    
    return render_template('User_Adoption_Center/post/edit_profile.html', 
                          user_information = user_information,
                          paymentOptions_registered = paymentOptions_registered,
                          paymentOptions_NoRegistered = paymentOptions_NoRegistered)