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
      cursor.execute(sql)
      conexion.commit()
      return "A new natural person has been successfully added"
    except Exception as ex:
      message = f"Error when adding a new natural person {ex}"
      raise Exception(message)
    finally:
      conexion.close()
    
  @classmethod
  def getNaturalPersonByAccessId(self, access_id):
    try:
      conexion = get_connection()
      cursor = conexion.cursor()
      sql = f"SELECT id, person_id, access_id, photo, name, description FROM naturalperson WHERE access_id = {access_id}"
      cursor.execute(sql)
      row = cursor.fetchone()
      if row != None:
        return NaturalPerson(row[0],row[1],row[2],row[3],row[4], row[5])
      else:
        return False
    except Exception as ex:
      message = f"An error occurred while consulting an NaturalPerson by Access {ex}"
      raise Exception(message)
    finally:
      conexion.close()
  
  @classmethod
  def getNaturalPersonById(self, id):
    try:
      conexion = get_connection()
      cursor = conexion.cursor()
      sql = f"SELECT id, person_id, access_id, photo, name, description FROM naturalperson WHERE id = {id}"
      cursor.execute(sql)
      row = cursor.fetchone()
      if row != None:
        return NaturalPerson(row[0],row[1],row[2],row[3],row[4], row[5])
      else:
        return False
    except Exception as ex:
      message = f"An error occurred while consulting a Natural person by id {ex}"
      raise Exception(message)
    finally:
      conexion.close()

  @classmethod
  def updateNaturalPerson(self, id, naturalPerson):
    try:
      conexion = get_connection()
      cursor = conexion.cursor()
      new_naturalPerson = naturalPerson.__dict__
      new_naturalPerson.pop("id")
      new_naturalPerson = {key: value for key, value in new_naturalPerson.items() if value is not None}
      fields = []
      for key, value in new_naturalPerson.items():
          if value == '':
            fields.append(f'{key} = NULL')
          elif isinstance(value, str):
            fields.append(f'{key} = "{value}"')
          else:
            fields.append(f'{key} = {value}')
      fieldsUpdate = ', '.join(fields)
      sql = f"UPDATE naturalperson SET {fieldsUpdate} WHERE id = {id}"
      cursor.execute(sql)
      conexion.commit()
      return "An update in natural person has been successfully"
    except Exception as ex:
      message = f"Error when update a natural person {ex}"
      raise Exception(message)
    finally:
      conexion.close()

  @classmethod
  def getUserScore(self, naturalperson_id):
      try:
          conexion = get_connection()
          cursor = conexion.cursor()
          sql = f"SELECT score FROM naturalperson WHERE id = {naturalperson_id}"
          cursor.execute(sql)
          row = cursor.fetchone()
          if row != None:
              # Convertir el resultado a cadena de texto antes de retornarlo
              return str(row[0])
          else:
              return "No se encontró un puntaje para el ID proporcionado."
      except Exception as ex:
          message = f"Ocurrió un error al consultar el puntaje del usuario por naturalperson_id {ex}"
          raise Exception(message)
      finally:
          conexion.close()
