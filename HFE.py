import cv2
import numpy as np

#HPF
img = cv2.imread('coin1.bmp',cv2.IMREAD_GRAYSCALE)
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)

rows,cols = img.shape
D0=60
h = np.zeros((rows,cols))
for i in range(rows):
	for j in range(cols):
		h[i,j] = 1.0-np.exp(-((i-rows/2.0)**2+(j-cols/2.0)**2)/(2*(D0**2)))

hfe = 0.5+(0.75*h)
f_i = hfe*fshift

f_i = np.fft.ifftshift(f_i)
img_back = np.fft.ifft2(f_i)
img_back = np.uint8(np.abs(img_back))

cv2.imshow('input_image',img)
cv2.imshow('ft',img_back)
cv2.waitKey(0)