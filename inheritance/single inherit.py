class Parent:
    eyes = None
    def __init__(self):
        print("parent constructor")
        self.eyes = 2

    def speak(self):
        print("I am a parent")


class Child(Parent):
    def __init__(self):
        super().__init__()

        print("child constructor")
        self.age = 10

    def speak(self):
        print(super.eyes)
        print("I am a child")


c = Child()
print(c.eyes)
c.speak()
