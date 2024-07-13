character_name = "Antony"
character_age = "29"

print("There one was a man named " + character_name + ",")
print("he was " + character_age + " years old,")

character_name = "Suresh"
print("Hee really liked the name " + character_name + ",")
print("but didn't like being " + character_age + ".")

# working with strings
print("Anthony\n\"Suresh\"")
phrase = "Antony suresh"
print(phrase + " is cool")
print(phrase.upper())
print(phrase.lower())
print(phrase.isupper())
print(phrase.upper().isupper())
print(phrase.lower())
print(phrase.upper().islower())
print(len(phrase))
print(phrase[0])
print(phrase.index("A"))
print(phrase.index("suresh"))
print(phrase.replace("suresh", "M"))

# working with numbers
print(2)
print(2 + 4)
print(2 + 4.5)
print(2 - 4.5)
print(2 * 4.5)
print(2 / 4.5)
print(3 * 4 + 5)
print(10 % 3)

my_num = 5
print(str(my_num) + " My favorite number")

number = -10
print(number)
print(abs(number))

print(pow(3, 3))
print(max(3, 5))
print(min(3, 5))

print(round(3.4))
print(round(3.6))

from math import *

print(floor(3.6))
print(ceil(3.4))
print(sqrt(4))
