from abc import ABC, abstractmethod


class Switchable(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass


class light(Switchable):

    def turn_off(self):
        print("Turning off the light")

    def turn_on(self):
        print("Turning on the light")


class Switch:
    def __init__(self, switchable: Switchable):

        self.switchable = switchable

    def toogle(self, state):
        if state == "off":
            self.switchable.turn_off()
        else:
            self.switchable.turn_on()


class Fan(Switchable):

    def turn_on(self):
        print("Turning on the fan")

    def turn_off(self):
        print("Turning off the fan")


l = light()

f = Fan()
s = Switch(l)

s.toogle("off")



# CLASS METHODS:

class MNO:
    var = 1

    @classmethod
    def tryMethod(cls):
        print("try")
        cls.var += 1
        return cls.var


print(MNO.tryMethod())
