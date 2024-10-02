import os
import cv2

# Path to the folder containing the images
folder_path = '../Not Setup/'

# Loop through all the files in the folder
for filename in os.listdir(folder_path):
    if "_" in filename:
        continue
    # Read the image
    img_path = os.path.join(folder_path, filename)
    img = cv2.imread(img_path)

    # Convert the image to grayscale
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # New file name with "A_" added at the back
    base_filename, file_extension = os.path.splitext(filename)
    new_filename = base_filename + "_B" + file_extension

    # Save the grayscale image with the new file name
    cv2.imwrite(os.path.join(folder_path, new_filename), gray_img)
    
    print(f"Processed: {filename}")

print("Conversion complete!")