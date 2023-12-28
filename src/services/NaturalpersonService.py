from src.database.mysql_db import get_connection
from src.models.NaturalPerson import NaturalPerson
class NaturalpersonService():
  @classmethod
  def addNewNaturalPerson(self, naturalPerson):
    try:
      conexion = get_connection()
      cursor = conexion.cursor()
      new_naturalPerson = naturalPerson.__dict__
      new_naturalPerson.pop("id")
      new_naturalPerson = {key: value for key, value in new_naturalPerson.items() if value is not None}
      columns = ', '.join(new_naturalPerson.keys())
      values = ', '.join("'" + str(valor) + "'" if isinstance(valor, str) else str(valor) for valor in new_naturalPerson.values())
      sql = f"INSERT INTO naturalperson ({columns}) VALUES ({values})"
      print(sql)
      cursor.execute(sql)
      conexion.commit()
      return "A new natural person has been successfully added"
    except Exception as ex:
      message = f"Error when adding a new natural person {ex}"
      raise Exception(message)
    
  @classmethod
  def getNaturalPersonByAccessId(self, access_id):
    try:
      conexion = get_connection()
      cursor = conexion.cursor()
      sql = f"SELECT * FROM naturalperson WHERE access_id = {access_id}"
      cursor.execute(sql)
      row = cursor.fetchone()
      if row != None:
        return NaturalPerson(row[0],row[1],row[2],None)
      else:
        return False
    except Exception as ex:
      message = f"An error occurred while consulting an NaturalPerson by Access {ex}"
      raise Exception(message)