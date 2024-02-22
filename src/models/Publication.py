class Publication:
    def __init__(self, id, topic_id, access_id, photo, title, description, date, status, photo_owner = None,name_owner = None, id_owner = None):
        self.id = id
        self.topic_id = topic_id
        self.access_id = access_id
        self.photo = photo
        self.title = title
        self.description = description
        self.date = date
        self.status = status
        self.photo_owner = photo_owner
        self.name_owner = name_owner
        self.id_owner = id_owner
