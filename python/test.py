#!/usr/bin/env python
# coding: utf-8

# In[17]:
import sys 
# print "脚本名：", sys.argv[0]  
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

# image = cv.imread('./nums/00005.png', cv.IMREAD_GRAYSCALE)
# image = image.astype('float32')
# image = 255-image
# image /= 255

image = cv.imread(sys.argv[1],cv.IMREAD_GRAYSCALE)
image = cv.resize(image,(28,28),interpolation=cv.INTER_CUBIC)

image = image.astype('float32')
image = 255-image
image /= 255

model2 = tf.keras.models.load_model("../python/model.h5")

pred = model2.predict(image.reshape(1, 28, 28, 1), batch_size=1)

print(pred.argmax())
