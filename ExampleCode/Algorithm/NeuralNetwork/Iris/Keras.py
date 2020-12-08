import numpy as np
import pandas as pd
import tensorflow as tf

from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.optimizers import Adam

def get_class(species):
    return {
        'setosa': [0, 0, 0],
        'versicolor': [0, 1, 0],
        'virginica': [0, 0, 1]
        }[species]

df = pd.read_csv('iris.csv')
values = df.values

X = np.array(values[:, :-1], dtype=np.float)
Y = np.array([get_class(species) for species in values[:, -1]])

Xtrain = np.concatenate((X[:35], X[50:85], X[100:135]))
Ytrain = np.concatenate((Y[:35], Y[50:85], Y[100:135]))
Xtest = np.concatenate((X[35:50], X[85:100], X[135:]))
Ytest = np.concatenate((Y[35:50], Y[85:100], Y[135:]))

model = Sequential()
model.add(Dense(5, input_dim=4, activation='relu'))
model.add(Dense(3, activation='softmax'))
adam = Adam(lr=0.005)

model.compile(optimizer=adam, loss='binary_crossentropy', metrics=['accuracy'])
model.fit(Xtrain, Ytrain, epochs=2000, shuffle=True)

_, score = model.evaluate(Xtest, Ytest)
print('test score = ', score)