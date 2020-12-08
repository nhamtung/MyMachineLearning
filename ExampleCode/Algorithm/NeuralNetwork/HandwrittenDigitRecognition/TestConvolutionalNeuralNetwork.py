import sys
import numpy as np
from scipy import misc
import matplotlib.pyplot as plt
from keras.models import model_from_json

# terminal: python -m pip install pillow --user
img = misc.imread("5.jpg", flatten=True)
img = 255 - img
img = misc.imresize(img, (28,28))
img = img.reshape(28,28,1).astype('float32')
img = img/255

f = open('mnist_cnn.json')
json_content = f.read()
f.close()

model = model_from_json(json_content)
model.load_weights('mnist_cnn.h5')

X = np.array([img])
y = model.predict(X)
print('Digit : ', np.argmax(y[0]))