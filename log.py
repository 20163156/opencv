import cv2
import numpy as np

def negative(image):
    image = np.uint8(abs(255-image))
    return image

def log_trans(image):
	image = np.uint8(40* np.log1p(abs(image)));
	return image

def inverse_trans(image):
	image = np.uint8(np.exp(image/40)-1);
	return image

def root_trans(image):
	image = np.uint8(np.sqrt(image))
	#hist_nor(image)
	return image

def power_trans(image,gamma):
    image = image / 255.0
    image = np.power(image,gamma)
    image = np.uint8(image*255)

    return image

image = cv2.imread("coin1.bmp",cv2.COLOR_BGR2GRAY)

#output = negative(image)
#output = log_trans(image)
#output = inverse_trans(image)
#output = root_trans(image)
#output = power_trans(image,0.2)
#output = power_trans(image,3.0)

cv2.imshow("input", image)
cv2.imshow("output", output)

cv2.waitKey(0)
