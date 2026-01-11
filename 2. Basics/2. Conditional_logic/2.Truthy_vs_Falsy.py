# In python everything is true except 0, false, empty string, empty set, empty list...

if "":
    print("This is empty")
else:
    print("Hii there")


# Short Circuiting (ignore the rest condition)

is_friend = True
is_user = False

if True or is_friend or is_user:
    print("You can talk")

if True  and is_friend:
    print("can't talk")
