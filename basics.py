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
unit = input("(K)g or (L)bs")

if(unit.upper() == "K") :
    converted = weight / 0.45
    print("Weight in lbs is : " + str(converted))
else :
    converted = weight * 0.45
    print("Weight in kg is : " + str(converted))