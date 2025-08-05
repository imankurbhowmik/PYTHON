# operator overloading
print("ankur" + "bhowmik")

x=1
y=2
z=3
print(x,y,z)  # comma separated 1 2 3

a = repr("ankur") #'ankur'
b = str("ankur")
print("ankur")
print(a)
print(b)

import math
print(math.floor(2.5))
print(math.floor(-2.5))  # -3
print(math.trunc(-2.5))  # -2

#oct(64)  or int("64", 8)
#hex(64)
#bin(64)

#0.1 + 0.1 + 0.1 issue
from decimal import Decimal
print(Decimal('0.1') + Decimal('0.1') + Decimal('0.1')) #0.3

from fractions import Fraction
print(Fraction(1, 3) + Fraction(1, 3) + Fraction(1, 3))

setOne = {1, 2, 3, 4, 5}
setTwo = {4, 5, 6, 7, 8}
print(setOne.union(setTwo))
print(setOne.intersection(setTwo))
print(setOne - {1, 2, 3, 4, 5})  #set()

print(True + 0)
print(True + 1)
print(False + 0)
print(False + 1)
print(True + True)  #2