#Database
from src.database.mysql_db import get_connection

#Model's
from src.models.Vaccine_Animal import VaccineAnimal
from src.models.Vaccine import Vaccine

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

  @classmethod
  def deleteVaccine_Animal(self, animal_id, vaccine_list):
    try:
      conexion = get_connection()
      cursor = conexion.cursor()
      if vaccine_list:
        sql = f"DELETE FROM vaccine_animal WHERE ( "
        Values = []
        for vaccine_id in vaccine_list:
          Values.append(f"vaccine_id = {vaccine_id}")
        insertions = ' OR '.join(Values)
        
        sql += insertions+f') AND animal_id = {animal_id};'
        cursor.execute(sql)
        conexion.commit()
        return "A new animal vaccine has been successfully added"
      else:
        return True
    except Exception as ex:
      message = f"Error when deleting an vaccine from animal {ex}"
      raise Exception(message)
    finally:
      conexion.close()

  @classmethod
  def getVaccineByAnimalId(self, animal_id):
    try:
      conexion = get_connection()
      cursor = conexion.cursor()
      sql = f"SELECT v.id, v.name, v.description FROM vaccine_animal va JOIN vaccine v ON va.vaccine_id = v.id WHERE va.animal_id = {animal_id}"
      cursor.execute(sql)
      rows = cursor.fetchall()
      out_vaccine = []
      if rows != None:
        for row in rows:
          out_vaccine.append(Vaccine(row[0],row[1],row[2]))
        return out_vaccine
      else:
        return False
    except Exception as ex:
      message = f"An error occurred while consulting operation by animal id {ex}"
      raise Exception(message)
    finally:
      conexion.close()

