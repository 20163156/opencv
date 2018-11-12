import cv2
import numpy as np

def median_filter(image):
	copy = image.copy()

	height = np.size(copy,0)
	width  = np.size(copy,1)

	for i in range(1, height-1):
		for j in range(1, width-1):
			neighbors = []

			for k in range(-1, 2):
				for l in range(-1, 2):

					nei_li = image[i+k, j+l]
					neighbors.append(nei_li)

			neighbors.sort()
			median = neighbors[4]
			copy[i,j] = median

	return copy

def laplace_filter(image):

	copy = image.copy()

	height = np.size(copy,0)
	width  = np.size(copy,1)

	laplace = np.array([[-1,-1,-1],[-1,9,-1],[-1,-1,-1]])

	for i in range(1, height-1):
		for j in range(1, width-1):
			sum= 0
			for k in range(-1, 2):
				for l in range(-1, 2):

					a = image[i+k, j+l]
					w = laplace[1+k,1+l]
					sum = sum + (a * w)
			
			copy[i,j] = sum

	return copy

def gauss_filter(image):

	copy = image.copy()

	height = np.size(copy,0)
	width  = np.size(copy,1)

	gauss = (1.0/57) * np.array(
			[[0, 1, 2, 1, 0],
			[1, 3, 5, 3, 1],
			[2, 5, 9, 5, 2],
			[1, 3, 5, 3, 1],
			[0, 1, 2, 1, 0]])

	for i in range(2, height-2):
		for j in range(2, width-2):
			sum= 0
			for k in range(-2, 3):
				for l in range(-2, 3):

					a = image[i+k, j+l]
					w = gauss[2+k,2+l]
					sum = sum + (a * w)
			
			copy[i,j] = sum

	return copy
'''
image = cv2.imread('coin1-spnoise5.bmp', cv2.IMREAD_GRAYSCALE)
output = median_filter(image)
cv2.imshow('median_input',image)
cv2.imshow('median_output',output)


image2 = cv2.imread('coin3-blur.bmp', cv2.IMREAD_GRAYSCALE)
output2 = laplace_filter(image2)
cv2.imshow('laplace_input',image2)
cv2.imshow('laplace_output',output2)
'''

image3 = cv2.imread('coin3-gaussian.bmp', cv2.IMREAD_GRAYSCALE)
output3 = gauss_filter(image3)
cv2.imshow('gauss_input',image3)
cv2.imshow('gauss_output',output3)


cv2.waitKey(0)
