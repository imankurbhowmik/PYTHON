num = 10
even_numbers_sum = 0

for i in range(1, num + 1):
    if i % 2 == 0:
        even_numbers_sum += i
print("Sum of even numbers from 1 to", num, "is:", even_numbers_sum)