#  := walrus operator asssign the value from a long expressions.

a = "heloooooooooooooo"

if len(a) > 10:
    print(f"Too lengthy, {len(a)} characters")
# -------------------

if (n := len(a)) > 10:
    print(f"Too lengthy, {n} characters")

# ----------------------

while ((n:= len(a)) > 1):
    print(a)
    a = a[:-1]