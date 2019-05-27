# import the necessary packages
from sklearn.preprocessing import LabelBinarizer
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import numpy as np
import glob
import cv2
import os
import matplotlib.pyplot as plt


def load_image_features(inputPath):
	# initialize the list of column names in the CSV file and then
	# load it using Pandas
	names = ['name of image','aspect_ratio','equi_diameter','extent','solidity','minoraxis_length','eccentricity','Species']
	df = pd.read_csv(inputPath, sep=" ",header = 0,  names=names)

	species = df["Species"].value_counts().keys().tolist()
	name_images = df["name of image"].value_counts().keys().tolist()

	# for (specie, name_image) in zip(species,name_images):
	# 	if 

def process_image_features(df, train, test):
	features = ['aspect_ratio','equi_diameter','extent','solidity','minoraxis_length','eccentricity']
	cs = MinMaxScaler()
	trainContinuous = cs.fit_transform(train[features])
	testContinuous = cs.transform(test[features])

	zipBinarizer = LabelBinarizer().fit(df["Species"])
	trainCategorical = zipBinarizer.transform(train["Species"])
	testCategorical = zipBinarizer.transform(test["Species"])

	trainX = np.hstack([trainCategorical, trainContinuous])
	testX = np.hstack([testCategorical, testContinuous])

	return (trainX, testX)


# def load_images(df, inputPath):
# 	images = []
# 	basePath = os.path.sep.join([inputPath, "{}_*".format(i + 1)])
# 	copePaths = sorted(list(glob.glob(basePath)))

# 	inputImages = []
# 	outputImage = np.zeros((64, 64, 3), dtype="uint8")

# 	# loop over the input house paths
# 	for copePath in copePaths:
# 			# load the input image, resize it to be 32 32, and then
# 			# update the list of input images
# 		image = cv2.imread(copePath)
# 		image = cv2.resize(image, (32, 32))
# 		inputImages.append(image)
 
# 	# return our set of images
# 	return np.array(images)



DATADIR= "C:/Users/iPlay™/Documents/Thesis/images/Training"
CATEGORIES = ["class_0","class_1","class_2","class_3","class_4","class_5","class_6","class_7","class_8"]
for category in CATEGORIES:
    path = os.path.join(DATADIR,category) #path to species 1 to 9
    print(path)
    for img in os.listdir(path):
        img_array = cv2.imread(os.path.join(path,img), cv2.IMREAD_GRAYSCALE)
        plt.imshow(img_array,cmap = "gray")
        plt.show()
        break
    break
image_size = 64
new_array = cv2.resize(img_array,(image_size,image_size))
plt.imshow(new_array,cmap ='gray')
plt.show()
training_data = []

# def create_training_data():
#     for category in CATEGORIES:
#         path = os.path.join(DATADIR,category) #path to species 1 to 9
#         class_num = CATEGORIES.index(category)
#         for img in os.listdir(path):
#             try:
#                 img_array = cv2.imread(os.path.join(path,img), cv2.IMREAD_GRAYSCALE)
#                 new_array = cv2.resize(img_array,(image_size,image_size))
#                 training_data.append([new_array,class_num ])
#             except Exception as e:
#             	print('nothing')
#                 # pass
# create_training_data()
# print(len(training_data))
# print(len(training_data))
# for  sample in training_data[:10]:
#     print(sample[1])

# X = []
# y = []
# # print(X)
# for features, label in training_data:
#     X.append(features)
#     y.append(label)
# X = np.array(X).reshape(-1,image_size,image_size, 1)
# import pickle 

# pickle_out = open("X.pickle","wb")
# pickle.dump(X, pickle_out)
# pickle_out.close()

# pickle_out = open("y.pickle","wb")
# pickle.dump(y, pickle_out)
# pickle_out.close() 

# #Reading pickle again

# pickle_in = open("X.pickle","rb")
# X = pickle.load(pickle_in)

# #example 
# print(X)