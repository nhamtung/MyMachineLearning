from sklearn import linear_model
import numpy as np
from scipy import sparse

X = [[52,173], [59,184], [67,194], [73,211], [64,196], [74,220], [54,188], [61,188], [65,207], [46,167], [72,217]]
Y = [132, 143, 153, 162, 154, 168, 137, 149, 159, 128, 166]

N = len(X)
Ntrain = int(0.7*N)

Xtrain = X[:Ntrain]
Ytrain = Y[:Ntrain]
Xtest = X[Ntrain:]
Ytest = Y[Ntrain:]

model = linear_model.LinearRegression()
model.fit(Xtrain, Ytrain)

Ypredict = model.predict(Xtest)

for i in range(len(Xtest)):
    print("Y = ", Ytest[i], ", Ypredict = ", Ypredict[i])

