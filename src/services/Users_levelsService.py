from src.database.mysql_db import get_connection
from src.models.Users_levels import Users_levels

class Users_levelsService():
    @classmethod
    def getUserTitle(self, naturalperson_id):
        try:
            conexion = get_connection()
            cursor = conexion.cursor()
            sql = f"SELECT levels.level_name as levelname FROM users_levels INNER JOIN levels ON users_levels.level_id = levels.id WHERE users_levels.naturalperson_id = {naturalperson_id} AND users_levels.status = 1"
            cursor.execute(sql)
            row = cursor.fetchone()
            if row != None:
                return Users_levels(None,None,None,None,None, row[0])
            else:
                return False
        except Exception as ex:
            message = f"An error occurred while consulting an UserTitle by naturalperson_id {ex}"
            raise Exception(message)
        finally:
            conexion.close()

    @classmethod
    def getalltitlegains(self, naturalperson_id):
        try:
            conexion = get_connection()
            cursor = conexion.cursor()
            sql = f"SELECT levels.id, levels.level_name FROM users_levels INNER JOIN levels ON users_levels.level_id = levels.id WHERE users_levels.naturalperson_id = {naturalperson_id}"
            cursor.execute(sql)
            rows = cursor.fetchall()
            out_users_levels = []
            if rows != None:
                for row in rows:
                    out_users_levels.append(Users_levels(None, None, row[0], None, None, row[1]))
                return out_users_levels
            else:
                return False
        except Exception as ex:
            message = f"An error occurred while consulting UserTitle by naturalperson_id {ex}"
            raise Exception(message)
        finally:
            conexion.close()

    @classmethod
    def updateUserSetTitle(self, naturalperson_id, level_id):
        try:
            conexion = get_connection()
            cursor = conexion.cursor()

            # Primero, cambiamos cualquier status existente de 1 a 0 para el naturalperson_id dado
            sql_update = f"UPDATE users_levels SET status = 0 WHERE naturalperson_id = {naturalperson_id} AND status = 1"
            cursor.execute(sql_update)

            # Luego, actualizamos el status de 0 a 1 para el naturalperson_id y level_id dados
            sql_update = f"UPDATE users_levels SET status = 1 WHERE naturalperson_id = {naturalperson_id} AND level_id = {level_id}"
            cursor.execute(sql_update)

            # Confirmamos los cambios
            conexion.commit()
        except Exception as ex:
            message = f"An error occurred while updating UserLevel by naturalperson_id and level_id {ex}"
            raise Exception(message)
        finally:
            conexion.close()


