from src.database.mysql_db import get_connection
from src.models.Animalphoto import Animalphoto
class AdoptioncenterService():
  @classmethod
  def addNewAdoptionCenter(self, Animalphoto):
    try:
      conexion = get_connection()
      cursor = conexion.cursor()
      new_animalphoto = Animalphoto.__dict__
      new_animalphoto.pop("id")
      new_animalphoto = {key: value for key, value in new_animalphoto.items() if value is not None}
      columns = ', '.join(new_animalphoto.keys())
      values = ', '.join("'" + str(valor) + "'" if isinstance(valor, str) else str(valor) for valor in new_animalphoto.values())
      sql = f"INSERT INTO animal_photo ({columns}) VALUES ({values})"
      cursor.execute(sql)
      conexion.commit()
      return "A new animal_photo has been successfully added"
    except Exception as ex:
      message = f"Error when adding a new animal_photo {ex}"
      raise Exception(message)
    finally:
      conexion.close()