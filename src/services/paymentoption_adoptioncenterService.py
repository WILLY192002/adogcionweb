#Database
from src.database.mysql_db import get_connection

#Model's
from src.models.Paymentoption_Adoptioncenter import PaymentOptionAdoptionCenter

class Paymentoption_AdoptioncenterService():
  @classmethod
  def getPaymentOptionAdoptionCenter(self, adoptioncenter_id):
    try:
      conexion = get_connection()
      cursor = conexion.cursor()
      
      sql = f"""SELECT PayOptAdopt.id, PayOptAdopt.paymentoption_id, PayOptAdopt.adoptioncenter_id, 
      PayOptAdopt.number_payment, PayOpt.name FROM paymentoption_adoptioncenter PayOptAdopt JOIN 
      paymentoption PayOpt ON PayOptAdopt.paymentoption_id = PayOpt.id WHERE PayOptAdopt.adoptioncenter_id = {adoptioncenter_id};
"""
      cursor.execute(sql)
      rows = cursor.fetchall()
      out_paymentoptions = []
      if rows!= None:
        for payOptionAdopt in rows:
          out_paymentoptions.append(PaymentOptionAdoptionCenter(payOptionAdopt[0], payOptionAdopt[1], payOptionAdopt[2],payOptionAdopt[3],payOptionAdopt[4]))
        return out_paymentoptions
      else:
        return False
    except Exception as ex:
      message = f"An error occurred while consulting payment options registered by adoption center {ex}"
      raise Exception(message)
    finally:
      conexion.close()

  @classmethod
  def deletePaymentOptionAdoptionCenter(self,adoptioncenter_id, paymentoption_id):
    try:
      conexion = get_connection()
      cursor = conexion.cursor()
      sql = f"DELETE FROM paymentoption_adoptioncenter WHERE adoptioncenter_id = {adoptioncenter_id} AND paymentoption_id = {paymentoption_id};"
      cursor.execute(sql)
      conexion.commit()
      return True
    except Exception as ex:
      message = f"An error occurred while deleting payment options from adoption center {ex}"
      raise Exception(message)
    finally:
      conexion.close()
  
  @classmethod
  def updatePaymentOptionAdoptionCenter(self,adoptioncenter_id, paymentoption_id, new_number):
    try:
      conexion = get_connection()
      cursor = conexion.cursor()
      print("Update:", type(adoptioncenter_id))
      sql = f"UPDATE paymentoption_adoptioncenter SET number_payment = {new_number} WHERE adoptioncenter_id = {adoptioncenter_id} AND paymentoption_id = {paymentoption_id};"
      print(sql)
      cursor.execute(sql)
      conexion.commit()
      return True
    except Exception as ex:
      message = f"An error occurred while updating payment options from adoption center {ex}"
      raise Exception(message)
    finally:
      conexion.close()
  
  @classmethod
  def insertPaymentOptionAdoptionCenter(self,paymentoption_adoptioncenter):
    try:
      conexion = get_connection()
      cursor = conexion.cursor()
      print("XD:",type(paymentoption_adoptioncenter.adoptioncenter_id))
      new_paymentoption_adoptioncenter = paymentoption_adoptioncenter.__dict__
      new_paymentoption_adoptioncenter.pop("id")
      new_paymentoption_adoptioncenter = {key: value for key, value in new_paymentoption_adoptioncenter.items() if value is not None}
      columns = ', '.join(new_paymentoption_adoptioncenter.keys())
      values = ', '.join("'" + str(valor) + "'" if isinstance(valor, str) else str(valor) for valor in new_paymentoption_adoptioncenter.values())
      sql = f"INSERT INTO paymentoption_adoptioncenter ({columns}) VALUES ({values});"
      print(sql)
      cursor.execute(sql)
      conexion.commit()
      return "A new payment option adoption center has been successfully added"
    except Exception as ex:
      message = f"An error occurred while adding payment options to adoption center {ex}"
      raise Exception(message)
    finally:
      conexion.close()
