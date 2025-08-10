list = ["banana", "apple", "orange", "banana", "kiwi", "apple"]

unique_item = set()

for item in list:
    if item in unique_item:
        print("Duplicate item found:", item)
        break
    unique_item.add(item)