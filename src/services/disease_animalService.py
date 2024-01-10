#Database
from src.database.mysql_db import get_connection

#Model's
from src.models.Disease_Animal import DiseaseAnimal

class Disease_AnimalService():
  @classmethod
  def addNewDisease_Animal(self, animal_id, disease_list):
    try:
      if disease_list:
        conexion = get_connection()
        cursor = conexion.cursor()
        
        sql = f"INSERT INTO disease_animal (disease_id, animal_id) VALUES "
        Values = []
        for disease_id in disease_list:
          Values.append(f"({disease_id},{animal_id})")
        insertions = ', '.join(Values)
        
        sql += insertions+';'
        cursor.execute(sql)
        conexion.commit()
        return "A new animal disease has been successfully added"
      else:
        return True
    except Exception as ex:
      message = f"Error when adding a new animal disease{ex}"
      raise Exception(message)
    finally:
      conexion.close()
