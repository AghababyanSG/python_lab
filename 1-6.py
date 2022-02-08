import math

import matplotlib.pyplot as plt
import numpy as np
from mpmath import nsum, inf

x = np.arange(-2, 2.01, 0.01)
print("select a and b")
out = np.array([nsum(lambda n: (0.5**n) * np.cos(math.pi * t * (float)(3.0 ** n)), [0, inf]) for t in x])
plt.plot(x, out)

plt.show()