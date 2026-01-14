# @decorators are like a super charge for our functions. it gives our functions some extra power.

# Higher Ordered Functions - A functions which expect a function as arg OR return a functions is called HOF.


def my_decorator(func):
    def wrap_func():
        print("*********")
        func()
        print("*********")

    return wrap_func


@my_decorator
def hello():
    print("hello")


# hello2 = my_decorator(hello)
# hello2()


# ------Making our own Decorator to find the performance time---------

from time import time


def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f"took {t2 - t1} s")
        return result

    return wrapper

@performance
def long_time():
    for i in range(1000):
        i * 5

long_time()