from src.database.mysql_db import get_connection
from src.models.Animal import Animal
class AnimalService():
  @classmethod
  def addNewAnimal(self, animal):
    try:
      conexion = get_connection()
      cursor = conexion.cursor()
      new_Animal = animal.__dict__
      new_Animal.pop("id")
      new_Animal = {key: value for key, value in new_Animal.items() if value is not None}
      columns = ', '.join(new_Animal.keys())
      values = ', '.join("'" + str(valor) + "'" if isinstance(valor, str) else str(valor) for valor in new_Animal.values())
      sql = f"INSERT INTO animal ({columns}) VALUES ({values})"
      cursor.execute(sql)
      conexion.commit()
      return "A new animal has been successfully added to adoption center"
    except Exception as ex:
      message = f"Error when adding a new animal to adoption center {ex}"
      raise Exception(message)
  
  @classmethod
  def getNoAdoptedAnimals(self, adoptioncenter_id):
    try:
      conexion = get_connection()
      cursor = conexion.cursor()
      sql = f"""SELECT animal.*, breed.name, species.name FROM animal 
      JOIN breed ON breed.id = animal.breed_id 
      JOIN species ON breed.species_id = species.id  
      WHERE is_adopted = false AND adoptioncenter_id = {adoptioncenter_id}"""
      cursor.execute(sql)
      rows = cursor.fetchall()
      out_animals = []
      if rows != None:
        for row in rows:
          out_animals.append(Animal(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10], row[11], row[12]))
        return out_animals
      else:
        return False
    except Exception as ex:
      message = f"An error occurred while consulting a No adopted Animals by adoption center {ex}"
      raise Exception(message)
  
  @classmethod
  def getNoAdoptedAnimalsFilter(self, adoptioncenter_id, filter_search, filter_specie, filter_Sex, filter_size, filter_age):
    try:
      conexion = get_connection()
      cursor = conexion.cursor()
      sql = f"""SELECT animal.*, breed.name, species.name FROM animal 
      JOIN breed ON breed.id = animal.breed_id 
      JOIN species ON breed.species_id = species.id  
      WHERE is_adopted = false AND adoptioncenter_id = {adoptioncenter_id}"""

      if filter_search != None:
        sql += f" AND (animal.name LIKE '{filter_search}')"
      if filter_specie != None:
        sql += f" AND species.id = '{filter_specie}'"
      if filter_Sex != None:
        sql += f" AND animal.sex = '{filter_Sex}'"
      if filter_size != None:
        sql += f" AND animal.size = '{filter_size}'"
      if filter_age != None:
        if filter_age == "1":
            sql += " AND animal.age BETWEEN 0 AND 3"
        elif filter_age == "2":
            sql += " AND animal.age BETWEEN 4 AND 7"
        elif filter_age == "3":
            sql += " AND animal.age BETWEEN 8 AND 11"
        elif filter_age == "4":
            sql += " AND animal.age BETWEEN 12 AND 15"
        elif filter_age == "5":
            sql += " AND animal.age > 16"
      sql += " ORDER BY id ASC"
      print(sql)
      cursor.execute(sql)
      rows = cursor.fetchall()
      out_animals = []
      if rows != None:
        for row in rows:
          out_animals.append(Animal(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12]))
        return out_animals
      else:
        return False
    except Exception as ex:
      message = f"An error occurred while consulting a No adopted Animals by adoption center and filters {ex}"
      raise Exception(message)

  @classmethod
  def getAdoptedAnimals(self, adoptioncenter_id):
    try:
      conexion = get_connection()
      cursor = conexion.cursor()
      sql = f"SELECT * FROM animal WHERE is_adopted = true AND adoptioncenter_id = {adoptioncenter_id}"
      cursor.execute(sql)
      rows = cursor.fetchall()
      out_animals = []
      if rows != None:
        for row in rows:
          out_animals.append(Animal(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10]))
        return out_animals
      else:
        return False
    except Exception as ex:
      message = f"An error occurred while consulting an adopted Animals by adoption center {ex}"
      raise Exception(message)
    
  @classmethod
  def updateAnimalInformation(self,animal):
    try:
      conexion = get_connection()
      cursor = conexion.cursor()
      id = animal.id
      new_Animal = animal.__dict__
      new_Animal.pop("id")
      new_Animal = {key: value for key, value in new_Animal.items() if value is not None}
      fields = []
      for key, value in new_Animal.items():
          if isinstance(value, str):
              fields.append(f'{key} = "{value}"')
          else:
              fields.append(f'{key} = {value}')
      fieldsUpdate = ', '.join(fields)
      sql = f"UPDATE animal SET {fieldsUpdate} WHERE id = {id}"
      cursor.execute(sql)
      conexion.commit()
      return "An update in animal has been successfully"
    except Exception as ex:
      message = f"Error when update an animal {ex}"
      raise Exception(message)