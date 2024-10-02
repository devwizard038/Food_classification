import os
import cv2
import numpy as np

# Path to the folder containing the images
folder_path = '../Not Setup/'

# Loop through all the files in the folder
for filename in os.listdir(folder_path):
    if "_" in filename:
        continue
    # Read the image
    img_path = os.path.join(folder_path, filename)
    img = cv2.imread(img_path)

    # Add Gaussian noise to the image
    mean = 0
    std_dev = 15
    noisy_img = img + np.random.normal(mean, std_dev, img.shape)

    # Clip the pixel values to the valid range [0, 255]
    noisy_img = np.clip(noisy_img, 0, 255).astype(np.uint8)
    
    # New file name with "A_" added at the back
    base_filename, file_extension = os.path.splitext(filename)
    new_filename = base_filename + "_A" + file_extension

    # Save the noisy image with the new file name
    cv2.imwrite(os.path.join(folder_path, new_filename), noisy_img)
    print("Processed:", filename)

print("Noise addition complete!")