import tensorflow as tf

from tensorflow.keras import layers
from tensorflow.keras import Model

from tensorflow.keras.optimizers import RMSprop

# For data: X_train, X_validation, y_train, y_validation
# OR datagenerated data: train_generator, validation_generator

###---STANDARD MODEL CREATION---###
model = tf.keras.models.Sequential(
                                  [tf.keras.layers.Conv2D(16, (2,2), activation = 'relu', input_shape = (9,9,3),
                                   tf.keras.layers.Flatten(),
                                   tf.keras.layers.Dense(32, activation = 'relu'),
                                   tf.keras.layers.Dense(1, activation = 'sigmoid')
                                   ])
                                   
model.compile(loss = 'binary_crossentropy', optimizer = RMSprop(lr=1e-4), metrics = ['acc']                                 

###---CHECK POINTING---###
filepath = '../file/path/etc/weights.{epoch:02d}-{val_loss:.2f}.hdf5'
checkpoint = tf.keras.callbacks.ModelCheckpoint(filepath,
                                                monitor = 'val_loss',
                                                verbose = 0,
                                                save_best_only = False,
                                                save_weights_only = False,
                                                mode = 'auto',
                                                period = 1)
                                                
###---LOADING MODEL---###
modified_model = tf.keras.models.load_model('model/file/path.hdf5')

modified_model.compile('loss = 'binary_crossentropy', optimizer = RMSprop(lr=1e-4), metrics = ['acc'])
