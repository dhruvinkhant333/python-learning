# ------------------------- Write to an Existing File ------------------------ #

# To write to an existing file, you must add a parameter to the open() function:
# "a" - Append - will append to the end of the file
# "w" - Write - will overwrite any existing content


with open("Python File Handling/demofile.txt" , "a") as f:
    f.write("now the file has more content ! ")

# open and read the file after the appending :

with open("Python File Handling/demofile.txt") as f:
    print(f.read())


# ------------------------ Overwrite Existing Content ------------------------ #

# To overwrite the existing content to the file, use the w parameter:

with open("Python File Handling/demofile.txt" , "w") as f:
    f.write("woops! i have deleted the content!")

#open and read the file after overwritting :

with open("Python File Handling/demofile.txt") as f:
    print(f.read())

# Note: the "w" method will overwrite the entire file.



# ----------------------------- Create a New File ---------------------------- #

# To create a new file in Python, use the open() method, with one of the following parameters:

# "x" - Create - will create a file, returns an error if the file exists
# "a" - Append - will create a file if the specified file does not exists
# "w" - Write - will create a file if the specified file does not exists

f = open("Python File Handling/myfile.txt" , "a")