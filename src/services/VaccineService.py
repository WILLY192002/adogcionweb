#Database
from src.database.mysql_db import get_connection

#Model's
from src.models.Vaccine import Vaccine

class VaccineService():
  @classmethod
  def getAllVaccine(self):
    try:
      conexion = get_connection()
      cursor = conexion.cursor()
      sql = f"SELECT * FROM vaccine"
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
      message = f"An error occurred while consulting vaccine {ex}"
      raise Exception(message)
    finally:
      conexion.close()