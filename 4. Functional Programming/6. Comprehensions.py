# List Comprehension
# creating and doing actions on list in a good, eficient way .

# my_list = []
# for char in "HELLO":
#     my_list.append(char)

# print(my_list)


# syntax: param for param in iterable
my_list2 = [char for char in "HELLO"]
# print(my_list2)

# -------------------------

my_list3 = [num for num in range(0, 100)]
# print(my_list3)


# -------------------------

my_list3 = [num * 2 for num in range(0, 100)]
# print(my_list3)

# ------------------------------

my_list4 = [num**2 for num in range(0, 100) if num % 2 == 0]
# print(my_list4)


# Set Comprehensions (we just need to change the [] sign to {} to make set . all are same it will just follow set rule or only unique items will be init)

my_set = {char for char in "HELLO"}
# print(my_set)


# Dictionary Comprehensions

simple_dict = {"a": 1, "b": 2}

my_dict = {k: v * 2 for k, v in simple_dict.items()} #loop in list
my_dict2 = {k: v * 2 for k, v in simple_dict.items() if v % 2 == 0} #conditions
my_dict3 = {n:n*2 for n in [1,2,3]}

print(my_dict3)
