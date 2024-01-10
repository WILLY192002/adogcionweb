#Database
from src.database.mysql_db import get_connection

#Model's
from src.models.Operation_Animal import OperationAnimal

class Operation_AnimalService():
  @classmethod
  def addNewOperation_Animal(self, animal_id, operation_list):
    try:
      if operation_list:
        conexion = get_connection()
        cursor = conexion.cursor()
        
        sql = f"INSERT INTO operation_animal (operation_id, animal_id) VALUES "
        Values = []
        for operation_id in operation_list:
          Values.append(f"({operation_id},{animal_id})")
        insertions = ', '.join(Values)
        
        sql += insertions+';'
        cursor.execute(sql)
        conexion.commit()
        return "A new operation animal has been successfully added"
      else:
        return True
    except Exception as ex:
      message = f"Error when adding a new natural person {ex}"
      raise Exception(message)
