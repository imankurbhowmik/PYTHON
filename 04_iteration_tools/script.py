import time

print("Ankur is here")

username = "Ankur"
print(username)

# f = open("script.py")
# f.readline()
# f.__next__()
# iter(f) is f  true

# for line in open("script.py"):
#     print(line)

# while True:
#     line = f.readline()
#     if not line: break
#     print(line)


myList = [1, 2, 3, 4, 5]

I = iter(myList)
# I is myList  false

print(I.__next__()) # Output: 1
print(I.__next__())      # Output: 2