# Q. square the list using lambda functions

my_list = [5, 4, 3]
# print(list(map(lambda item: item * 2, my_list)))


# Q. List sorting using lambda.
a = [(0, 2), (4, 3), (10, -1), (9, 9)]
a.sort(key=lambda k: k[1])
# print(a)



# Q find duplicates in list using complrehensions

some_list = ['a', 'a', 'b','c','d','e','n', 'm','n','o','z','e']

duplicates = list(set([x for x in some_list if some_list.count(x) > 1]))
print(duplicates)