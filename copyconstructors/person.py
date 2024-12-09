# import copy
#
#
# class place:
#     def __init__(self, street):
#         self.street = street
#
#
# class attendance:
#     def __init__(self, value):
#         self.value = value
#
# class Person:
#     def __init__(self, name, age, adr, attd):
#         self.name = name
#         self.age = age
#         self.place = adr
#         self.att = attd
#
#     def __copy__(self):
#         new_att = copy.deepcopy(self.att)
#         return Person(self.name, self.age, self.place, new_att)
#
#
# person = Person("abc", 25, place("abc"))
#
# person4 = person
#
#
# #shallow copy
# person2 = copy.copy(person)
#
# person3 = copy.deepcopy(person)
#
# print(person3)
#
#
# person5 = person.__copy__()
#
#
#
from collections import namedtuple, deque, Counter, defaultdict, OrderedDict, ChainMap

Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x, p.y)


# DEQUE:  A double ended queue...

dq = deque(['a', 'b', 'c'])
dq.append('d') # Add to right..
print(dq)

dq.appendleft('z')
print(dq)

dq.pop()
print(dq)
dq.popleft()
print(dq)


data = [1,2,3,4,51,1,2,3,"a"]
z= "acbbdsn"
# find frequency of each..
counter = Counter(z)

print(counter)

dd = defaultdict(int)

dd['a'] +=1
print(dd)
print(dd['z'])


#  ordered list: sorting based on keys of input order..

od = OrderedDict()
od['a'] = 1
od['c'] = 2
od['b'] = 3

print(od)


# chainMap:

d1 = {'a': 1, 'b': 2}

d2 = {'b': 3, 'd': 4}

chain = ChainMap(d1, d2)

print(chain['b'])

chain['c'] = 5

print(chain)

print(d1)
#
# del chain['c']
#
# print(chain)
#
# del chain['d']
#
# print(chain)

chain['b'] = 5

print(chain)


