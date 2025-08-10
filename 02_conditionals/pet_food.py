pet = "dog"
age = 5

if pet == "dog":
    if age < 1:
        print("puppy food")
    elif age < 7:
        print("adult dog food")
    else:
        print("senior dog food")
elif pet == "cat":
    if age < 1:
        print("kitten food")
    elif age < 10:
        print("adult cat food")
    else:
        print("senior cat food")
else:
    print("unknown pet food")