from flask_login import UserMixin

class AdoptionCenter(UserMixin):
    def __init__(self, id, person_id, access_id, photo, name, description, nit, contact, address, googlemaps, city, department, user_type_id = None,user_type_name = None, email = None):
        self.id = id
        self.person_id = person_id
        self.access_id = access_id
        self.photo = photo
        self.name = name
        self.description = description
        self.nit = nit
        self.contact = contact
        self.address = address
        self.googlemaps = googlemaps
        self.city = city
        self.department = department
        self.user_type_id = user_type_id
        self.user_type_name = user_type_name
        self.email = email
