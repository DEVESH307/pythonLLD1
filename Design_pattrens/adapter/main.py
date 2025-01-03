from Design_pattrens.adapter.adapters.YesBankAdapter import *
from Design_pattrens.adapter.adapters.AxisBankAdapter import *
from Design_pattrens.adapter.phonepe import Phonepe

if __name__ == '__main__':
    b = AxisBankAdapter()
    p = Phonepe(b)
    print((p.checkBalance()))