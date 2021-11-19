import cv2
import os
from os import listdir, name
from os.path import isfile, join

dir = "C:/Users/xrace/Desktop/Pack 1 -- Portraits"

list = os.listdir(dir) # dir is your directory path
number_image = len(list)


onlyfiles = [f for f in listdir(dir) if isfile(join(dir, f))]

print(onlyfiles)

for i in range(number_image):

  author = onlyfiles[i]



  dirname = "C:/Users/xrace/Desktop/Pack 1 -- Portraits/%s"%author
  os.mkdir(dirname)

  image_name = "C:/Users/xrace/Desktop/Pack 1 -- Portraits/%s.png"%author
  
  input = cv2.imread(image_name)

  # Get input size
  height, width = input.shape[:2]

  a = round(500/width, 3)
    
  newh = int(height * a)
  neww = 500

  g = 1
  while g < 7:
    if g == 1:
      x = 50
      size = "50px_%s.png"%author
    elif g ==2:
      x = 20
      size = "20px_%s.png"%author
    elif g == 3:
      x = 10
      size = "10px_%s.png"%author
    elif g == 4 :
      x = 4 
      size = "4px_%s.png"%author
    elif g == 5 :
      x = 2 
      size = "2px_%s.png"%author


    z = round(x/width, 3)
    
    y = int(height * z)

    if g == 6 :
      x = 1 
      y = 1 
      size = "1px_%s.png" %author

    # Resize input to "pixelated" size
    temp = cv2.resize(input, (x, y), interpolation=cv2.INTER_LINEAR)

    # Initialize output image
    output = cv2.resize(temp, (neww, newh), interpolation=cv2.INTER_NEAREST)


    cv2.imwrite(os.path.join(dirname, size), output)
    g = g + 1
  cv2.imwrite(os.path.join(dirname, "%s.png"%author), input)
  os.remove(image_name)
