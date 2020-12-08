import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

df = pd.read_csv('iris.csv')
values = df.values
X = np.array(values[:, :-1], dtype=np.float)
Y = values[:, -1]

Xtrain = np.concatenate((X[:35], X[50:85], X[100:135]))
Ytrain = np.concatenate((Y[:35], Y[50:85], Y[100:135]))
Xtest = np.concatenate((X[35:50], X[85:100], X[135:]))
Ytest = np.concatenate((Y[35:50], Y[85:100], Y[135:]))

Ntrain = len(Xtrain)
Ntest = len(Xtest)

model = KNeighborsClassifier(n_neighbors=3)
model.fit(Xtrain, Ytrain)

score = model.score(Xtest, Ytest)
print('test score = ', score)