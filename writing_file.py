# Let's Write the file

# here we are appeand the file
# when we using w it will override the old file instead we can use this to create a new file
# friends_file = open("friends.txt", "r")
# friends_file = open("friends.txt", "a")
# friends_file = open("friends1.txt", "w")
friends_file = open("friends2.txt", "w")

# print(friends_file.read())
friends_file.write("<h1>Heading</h1>")

friends_file.close()
