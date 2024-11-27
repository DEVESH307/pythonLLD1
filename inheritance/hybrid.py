import math


class Base:
    def __init__(self):
        print("Base Class Init")
        self.value = 1

    def speak(self):
        print("Base Method Base")


class Parent:
    def __init__(self):
        print("parent constructor")
        self.eyes = 2

    def speak(self):
        print("I am a parent")


class Child(Parent):
    def __init__(self):
        print("child constructor")
        self.age = 10
        super().__init__()

    def speak(self):
        print("I am a child")


class GrandChild(Child, Base):
    pass



class GrandChild2(Child):
    pass


gc = GrandChild()
gc.speak()

print(GrandChild.mro())