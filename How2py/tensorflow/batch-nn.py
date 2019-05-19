import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Train generator
train_datagen = ImageDataGenerator(rescale=1./255)

train_generator = train_datagen.flow_from_directory(
        train_dir,  
        target_size=(IMG_DIM, IMG_DIM), 
        batch_size= BATCH_SIZE,
        class_mode='binary') # for binary_crossentropy
        
# Train the model
history = model.fit_generator(
      train_generator,
      steps_per_epoch=100,  # 2000 images = batch_size * steps
      epochs=10,
      validation_data=validation_generator,
      validation_steps=50,  # 1000 images = batch_size * steps
      verbose=2)
