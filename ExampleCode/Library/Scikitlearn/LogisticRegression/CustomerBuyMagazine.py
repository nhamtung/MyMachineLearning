import pandas as pd
from sklearn.linear_model import LogisticRegression

df = pd.read_csv('KidCreative.csv')
values = df.values
Y = values[:, 1]
X = values[:, 2:]

print("Y = ", Y)
print("X = ", X)

N = len(X)
Ntrain = int(0.7 * N)
Xtrain = X[:Ntrain]
Ytrain = Y[:Ntrain]
Xtest = X[Ntrain:]
Ytest = Y[Ntrain:]

model = LogisticRegression()
model.fit(Xtrain, Ytrain)
print('train score = ', model.score(Xtrain, Ytrain))
Yval = model.predict(Xtest)
print('testcore = ', model.score(Xtest, Ytest))