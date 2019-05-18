import cv2
import numpy as np

bounding_box_image = cv2.imread('C:/Users/Jigu/OneDrive/Documents/Thesis/Thesis/Square-implementation/Image_cont.jpg')
grayimage = cv2.cvtColor(bounding_box_image, cv2.COLOR_BGR2GRAY)

ret, mask = cv2.threshold(grayimage, 254, 255, cv2.THRESH_BINARY)

cv2.imshow('mask', mask)
cv2.waitKey(0)

image, contours, hierarchy = cv2.findContours(mask, cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)

for contour in contours:

    if cv2.contourArea(contour) < 200:
        continue

    rect = cv2.minAreaRect(contour)
    box = cv2.boxPoints(rect)

    ext_left = tuple(contour[contour[:, :, 0].argmin()][0])
    ext_right = tuple(contour[contour[:, :, 0].argmax()][0])
    ext_top = tuple(contour[contour[:, :, 1].argmin()][0])
    ext_bot = tuple(contour[contour[:, :, 1].argmax()][0])

    roi_corners = np.array([box], dtype=np.int32)

    cv2.polylines(bounding_box_image, roi_corners, 1, (255, 0, 0), 3)
    cv2.imshow('image', bounding_box_image)
    cv2.waitKey(0)

    cropped_image = grayimage[ext_top[1]:ext_bot[1], ext_left[0]:ext_right[0]]
    cv2.imwrite('crop.jpg', cropped_image)