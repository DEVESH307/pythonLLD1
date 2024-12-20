
from Design_pattrens.factoryDP.flutter.factories.OSFactory import OSFactory
def deploy(val):
    abs = OSFactory().decide(val)
    Button = abs.create_button().click()


if __name__ == '__main__':
    deploy("ios")