from Design_pattrens.strgy_design.CreditCard import CreditCard
from Design_pattrens.strgy_design.DebitCrad import DebitCard


class PaymentFactory:
    strgies = {
        'credit_card': CreditCard,
        'debit_card': DebitCard,
    }

    @staticmethod
    def get_strgy(mode):
        available_modes = PaymentFactory.strgies.get(mode)
        if not available_modes:
            raise ValueError(f'Unknown payment mode: {mode}')

        return available_modes()