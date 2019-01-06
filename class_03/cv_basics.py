# OpenCV --> to work with Images, read or write or resize
# pip install opencv-python

import cv2
import numpy as np

img = cv2.imread("hero.jpg")

print(img)
print(img.shape)

for i in range(img.shape[0]):
	for j in range(img.shape[1]):
		if(img[i,j,:].all()>=250):
			img[i,j,:] = np.array([0,255,0])

print("Loop Complete!")
cv2.imshow("My Image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()





