import os, shutil
import tensorflow as tf
import keras
from keras import layers, regularizers
from keras import models
from keras.models import load_model
from keras import optimizers
from keras.preprocessing.image import ImageDataGenerator
from keras import metrics
from keras.applications import VGG16, InceptionResNetV2

callbacks_list = [
    keras.callbacks.EarlyStopping(
        monitor='acc',
        patience=10,
    ),
    keras.callbacks.ModelCheckpoint(
        filepath='my_model.h5',
        monitor='val_loss',
        save_best_only=True,
    )
]

train_dir = '../Train'
validation_dir = '../Validate'

model = models.Sequential()
conv_base = InceptionResNetV2(weights='imagenet', include_top=False, input_shape=(224, 224, 3))
model.add(conv_base)
model.add(layers.Flatten())
model.add(layers.Dense(256, activation='relu', kernel_regularizer=regularizers.l2(0.01)))
model.add(layers.Dense(3, activation='softmax'))

"""

model = keras.models.load_model('my_model.h5')
"""
vgg_model = model.get_layer('vgg16')
vgg_model.summary()


vgg_model.trainable = True
set_trainable = False
for layer in vgg_model.layers:
    if layer.name == 'block5_conv1':
        set_trainable = True
    if set_trainable:
        layer.trainable = True
    else:
        layer.trainable = False


model.compile(loss='categorical_crossentropy', optimizer=optimizers.RMSprop(lr=1e-5), metrics=['acc'])

train_datagen = ImageDataGenerator(rescale=1./255, rotation_range=60, width_shift_range=0.2, height_shift_range=0.2, shear_range=0.2, zoom_range=0.2, horizontal_flip=True)
test_datagen = ImageDataGenerator(rescale=1./255)
train_generator = train_datagen.flow_from_directory(train_dir, target_size=(224, 224), batch_size=50, class_mode='categorical')
validation_generator = test_datagen.flow_from_directory(validation_dir, target_size=(224, 224), batch_size=50, class_mode='categorical')

model.fit_generator(train_generator, steps_per_epoch=216, epochs=100, validation_data=validation_generator, validation_steps=24, callbacks=callbacks_list)

model.save('weight.h5')