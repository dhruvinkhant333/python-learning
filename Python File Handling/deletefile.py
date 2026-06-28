# ------------------------------- Delete a File ------------------------------ #
# To delete a file, you must import the OS module, and run its os.remove() function:

import os
os.remove("Python File Handling/myfile.txt")


# --------------------------- Check if File exist: --------------------------- #
# To avoid getting an error, you might want to check if the file exists before you try to delete it:

import os 
if os.path.exists("Python File Handling/myfile.txt"):
    os.remove("Python File Handling/myfile.txt")
else:
    print("the file does not exist")


# ------------------------------- Delete Folder ------------------------------ #
# To delete an entire folder, use the os.rmdir() method:

import os 
os.rmdir("myfolder")

# Note: You can only remove empty folders.