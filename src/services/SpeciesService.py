from src.database.mysql_db import get_connection
from src.models.Species import Species

class SpeciesService():
  @classmethod
  def getAllSpecies(self):
    try:
      conexion = get_connection()
      cursor = conexion.cursor()
      sql = f"SELECT * FROM species"
      cursor.execute(sql)
      rows = cursor.fetchall()
      out_species = []
      if rows != None:
        for row in rows:
          out_species.append(Species(row[0],row[1]))
        return out_species
      else:
        return False
    except Exception as ex:
      message = f"An error occurred while consulting species {ex}"
      raise Exception(message)