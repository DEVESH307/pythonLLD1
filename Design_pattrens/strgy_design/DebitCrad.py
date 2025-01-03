from Design_pattrens.strgy_design.PaymentStrgy import PaymentStrgy


class DebitCard(PaymentStrgy):
    def pay(self, amount):
        print("pay with DC")
