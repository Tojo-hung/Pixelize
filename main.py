import cv2
import os

dir = # folder with images

list = os.listdir(dir) # dir is your directory path
number_image = len(list)

for i in range(number_image):
 
  image_name = "%d.png"%i
  
  input = cv2.imread(image_name)

  # Get input size
  height, width = input.shape[:2]

  # Desired "pixelated" size
  w, h = (x, 16)

# Resize input to "pixelated" size
temp = cv2.resize(input, (w, h), interpolation=cv2.INTER_LINEAR)

# Initialize output image
output = cv2.resize(temp, (width, height), interpolation=cv2.INTER_NEAREST)

cv2.imshow('Input', input)
cv2.imshow('Output', output)

cv2.waitKey(0)
