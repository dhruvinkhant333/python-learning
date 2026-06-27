# To open the file, use the built-in open() function.

# The open() function returns a file object, which has a read() method for reading the content of the file:

f = open("Python File Handling/demofile.txt")
print(f.read())
f.close()
# Note: You should always close your files. In some cases, due to buffering, changes made to a file may not show until you close the file.

# Then you do not have to worry about closing your files, the with statement takes care of that.

with open("Python File Handling/demofile.txt") as f:
    print(f.read())


# ------------------------ Read Only Parts of the File ----------------------- #
# By default the read() method returns the whole text, but you can also specify how many characters you want to return:


with open("Python File Handling/demofile.txt") as f:
    print(f.read(10))


# -------------------------------- Read Lines -------------------------------- #
# You can return one line by using the readline() method:

with open("Python File Handling/demofile.txt") as f:
    print(f.readline())

# By looping through the lines of the file, you can read the whole file, line by line:

with open("Python File Handling/demofile.txt") as f:
    for x in f :
        print(x)