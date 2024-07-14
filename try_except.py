# Catching errors in python

# Try / Except Method

# number = int(input("Enter a number: "))

# value = 10/0
# try:
#     # value = 10 / 0
#     number = int(input("Enter a number: "))
#     print(number)
# except ZeroDivisionError:
#     print("Divided by zero")
# except ValueError:
#     print("Invalid Input")


try:
    answer =  value = 10 / 0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("Invalid Input")
