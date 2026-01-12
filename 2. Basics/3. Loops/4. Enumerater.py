# enumerate()

# for index, char in enumerate([1,2,3,4,5]):
#  print(index, char)

# ------------------------------

for index, number in enumerate(list(range(100))):
    if number == 5:
        print(f"index of 5 is {index}")
