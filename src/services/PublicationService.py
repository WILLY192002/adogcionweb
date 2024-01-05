#Database
from src.database.mysql_db import get_connection

#Model's
from src.models.Publication import Publication

class PublicationService():
  @classmethod
  def getAllPublicationByUserType(self, user_type_id):
    try:
      conexion = get_connection()
      cursor = conexion.cursor()
      sql = f"SELECT p.* FROM publication p JOIN access a ON p.access_id = a.id WHERE a.user_type_id = {user_type_id} AND p.is_activate = 1 ORDER BY date DESC;"
      cursor.execute(sql)
      row = cursor.fetchall()
      out_publication = []
      if row != None:
        for pub in row:
          out_publication.append(Publication(pub[0],pub[1],pub[2],None, None,pub[3],pub[4],pub[5],pub[6],pub[7]))
        return out_publication
      else:
        return False
    except Exception as ex:
      message = f"An error occurred while consulting publications by user type {ex}"
      raise Exception(message)
  
  @classmethod
  def getAllPublicationByAccessId(self, access_id):
    try:
      conexion = get_connection()
      cursor = conexion.cursor()
      sql = f"SELECT * FROM publication WHERE access_id = {access_id} AND is_activate = 1 ORDER BY date DESC;"
      cursor.execute(sql)
      row = cursor.fetchall()
      out_publication = []
      if row != None:
        for pub in row:
          out_publication.append(Publication(pub[0],pub[1],pub[2],None, None,pub[3],pub[4],pub[5],pub[6],pub[7]))
        return out_publication
      else:
        return False
    except Exception as ex:
      message = f"An error occurred while consulting publications by access {ex}"
      raise Exception(message)
    
  @classmethod
  def getAllPublicationByCategoryId(self, category_id, access_id):
    try:
      conexion = get_connection()
      cursor = conexion.cursor()
      sql = f"SELECT p.* FROM publication AS p JOIN topic ON p.topic_id = topic.id WHERE topic.category_id = {category_id}"
      if access_id != None:
        sql += f" AND p.access_id = {access_id}"
      cursor.execute(sql)
      row = cursor.fetchall()
      out_publication = []
      if row != None:
        for pub in row:
          out_publication.append(Publication(pub[0],pub[1],pub[2],None, None,pub[3],pub[4],pub[5],pub[6],pub[7]))
        return out_publication
      else:
        return False
    except Exception as ex:
      message = f"An error occurred while consulting publications by category{ex}"
      raise Exception(message)