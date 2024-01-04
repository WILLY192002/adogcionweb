class PaymentOptionAdoptionCenter:
    def __init__(self, id, paymentoption_id, adoptioncenter_id, number_payment, name_paymentoption = None):
        self.id = id
        self.paymentoption_id = paymentoption_id
        self.adoptioncenter_id = adoptioncenter_id
        self.number_payment = number_payment
        self.name_paymentoption = name_paymentoption
