import cv2
import numpy as np
 

img = cv2.imread('C:/Users/Jigu/OneDrive/Documents/Thesis/Thesis/Square-implementation/1.jpg' , 0) # import image as grayscale array

# threshold image
img_b = cv2.GaussianBlur(img, (13, 13), 2)
ret, img_th = cv2.threshold(img_b, 40, 255, cv2.THRESH_BINARY_INV)
# find contours
(_,cnts,_) = cv2.findContours(img_th.copy(), cv2.RETR_TREE, 
cv2.CHAIN_APPROX_SIMPLE)
print(str(len(cnts))+' contours detected')

# find maximum area contour
area = np.array([cv2.contourArea(cnts[i]) for i in range(len(cnts))]) # 
list of all areas
maxa_ind = np.argmax(area) # index of maximum area contour

plt.figure(figsize=(10,4))
plt.subplot(1,3,1)
plt.imshow(img_b)
plt.title('GaussianBlurr')
plt.subplot(1,3,2)
plt.imshow(img_th)
plt.title('threshold')
plt.subplot(1,3,3)
xx = [cnts[maxa_ind][i][0][0] for i in range(len(cnts[maxa_ind]))]
yy = [cnts[maxa_ind][i][0][1] for i in range(len(cnts[maxa_ind]))]
ROI.append([min(xx),max(xx),min(yy),max(yy)])
plt.imshow(img)
plt.plot(xx,yy,'r',linewidth=3)
plt.title('largest contour')