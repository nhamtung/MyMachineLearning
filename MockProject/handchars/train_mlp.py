import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam

input_size = 32
classes = [chr(c) for c in range(ord('a'), ord('z') + 1)]
num_classes = len(classes)

num_pixels = input_size * input_size

Xtrain = np.fromfile('Xtrain.np', dtype=np.uint8).reshape(-1, num_pixels)
ytrain = np.fromfile('Ytrain.np', dtype=np.uint8).reshape(-1, num_classes)
Xtest = np.fromfile('Xtest.np', dtype=np.uint8).reshape(-1, num_pixels)
ytest = np.fromfile('Ytest.np', dtype=np.uint8).reshape(-1, num_classes)

Xtrain = Xtrain.astype('float32') / 255
Xtest = Xtest.astype('float32') / 255

model = Sequential()
model.add(Dense(num_pixels, input_dim=num_pixels, kernel_initializer='normal', activation='relu'))
model.add(Dense(num_classes, kernel_initializer='normal', activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(Xtrain, ytrain, validation_data=(Xtest, ytest), epochs=10, batch_size=200, verbose=True)


f = open('model_mlp.json', 'w')
f.write(model.to_json())
f.close()

model.save_weights('model_mlp_weights.h5')