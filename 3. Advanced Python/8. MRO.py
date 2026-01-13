# MRO (Method Resolution Order) defines the sequence Python searches for methods/attributes in a class hierarchy, especially crucial for multiple inheritance.

# How It Works
# Python uses C3 linearization: class first, then parents left-to-right, respecting inheritance order without cycles.
# ​

# python
# class A: pass
# class B(A): pass
# class C(A): pass
# class D(B, C): pass

# print(D.__mro__)
# # (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)
# Check MRO Anytime
# ClassName.__mro__ - tuple of search order

# ClassName.mro() - returns same list