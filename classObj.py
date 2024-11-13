#
# person_1_name = 'karan'
# person_1_age = 18
# person_1_psp = 30
#
# def print_std(std_1_name, std_1_age, std_1_psp):
#     print("name:" + std_1_name + " age:" + str(std_1_age) + " psp:" + str(std_1_psp))
#
#
# person_2_name = 'dushyant' # instructor
# person_2_age = 30
#
# print_std(person_1_name, person_1_age, person_1_psp)
#
# def print_inst(person_1_name, person_1_age, classrating_1):
#     print("name:" + person_1_name + " age:" + str(person_1_age) + " class_r:" + str(classrating_1))
#
# person_2_class_rating = 20
#
# print_inst(person_2_name, person_2_age, person_2_class_rating)
#


#  PUBLIC:

class student:
    name = None
    psp = None

    def __init__(self, name, psp):
        self.name = name
        self.psp = psp

    def print_name(self):
        print(self.name)


karan = student("karan", 20)
karan.print_name()

vinod = student("vinod", 40)
vinod.print_name()
print("name:" + vinod.name)


#  ACCESS MODIFIERS:

#  PRIVATE:

class PrivateStudent:

    def __init__(self, name):
        self.__name = name

    def print_name(self):
        print(self.__name)


abc = PrivateStudent("abc")
# abc.print_name()

print("private var:" + abc._PrivateStudent__name)


#  PROTECTED

class Father:

    def __init__(self, name):
        self._name = name


class Child(Father):
    pass


f = Father("father abc")
c = Child("child abc")

print("father_name:" + f._name)