# If statements

# is_male = False
#
# if is_male:
#     print("You are not a male")


# or operator with else statement
# is_male = True
# is_tall = True
#
# if is_male or is_tall:
#     print("You are a male or tall or both")
# else:
#     print("You neither male nor tall")

# is_male = True
# is_tall = False
#
# if is_male and is_tall:
#     print("You are a tall male")
# elif is_male and not is_tall:
#     print("You are a short male")
# elif not is_male and is_tall:
#     print("You are not a male but are tall")
# else:
#     print("You are not a male or not tall")


# if statement and comparison
def man_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


print(man_num(300, 20, 60))