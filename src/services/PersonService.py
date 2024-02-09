from src.database.mysql_db import get_connection
from src.models.Person import Person
class PersonService():
  @classmethod
  def addNewPerson(self, person):
    try:
      conexion = get_connection()
      cursor = conexion.cursor()
      new_person = person.__dict__
      new_person.pop("id")
      new_person = {key: value for key, value in new_person.items() if value is not None}
      columns = ', '.join(new_person.keys())
      values = ', '.join("'" + str(valor) + "'" if isinstance(valor, str) else str(valor) for valor in new_person.values())
      sql = f"INSERT INTO person ({columns}) VALUES ({values})"
      cursor.execute(sql)
      conexion.commit()
      return "A new person has been successfully added"
    except Exception as ex:
      message = f"Error when adding a new person {ex}"
      raise Exception(message)
  
  @classmethod
  def getPersonByIdentificationNumber(self, identification):
    try:
      conexion = get_connection()
      cursor = conexion.cursor()
      sql = f"SELECT id, first_name, middle_name, first_surname, second_lastname, identification_type, identification_number, contact, city, department FROM person WHERE identification_number = {identification}"
      cursor.execute(sql)
      row = cursor.fetchone()
      if row != None:
        return Person(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9])
      else:
        return False
    except Exception as ex:
      message = f"An error occurred while consulting a person by identification number{ex}"
      raise Exception(message)
    finally:
      conexion.close()
  
  @classmethod
  def getPersonById(self, id):
    try:
      conexion = get_connection()
      cursor = conexion.cursor()
      sql = f"SELECT id, first_name, middle_name, first_surname, second_lastname, identification_type, identification_number, contact, city, department FROM person WHERE id = {id}"
      cursor.execute(sql)
      row = cursor.fetchone()
      if row != None:
        return Person(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9])
      else:
        return False
    except Exception as ex:
      message = f"An error occurred while consulting a person by id{ex}"
      raise Exception(message)
    finally:
      conexion.close()
  
  @classmethod
  def updatePerson(self, id, Person):
    try:
      conexion = get_connection()
      cursor = conexion.cursor()
      new_Person = Person.__dict__
      new_Person.pop("id")
      new_Person = {key: value for key, value in new_Person.items() if value is not None}
      fields = []
      for key, value in new_Person.items():
          if value == '':
            fields.append(f'{key} = NULL')
          elif isinstance(value, str):
            fields.append(f'{key} = "{value}"')
          else:
            fields.append(f'{key} = {value}')
      fieldsUpdate = ', '.join(fields)
      sql = f"UPDATE person SET {fieldsUpdate} WHERE id = {id}"
      cursor.execute(sql)
      conexion.commit()
      return "An update in person has been successfully"
    except Exception as ex:
      message = f"Error when update a person {ex}"
      raise Exception(message)
    finally:
      conexion.close()