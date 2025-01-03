from Design_pattrens.adapter.adapters.BankAdapterABC import *
from Design_pattrens.adapter.banks.yesbank import *


class YesBankAdapter(BankAdapterABC):
    def __init__(self):
        self.bank = YesBank()

    def checkBalance(self):
        return int(self.bank.balance())
