print("hello world")

def python(n):
    print("hello " + n)

python("Ankur")

import os
os.getcwd() # get current working directory

for c in "chai":
    print(c)

import sys
sys.platform  # get platform win32

from importlib import reload # reload
reload() #put imported file name

import math
print(math.pi)

import random
print(random.random())
print(random.choice([1, 2, 3, 4, 5]))
print(random.randint(1, 10))
print(random.shuffle([1, 2, 3, 4, 5]))

l1 = [1, 2, 3, 4, 5]
import copy

l2 = copy.copy(l1) 
l3 = copy.deepcopy(l1) # deep copy

# l1 is l2 and l1 is l3 gives false but l1==l2 and l1==l3 gives true