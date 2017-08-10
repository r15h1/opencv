# Contours can be explained simply as a curve joining all the continuous points (along the boundary), 
# having same color or intensity. 
# The contours are a useful tool for shape analysis and object detection and recognition.

# For better accuracy, use binary images. 
# So before finding contours, apply threshold or canny edge detection.
# findContours function modifies the source image. So if you want source image even after finding contours, already store it to some other variables.
# In OpenCV, finding contours is like finding white object from black background. So remember, object to be found should be white and background should be black.


import numpy as np
import cv2

im = cv2.imread('Messi.jpg')
imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,127,255,0)

# find contours in an image
# there are three arguments in cv2.findContours() function, 
#   first one is source image, 
#   second is contour retrieval mode, 
#   third is contour approximation method. 
# 
# And it outputs the image, contours and hierarchy. 
# contours is a Python list of all the contours in the image. 
# Each individual contour is a Numpy array of (x,y) coordinates of boundary points of the object.

image, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

# To draw the contours, cv2.drawContours function is used. 
# It can also be used to draw any shape provided you have its boundary points. 
# Its first argument is source image, second argument is the contours which should be passed as a Python list, 
# third argument is index of contours (useful when drawing individual contour. 
# To draw all contours, pass -1) and remaining arguments are color, thickness etc.

#To draw all the contours in an image:
#img = cv2.drawContours(im, contours, -1, (0,255,0), 3)
#cv2.imshow('contour',image)

#To draw an individual contour, say 4th contour:
#img2 = cv2.drawContours(im, contours, 3, (0,255,0), 3)
#cv2.imshow('individual contour',img2)

#But most of the time, below method will be useful:
cnt = contours[10]
img3 = cv2.drawContours(im, [cnt], 0, (0,255,0), 3)
cv2.imshow('individual contour 2',img3)

cv2.waitKey(0)
cv2.destroyAllWindows()