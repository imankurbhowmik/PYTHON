# variables
age = 22
age = 30
print(age)

# datatypes
first_name = "Ankur"
is_online = False

print("Hello World")

#string concatenation
name = input("What is your name ? ")
print("Hello " + name)

#type conversion
birth_year = input("Enter your birth year: ")
age = 2025 - int(birth_year)
print(age)
int()
float()
bool()
str()

#sum
first = float(input("Type first number "))
second = float(input("Type second number "))
sum = first + second
print("Sum : " + str(sum))

#strings
str = "python for beginners"
print(str.upper())
print(str) #doesnt change
print(str.find('y'))
print(str.replace('for', '4'))
print("Python" in str)

# arithmatic operators
print(10 + 2)
print(10 / 4)
print(10 // 4)
print(10 % 2)
print(10 ** 2)
x = 4
x += 5
print(x)

# operator precedence
x = 3 + 7 * 6
y = (3 + 7) * 6
print(y)

# comparison operators
x = 3 > 4
y = 5 <= 5
z = 5 == 6
c = 5 != 7

# logical operators
price = 5
print(price > 4 and price < 7)
print(price < 3 or price > 8)
print(not price < 6)

# if
temperature = 23

if temperature > 30 :
    print("Its a hot day")
    print("Drink plenty of water")
elif temperature > 20 :
    print("Its a nice day")
else :
    print("Its cold")
print("Done")

# exercise
weight  = float(input("Enter weight : "))
unit = input("(K)g or (L)bs ")

if unit.upper() == "K" :
    converted = weight / 0.45
    print("Weight in lbs is : " + str(converted))
else :
    converted = weight * 0.45
    print("Weight in kg is : " + str(converted))

# while loops
i=1
while i<=5 :
    print(i)
    i = i + 1

i=1
while i<=5 :
    print(i * '*')
    i = i + 1


# lists
names = ["Ankur", "Hehe"]
print(names)
print(names[0])
print(names[-2])
names[0] = "jon"
print(names[0:3])

numbers = [1, 3, 4, 6, 7 , 0]
numbers.append(9)
print(numbers)
numbers.insert(0, -1)
numbers.remove(4)
numbers.clear()
print(1 in numbers)
print(len(numbers))

# for loops
for item in numbers:
    print(item)

j = 0
while j < len(numbers) :
    print(numbers[j])
    j = j+1


# range function
nums = range(5)
nums2 = range(5,10)
nums3 = range(5, 10, 2)
print (nums)

for numbers in nums:
    print(numbers)


# tuples
integers = (1, 2, 3, 3)
print(integers.count(3))
print(integers.index(1))