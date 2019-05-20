#part1
import tensorflow as tf
import keras
from keras.backend.tensorflow_backend import set_session
from keras.models import Sequential
from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense

#part2
from keras.preprocessing.image import ImageDataGenerator

#part3
from IPython.display import display
from PIL import Image

#For testing
import numpy as np 
from keras.preprocessing import image

# import regularizer
from keras.regularizers import l1	
from keras.regularizers import l2



config = tf.ConfigProto(
    gpu_options = tf.GPUOptions(per_process_gpu_memory_fraction=0.10)
    # device_count = {'GPU': 1}
)
config.gpu_options.allow_growth = True
session = tf.Session(config=config)
set_session(session)



#Initialize the CNN
classifier = Sequential()

#Step1 Convolution
classifier.add(Convolution2D(32,3,3,input_shape = (64,64,3),activation='relu',  bias_regularizer=l2(0.01)))

#Step2 Pooling
classifier.add(MaxPooling2D(pool_size = (2,2)))

#Step3 Flattening
classifier.add(Flatten())

#Step4 Full Connection
classifier.add(Dense(output_dim = 128, activation = 'relu'))
classifier.add(Dense(output_dim = 9, activation ='softmax'))

#Compiling the CNN
classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

#Part 2 Fitting  the CNN to the images
train_datagen = ImageDataGenerator(rescale = 1./255, shear_range = 0.2, zoom_range = 0.2, horizontal_flip = True)

test_datagen = ImageDataGenerator(rescale = 1./255)

training_set = train_datagen.flow_from_directory('images/Training', target_size = (64,64), batch_size = 32, class_mode = 'categorical')

test_set = test_datagen.flow_from_directory('images/Test', target_size = (64,64), batch_size = 32, class_mode='categorical')

classifier.fit_generator(training_set,steps_per_epoch = 8000, epochs = 10, validation_data = test_set, validation_steps = 800)

classifier.save('CNN-5.model')
