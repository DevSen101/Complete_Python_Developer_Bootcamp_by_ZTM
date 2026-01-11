# for loop

# for item in [1, 2, 3, 4, 5, 6, 7, 8]:
#     print(f"item is:  {item}")

# for i in (1, 2, 3):
#     for x in ["a", "b", "c", "d"]:
#         print(i, x)

# for iterate in iterable
# iterate - one by one check each item in the collection
# iterable - is collection which iterate it can be list, dictionary, tuple, set, string

user = {"name": "Dev", "age": 21, "can_swim": False}

for item in user:
    print(item)


# return items()
for item in user.items():
    print(item)

# return key()
for item in user.keys():
    print(item)

# return values()
for item in user.values():
    print(item)

for key, value in user.items():
    print(f'key: {key}, value: {value}')