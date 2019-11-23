#!/usr/bin/env python
# coding: utf-8

# In[17]:
import tensorflow as tf 

from keras.layers import Dense, Flatten, Dropout
from keras.layers import Conv2D, MaxPooling2D
from keras.models import Sequential
from keras.datasets import mnist
from keras.losses import categorical_crossentropy
from keras.utils.np_utils import to_categorical
from keras import backend as K
from keras import optimizers
from PIL import Image
import cv2 as  cv
import matplotlib.pyplot as plt
import time
import numpy as np
import os

# Load mnist data
(X_train, y_train), (X_test, y_test) = mnist.load_data()
w = h = X_train.shape[1] # image size(width, height)
lr = 1e-4 # learning_rate
adam = optimizers.Adam(lr) # adam optimizer
batch_size = 64 # batch size
y_dim = 10 # output dimension
epochs = 4

# Pre-processing data
X_train, X_test = X_train / 255., X_test / 255.
X_train, X_test = X_train.reshape([X_train.shape[0], 28, 28, 1]), X_test.reshape([X_test.shape[0], 28, 28, 1])
X_train = X_train.astype(np.float32, copy=False)
X_test = X_test.astype(np.float32, copy=False)

y_train = to_categorical(y_train, y_dim)
y_test = to_categorical(y_test, y_dim)

# CNN model(with convolutional layers, maxpooling layers and dropout layers)
model = Sequential()
model.add(Conv2D(32, kernel_size=(3, 3), activation='relu'))
model.add(Conv2D(32, kernel_size=(3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(y_dim, activation='softmax'))

# Complie the model
model.compile(loss = categorical_crossentropy,optimizer = adam, metrics=['accuracy'])

# Training session
history = model.fit(X_train, y_train, batch_size = batch_size, epochs = epochs,
         validation_data = (X_test, y_test), verbose = 1)

# Report loss and accuracy for test data
score = model.evaluate(X_test, y_test, verbose=0)
print('Test loss:', score[0])
print('Test accuracy:', score[1])


model.save("model.h5") # 把模型保存成 h5 文件


# image = cv.imread('./nums/00005.png', cv.IMREAD_GRAYSCALE)
# image = image.astype('float32')
# image = 255-image
# image /= 255

# model2 = tf.keras.models.load_model("model.h5")

# pred = model2.predict(image.reshape(1, 28, 28, 1), batch_size=1)

# print(pred.argmax())
