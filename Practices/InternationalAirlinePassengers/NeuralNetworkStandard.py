import numpy as np
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.optimizers import Adam
from keras.utils import to_categorical
import matplotlib.pyplot as plt

def create_input_vec(x):
    x1 = (x//12) * 12
    last_year_avg = np.mean(Y[x1-12:x1])
    return [x, last_year_avg] + list(to_categorical(x%12, 12))

df = pd.read_csv("international-airline-passengers.csv")
Y = df.values[:,1].astype('float32')
N = len(Y)

Xtrain = np.array([create_input_vec(x) for x in range(12, N-12)])
Ytrain = Y[12:N-12]
Xtest = np.array([create_input_vec(x) for x in range(N-12, N)])
Ytest = Y[-12:]

model = Sequential()
model.add(Dense(50, input_dim=14, activation='relu'))
model.add(Dense(1))

adam = Adam(lr=0.005, decay=1e-6)
model.compile(optimizer=adam, loss='mse')

model.fit(Xtrain, Ytrain, epochs=3000)

Ypred_train = model.predict(Xtrain).reshape(-1)
Ypred_test = model.predict(Xtest).reshape(-1)
mae = 100 * np.mean(np.abs(Ypred_test-Ytest)/Ytest)
print('Mean absolute error (%) = ', mae)

plt.rcParams['figure.figsize'] = [12, 8]
plt.plot(range(12, N-12), Ytrain)
plt.plot(range(12, N-12), Ypred_train, '--')
plt.plot(range(N-12, N), Ytest)
plt.plot(range(N-12, N), Ypred_test, '--')
plt.ylim(ymin=0)
plt.show()