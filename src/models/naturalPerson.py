from flask_login import UserMixin

class NaturalPerson(UserMixin):
    def __init__(self, id, access_id, person_id, photo, user_type_id = None,user_type_name = None):
        self.id = id
        self.access_id = access_id
        self.person_id = person_id
        self.photo = photo
        self.user_type_id = user_type_id
        self.user_type_name = user_type_name