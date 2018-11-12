import cv2
import numpy as np

def histo(image):
	copy = image.copy();

	m = np.size(copy,0)
	n = np.size(copy,1)
	
	hist = np.zeros(256)
	hist_nor = np.zeros(256)
	hist_cumul = np.zeros(256)
	# histogram normalization
	for j in range(m):
		for i in range(n):

			hist[copy[j,i]] = hist[copy[j,i]] + 1

	for i in range(256):
		hist_nor[i] = hist[i] / (m * n)
		
	#histogram equalization
	for i in range(1,256):
		hist_cumul[i] = hist_cumul[i-1] + hist_nor[i]

	for i in range(256):
		hist_cumul[i] = round(hist_cumul[i] * 255.0)

	#cover
	for j in range(m):
		for i in range(n):
			copy[j,i] = hist_cumul[copy[j,i]]

	return copy
image = cv2.imread("coin1.bmp")
output = histo(image);
cv2.imshow("input", image)
cv2.imshow("output", output)
cv2.waitKey(0)