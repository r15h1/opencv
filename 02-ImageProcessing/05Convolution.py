# As for one-dimensional signals, images also can be filtered with various low-pass filters (LPF), high-pass filters (HPF), etc. 
# A LPF helps in removing noise, or blurring the image. 
# A HPF filters helps in finding edges in an image.

# OpenCV provides a function, cv2.filter2D(), to convolve a kernel with an image. 
# As an example, we will try an averaging filter on an image. A 5x5 averaging filter kernel can be defined.
# Filtering with the above kernel results in the following being performed: 
#   for each pixel, a 5x5 window is centered on this pixel, 
#   all pixels falling within this window are summed up, and the result is then divided by 25. 
#   This equates to computing the average of the pixel values inside that window. 
#   This operation is performed for all the pixels in the image to produce the output filtered image. 

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('Messi.jpg')

kernel = np.ones((5,5),np.float32)/25
dst = cv2.filter2D(img,-1,kernel)

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(dst),plt.title('Averaging')
plt.xticks([]), plt.yticks([])
plt.show()