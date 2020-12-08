import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

def ConvertGender(species):
    return {
        'Male': 0,
        'Female': 1,
    }[species]
def ConvertGeography(species):
    return {
        'France': 0,
        'Spain': 1,
        'Germany': 2,
    }[species]

pf = pd.read_csv("Churn_Modelling.csv")
values = pf.values

X1 = np.array([values[:, 3]])
X2 = np.array([[ConvertGeography(species) for species in values[:, 4]]], dtype=int)
X3 = np.array([[ConvertGender(species) for species in values[:, 5]]], dtype=int)
X4 = np.array(values[:, 6:-1])

X = np.concatenate((X1.T, X2.T, X3.T, X4), axis=1)
Y = np.array(values[:, -1], dtype=int)

Xtrain = X[: int(0.7*len(X))]
Ytrain = Y[: int(0.7*len(Y))]
Xtest = X[int(0.7*len(X)):]
Ytest = Y[int(0.7*len(Y)):]

model = KNeighborsClassifier(n_neighbors=5)
model.fit(Xtrain, Ytrain)

score = model.score(Xtest, Ytest)
print('test score = ', score)