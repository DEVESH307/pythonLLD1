from Design_pattrens.prototype.Zombie import *

z = Zombie(100, sword=sword(100))

arr = []
for i in range(100):
    arr.append(Zombie(100, sword=sword(100)))

arr[0].health = 0

arr[0].sword.val = 9

print(arr[0].sword.val)
print(arr[1].sword.val)