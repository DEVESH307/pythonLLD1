from typing import List, Any, Dict, Optional, Union, Tuple

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


def prinVal(valL: Any) -> None:
    print(val)


prinVal(10)
print([10])

# Generics...


# class Stack:
#     def __init__(self) -> None:
#         self.stack: List[int] = []
#
#     def push(self, val: int) -> None:
#         self.stack.append(val)
#
#     def pop(self) -> int:
#         return self.stack.pop()
#
#
# class Stack:
#     def __init__(self) -> None:
#         self.stack: List[str] = []
#
#     def push(self, val: str) -> None:
#         self.stack.append(val)
#
#     def pop(self) -> str:
#         return self.stack.pop()


from typing import Generic, TypeVar

R = TypeVar("R")


class Stack(Generic[R]):
    def __init__(self, val: List[R]) -> None:
        self.stack: List[R] = val

    def push(self, val: R) -> None:
        self.stack.append(val)

    def pop(self) -> R:
        return self.stack.pop()


# stack1 = Stack[int](["a", "v"])

T = TypeVar("T", int, float)


def add(a: T, b: T) -> T:
    return a + b


def add2(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    return a + b


add2(1, 2.0)


def test(*args: Tuple[int, float]) -> None:
    print(args)


test((1, 2.0))

from typing import Callable, TypeVar

T1 = TypeVar("T1")
R1 = TypeVar("R1")


def log_dec(func: Callable[[T1], R1]) -> Callable[[T1], R1]:
    def wrapper(*args: T1, **kwargs: T1) -> R1:
        print("hello")
        return func(*args, **kwargs)

    return wrapper


@log_dec
def double(x: int) -> int:
    return x * 2


result = double(10)
