class PaymentOptionAdoptionCenter:
    def __init__(self, id, paymentoption_id, adoptioncenter_id, number, name_paymentoption = None):
        self.id = id
        self.paymentoption_id = paymentoption_id
        self.adoptioncenter_id = adoptioncenter_id
        self.number = number
        self.name_paymentoption = name_paymentoption
