import cv2
import numpy as np

# load image
img = cv2.imread('cleared_border.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # convert to grayscale
# threshold to get just the signature (INVERTED)
retval, thresh_gray = cv2.threshold(gray, thresh=100, maxval=255,type=cv2.THRESH_BINARY_INV)

image, contours, hierarchy = cv2.findContours(thresh_gray,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img,contours,-1,(0,255,0),3)

for h,cnt in enumerate(contours):
    mask = np.zeros(gray.shape,np.uint8)
    cv2.drawContours(mask,[cnt],0,255,-1)
    mean = cv2.mean(img,mask = mask)


moments = cv2.moments(cnt)
print(moments)
area = moments['m00']
print(area)
cv2.imshow("Contours", img)
cv2.waitKey(0)
