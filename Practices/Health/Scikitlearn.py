from sklearn import linear_model
import pandas as pd
import xlrd
import numpy as np
from scipy import sparse

xls = pd.ExcelFile("mlr07.xls")
df = xls.parse(0)
X = df[["X2", "X3", "X4", "X5"]].values
Y = df["X1"].values

Ntrain = int(0.7*len(X))

Xtrain = X[:Ntrain]
Ytrain = Y[:Ntrain]
Xtest = X[Ntrain:]
Ytest = Y[Ntrain:]

model = linear_model.LinearRegression()
model.fit(Xtrain, Ytrain)

a = model.coef_[0]
b = model.intercept_
print("a = ", a)
print("b = ", b)

Ypredict = model.predict(Xtest)

for i in range(len(Xtest)):
    print("Y = ", Ytest[i], ", Ypredict = ", Ypredict[i])