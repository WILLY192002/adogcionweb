#Database
from src.database.mysql_db import get_connection

#Model's
from src.models.Topic import Topic

class TopicService():
  @classmethod
  def getAllTopics(self):
    try:
      conexion = get_connection()
      cursor = conexion.cursor()
      sql = f"SELECT * FROM topic"
      cursor.execute(sql)
      row = cursor.fetchall()
      out_topic = []
      if row != None:
        for topic in row:
          out_topic.append(Topic(topic[0],topic[1], topic[2]))
          return out_topic
      else:
        return False
    except Exception as ex:
      message = f"An error occurred while consulting Topics {ex}"
      raise Exception(message)
  
  @classmethod
  def getTopicByName(self, name):
    try:
      conexion = get_connection()
      cursor = conexion.cursor()
      sql = f"SELECT * FROM topic WHERE name = {name}"
      cursor.execute(sql)
      row = cursor.fetchone()
      if row != None :
        return Topic(row[0],row[1], row[2])
      else:
        return None
    except Exception as ex:
      message = f"An error occurred while consulting a Topic {ex}"
      raise Exception(message)
  
  @classmethod
  def getAllTopicByCategory(self, category_id):
    try:
      conexion = get_connection()
      cursor = conexion.cursor()
      sql = f"SELECT * FROM topic WHERE category_id = {category_id}"
      cursor.execute(sql)
      row = cursor.fetchall()
      out_topic = []
      if row != None:
        for topic in row:
          out_topic.append(Topic(topic[0],topic[1],topic[2]))
        return out_topic
      else:
        return None
    except Exception as ex:
      message = f"An error occurred while consulting Topics {ex}"
      raise Exception(message)