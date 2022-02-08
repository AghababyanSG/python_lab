import matplotlib.pyplot as plt
import numpy as np
x = [1, 2, 3, 4, 5]
y = [0.99, 0.49, 0.35, 0.253, 0.18]

coefficients = np.polyfit(x, y, deg=2, cov=True)
print(coefficients)
poly = np.poly1d(coefficients[0])
new_x = np.linspace(x[0], x[4])
new_y = poly(new_x)
plt.plot(x, y, "o", new_x, new_y)

plt.errorbar(x, y, xerr=0.05, yerr=0.1)
plt.grid()
plt.show()
