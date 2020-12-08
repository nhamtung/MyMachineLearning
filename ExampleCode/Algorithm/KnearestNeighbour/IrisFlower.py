import numpy as np
import pandas as pd
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
K = 3
def predict(x):
    distances = [(np.sum((x-Xtrain[i])*(x-Xtrain[i])), i)
    for i in range(Ntrain)]
    distances = sorted(distances)
    y_samples = [Ytrain[distances[i][1]] for i in range(K)]
    predict = None
    Nmax = 0
    map_counts = {}
    for species in y_samples:
        map_counts[species] = map_counts.get(species,0) + 1
        if map_counts[species] > Nmax:
            predict = species
            Nmax = map_counts[species]
    return predict
Ypredict = [predict(Xtest[i]) for i in range(Ntest)]
Ncorrect = len([i for i in range(Ntest) if Ypredict[i] == Ytest[i]])
print('test score = ', Ncorrect/Ntest)