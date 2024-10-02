import os

# Specify the folder path
folder_path = "../Not Setup/"

# Get a list of all files in the folder
files = os.listdir(folder_path)

# Create a dictionary to store file names without extensions and their counts
file_counts = {}

# Count the occurrences of each file name without extension
for file in files:
    file_name, file_extension = os.path.splitext(file)
    file_counts[file_name] = file_counts.get(file_name, 0) + 1

# Delete files with count greater than 1
for file_name, count in file_counts.items():
    if count > 1:
        for file in files:
            if file.startswith(file_name):
                file_path = os.path.join(folder_path, file)
                os.remove(file_path)
                print(f"Deleted file: {file_path}")