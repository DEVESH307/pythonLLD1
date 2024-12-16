import time

my_list = ['page 1', 'page 2', 'page 3', 'page4']

# for i in my_list:
#     print(i)

iterator = iter(my_list)

print(next(iterator))

# complex operation taking x secs...

print(next(iterator))

print(next(iterator))


# Range Method: start, end..

class my_itr:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.start <= self.end:
            temp = self.start
            self.start += 1
            return temp
        else:
            raise StopIteration


ite = my_itr(1, 10)

print(next(ite))  # 1

for i in my_itr(1, 10):
    print(i)


def infinite_fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


fib = infinite_fib()
print(next(fib))  # 0
print(next(fib))  # 0
print(next(fib))
print(next(fib))

print("abc--- logic that tool 100sec ")

print(next(fib))


def next_even(tillLimit):
    num = 0
    while num<tillLimit:
        yield num
        print("abc")
        num += 2


next_gen = next_even(5)

print(next(next_gen))
print(next(next_gen))