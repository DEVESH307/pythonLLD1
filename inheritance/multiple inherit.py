# class Base:
#     def __init__(self):
#         print("Base Class Init")
#         self.value = 1
#
#     def base_method(self):
#         print("Base Method Base")
#

class Parent1:
    def __init__(self):
        print("Parent Class Init")
        self.nose = 1

    def func1(self):
        print("Parent1 Class func1")

    def func2(self, a):
        print("Parent1 Class func2" + a)


class Parent2:
    def __init__(self):
        print("Parent2 Class Init")
        self.name = "Parent2"

    def func2(self, a):
        print("Parent2 Class func2" + a)


class Child(Parent1, Parent2):
    def __init__(self):
        print("Child Class Init")
        Parent1.__init__(self)
        Parent2.__init__(self)
        self.legs = 2


c = Child()
print(c.name)
# c.func2()
Parent2.func2(c, "10")

print(Child.mro())
