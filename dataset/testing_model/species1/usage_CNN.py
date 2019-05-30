import numpy as np
from keras.preprocessing import image
import tensorflow as tf
from Uniform_Cropping import crop_image
import glob, os, errno
import cv2

mydir = r'C:/Users/63917/Documents/Jigo/Thesis/images/testingmodel/species1'
new_width = 1000     #Enter the crop image width
new_height = 1000    #Enter the crop image height
for fil in glob.glob("*.jpg"):
	image = cv2.imread(fil,0)
	cropped_img = crop_image(fil,new_height,new_width)
	test_image = cropped_img.load_img(cropped_img, target_size = (64,64))
	test_image = cropped_img.img_to_array(test_image)
	test_image = np.expand_dims(test_image, axis = 0)
	model = tf.keras.models.load_model("CNN.model")
	result = model.predict(test_image)
	print(result)
