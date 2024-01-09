#Database
from src.database.mysql_db import get_connection

#Model's
from src.models.Access import Access

#utils
from src.utils import security_password as sp

class AccessService():
  @classmethod
  def addNewAccess(self, access):
    try:
      conexion = get_connection()
      cursor = conexion.cursor()
      access.password = sp.generate_password_hash(access.password)
      new_access = access.__dict__
      new_access.pop("id")
      new_access = {key: value for key, value in new_access.items() if value is not None}
      columns = ', '.join(new_access.keys())
      values = ', '.join("'" + str(valor) + "'" if isinstance(valor, str) else str(valor) for valor in new_access.values())
      sql = f"INSERT INTO access ({columns}) VALUES ({values})"
      cursor.execute(sql)
      conexion.commit()
      return "A new access has been successfully added"
    except Exception as ex:
      message = f"Error when adding a new access {ex}"
      raise Exception(message)
    finally:
      conexion.close()

  @classmethod
  def getAccessByEmail(self, email):
    try:
      conexion = get_connection()
      cursor = conexion.cursor()
      sql = f"SELECT * FROM access WHERE email = '{email}'"
      cursor.execute(sql)
      row = cursor.fetchone()
      if row != None:
        return Access(row[0],row[1],None,row[3],row[4])
      else:
        return False
    except Exception as ex:
      message = f"An error occurred while consulting an access {ex}"
      raise Exception(message)
    finally:
      conexion.close()
  
  @classmethod
  def getAccessById(self, id):
    try:
      conexion = get_connection()
      cursor = conexion.cursor()
      sql = f"SELECT * FROM access WHERE id = {id}"
      cursor.execute(sql)
      row = cursor.fetchone()
      if row != None:
        return Access(row[0],row[1],None,row[3],row[4])
      else:
        return False
    except Exception as ex:
      message = f"An error occurred while consulting an access {ex}"
      raise Exception(message)
    finally:
      conexion.close()
  
  @classmethod
  def verifyUser(self, access):
    try:
      conexion = get_connection()
      cursor = conexion.cursor()
      sql = f"SELECT * FROM access WHERE email = '{access.email}'"
      cursor.execute(sql)
      row = cursor.fetchone()
      if row != None:
        if (sp.check_password(row[2], access.password)):
          access.id = row[0]
          access.password = True
          access.user_type_id = row[3]
          access.is_activate = row[4]
          return access
        else:
          return False
      else:
        return False
    except Exception as ex:
      message = f"Error when checking user {ex}"
      raise Exception(message)
    finally:
      conexion.close()
