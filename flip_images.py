import os
import cv2
import random

# Path to the folder containing the images
folder_path = "../Not Setup/"

# List all files in the folder
files = os.listdir(folder_path)

for file in files:
    if "_" in file:
        continue
    # Read the image
    image = cv2.imread(os.path.join(folder_path, file))
    
    # Randomly choose to flip horizontally or vertically
    flip_direction = random.choice([0, 1])
    flipped_image = cv2.flip(image, flip_direction)
    
    # Get the filename without extension
    filename = os.path.splitext(file)[0]
    
    # Save the flipped image with "_D" added to the filename
    cv2.imwrite(os.path.join(folder_path, filename + "_D.jpg"), flipped_image)
    print("Flipped:", file)
    
print("Done!")