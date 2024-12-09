from functools import reduce
from typing import Callable, Iterable

x = lambda f: (f - 32) * 5 / 9

list_f = [32, 68, 104]

print(list(map(x, list_f)))

# add a number as a param to list using map

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = map(lambda x, y: x + y, a[::2], a[1::2])

print(list(result))

z = list(map(lambda i: a[i] + a[i + 1], range(0, len(a), 2)))
print(z)

m = filter(lambda k: k % 2 == 0, a)

print(m)
print(list(m))

num = [1, 2, 3, 4, 5]

output = filter(lambda x: x * x > 10, num)

val = filter(lambda x: x > 10, map(lambda x: x * x, num))
print(list(val))

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

product = reduce(lambda x, y: x * y, nums, 0)

print(product)

val = reduce(lambda x, y: x + y, filter(lambda x: x > 10, map(lambda x: x * x, num)))

print(val)

a = [10]

print(reduce(lambda x, y: x + y, a))

addr: Callable[[int, int], int] = lambda x, y: x + y

val = map(lambda x: x * x, num)

for x in val:
    print(x)

val: Callable[[Iterable[int]], int] = reduce(lambda x, y: x + y, filter(lambda x: x > 10, map(lambda x: x * x, num)))
