# ------------------------------- Delete a File ------------------------------ #
# To delete a file, you must import the OS module, and run its os.remove() function:

# Example:
# import os
# os.remove("Python File Handling/myfile.txt")

# --------------------------- Check if File exist: --------------------------- #
# To avoid getting an error, you might want to check if the file exists before you try to delete it:

import os

file_path = "Python File Handling/myfile.txt"
if os.path.exists(file_path):
    # os.remove(file_path)
    print(f"File '{file_path}' exists and can be deleted.")
else:
    print(f"The file '{file_path}' does not exist.")


# ------------------------------- Delete Folder ------------------------------ #
# To delete an entire folder, use the os.rmdir() method:

# Example:
import os
os.rmdir("myfolder")

# Note: You can only remove empty folders.

# --------------------- Delete a Non-Empty Folder (BE CAREFUL) --------------------- #
# To delete a folder and all of its contents, use the shutil.rmtree() function.
# This is a powerful and destructive operation. It deletes everything inside!

import shutil

folder_path = "my_non_empty_folder"

if os.path.exists(folder_path):
    # shutil.rmtree(folder_path) # Uncomment to actually delete
    print(f"Folder '{folder_path}' and all its contents can be deleted.")
else:
    print(f"Folder '{folder_path}' does not exist.")