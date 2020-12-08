import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.optimizers import Adam
import tensorflow as tf


years = list(range(1990, 2008))
energies = [8761, 8818, 8830, 8923, 8993, 9215, 9447, 9540, 9593, 9789, 10016, 10114, 10330, 10688, 11171, 11489, 11835, 12152]

X = [[x] for x in years]
Y = [y/1000 for y in energies]
Xtrain = X[:-2]
Ytrain = Y[:-2]
Xtest = X[-2:]
Ytest = Y[-2:]

scaler = MinMaxScaler()
scaler.fit(Xtrain)

Xtrain = scaler.transform(Xtrain)
Xtest = scaler.transform(Xtest)

model = Sequential()
model.add(Dense(50, input_dim=1, activation='softplus'))
model.add(Dense(1))

adam = Adam(lr=0.01)
model.compile(optimizer=adam, loss='mse')

model.fit(Xtrain, Ytrain, epochs=5000)

Ypredict = model.predict(Xtest)
for i in range(2):
    predict = round(1000 * Ypredict[i][0])
    err = round(100 * (predict - energies[-2+i])/energies[-2+i],1)
    print('Year {}, real : {}, predict : {}, err(%) : {}'.format (years[-2+i], energies[-2+i], predict, err))

plt.plot(years, energies, '.', label='real')
plt.plot(years[:-2], 1000 * model.predict(Xtrain), label='validate')
plt.plot(years[-2:], 1000 * model.predict(Xtest), '.', label='predict')
plt.legend(loc='upper left')
plt.show()