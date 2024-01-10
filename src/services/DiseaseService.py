#Database
from src.database.mysql_db import get_connection

#Model's
from src.models.Disease import Disease

class DiseaseService():
  @classmethod
  def getAllDiseases(self):
    try:
      conexion = get_connection()
      cursor = conexion.cursor()
      sql = f"SELECT * FROM disease"
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
      message = f"An error occurred while consulting disease {ex}"
      raise Exception(message)
    finally:
      conexion.close()