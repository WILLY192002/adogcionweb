from flask_login import UserMixin
class Access(UserMixin):
    def __init__(self, id, email, password, user_type_id, is_activate):
        self.id = id
        self.email = email
        self.password = password
        self.user_type_id = user_type_id
        self.is_activate = is_activate
