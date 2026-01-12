# return keyword
# return break the function and come out

def sum(x, y):
    def an_func(a, b):
        return a + b
    return an_func(x,y)

total = sum(10,10)
print(total)