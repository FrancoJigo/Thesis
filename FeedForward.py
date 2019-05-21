# Load libraries
import numpy as np
from keras.datasets import reuters
from keras.utils.np_utils import to_categorical
from keras.preprocessing.text import Tokenizer
from keras import models
from keras import layers

# Set random seed
np.random.seed(0)

# Set the number of features we want
number_of_features = 6

# Load feature and target data
# (train_data, train_target_vector), (test_data, test_target_vector) = reuters.load_data(num_words=number_of_features)


# Convert feature data to a one-hot encoded feature matrix
tokenizer = Tokenizer(num_words=number_of_features)
train_features = tokenizer.sequences_to_matrix(train_data, mode='binary')
test_features = tokenizer.sequences_to_matrix(test_data, mode='binary')

# One-hot encode target vector to create a target matrix
train_target = to_categorical(train_target_vector)
test_target = to_categorical(test_target_vector)