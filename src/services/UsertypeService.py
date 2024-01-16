from src.database.mysql_db import get_connection
from src.models.Usertype import UserType

class UsertypeService():
  @classmethod
  def addNewUsertype(self, UserType):
    try:
      conexion = get_connection()
      cursor = conexion.cursor()
      new_UserType= UserType.__dict__
      new_UserType.pop("id")
      new_UserType = {key: value for key, value in new_UserType.items() if value is not None}
      columns = ', '.join(new_UserType.keys())
      values = ', '.join("'" + str(valor) + "'" if isinstance(valor, str) else str(valor) for valor in new_UserType.values())
      sql = f"INSERT INTO usertype ({columns}) VALUES ({values})"
      cursor.execute(sql)
      conexion.commit()
      return "A new usertype has been successfully added"
    except Exception as ex:
      message = f"Error when adding a new usertype {ex}"
      raise Exception(message)
    finally:
      conexion.close()

  @classmethod
  def getUserTypeByName(self, name):
    try:
      conexion = get_connection()
      cursor = conexion.cursor()
      sql = f"SELECT id, name FROM usertype WHERE name = '{name}'"
      cursor.execute(sql)
      row = cursor.fetchone()
      if row != None:
        return UserType(row[0],row[1])
      else:
        return False
    except Exception as ex:
      message = f"An error occurred while consulting an usertype {ex}"
      raise Exception(message)
    finally:
      conexion.close()
  
  @classmethod
  def verifyUserTypeAdoptionCenter(self, user_type_id):
    try:
      conexion = get_connection()
      cursor = conexion.cursor()
      user_type_name = 'UT-ADOPTION_CENTER'
      sql = f"SELECT id, name FROM usertype WHERE name = '{user_type_name}'"
      cursor.execute(sql)
      row = cursor.fetchone()
      if row != None:
        if user_type_id == UserType(row[0],row[1]).id:
          return True
        else:
          return False
      else:
        return False
    except Exception as ex:
      message = f"An error occurred while consulting an usertype 'Adoption Center' {ex}"
      raise Exception(message)
    finally:
      conexion.close()
  
  @classmethod
  def verifyUserTypeNatrualPerson(self, user_type_id):
    try:
      conexion = get_connection()
      cursor = conexion.cursor()
      user_type_name = 'UT-NATURAL_PERSON'
      sql = f"SELECT id, name FROM usertype WHERE name = '{user_type_name}'"
      cursor.execute(sql)
      row = cursor.fetchone()
      if row != None:
        if user_type_id == UserType(row[0],row[1]).id:
          return True
        else:
          return False
      else:
        return False
    except Exception as ex:
      message = f"An error occurred while consulting an usertype 'Natural Person' {ex}"
      raise Exception(message)
    finally:
      conexion.close()