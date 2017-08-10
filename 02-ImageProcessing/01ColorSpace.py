# convert images from one color-space to another, like BGR \leftrightarrow Gray, BGR \leftrightarrow HSV etc
# There are more than 150 color-space conversion methods available in OpenCV. 
# But we will look into only two which are most widely used ones, BGR \leftrightarrow Gray and BGR \leftrightarrow HSV
# For BGR rightarrow Gray conversion we use the flags cv2.COLOR_BGR2GRAY. 
# Similarly for BGR \rightarrow HSV, we use the flag cv2.COLOR_BGR2HSV.

import cv2
flags = [i for i in dir(cv2) if i.startswith('COLOR_')]
print flags