import cv2
import os

dir = "C:/Users/xrace/Documents/Pixel"

list = os.listdir(dir) # dir is your directory path
number_image = len(list)

for i in range(number_image):
  i = i+1

  dirname = "C:/Users/xrace/Documents/Pixel/image%d"%i
  os.mkdir(dirname)

  image_name = "C:/Users/xrace/Documents/Pixel/image%d.png"%i
  
  input = cv2.imread(image_name)

  # Get input size
  height, width = input.shape[:2]

  g = 1
  while g < 5:
    if g == 1:
      x = 20
      size = "20px_image%d.png"%i
    elif g ==2:
      x = 10
      size = "10px_image%d.png"%i
    elif g == 3:
      x = 5
      size = "5px_image%d.png"%i
    elif g == 4 :
      x = 2 
      size = "2px_image%d.png"%i

    z = round(x/width, 3)
    
    y = int(height * z)
    print(y)

   

    # Resize input to "pixelated" size
    temp = cv2.resize(input, (x, y), interpolation=cv2.INTER_LINEAR)

    # Initialize output image
    output = cv2.resize(temp, (width, height), interpolation=cv2.INTER_NEAREST)

    cv2.imshow('Output', output)
    cv2.imwrite(os.path.join(dirname, size), output)
    g += 1
  cv2.imwrite(os.path.join(dirname, "image%d.png"%i), input)
  os.remove(image_name)
