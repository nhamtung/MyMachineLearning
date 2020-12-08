import matplotlib.pyplot as plt

X = [[52,173], [59,184], [67,194], [73,211], [64,196], [74,220], [54,188], [61,188], [65,207], [46,167], [72,217]]
Y = [132, 143, 153, 162, 154, 168, 137, 149, 159, 128, 166]

plt.plot(X, Y)
plt.xlabel("Parameter")
plt.ylable("Systolic Blood Pressure")
plt.show()

