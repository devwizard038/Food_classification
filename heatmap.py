import numpy as np
import tensorflow as tf
from keras.models import Model
from keras.models import load_model
from keras.applications.vgg16 import preprocess_input
import cv2
from keras import backend as K
import matplotlib.pyplot as plt

model = load_model('my_model.h5')
vgg_model = model.get_layer('vgg16')

image_path = './Good/X39-GPJ.jpg'
img = cv2.imread(image_path)
img = cv2.resize(img, (150, 150))
img = np.expand_dims(img, axis=0)
img = img.astype('float32')
img /= 255.
preprocessed_input = preprocess_input(img)

model.predict(img)

layer_name = 'block3_conv1'
filter_index = 0
layer_output = vgg_model.get_layer(layer_name).output
loss = K.mean(layer_output[:, :, :, filter_index])
grads = K.gradients(loss, model.input)[0]

print(grads)