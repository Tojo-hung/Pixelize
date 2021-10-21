import cv2
import os

dir = "C:/Users/xrace/Documents/Pixel"

list = os.listdir(dir) # dir is your directory path
number_image = len(list)

for i in range(number_image):
  i = i+1

  image_name = "C:/Users/xrace/Documents/Pixel/image%d.png"%i
  
  input = cv2.imread(image_name)

  # Get input size
  height, width = input.shape[:2]

  g = 1
  while g < 5:
    if g == 1:
      x = 20
    elif g ==2:
      x = 10
    elif g == 3:
      x = 5
    elif g == 4 :
      x = 2 

    z = round(x/width, 2)
    
    y = int(height * z)
    print(y)

   

    # Resize input to "pixelated" size
    temp = cv2.resize(input, (x, y), interpolation=cv2.INTER_LINEAR)

    # Initialize output image
    output = cv2.resize(temp, (width, height), interpolation=cv2.INTER_NEAREST)

    cv2.imshow('Input', input)
    cv2.imshow('Output', output)

    k = cv2.waitKey(5000) & 0xff
    cv2.destroyAllWindows()
    g += 1
