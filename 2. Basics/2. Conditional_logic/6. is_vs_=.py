# == checks value equality (same value, type conversion may happen)
# is checks identity (same object in memory)

# Truthy values:
# 1, non-empty strings, non-empty lists

# Falsy values:
# 0, empty string "", empty list []

# Examples:
# True == 1  -> True
# print(True == 1)

# "" == 1    -> False
# print('1' == False)

# [] == 1    -> False
# print([1] == False)

# 10 == 10.0 -> True
# print(10 == 10.0)

# [] == []   -> True
# [] is []   -> False

print([123] is [123])
print([123] == [123])

# Memory concept:
# Numbers and strings may share memory
# Lists, dicts, sets create new memory every time
# If a = b, both point to same object -> a is b is True
