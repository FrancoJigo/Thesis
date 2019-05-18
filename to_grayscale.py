import cv2


img= cv2.imread('C:/Users/Jigu/Documents/Thesis/Thesis/Square-implementation/images/1.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
median_filtered_image = cv2.medianBlur(gray, 3)
# cv2.imwrite('C:/Users/Jigu/Documents/Thesis/Thesis/Square-implementation/images/Test_gray.jpg', gray)
screen_res = 1280, 720
scale_width = screen_res[0] / img.shape[1]
scale_height = screen_res[1] / img.shape[0]
scale = min(scale_width, scale_height)
window_width = int(img.shape[1] * scale)
window_height = int(img.shape[0] * scale)

cv2.namedWindow('dst_rt_gray', cv2.WINDOW_NORMAL)
cv2.resizeWindow('dst_rt_gray', window_width, window_height)
cv2.namedWindow('dst_rt', cv2.WINDOW_NORMAL)
cv2.resizeWindow('dst_rt', window_width, window_height)
cv2.namedWindow('dst_rt_median', cv2.WINDOW_NORMAL)
cv2.resizeWindow('dst_rt_median', window_width, window_height)


cv2.imshow('dst_rt', img)
cv2.imshow('dst_rt_gray', gray)
cv2.imshow('dst_rt_median', gray)
cv2.waitKey(0)
cv2.destroyAllWindows()