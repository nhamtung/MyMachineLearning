import numpy as np
import pandas as pd
from keras.utils import to_categorical
from sklearn import linear_model
import matplotlib.pyplot as plt
import tensorflow as tf

df_weather = pd.read_csv('nyc_weather.csv')

map_temperature = {}
for time_stamp, temp in df_weather.values:
    map_temperature[time_stamp] = temp

df_demand = pd.read_csv('nyc_demand.csv')
demands = df_demand['demand'].values
timeStamps = df_demand['timeStamp'].values
dateTimes = pd.DatetimeIndex(timeStamps)

N = len(demands)
ellapse_days = np.array([(x - dateTimes[0]).days for x in dateTimes])
max_ellapse_day = np.max(ellapse_days)
max_temperature = max(map_temperature.values())
max_demand = max(demands)

X = []
Y = []

for i in range(N):
    if (timeStamps[i] not in map_temperature) or (ellapse_days[i] == 0):
        continue

    temperature = map_temperature[timeStamps[i]]
    hour = dateTimes[i].hour
    is_weekend = 1 if dateTimes[i].weekday() >= 5 else 0
    month = dateTimes[i].month

    previous_day_indexes = np.where(ellapse_days == ellapse_days[i] - 1)[0]
    previous_day_avg_demand = np.mean(demands[previous_day_indexes])  #Dien nang tieu thu trung binh trong 1 ngay

    x = []
    x.append(temperature / max_temperature)
    x.extend(list(to_categorical(hour, 24)))
    x.append(ellapse_days[i] / max_ellapse_day)
    x.append(is_weekend)
    x.extend(list(to_categorical(month - 1, 12)))
    x.append(previous_day_avg_demand / max_demand)
    X.append(x)
    Y.append(demands[i] / max_demand)

X = np.array(X)
Y = np.array(Y)

Ntrain = int(len(X)*0.7)
Xtrain = X[:Ntrain]
Ytrain = Y[:Ntrain]
Xtest = X[Ntrain:]
Ytest = Y[Ntrain:]

model = linear_model.LinearRegression()
model.fit(Xtrain, Ytrain)
Ypred = model.predict(Xtest)

print('Mean absolute error (%) = ', np.mean(np.abs((Ypred-Ytest)/Ytest*100)))

plt.plot(max_demand * Ytest, label='real')
plt.plot(max_demand * Ypred, label='prediction')
plt.ylim(0)
plt.legend(loc='lower center')
plt.show()