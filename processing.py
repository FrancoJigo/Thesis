# coding: utf-8
import cv2
import numpy as np
import argparse
from interact_crop import *
from segmentation import *
from PIL import Image, ImageChops
from border_clear import *
from find_contours import *


def image_resize(img):
    img = cv2.imread(image, cv2.IMREAD_UNCHANGED) 
    # print('Original Dimensions : ',img.shape)     
    scale_percent = 60 # percent of original size
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    # resize image
    resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)     
    # print('Resized Dimensions : ',resized.shape)
    cv2.imshow("Resized_image", resized)
    resized_image = cv2.imwrite('Resized_image.jpg', resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    # return resized_image



ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())
image = args["image"]




#This is where all the main command is happening
image_resize(image)
image_crop('Resized_image.jpg')
image_segmentation('cropedimage.jpg')
image_clearborder('Segmentedimage.jpg')
image_findContour('cleared_border.jpg')

