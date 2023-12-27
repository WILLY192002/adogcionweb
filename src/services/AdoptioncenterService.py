from src.database.mysql_db import get_connection
class AdoptioncenterService():
  @classmethod
  def addNewAdoptionCenter(self, Adoptioncenter):
    try:
      conexion = get_connection()
      cursor = conexion.cursor()
      new_Adoptioncenter = Adoptioncenter.__dict__
      new_Adoptioncenter.pop("id")
      new_Adoptioncenter = {key: value for key, value in new_Adoptioncenter.items() if value is not None}
      columns = ', '.join(new_Adoptioncenter.keys())
      values = ', '.join("'" + str(valor) + "'" if isinstance(valor, str) else str(valor) for valor in new_Adoptioncenter.values())
      sql = f"INSERT INTO adoptioncenter ({columns}) VALUES ({values})"
      print(sql)
      cursor.execute(sql)
      conexion.commit()
      return "A new adoption center has been successfully added"
    except Exception as ex:
      message = f"Error when adding a new adoption center {ex}"
      raise Exception(message)