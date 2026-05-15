import os

# Define the current and new names
old_name = "files/trial-rename.jpeg"
new_name = "files/mad-sokka.jpeg"

# Rename the file
os.rename(old_name, new_name)

print("File renamed successfully!")
