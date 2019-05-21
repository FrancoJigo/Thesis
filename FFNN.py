import numpy as np
import matplotlib.pyplot as plt
import os
import cv2

# def sigmoid(x):
#     return 1.0/(1+ np.exp(-x))

# def sigmoid_derivative(x):
#     return x * (1.0 - x)

# class NeuralNetwork:
#     def __init__(self, x, y):
#         self.input      = x
#         self.weights1   = np.random.rand(self.input.shape[1],4) 
#         self.weights2   = np.random.rand(4,1)                 
#         self.y          = y
#         self.output     = np.zeros(self.y.shape)

#     def feedforward(self):
#         self.layer1 = sigmoid(np.dot(self.input, self.weights1))
#         self.output = sigmoid(np.dot(self.layer1, self.weights2))

#     def backprop(self):
#         # application of the chain rule to find derivative of the loss function with respect to weights2 and weights1
#         d_weights2 = np.dot(self.layer1.T, (2*(self.y - self.output) * sigmoid_derivative(self.output)))
#         d_weights1 = np.dot(self.input.T,  (np.dot(2*(self.y - self.output) * sigmoid_derivative(self.output), self.weights2.T) * sigmoid_derivative(self.layer1)))

#         # update the weights with the derivative (slope) of the loss function
#         self.weights1 += d_weights1
#         self.weights2 += d_weights2


DATADIR= "C:/Users/63917/Documents/Jigo/Thesis/images/Training"
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

def create_training_data():
    for category in CATEGORIES:
        path = os.path.join(DATADIR,category) #path to species 1 to 9
        class_num = CATEGORIES.index(category)
        for img in os.listdir(path):
            try:
                img_array = cv2.imread(os.path.join(path,img), cv2.IMREAD_GRAYSCALE)
                new_array = cv2.resize(img_array,(image_size,image_size))
                training_data.append([new_array,class_num ])
            except Exception as e:
                pass
create_training_data()
print(len(training_data))

import random

random.shuffle(training_data)

for  sample in training_data[:10]:
    print(sample[1])

X = []
y = []

for features, label in training_data:
    X.append(features)
    y.append(label)

X = np.array(X).reshape(-1,image_size,image_size, 1)


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
# print(X[1])



# if __name__ == "__main__":
#     X = np.array([[0,0,1],
#                   [0,1,1],
#                   [1,0,1],
#                   [1,1,1]])
#     y = np.array([[0],[1],[1],[0]])
#     nn = NeuralNetwork(X,y)

#     for i in range(1500):
#         nn.feedforward()
#         nn.backprop()

#     print(nn.output)