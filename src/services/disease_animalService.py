#Database
from src.database.mysql_db import get_connection

#Model's
from src.models.Disease_Animal import DiseaseAnimal
from src.models.Disease import Disease

class Disease_AnimalService():
  @classmethod
  def addNewDisease_Animal(self, animal_id, disease_list):
    try:
      
      conexion = get_connection()
      cursor = conexion.cursor()
      if disease_list:
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

  @classmethod
  def deleteDisease_Animal(self, animal_id, disease_list):
    try:
      conexion = get_connection()
      cursor = conexion.cursor()
      if disease_list:
        sql = f"DELETE FROM disease_animal WHERE ( "
        Values = []
        for disease_id in disease_list:
          Values.append(f"disease_id = {disease_id}")
        insertions = ' OR '.join(Values)
        
        sql += insertions+f') AND animal_id = {animal_id};'
        cursor.execute(sql)
        conexion.commit()
        return "A new animal disease has been successfully added"
      else:
        return True
    except Exception as ex:
      message = f"Error when deleting an disease from animal {ex}"
      raise Exception(message)
    finally:
      conexion.close()
  
  @classmethod
  def getDiseaseByAnimalId(self, animal_id):
    try:
      conexion = get_connection()
      cursor = conexion.cursor()
      sql = f"SELECT d.id, d.name, d.description FROM disease_animal da JOIN disease d ON da.disease_id = d.id WHERE da.animal_id = {animal_id}"
      cursor.execute(sql)
      rows = cursor.fetchall()
      out_disease = []
      if rows != None:
        for row in rows:
          out_disease.append(Disease(row[0],row[1],row[2]))
        return out_disease
      else:
        return False
    except Exception as ex:
      message = f"An error occurred while consulting disease by animal id {ex}"
      raise Exception(message)
    finally:
      conexion.close()
