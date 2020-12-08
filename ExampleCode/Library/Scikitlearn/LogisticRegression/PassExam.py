from sklearn.linear_model import LogisticRegression

data = [
        (0.50, 0),
        (0.75, 0),
        (1.00, 0),
        (1.25, 0),
        (1.50, 0),
        (1.75, 0),
        (1.75, 1),
        (2.00, 0),
        (2.25, 1),
        (2.50, 0),
        (2.75, 1),
        (3.00, 0),
        (3.25, 1),
        (3.50, 0),
        (4.00, 1),
        (4.25, 1),
        (4.50, 1),
        (4.75, 1),
        (5.00, 1),
        (5.50, 1)
    ]
n = len(data)
X = [data[i][0:1] for i in range(0,n)]
Y = [data[i][1] for i in range(0,n)]

model = LogisticRegression(C = 5)
model.fit(X, Y)

print("a = ", model.coef_)
print("b = ", model.intercept_)

score = model.score(X,Y)
print("score = ", score)

P = model.predict_proba(X)
print("x\t y\t Prob\t Predict")

for i in range(0,n):
    x, y, p = X[i][0], Y[i], P[i][1]
    print("%0.2f \t %d\t %.2f\t %d" %(x,y,p,round(p)))
