import cv2
import numpy as np
 
# Read image
image= cv2.imread('Segmentedimage.jpg')
     
# grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# cv2.imshow('gray', gray)

# binary
ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)
# cv2.imshow('threshold', thresh)

# dilation
kernel = np.ones((10, 1), np.uint8)
img_dilation = cv2.dilate(thresh, kernel, iterations=1)
# cv2.imshow('dilated', img_dilation)

# find contours
im2, ctrs, hier = cv2.findContours(img_dilation.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# sort contours
sorted_ctrs = sorted(ctrs, key=lambda ctr: cv2.boundingRect(ctr)[0])

for i, ctr in enumerate(sorted_ctrs):
    # Get bounding box
    x, y, w, h = cv2.boundingRect(ctr)

    # Getting ROI
    roi = image[y:y + h, x:x + w]

    # show ROI
    # cv2.imshow('segment no:'+str(i),roi)
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    if w > 15 and h > 15:
        cv2.imwrite('C:\\Users\\PC\\Desktop\\output\\{}.png'.format(i), roi)

# window scaling
screen_res = 1280, 720
scale_width = screen_res[0] / image.shape[1]
scale_height = screen_res[1] / image.shape[0]
scale = min(scale_width, scale_height)
window_width = int(image.shape[1] * scale)
window_height = int(image.shape[0] * scale)

cv2.namedWindow('marked_areas', cv2.WINDOW_NORMAL)
cv2.resizeWindow('marked_areas', window_width, window_height)

cv2.imshow('marked_areas', image)
cv2.waitKey(0)