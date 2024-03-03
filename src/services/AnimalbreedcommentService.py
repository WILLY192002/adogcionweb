from src.database.mysql_db import get_connection
from src.models.AnimalBreedComment import AnimalBreedComment
from flask import jsonify
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
      sql_call = f"CALL update_naturalperson_score({AnimalBreedComment.access_id}, 20);"
      cursor.execute(sql)
      cursor.execute(sql_call)
      conexion.commit()
      return "A new animal breed comment has been successfully added"
    except Exception as ex:
      message = f"Error when adding an animal breed comment {ex}"
      raise Exception(message)
    finally:
      conexion.close()
  
  @classmethod
  def getAllAnimalBreedComment(self):
    try:
      conexion = get_connection()
      cursor = conexion.cursor()
      sql = f""" SELECT abc.id, abc.access_id, abc.breed_id, abc.description, abc.date, abc.status, 
      COALESCE(np.name, ac.name) AS name, COALESCE(np.photo, ac.photo) AS photo
      FROM animal_breed_comment abc
      LEFT JOIN naturalperson np ON abc.access_id = np.access_id 
      LEFT JOIN adoptioncenter ac ON abc.access_id = ac.access_id 
      WHERE status = 1 ORDER BY date DESC;"""
      cursor.execute(sql)
      row = cursor.fetchall()
      out_comments = []
      if row != None:
        for comment in row:
          out_comments.append(AnimalBreedComment(comment[0],comment[1],comment[2],comment[3],comment[4],comment[5],comment[6],comment[7]))
        return out_comments
      else:
        return False
    except Exception as ex:
      message = f"An error occurred while consulting all animal breed comment {ex}"
      raise Exception(message)
    finally:
      conexion.close()

  @classmethod
  def getAllAnimalBreedCommentBybreed_id(self, breed_id):
    try:
      conexion = get_connection()
      cursor = conexion.cursor()
      sql = f""" SELECT abc.id, abc.access_id, abc.breed_id, abc.description, abc.date, abc.status, 
      COALESCE(np.name, ac.name) AS name, COALESCE(np.photo, ac.photo) AS photo
      FROM animal_breed_comment abc
      LEFT JOIN naturalperson np ON abc.access_id = np.access_id 
      LEFT JOIN adoptioncenter ac ON abc.access_id = ac.access_id 
      WHERE status = 1 AND breed_id = {breed_id} ORDER BY date DESC;"""
      cursor.execute(sql)
      row = cursor.fetchall()
      out_comments = []
      if row != None:
        for comment in row:
          out_comments.append(AnimalBreedComment(comment[0],comment[1],comment[2],comment[3],comment[4],comment[5],comment[6],comment[7]))
        return out_comments
      else:
        return False
    except Exception as ex:
      message = f"An error occurred while consulting all animal breed comment by animal breed{ex}"
      raise Exception(message)
    finally:
      conexion.close()


  @classmethod
  def reportComment(self, comment_id):
    try:
      conexion = get_connection()
      cursor = conexion.cursor()
      sql = f"UPDATE animal_breed_comment SET report = report + 1 WHERE id = {comment_id};"
      sql_report = f"CALL score_decrement({comment_id});"
      sql_call = f"CALL deactivate_comment_procedure({comment_id});"
      cursor.execute(sql)
      cursor.execute(sql_report)
      cursor.execute(sql_call)
      conexion.commit()
      return jsonify(status="success"), 200
    except Exception as ex:
      # message = f"An error occurred while deleting publications by topic {ex}"
      return jsonify(status="error", message="An error occurred while reporting comment from animal profile"), 400
      raise Exception(message)
    finally:
      conexion.close()