import numpy as np
import pandas as pd
from sklearn import svm
from scipy import sparse

def get_class(species):
    return {
        'setosa': 0,
        'versicolor': 1,
        'virginica': 2
    }[species]

df = pd.read_csv('iris.csv')
values = df.values

X = np.array(values[:, :-1], dtype=np.float)
Y = [get_class(species) for species in values[:, -1]]

Xtrain = np.concatenate((X[:35], X[50:85], X[100:135]))
Ytrain = Y[:35] + Y[50:85] + Y[100:135]
Xtest = np.concatenate((X[35:50], X[85:100], X[135:]))
Ytest = Y[35:50] + Y[85:100] + Y[135:]

model = svm.SVC(kernel='linear')
model.fit(Xtrain, Ytrain)
print('test score = ', model.score(Xtest, Ytest))