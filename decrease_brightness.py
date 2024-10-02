import cv2
import os

# Function to decrease brightness of an image
def decrease_brightness(image):
    return cv2.convertScaleAbs(image, alpha=0.7, beta=0)

# Path to the folder containing the images
folder_path = '../Not Setup/'

# Loop through all files in the folder
for filename in os.listdir(folder_path):
    if "_" in filename:
        continue
    # Read the image
    image_path = os.path.join(folder_path, filename)
    image = cv2.imread(image_path)

    # Decrease brightness
    bright_decreased = decrease_brightness(image)

    # Save the modified image with "A_" added to the file name
    base_filename, file_extension = os.path.splitext(filename)
    new_filename = base_filename + "_C" + file_extension
    new_image_path = os.path.join(folder_path, new_filename)
    cv2.imwrite(new_image_path, bright_decreased)

    print(f"Processed: {filename}")

print("All images processed and saved with decreased brightness.")