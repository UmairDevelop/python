import os

# Get current working directory
print(os.getcwd())   # e.g., "/home/umair/projects"

# Change working directory
os.chdir("/home/umair/Desktop")

# List files in a directory
print(os.listdir("."))   # "." means current folder

# Make a new directory
os.mkdir("test_folder")

# Make multiple directories at once
os.makedirs("a/b/c", exist_ok=True)

# Remove a directory (only if empty)
os.rmdir("test_folder")

# Remove multiple dirs
os.removedirs("a/b/c")

# Rename a file or folder
os.rename("old.txt", "new.txt")

# Delete a file
os.remove("new.txt")

# Join paths safely (instead of manual "/")
path = os.path.join("/home/umair", "file.txt")
print(path)
