#Database
from src.database.mysql_db import get_connection

#Model's
from src.models.paymentoption import PaymentOption

class PaymentoptionService():
  @classmethod
  def getNoPaymentOptionAdoptionCenter(self, adoptioncenter_id):
    try:
      conexion = get_connection()
      cursor = conexion.cursor()
      sql = f"""SELECT po.* FROM paymentoption po WHERE NOT EXISTS 
      (SELECT 1 FROM paymentoption_adoptioncenter pa WHERE pa.paymentoption_id = po.id AND 
      pa.adoptioncenter_id = {adoptioncenter_id});"""
      cursor.execute(sql)
      rows = cursor.fetchall()
      out_paymentoptions = []
      if rows!= None:
        for payOption in rows:
          out_paymentoptions.append(PaymentOption(payOption[0], payOption[1]))
        return out_paymentoptions
      else:
        return False
    except Exception as ex:
      message = f"An error occurred while consulting payment options adoption center {ex}"
      raise Exception(message)