import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('Messi.jpg',3)
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()