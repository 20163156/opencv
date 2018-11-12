
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('coin1-spnoise3.bmp',cv2.IMREAD_GRAYSCALE)
f = np.fft.fft2(img) 
fshift = np.fft.fftshift(f)

rows, cols = img.shape
crow, ccol = rows/2, cols/2 

d = 60
fshift[0:rows, 0:ccol-d] = 0
fshift[0:rows, ccol+d:cols] = 0

fshift[0:crow-d, 0:cols] = 0
fshift[crow+d:rows,0:cols] = 0


f_ishift = np.fft.ifftshift(fshift)
img_back = np.fft.ifft2(f_ishift)
img_back = np.uint8(np.abs(img_back))

cv2.imshow('input image',img)
cv2.imshow('fft image',img_back)
cv2.resizeWindow('image', 600,600)

cv2.waitKey(0)