class Animal:
    def __init__(self, id, adoptioncenter_id, photo, name, breed_id, sex, age, size, weight, diet, is_adopted, breed_name = None, species_name = None):
        self.id = id
        self.adoptioncenter_id = adoptioncenter_id
        self.photo = photo
        self.name = name
        self.breed_id = breed_id
        self.sex = sex
        self.age = age
        self.size = size
        self.weight = weight
        self.diet = diet
        self.is_adopted = is_adopted
        self.breed_name = breed_name
        self.species_name = species_name
