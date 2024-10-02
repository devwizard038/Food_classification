import cv2
import os
import numpy as np

folder_path = '../Not Setup/'

for filename in os.listdir(folder_path):
  # Read the image
  img_path = os.path.join(folder_path, filename)
  image = cv2.imread(img_path)

  # Convert the image to grayscale
  gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

  # Apply thresholding (you can use other image processing techniques here)
  _, thresh = cv2.threshold(gray, int(gray.mean()), 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

  # Find contours in the thresholded image
  contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

  # Find the largest contour based on area
  largest_contour = max(contours, key=cv2.contourArea)

  # Get the bounding box of the largest contour
  x, y, w, h = cv2.boundingRect(largest_contour)

  # Crop the region of interest (ROI) from the original image
  cropped_image = image[y:y+h, x:x+w]

  # Display the cropped image
  cv2.imwrite(img_path , cropped_image)
  print("Cropped:", filename)