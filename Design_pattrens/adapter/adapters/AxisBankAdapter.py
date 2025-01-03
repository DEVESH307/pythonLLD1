from Design_pattrens.adapter.adapters.BankAdapterABC import *
from Design_pattrens.adapter.banks.AxisBank import *


class AxisBankAdapter(BankAdapterABC):
    def __init__(self):
        self.bank = AxisBank()

    def checkBalance(self):
        return self.bank.bal()
