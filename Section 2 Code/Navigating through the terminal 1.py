# show the terminal on PyCharm and on the command line

# ls, cd, mkdir


import os

# print(os.getcwd())

# terminal dragging files

directory = os.chdir("/Users/guillermovalleschavez/Downloads")

# print(os.listdir(directory))

# os.rename("1345hhhssg.PNG", "Screenshot.PNG")

# check existance of a path

print(os.path.exists("hello"))

# check for files
print(os.path.isfile("python"))
#
# check for directory
print(os.path.isdir("PNG"))