import numpy as np

num = 4
harmonic_approx = np.log(num) + 0.57721 + (1 / (2 * num)) - (1 / (12 * num ** 2))
print(harmonic_approx)
