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
from src.services.TopicService import TopicService
from src.services.AnimalService import AnimalService 
from src.services.SpeciesService import SpeciesService 

#models
from src.models.Adoptioncenter import AdoptionCenter
from src.models.Paymentoption_Adoptioncenter import PaymentOptionAdoptionCenter
from src.models.Publication import Publication

main = Blueprint('view_profile_adoption_center',__name__)

@main.route('/view/profile=<id>/adoption_center/<name>', methods = ['GET', 'POST'])
def viewProfileAdoptionCenter(id,name):
  if request.method == 'POST':
    if current_user.is_authenticated and current_user.get_id() == id:
      adoption_center_name = request.form['name'].capitalize() if request.form['name'] != '' else None
      adoption_center_description = request.form['description'].capitalize() if request.form['description'] != '' else None
      adoption_center_department = request.form['department'].capitalize() if request.form['department'] != '' else None
      adoption_center_city = request.form['city'].capitalize() if request.form['city'] != '' else None
      adoption_center_contact = request.form['contact'] if request.form['contact'] != '' else None
      
      photo = request.form['hiddenField'] if request.form['hiddenField'] != '' else None
      upload_photo = ImageService.upload_image_to_imgbb(photo)
      adoption_center_photo = upload_photo['data']['url'] if photo else None

      #Model adoption center with update fields
      update_adoption_center = AdoptionCenter(None, None, None, adoption_center_photo,adoption_center_name,
                                              adoption_center_description,None,adoption_center_contact,
                                              None,None,adoption_center_city,adoption_center_department,None, None, None)
      AdoptioncenterService.updateAdoptionCenter(current_user.get_id(),update_adoption_center)
      return redirect(url_for('view_profile_adoption_center.viewProfileAdoptionCenter', name = current_user.name, id = current_user.get_id()))
    else:
      return render_template('auth/no_authorized.html')
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

@main.route('/view/profile=<id>/adoption_center/<name>/adopt_animals', methods = ['GET', 'POST'])
def viewProfileAdoptAnimals(id,name):
  #INFORMATION PROFILE
  user_information = AdoptioncenterService.getAdoptionCenterById(id)
  access_user_information = AccessService.getAccessById(user_information.access_id)
  user_information.user_type_id = access_user_information.user_type_id
  user_information.email = access_user_information.email
  topic_adopted_id = 0

  categories = CategoryService.getAllCategories()
  species = SpeciesService.getAllSpecies()
  topics = False
  actuallySeccion = "Adoptar"
  PaymentOptions = Paymentoption_AdoptioncenterService.getPaymentOptionAdoptionCenter(id)

  if request.method == 'POST':
    filter_search = request.form.get('filter_search') if request.form.get('filter_search') != '' else None
    filter_specie = request.form.get('filter_specie') if request.form.get('filter_specie') != '' else None
    filter_sex = request.form.get('filter_sex') if request.form.get('filter_sex') != '' else None
    filter_size = request.form.get('filter_size') if request.form.get('filter_size') != '' else None
    filter_age = request.form.get('filter_age') if request.form.get('filter_age') != '' else None
    print(filter_search,"--",filter_specie,"--",filter_sex,"--",filter_size,"--",filter_age,"--",)

    No_adopted_animals = AnimalService.getNoAdoptedAnimalsFilter(user_information.id,filter_search,filter_specie,filter_sex,filter_size,filter_age)
    publications = []
    for animal in No_adopted_animals:
      description = "*.Raza: "+animal.breed_name+"\n"+"*.Edad: "+str(animal.age)+"\n"+"*.Tamaño: "+animal.size+"\n"
      publications.append(Publication(None,topic_adopted_id, user_information.access_id, animal.photo, animal.name, description,None,True))

    return render_template('User_Adoption_Center/profile_adoption_center.html',
                            user_information=user_information, 
                            publications = publications, 
                            categories = categories, 
                            species = species,
                            topics = topics, 
                            actuallySeccion = actuallySeccion, 
                            PaymentOptions = PaymentOptions, 
                            topic_adopted_id = topic_adopted_id)
    
  else: 
    #PUBLICATIONS, CATEGORIES, ACTUALLY SECCION
    No_adopted_animals = AnimalService.getNoAdoptedAnimals(id)
    print("Tamaño: ", len(No_adopted_animals))
    publications = []
    for animal in No_adopted_animals:
      description = "*.Raza: "+animal.breed_name+"\n"+"*.Edad: "+str(animal.age)+"\n"+"*.Tamaño: "+animal.size+"\n"
      publications.append(Publication(None,topic_adopted_id, user_information.access_id, animal.photo, animal.name, description,None,True))
    
    return render_template('User_Adoption_Center/profile_adoption_center.html',
                            user_information=user_information, 
                            publications = publications, 
                            categories = categories, 
                            species = species,
                            topics = topics, 
                            actuallySeccion = actuallySeccion, 
                            PaymentOptions = PaymentOptions, 
                            topic_adopted_id = topic_adopted_id)

@main.route('/view/profile=<id>/adoption_center/<name>/filterby=<string:category>', methods = ['GET', 'POST'])
def viewProfileAdoptionCenterByCategory(id, name, category):
  if request.method == 'POST':
    filter_topic = request.form.get('filter_topic') if request.form.get('filter_topic') != None else False
    if filter_topic:
      return redirect(url_for('view_profile_adoption_center.viewProfileAdoptionCenterByTopic', id = id , name = name, category = category, topic = filter_topic))
    else:
      return redirect(request.referrer)
  else:
    #INFORMATION PROFILE
    user_information = AdoptioncenterService.getAdoptionCenterById(id)
    access_user_information = AccessService.getAccessById(user_information.access_id)
    user_information.user_type_id = access_user_information.user_type_id
    user_information.email = access_user_information.email

    #PUBLICATIONS, CATEGORIES, ACTUALLY SECCION
    publications = PublicationService.getAllPublicationByCategoryId(category,user_information.access_id)
    categories = CategoryService.getAllCategories()
    topics = TopicService.getAllTopicByCategory(category)
    actuallySeccion = category
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

@main.route('/view/profile=<id>/adoption_center/<name>/filterby=<string:category>/topic=<string:topic>', methods = ['GET'])
def viewProfileAdoptionCenterByTopic(id, name, category,topic):
  #INFORMATION PROFILE
  user_information = AdoptioncenterService.getAdoptionCenterById(id)
  access_user_information = AccessService.getAccessById(user_information.access_id)
  user_information.user_type_id = access_user_information.user_type_id
  user_information.email = access_user_information.email

  #PUBLICATIONS, CATEGORIES, ACTUALLY SECCION
  publications = PublicationService.getAllPublicationByTopic(user_information.access_id,topic)
  categories = CategoryService.getAllCategories()
  topics = TopicService.getAllTopicByCategory(category)
  actuallySeccion = category
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

@main.route('/edit_information/profile=<id>/adoption_center/<name>', methods = ['GET', 'POST'])
def editProfileAdoptionCenter(id, name):
  if request.method == 'POST':
    if current_user.is_authenticated and current_user.get_id() == id: 
      #Adoption Center information
      adoption_center_name = request.form['name'].capitalize() if request.form['name'] != '' else None
      adoption_center_description = request.form['description'].capitalize() if request.form['description'] != '' else None
      adoption_center_department = request.form['department'].capitalize() if request.form['department'] != '' else None
      adoption_center_city = request.form['city'].capitalize() if request.form['city'] != '' else None
      adoption_center_contact = request.form['contact'] if request.form['contact'] != '' else None

      photo = request.form['hiddenField'] if request.form['hiddenField'] != '' else None
      upload_photo = ImageService.upload_image_to_imgbb(photo)
      adoption_center_photo = upload_photo['data']['url'] if photo else None

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
      for i in range(len(paymentOptions_registered_selected)):
        if number_paymentOptions_registered_selected[i] == '':
          Paymentoption_AdoptioncenterService.deletePaymentOptionAdoptionCenter(current_user.get_id(),int(paymentOptions_registered_selected[i]))
        else:
          Paymentoption_AdoptioncenterService.updatePaymentOptionAdoptionCenter(current_user.get_id(),int(paymentOptions_registered_selected[i]),number_paymentOptions_registered_selected[i])

      for i in range(len(paymentOptions_Noregistered_selected)):
        new_PaymentOptionAdoptionCenter = PaymentOptionAdoptionCenter(None, int(paymentOptions_Noregistered_selected[i]),int(current_user.get_id()),number_paymentOptions_Noregistered_selected[i])
        Paymentoption_AdoptioncenterService.insertPaymentOptionAdoptionCenter(new_PaymentOptionAdoptionCenter)
      
      return redirect(url_for('view_profile_adoption_center.viewProfileAdoptionCenter', name = current_user.name, id = current_user.get_id()))
    else:
      return render_template('auth/no_authorized.html')
  else:
    if current_user.is_authenticated and current_user.get_id() == id:
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
    else:
      return render_template('auth/no_authorized.html')





# form_id = request.form['form_id']
#     if form_id == 'filter_adoption_seccion':
#       barraFilter = request.form['filter_search']
#       especieFilter = request.form['filter_specie']
#       sexoFilter = request.form['filter_sex']
#       tamanioFilter = request.form['filter_size']
#       edadFilter = request.form['filter_age']
      
#       return 'xd'