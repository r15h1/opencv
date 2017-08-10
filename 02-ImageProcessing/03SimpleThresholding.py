# If pixel value is greater than a threshold value, it is assigned one value (may be white), else it is assigned another value (may be black). 
# The function used is cv2.threshold. First argument is the source image, which should be a grayscale image. 
# Second argument is the threshold value which is used to classify the pixel values. 
# Third argument is the maxVal which represents the value to be given if pixel value is more than (sometimes less than) the threshold value. 
# OpenCV provides different styles of thresholding and it is decided by the fourth parameter of the function. Different types are:

# cv2.THRESH_BINARY
# cv2.THRESH_BINARY_INV
# cv2.THRESH_TRUNC
# cv2.THRESH_TOZERO
# cv2.THRESH_TOZERO_INV

import cv2
import numpy as np
from matplotlib import pyplot as plt

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('Messi.jpg',0)
ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
ret,thresh2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
ret,thresh3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
ret,thresh4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
ret,thresh5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)

titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]

for i in xrange(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()