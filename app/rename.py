import os

# Define the current and new names
old_name = "/files/trial.jpeg"
new_name = "/files/trial-ranme.jpeg"

# Rename the file
os.rename(old_name, new_name)
