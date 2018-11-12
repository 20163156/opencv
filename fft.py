import cv2
import numpy as np
import matplotlib.pyplot as plt
def fourier():

	image = cv2.imread("coin1-spnoise3.bmp",cv2.IMREAD_GRAYSCALE)
	f = np.fft.fft2(image)
	fshift = np.fft.fftshift(f)
	magnitude_spectrum = 20 * np.log(np.abs(fshift))

	plt.subplot(1,1,1)
	plt.imshow(magnitude_spectrum,cmap = 'gray')
	plt.title('magnitude_spectrum'),plt.xticks([]),plt.yticks([])
	plt.show()
	
fourier();
