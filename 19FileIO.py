s = "Harry is a good boy. "

# Writing a file

with open("test.txt", "w") as f:
    f.write(s)

# OR

# fp=open("test.txt", "w")
# fp.write(s)
# fp.close()

# Reading a file

# with open("test.txt", "r") as f:
#     s = f.read()
#     print(s)

# OR

# f=open("test.txt", "r")
# s= f.read()
# print(s)
# f.close()

# Append a file

# with open("test.txt", "a") as f:
#     f.write(s)
#     print(s)

# OR

# f = open("test.txt", "a")
# f.write(s)
# print(s)
# f.close()
