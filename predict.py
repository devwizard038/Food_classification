import os, shutil
import tensorflow as tf
import keras
from keras import layers
from keras import models
from keras.models import load_model
from keras import optimizers
from keras.preprocessing.image import ImageDataGenerator
from keras import metrics
from keras.applications import VGG16
from keras.preprocessing import image
import numpy as np
import matplotlib.pyplot as plt

img_path = './Good/X39-GPJ.jpg'

model = load_model('my_model.h5')

img = image.load_img(img_path, target_size=(224, 224))
img_tensor = image.img_to_array(img)
img_tensor = np.expand_dims(img_tensor, axis=0)
img_tensor /= 255.
print(model.predict(img_tensor))

vgg16_model = model.layers[0]

# Get the activations from block5_conv2 layer of VGG16 model
layer_output = vgg16_model.get_layer('block1_conv1').output
activation_model = models.Model(inputs=vgg16_model.get_input_at(0), outputs=layer_output)

# Predict activations for the input image
activations = activation_model.predict(img_tensor)

# Display the activation of the first filter in block5_conv2 layer using 'viridis' colormap
plt.matshow(activations[0, :, :, 0], cmap='viridis')
plt.show()