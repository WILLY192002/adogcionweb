from flask_login import UserMixin

class NaturalPerson(UserMixin):
    def __init__(self, id, access_id, person_id, photo):
        self.id = id
        self.access_id = access_id
        self.person_id = person_id
        self.photo = photo
