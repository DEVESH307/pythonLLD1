from typing import List, Any, Dict, Optional

age: int = 10

print(age)

age = 20
print(age)


#  TYPING TECHNIQUES...

def sqrDivideBy2(num: float) -> int:
    return int((num * num) // 2)


val: int = sqrDivideBy2(10.0)


def printSqr(num: int) -> None:
    print(num * num)


printSqr(10)

# nums: List[Any] = [1, 2, 3, 4, 5, 6, 67, "dsknf"]
nums: List[int] = [1, 2, 3, 4, 5, 6, 67]

valDict: dict[int, str] = {1: "hey", 2: "2"}

numset: set[int] = {1, 2, 3, 4, 5, 6, 67}

z: List[List[int]] = [[1, 2, 4], [1, 2, 456], [5]]

TypeVector = list[list[int]]
m: TypeVector = [[1, 2, 3, 5], [1, 2, 3]]


def greet(name: Optional[str] = None) -> str:
    return f"Hello, {name}"


print(greet())


class Person:

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age


def getPersonName(person: Person) -> str:
    return person.name


getPersonName(Person("john", 10))



def prinVal(valL: Any)-> None:
    print(val)

prinVal(10)
print([10])

# Generics...