
from sklearn.linear_model import LogisticRegression
import numpy as np
import pandas as pd
from scipy import sparse

# a = np.array([[1, 2], [3, 4]])
# b = np.array([[5, 6]])
# c1 = np.concatenate((a, b), axis=0)
# print("\nC1 = \n", c1)
# c2 = np.concatenate((a, b.T), axis=1)
# print("\nC2 = \n", c2)

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
# print("X1 = \n", X1)
# print("X2 = \n", X2)
# print("X3 = \n", X3)

X = np.concatenate((X1.T, X2.T, X3.T, X4), axis=1)
print("\nX = \n", X)

Y = np.array(values[:, -1], dtype=int)
print("Y = ", Y)

Xtrain = X[: int(0.7*len(X))]
Ytrain = Y[: int(0.7*len(Y))]
Xtest = X[int(0.7*len(X)):]
Ytest = Y[int(0.7*len(Y)):]
# print("Xtrain: ", Xtrain)
# print("Ytrain: ", Ytrain)
# print("Xtest: ", Xtest)
# print("Ytest: ", Ytest)

model = LogisticRegression()
model.fit(Xtrain, Ytrain)
print("train score = ", model.score(Xtrain, Ytrain))

Ypredict = model.predict(Xtest)
print("test score = ", model.score(Xtest, Ytest))

for i in range(len(Xtest)):
    print("Ytest = ", Ytest[i], ", \tYpredict = ", Ypredict[i])
