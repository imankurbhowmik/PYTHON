chai_types = {"masala": "spicy", "ginger": "sweet", "lemon": "sour"}

print(chai_types)
print(chai_types["masala"])
print(chai_types.get("masala"))

chai_types["masala"] = "very spicy"

for chai in chai_types:
    print(chai, chai_types[chai])

for chai, taste in chai_types.items():
    print(chai, taste)

chai_types["mint"] = "refreshing"

chai_types.pop("masala")  # remove key "masala"
chai_types.popitem()  # remove last inserted item

del chai_types["ginger"]  # delete key "ginger"

chai_types_copy = chai_types.copy()  # shallow copy

tea_shop = {
    "chai": {
        "masala": 10,
        "ginger": 5
    },
    "coffee": {
        "black": 10,
        "earl grey": 5
    }
}

squared_nums = {x: x**2 for x in range(10)}
squared_nums.clear()  # clear all items

keys = ["masala", "ginger", "lemon"]
default_values = "delicious"
chai_types = dict.fromkeys(keys, default_values)  # create dictionary with default values