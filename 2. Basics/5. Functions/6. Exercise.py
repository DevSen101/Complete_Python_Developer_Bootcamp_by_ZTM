# create a function to give highest even of list


def highest_even(li):
    evens = []
    for items in li:
        if items % 2 == 0:
         evens.append(items)
    return max(evens)


print(highest_even([1, 2, 3, 4, 9, 7, 8, 6, 4, 5, 1, 23, 5, 8, 45]))
