import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

def get_class(species):
    return {
        'setosa': 0,
        'versicolor': 1,
        'virginica': 2
        }[species]

df=pd.read_csv("iris.csv")
values = df.values
X = np.array(values[:, :-1], dtype=np.float)
Y = [get_class(species) for species in values[:, -1]]
print("X = ", X)
print("Y = ", Y)

Xtrain = np.concatenate((X[:35], X[50:85], X[100:135]))
Ytrain = Y[:35] + Y[50:85] + Y[100:135]
Xtest = np.concatenate((X[35:50], X[85:100], X[135:]))
Ytest = Y[35:50] + Y[85:100] + Y[135:]

model = DecisionTreeClassifier()
model.fit(Xtrain, Ytrain)

print("train score = ", model.score(Xtrain, Ytrain))
print("test score = ", model.score(Xtest, Ytest))

import pydotplus
import sklearn

class_names = ['setosa', 'versicolor', 'virginica']
feature_names=['sepal length', 'sepal width', 'petal length', 'petal width']

dot_data = sklearn.tree.export_graphviz(model, out_file=None, feature_names=feature_names, class_names=class_names,
                                        filled=True, rounded=True)

graph = pydotplus.graph_from_dot_data(dot_data)
f = open('tree.png', 'wb')
f.write(graph.create_png())
f.close()

