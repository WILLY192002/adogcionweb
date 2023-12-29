#Database
from src.database.mysql_db import get_connection

#Model's
from src.models.Category import Category

class CategoryService():
  @classmethod
  def getAllCategories(self):
    try:
      conexion = get_connection()
      cursor = conexion.cursor()
      sql = f"SELECT * FROM category"
      cursor.execute(sql)
      row = cursor.fetchall()
      out_category = []
      if row != None:
        for category in row:
          out_category.append(Category(category[0],category[1]))
          return out_category
      else:
        return None
    except Exception as ex:
      message = f"An error occurred while consulting Categories {ex}"
      raise Exception(message)
  
  @classmethod
  def getCategoryByName(self, name):
    try:
      conexion = get_connection()
      cursor = conexion.cursor()
      sql = f"SELECT * FROM category WHERE name = {name}"
      cursor.execute(sql)
      row = cursor.fetchone()
      if row != None :
        return Category(row[0],row[1])
      else:
        return None
    except Exception as ex:
      message = f"An error occurred while consulting a Category {ex}"
      raise Exception(message)