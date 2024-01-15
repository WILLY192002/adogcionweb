from flask_login import UserMixin

class NaturalPerson(UserMixin):
    def __init__(self, id, access_id, person_id, photo, name,user_type_id = None,user_type_name = None, email = None):
        self.id = id
        self.access_id = access_id
        self.person_id = person_id
        self.photo = photo
        self.name = name
        self.user_type_id = user_type_id
        self.user_type_name = user_type_name
        self.email = email
