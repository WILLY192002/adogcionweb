#Database
from src.database.mysql_db import get_connection

#Model's
from src.models.Operation_Animal import OperationAnimal
from src.models.Operation import Operation

class Operation_AnimalService():
  @classmethod
  def addNewOperation_Animal(self, animal_id, operation_list):
    try:
      conexion = get_connection()
      cursor = conexion.cursor()
      if operation_list:
        sql = f"INSERT INTO operation_animal (operation_id, animal_id) VALUES "
        Values = []
        for operation_id in operation_list:
          Values.append(f"({operation_id},{animal_id})")
        insertions = ', '.join(Values)
        
        sql += insertions+';'
        cursor.execute(sql)
        conexion.commit()
        return "A new animal operation has been successfully added"
      else:
        return True
    except Exception as ex:
      message = f"Error when adding a new animal operation{ex}"
      raise Exception(message)
    finally:
      conexion.close()

  @classmethod
  def deleteOperation_Animal(self, animal_id, operation_list):
    try:
      conexion = get_connection()
      cursor = conexion.cursor()
      if operation_list:
        sql = f"DELETE FROM operation_animal WHERE ( "
        Values = []
        for operation_id in operation_list:
          Values.append(f"operation_id = {operation_id}")
        insertions = ' OR '.join(Values)
        
        sql += insertions+f') AND animal_id = {animal_id};'
        cursor.execute(sql)
        conexion.commit()
        return "A new animal operation has been successfully added"
      else:
        return True
    except Exception as ex:
      message = f"Error when deleting an operation from animal {ex}"
      raise Exception(message)
    finally:
      conexion.close()

  @classmethod
  def getOperationByAnimalId(self, animal_id):
    try:
      conexion = get_connection()
      cursor = conexion.cursor()
      sql = f"SELECT o.id, o.name, o.description FROM operation_animal oa JOIN operation o ON oa.operation_id = o.id WHERE oa.animal_id = {animal_id}"
      cursor.execute(sql)
      rows = cursor.fetchall()
      out_operations = []
      if rows != None:
        for row in rows:
          out_operations.append(Operation(row[0],row[1],row[2]))
        return out_operations
      else:
        return False
    except Exception as ex:
      message = f"An error occurred while consulting operation by animal id {ex}"
      raise Exception(message)
    finally:
      conexion.close()

