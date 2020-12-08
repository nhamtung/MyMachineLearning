import pandas as pd

df = pd.read_csv("iris.csv")
values = df.values

X1 = values[50:100, 2:4]
X2 = values[100:150, 2:4]

X1train, X1test = X1[:35], X1[35:]
X2train, X2test = X2[:35], X2[35:]

# import matplotlib.pyplot as plt
# plt.plot(X1train[:, 0], X1train[:, 1], '.', label='versicolor')
# plt.plot(X2train[:, 0], X2train[:, 1], '.', label='virginica')
# plt.xlabel('Petal length')
# plt.ylabel('Petal width')
# plt.legend(loc='upper left')
# plt.show()

def predict(petal_length, petal_width):
    distance = (petal_width-1.16)/(1.98-1.16) + (petal_length-5.67)/(5.67-4.18)
    return 1 if distance > 0 else 0

Y1predict = [predict(x[0], x[1]) for x in X1test]
Y2predict = [predict(x[0], x[1]) for x in X2test]

N1correct = len([1 for i in range(len(X1test)) if Y1predict[i] == 0])
N2correct = len([1 for i in range(len(X2test)) if Y2predict[i] == 1])
Ncorrect = N1correct + N2correct

print('score = ', Ncorrect/(len(X1test)+len(X2test)))