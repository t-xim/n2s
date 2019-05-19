from keras.applications.resnet50 import ResNet50
from keras.preprocessing import image
from keras.applications.resnet50 import preprocess_input, decode_predictions
import numpy as np

###---OUT-OF-THE-BOX MODELS---###

###---ResNet---###
Res_Model = ResNet50(weights = 'imagenet')


###---VGG16---###
vgg_base = VGG16(weights = 'imagenet', 
                 include_top = False, 
                 input_shape(IMG_DIM, IMG_DIM, 3))

# Setting trainable layers
for layer in vgg.layers:
  layer.trainable = False
  
# Setting almost all layers trainable (last 4 trainable)
for layer in vgg.layers[:-4]:
  layer.trainable = False
