import cv2
import numpy as np

def negative(image):
    image = abs(255-image)
    return image

image = cv2.imread("coin1.bmp",cv2.IMREAD_GRAYSCALE)
output = negative(image);

cv2.imshow("input", image)
cv2.imshow("output", output)
cv2.waitKey(0)
