input_string = "teeterabscd"

for char in input_string:
    if input_string.count(char) == 1:
        print("First non-repeated character is:", char)
        break