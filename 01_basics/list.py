tea_varities = ["green", "black", "herbal", "earl grey"]
print(tea_varities)
print(tea_varities[0])
print(tea_varities[-1])
print(tea_varities[0:2])
print(tea_varities[-2:])

tea_varities[1:1] = "lemon"
print(tea_varities) #['green', 'l', 'e', 'm', 'o', 'n', 'black', 'herbal', 'earl grey']

tea_varities[1:1] = ["lemon"]
print(tea_varities) #['green', 'lemon', 'black', 'herbal', 'earl grey']

tea_varities[1:1] = []
print(tea_varities) #['green', 'black', 'herbal', 'earl grey']

for tea in tea_varities:
    print(tea, end = " ")

tea_varities.append("earl grey")
tea_varities.pop() #default last
tea_varities.remove("earl grey")

tea_varities.insert(1, "earl grey")
tea_varities.clear()

squared_nums = [x**2 for x in range(10)]
print(squared_nums)