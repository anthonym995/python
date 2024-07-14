# python read wite file

# for reading the file
# open("friends.txt", "read")

# for writing the file
# open("friends.txt", "write")

# for append the file
# open("friends.txt", "a")

# for read and write
# open("friends.txt", "r+")

# for read
# open("friends.txt", "r")


# friends_file = open("friends.txt", "r")
# print(friends_file.readable()) gives true



# friends_file = open("friends.txt", "w")
# print(friends_file.readable()) gives false


# actually reads the file
friends_file = open("friends.txt", "r")
# print(friends_file.read())
# print(friends_file.readline())
# print(friends_file.readline())
# print(friends_file.readlines())
# print(friends_file.readlines()[0])

# using for loops
for friend in friends_file.readlines():
    print(friend)



friends_file.close()