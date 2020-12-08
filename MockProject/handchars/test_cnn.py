import numpy as np
import os
from keras.models import model_from_json
from skimage.io import imread
from skimage.transform import resize

test_images_folder = "test_images"

input_size = 32
classes = [chr(c) for c in range(ord('a'), ord('z') + 1)]

f = open('model_cnn.json')
json_content = f.read()
f.close()

model = model_from_json(json_content)
model.load_weights('model_cnn_weights.h5')

def predict(img_path):    
    img = imread(img_path)
    img = img[:,:,-1]
    img = resize(img, (input_size, input_size), preserve_range=True)
    X = img.astype('float32')/255.0
    X = X.reshape((1, input_size, input_size, 1))
    y = model.predict(X)[0]
    return classes[np.argmax(y)]
    
for f in os.listdir(test_images_folder):
    img_path = os.path.join(test_images_folder, f)
    c = predict(img_path)
    print('Input {} , output : {}'.format(img_path, c))