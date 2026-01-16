# module - is basically a python file which has some functions we want to use.
# package - is one level up its a folder which have some one or more modules
import utility as oulala  # import utility and name as oulala
from utility import *  # from utility import everything
from utility import add
import shopping.shopping_cart
from shopping import shopping_cart
from shopping.shopping_cart import buy  # another way to import
import random

# print(utility.add(1, 2))
# print(shopping.shopping_cart.buy('apple'))

print(random)
help(random)
