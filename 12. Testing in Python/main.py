# Testing - in python stands for checking that each unit, feature and functionality of our code giving satisfied result.
# writing a function here and will test in test.py


def do_stuff(num=0):
    try:
        if num:
            return int(num) + 10
        else:
            return "please enter numbers"
    except ValueError as err:
        return err
