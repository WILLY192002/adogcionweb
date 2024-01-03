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
      sql = f"""SELECT PayOptAdopt.*, PayOpt.name FROM paymentoption_adoptioncenter PayOptAdopt JOIN 
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
      message = f"An error occurred while consulting payment options adoption center {ex}"
      raise Exception(message)