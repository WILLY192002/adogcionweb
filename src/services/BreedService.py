from src.database.mysql_db import get_connection
from src.models.Breed import Breed

class BreedService():
  @classmethod
  def getAllBreeds(self):
    try:
      conexion = get_connection()
      cursor = conexion.cursor()
      sql = f"SELECT id, name, species_id FROM breed"
      cursor.execute(sql)
      rows = cursor.fetchall()
      out_breeds = []
      if rows != None:
        for row in rows:
          out_breeds.append(Breed(row[0],row[1],row[2]))
        return out_breeds
      else:
        return False
    except Exception as ex:
      message = f"An error occurred while consulting breeds {ex}"
      raise Exception(message)
    finally:
      conexion.close()
  
  @classmethod
  def getBreedsBySpecie(self, species_id):
    try:
      conexion = get_connection()
      cursor = conexion.cursor()
      sql = f"SELECT id, name, species_id FROM breed WHERE species_id = {species_id}"
      cursor.execute(sql)
      rows = cursor.fetchall()
      out_breeds = []
      if rows != None:
        for row in rows:
          out_breeds.append(Breed(row[0],row[1],row[2]))
        return out_breeds
      else:
        return False
    except Exception as ex:
      message = f"An error occurred while consulting breeds by species {ex}"
      raise Exception(message)
    finally:
      conexion.close()