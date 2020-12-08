from distutils.log import Log

import pandas as pd

df = pd.read_csv("binary.csv")
X = df[["gre", "gpa", "rank"]].values
Y = df["admit"].values

N = len(X)
Ntrain = int(0.7*N)
Xtrain = X[:Ntrain]
Ytrain = Y[:Ntrain]
Xtest = X[Ntrain:]
Ytest = Y[Ntrain:]

from sklearn.linear_model import LogisticRegression

model = LogisticRegression()
model.fit(Xtrain, Ytrain)
print("train score = ", model.score(Xtrain, Ytrain))

Yval = model.predict(Xtest)
print("testcore = ", model.score(Xtest, Ytest))

