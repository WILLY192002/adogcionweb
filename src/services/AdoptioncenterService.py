from src.database.mysql_db import get_connection
from src.models.Adoptioncenter import AdoptionCenter
class AdoptioncenterService():
  @classmethod
  def addNewAdoptionCenter(self, Adoptioncenter):
    try:
      conexion = get_connection()
      cursor = conexion.cursor()
      new_Adoptioncenter = Adoptioncenter.__dict__
      new_Adoptioncenter.pop("id")
      new_Adoptioncenter = {key: value for key, value in new_Adoptioncenter.items() if value is not None}
      columns = ', '.join(new_Adoptioncenter.keys())
      values = ', '.join("'" + str(valor) + "'" if isinstance(valor, str) else str(valor) for valor in new_Adoptioncenter.values())
      sql = f"INSERT INTO adoptioncenter ({columns}) VALUES ({values})"
      cursor.execute(sql)
      conexion.commit()
      return "A new adoption center has been successfully added"
    except Exception as ex:
      message = f"Error when adding a new adoption center {ex}"
      raise Exception(message)
    finally:
      conexion.close()
    
  @classmethod
  def getAdoptionCenterByAccessId(self, access_id):
    try:
      conexion = get_connection()
      cursor = conexion.cursor()
      sql = f"SELECT * FROM adoptioncenter WHERE access_id = {access_id}"
      cursor.execute(sql)
      row = cursor.fetchone()
      if row != None:
        return AdoptionCenter(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10], row[11])
      else:
        return False
    except Exception as ex:
      message = f"An error occurred while consulting an Adoption Center by Access {ex}"
      raise Exception(message)
    finally:
      conexion.close()
  
  @classmethod
  def getAdoptionCenterById(self, id):
    try:
      conexion = get_connection()
      cursor = conexion.cursor()
      sql = f"SELECT * FROM adoptioncenter WHERE id = {id}"
      cursor.execute(sql)
      row = cursor.fetchone()
      if row != None:
        return AdoptionCenter(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10], row[11])
      else:
        return False
    except Exception as ex:
      message = f"An error occurred while consulting an Adoption Center by id {ex}"
      raise Exception(message)
    finally:
      conexion.close()
  
  @classmethod
  def updateAdoptionCenter(self, id, Adoptioncenter):
    try:
      conexion = get_connection()
      cursor = conexion.cursor()
      new_Adoptioncenter = Adoptioncenter.__dict__
      new_Adoptioncenter.pop("id")
      new_Adoptioncenter = {key: value for key, value in new_Adoptioncenter.items() if value is not None}
      fields = []
      for key, value in new_Adoptioncenter.items():
          if isinstance(value, str):
              fields.append(f'{key} = "{value}"')
          else:
              fields.append(f'{key} = {value}')
      fieldsUpdate = ', '.join(fields)
      sql = f"UPDATE adoptioncenter SET {fieldsUpdate} WHERE id = {id}"
      cursor.execute(sql)
      conexion.commit()
      return "An update in adoption center has been successfully"
    except Exception as ex:
      message = f"Error when update a adoption center {ex}"
      raise Exception(message)
    finally:
      conexion.close()