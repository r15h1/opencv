# Morphological transformations are some simple operations based on the image shape. 
# It is normally performed on binary images. 
# It needs two inputs, one is our original image, second one is called structuring element or kernel which decides the nature of operation. 
# Two basic morphological operators are Erosion and Dilation. Then its variant forms like Opening, Closing, Gradient etc also comes into play. 
# We will see them one-by-one with help of following image:

# The basic idea of erosion is just like soil erosion only, it erodes away the boundaries of foreground object (Always try to keep foreground in white). 
# So what does it do? The kernel slides through the image (as in 2D convolution). 
# A pixel in the original image (either 1 or 0) will be considered 1 only if all the pixels under the kernel is 1, otherwise it is eroded (made to zero).

# So what happends is that, all the pixels near boundary will be discarded depending upon the size of kernel. 
# So the thickness or size of the foreground object decreases or simply white region decreases in the image. 
# It is useful for removing small white noises (as we have seen in colorspace chapter), detach two connected objects etc.

import cv2
import numpy as np

img = cv2.imread('Messi.jpg',0)
kernel = np.ones((5,5),np.uint8)
erosion = cv2.erode(img,kernel,iterations = 1)
cv2.imshow('erosion',erosion)

# It is just opposite of erosion. Here, a pixel element is 1 if atleast one pixel under the kernel is 1. 
# So it increases the white region in the image or size of foreground object increases. 
# Normally, in cases like noise removal, erosion is followed by dilation. Because, erosion removes white noises, but it also shrinks our object. 
# So we dilate it. Since noise is gone, they won't come back, but our object area increases. It is also useful in joining broken parts of an object.
dilation = cv2.dilate(img,kernel,iterations = 1)
cv2.imshow('dilation',dilation)

#Morphological Gradient - It is the difference between dilation and erosion of an image.
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
cv2.imshow('gradient',gradient)

cv2.waitKey(0)
cv2.destroyAllWindows()