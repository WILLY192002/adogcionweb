#Database
from src.database.mysql_db import get_connection

#Model's
from src.models.Vaccine_Animal import VaccineAnimal

class Vaccine_AnimalService():
  @classmethod
  def addNewVaccine_Animal(self, animal_id, vaccine_list):
    try:
      
      conexion = get_connection()
      cursor = conexion.cursor()
      if vaccine_list:
        sql = f"INSERT INTO vaccine_animal (vaccine_id, animal_id) VALUES "
        Values = []
        for vaccine_id in vaccine_list:
          Values.append(f"({vaccine_id},{animal_id})")
        insertions = ', '.join(Values)
        
        sql += insertions+';'
        cursor.execute(sql)
        conexion.commit()
        return "A new animal vaccine has been successfully added"
      else:
        return True
    except Exception as ex:
      message = f"Error when adding a new animal vaccine {ex}"
      raise Exception(message)
    finally:
      conexion.close()
