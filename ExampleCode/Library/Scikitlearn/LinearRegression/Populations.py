import numpy
import scipy
from sklearn import linear_model

years = [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010]
populations = [
                6067000000,
                6137000000,
                6215000000,
                6314000000,
                6396000000,
                6477000000,
                6555000000,
                6625000000,
                6705000000,
                6809972000,
                6892319000
              ]
X = [[x] for x in years]
Y = populations

model = linear_model.LinearRegression()
model.fit(X, Y)
a = model.coef_[0]
b = model.intercept_

print("a = ", a)
print("b = ", b)
print('2011 population : ', model.predict(2011)[0])
print('2012 population : ', model.predict(2012)[0])