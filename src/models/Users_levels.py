class Users_levels:
    def __init__(self, id, naturalperson_id, level_id, date_achieved, status, levelname = None):
        self.id = id
        self.naturalperson_id = naturalperson_id
        self.level_id = level_id
        self.date_achieved = date_achieved
        self.status = status
        self.levelname = levelname