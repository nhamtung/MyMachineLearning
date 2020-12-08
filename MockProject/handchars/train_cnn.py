import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import Flatten
from keras.layers.convolutional import Conv2D
from keras.layers.convolutional import MaxPooling2D
from keras.optimizers import Adam

input_size = 32
classes = [chr(c) for c in range(ord('a'), ord('z') + 1)]
num_classes = len(classes)

Xtrain = np.fromfile('Xtrain.np', dtype=np.uint8).reshape(-1, input_size, input_size, 1)
ytrain = np.fromfile('Ytrain.np', dtype=np.uint8).reshape(-1, num_classes)
Xtest = np.fromfile('Xtest.np', dtype=np.uint8).reshape(-1, input_size, input_size, 1)
ytest = np.fromfile('Ytest.np', dtype=np.uint8).reshape(-1, num_classes)

Xtrain = Xtrain.astype('float32') / 255
Xtest = Xtest.astype('float32') / 255

model = Sequential()
model.add(Conv2D(32, (5, 5), input_shape=(input_size, input_size, 1), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.2))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dense(num_classes, activation='softmax'))

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(Xtrain, ytrain, validation_data=(Xtest, ytest), epochs=10, batch_size=200, verbose=True)

f = open('model_cnn.json', 'w')
f.write(model.to_json())
f.close()

model.save_weights('model_cnn_weights.h5')