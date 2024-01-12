#Database
from src.database.mysql_db import get_connection

#Model's
from src.models.Publication import Publication

class PublicationService():
  @classmethod
  def addNewPublication(self, publication):
    try:
      conexion = get_connection()
      cursor = conexion.cursor()
      new_publication = publication.__dict__
      new_publication.pop("id")
      new_publication = {key: value for key, value in new_publication.items() if value is not None}
      columns = ', '.join(new_publication.keys())
      values = ', '.join("'" + str(valor) + "'" if isinstance(valor, str) else str(valor) for valor in new_publication.values())
      sql = f"INSERT INTO publication ({columns}) VALUES ({values})"
      cursor.execute(sql)
      conexion.commit()
      return "A new publication has been successfully added"
    except Exception as ex:
      message = f"Error when adding a new publication center {ex}"
      raise Exception(message)
    finally:
      conexion.close()

  @classmethod
  def getAllPublicationByAdoptionCenter(self, filter_search, filter_topic, filter_category):
    try:
      conexion = get_connection()
      cursor = conexion.cursor()
      sql = """SELECT p.*, ac.photo, ac.name, ac.id FROM publication p JOIN access a ON p.access_id = a.id 
      JOIN adoptioncenter ac ON a.id = ac.access_id
      WHERE p.is_activate = 1"""
      if filter_search != None:
        sql += f" AND ac.name LIKE '%{filter_search}%'"
      if filter_topic != None:
        sql += f' AND p.topic_id = {filter_topic}'
      if filter_category != None and filter_topic == None:
        sql += ' AND ('
        sql += ' OR'.join((' p.topic_id = ' + str(x.id)) for x in filter_category)
        sql += ') '

      sql += ' ORDER BY date DESC;'
      cursor.execute(sql)
      row = cursor.fetchall()
      out_publication = []
      if row != None:
        for pub in row:
          out_publication.append(Publication(pub[0],pub[1],pub[2],pub[3],pub[4],pub[5],pub[6],pub[7], pub[8], pub[9],pub[10]))
        return out_publication
      else:
        return False
    except Exception as ex:
      message = f"An error occurred while consulting publications by user type {ex}"
      raise Exception(message)
    finally:
      conexion.close()
  
  

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
          out_publication.append(Publication(pub[0],pub[1],pub[2],pub[3],pub[4],pub[5],pub[6],pub[7]))
        return out_publication
      else:
        return False
    except Exception as ex:
      message = f"An error occurred while consulting publications by access {ex}"
      raise Exception(message)
    finally:
      conexion.close()
    
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
          out_publication.append(Publication(pub[0],pub[1],pub[2],pub[3],pub[4],pub[5],pub[6],pub[7]))
        return out_publication
      else:
        return False
    except Exception as ex:
      message = f"An error occurred while consulting publications by category{ex}"
      raise Exception(message)
    finally:
      conexion.close()
  
  @classmethod
  def getAllPublicationByTopic(self, access_id, topic_id):
    try:
      conexion = get_connection()
      cursor = conexion.cursor()
      sql = f"SELECT * FROM publication WHERE access_id = {access_id} AND topic_id = {topic_id} AND is_activate = 1 ORDER BY date DESC;"
      cursor.execute(sql)
      row = cursor.fetchall()
      out_publication = []
      if row != None:
        for pub in row:
          out_publication.append(Publication(pub[0],pub[1],pub[2],pub[3],pub[4],pub[5],pub[6],pub[7]))
        return out_publication
      else:
        return False
    except Exception as ex:
      message = f"An error occurred while consulting publications by topic {ex}"
      raise Exception(message)
    finally:
      conexion.close()