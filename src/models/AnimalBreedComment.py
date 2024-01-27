class AnimalBreedComment():
  def __init__(self,id, access_id, breed_id, description, date, is_active, owner_name = None, owner_photo = None):
    self.id = id
    self.access_id = access_id
    self.breed_id = breed_id
    self.description = description
    self.date = date
    self.is_active = is_active
    self.owner_name = owner_name
    self.owner_photo = owner_photo