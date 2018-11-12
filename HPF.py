import cv2
import numpy as np
from matplotlib import pyplot as plt
#HPF
img = cv2.imread('coin1-spnoise3.bmp',cv2.IMREAD_GRAYSCALE)
f = np.fft.fft2(img) 
fshift = np.fft.fftshift(f)

rows, cols = img.shape
crow, ccol = rows/2, cols/2 
d = 60
fshift[crow-d:crow+d, ccol-d:ccol+d] = 0

f_ishift = np.fft.ifftshift(fshift)
img_back = np.fft.ifft2(f_ishift)
img_back = np.uint8(np.abs(img_back))

cv2.imshow('input image',img)
cv2.imshow('fft image',img_back)
cv2.waitKey(0)