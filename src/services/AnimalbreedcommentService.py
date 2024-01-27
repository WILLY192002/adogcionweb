from src.database.mysql_db import get_connection
from src.models.AnimalBreedComment import AnimalBreedComment
class AnimalbreedcommentService():
  @classmethod
  def addNewAnimalBreedComment(self, AnimalBreedComment):
    try:
      conexion = get_connection()
      cursor = conexion.cursor()
      new_AnimalBreedComment = AnimalBreedComment.__dict__
      new_AnimalBreedComment.pop("id")
      new_AnimalBreedComment = {key: value for key, value in new_AnimalBreedComment.items() if value is not None}
      columns = ', '.join(new_AnimalBreedComment.keys())
      values = ', '.join("'" + str(valor) + "'" if isinstance(valor, str) else str(valor) for valor in new_AnimalBreedComment.values())
      sql = f"INSERT INTO animal_breed_comment ({columns}) VALUES ({values})"
      print(sql)
      cursor.execute(sql)
      conexion.commit()
      return "A new animal breed comment has been successfully added"
    except Exception as ex:
      message = f"Error when adding an animal breed comment center {ex}"
      raise Exception(message)
    finally:
      conexion.close()