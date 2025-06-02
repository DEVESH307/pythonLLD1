# 0. Single Inheritance Example
# class Parent:
#     eyes = None
#     def __init__(self):
#         print("parent constructor")
#         self.eyes = 2

#     def speak(self):
#         print("I am a parent")


# class Child(Parent):
#     def __init__(self):
#         super().__init__()
#         print("child constructor")
#         self.age = 10

#     def speak(self):
#         print(self.eyes)
#         print("I am a child")

# c = Child()
# print(c.eyes)
# # Output:2
# c.speak()
# print(c.age)
# # Output:10


# # 1. Single Inheritance
# class parent:
#     def display(self):
#         print("display parent...")

# class child(parent):
#     def display(self):
#         print("display child...")

# c = child()
# c.display()
# # Output: display child...


# # 2. Single Inheritance with constructor
# class parent:
#     def __init__(self):
#         self.eyes = 2

#     def display(self):
#         print("display parent...")

# class child(parent):
#     def __init__(self, age):
#         self.age = age

# c = child(10)
# print(c.age)
# # Output: 10
# print(c.eyes)
# # Output: error, as eyes is not defined in child class
# # To fix the error, we can call the parent constructor in the child constructor


# # 3. Single Inheritance with constructor and method overriding
# class parent:
#     def __init__(self):
#         self.eyes = 2

#     def display(self):
#         print("display parent...")

# class child(parent):
#     def __init__(self, age):
#         super().display()
#         self.age = age

# c = child(10)
# print(c.age)
# # Output: 10
# print(c.eyes)
# # Output: 2
# c.display()
# # Output: display parent...


# # 4. Single Inheritance with constructor, method overriding, and attribute initialization
# class parent:
#     def __init__(self):
#         self.eyes = 2

#     def display(self):
#         print("display parent...")

# class child(parent):
#     def __init__(self, age):
#         self.eyes = 1
#         super().__init__()
#         self.age = age

# c = child(10)
# print(c.age)
# # Output: 10
# print(c.eyes)
# # Output: 2
# c.display()
# # Output: display parent...


# # 5. Single Inheritance with constructor, method overriding, and attribute initialization (with different order of initialization)
# class parent:
#     def __init__(self):
#         self.eyes = 2

#     def display(self):
#         print("display parent...")

# class child(parent):
#     def __init__(self, age):
#         super().__init__()
#         self.eyes = 1
#         self.age = age

# c = child(10)
# print(c.age)
# # Output: 10
# print(c.eyes)
# # Output: 1
# c.display()
# # Output: display parent...


# # 6. Single Inheritance with constructor, method overriding, and multiple display methods
# class parent:
#     def __init__(self):
#         self.eyes = 2

#     # def display(self, a):
#     #     print("a display")

#     def display(self):
#         print("display parent...")

#     def display(self, a):
#         print("a display")

# class child(parent):
#     def __init__(self, age):
#         self.eyes = 1
#         self.age = age
#         super().display()

# c = child(10)
# print(c.age)
# # Output: 10
# print(c.eyes)
# # Output: 1
# c.display()
# # Output: TypeError: parent.display() missing 1 required positional argument: 'a'


# # 7. Single Inheritance with constructor, method overriding, and multiple display methods (with different order of initialization)
# class parent:
#     # def __init__(self, a):
#     #     self.eyes = 3

#     def __init__(self):
#         self.eyes = 2

#     def __init__(self, a):
#         self.eyes = 3

#     def display(self):
#         print("display parent...")

#     def display(self, a):
#         print("a display")

# class child(parent):
#     def __init__(self, age):
#         self.eyes = 1
#         self.age = age
#         super().display()

# c = child(10)
# # Output: error, as parent constructor is not called correctly
# print(c.age)
# # Output: 10
# print(c.eyes)
# # Output: 1
# c.display()
# # Output: TypeError: parent.display() missing 1 required positional argument: 'a'


# 8. Single Inheritance with constructor, method overriding, and attribute initialization (with different order of initialization)
class parent:
    eyes = None
    def __init__(self):
        self.eyes = 2

    def display(self):
        print("display parent...")

class child(parent):
    def __init__(self, age):
        self.eyes = 1
        self.age = age
        super().display()

    def display(self):
        super().display()
        print("child display...")

c = child(10)
# output: display parent...
print(c.age)
# Output: 10
print(c.eyes)
# Output: 1
c.display()
# Output: display parent...
# Output: child display...

