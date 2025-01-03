from Design_pattrens.strgy_design.PaymentStrgy import PaymentStrgy


class CreditCard(PaymentStrgy):

    def pay(self, amount):
        print("paid using CC")

