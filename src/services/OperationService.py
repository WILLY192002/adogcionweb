#Database
from src.database.mysql_db import get_connection

#Model's
from src.models.Operation import Operation

class OperationService():
  @classmethod
  def getAllOperations(self):
    try:
      conexion = get_connection()
      cursor = conexion.cursor()
      sql = f"SELECT * FROM operation"
      cursor.execute(sql)
      rows = cursor.fetchall()
      out_operation = []
      if rows != None:
        for row in rows:
          out_operation.append(Operation(row[0],row[1],row[2]))
        return out_operation
      else:
        return False
    except Exception as ex:
      message = f"An error occurred while consulting operation {ex}"
      raise Exception(message)
    finally:
      conexion.close()