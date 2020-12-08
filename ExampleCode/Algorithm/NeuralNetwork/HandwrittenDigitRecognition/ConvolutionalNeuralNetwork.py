from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import Flatten
from keras.layers.convolutional import Conv2D
from keras.layers.convolutional import MaxPooling2D
from keras.optimizers import Adam
from keras.utils import to_categorical

(Xtrain, ytrain), (Xtest, ytest) = mnist.load_data()
print(Xtrain)
print(Xtrain.shape)
print(Xtrain.dtype)

print(Xtrain.shape[0])
# Xtrain = Xtrain.reshape(Xtrain.shape[0], 28, 28, 1).astype('float32')
# Xtest = Xtest.reshape(Xtest.shape[0], 28, 28, 1).astype('float32')
# Xtrain = Xtrain / 255
# Xtest = Xtest / 255
# ytrain = to_categorical(ytrain)
# ytest = to_categorical(ytest)
# num_classes = ytest.shape[1]
#
# model = Sequential()
# model.add(Conv2D(32, (5, 5), input_shape=(28, 28, 1), activation='relu'))
# model.add(MaxPooling2D(pool_size=(2, 2)))
# model.add(Dropout(0.2))
# model.add(Flatten())
# model.add(Dense(128, activation='relu'))
# model.add(Dense(num_classes, activation='softmax'))
# model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
# model.fit(Xtrain, ytrain, validation_data=(Xtest, ytest), epochs=10, batch_size=200, verbose=2)
# f = open('mnist_cnn.json', 'w')
# f.write(model.to_json())
# f.close()
# model.save_weights('mnist_cnn.h5')