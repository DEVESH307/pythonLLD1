from Design_pattrens.factoryDP.flutter.factories.AndroidFactory import *
from Design_pattrens.factoryDP.flutter.factories.IOSFactory import *



class OSFactory:
    def decide(self, val):
        if val == "Android":
            return AndroidFactory()
        else:
            return IosFactory()
