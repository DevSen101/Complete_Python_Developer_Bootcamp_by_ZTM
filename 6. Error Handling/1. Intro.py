# Error handling  - handling the errors
# Typeerror
# Syntax error
# Zerovalue error
# index error ........etc

# --------------------------------
while True:
    try:
        age = int(input("Please enter your age: "))
        10 / age
        raise Exception('hey cut it out')
    except ValueError:  # when we give anywrong value like string
        print("Not a valid age.")
        continue
    except ZeroDivisionError:   #when we give zero error
        print("Enter age higher than 0")
        break
    else:                             #if there is no exception then this run
        print("Thank You!")
        # break
    finally:
        print('Ok! finally i am done')
    print('Can u hear me!')     


# -------------------------------------


# def sum(n1, n2):
#     try:
#         return n1 + n2
#     # except TypeError
#     # except TypeError as err:
#     # except (TypeError, ZeroDivisionError):
#     except (TypeError, ZeroDivisionError) as err:

#         print("Oops! something went wrong", err)


# print(sum(1, '5'))
