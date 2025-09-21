from pathlib import Path

# Current working directory
p = Path.cwd()
print(p)   # e.g., "/home/umair/projects"

# Create a new path
desktop = Path.home() / "Desktop"
print(desktop)

# List files in a directory
for file in desktop.iterdir():
    print(file)

# Check if a path exists
print(desktop.exists())   # True/False

# Check if it's a file or folder
print(desktop.is_file())
print(desktop.is_dir())

# Make directory
(Path.cwd() / "new_folder").mkdir(exist_ok=True)

# Rename
(Path("old.txt")).rename("new.txt")

# Delete file
Path("new.txt").unlink()

# Delete empty folder
Path("new_folder").rmdir()

# Read and write text
f = Path("hello.txt")
f.write_text("Hello Umair!")   # create/write
print(f.read_text())           # read
