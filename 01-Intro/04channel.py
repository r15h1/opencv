import cv2
import numpy as np

img = cv2.imread('Messi.jpg')

px = img[100,100]
print px

blue = img[100, 100, 0]
print blue

#better pixel accessing method
# accessing RED value
print img.item(100,100,0)
print img.item(100,100,1)
print img.item(100,100,2)

# modifying RED value
img.itemset((10,10,2),100)
print img.item(10,10,2)

#returns a tuple of number of rows, columns and channels (if image is color):
print img.shape

#total number of pixels
print "size: {0}", img.size

#image datatype
print img.dtype
ball = img[100:60, 160:120]
img[0:0, 60:60] = ball

while(1):
    cv2.imshow('image',img)
    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()