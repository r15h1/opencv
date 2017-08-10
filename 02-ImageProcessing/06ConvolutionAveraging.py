# done by convolving the image with a normalized box filter. 
# It simply takes the average of all the pixels under kernel area and replaces the central element with this average. 
# This is done by the function cv2.blur() or cv2.boxFilter(). Check the docs for more details about the kernel. 
# We should specify the width and height of kernel

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('Messi.jpg')

blur = cv2.blur(img,(5,5))

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()