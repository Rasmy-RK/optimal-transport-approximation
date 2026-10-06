import numpy as np

np.random.seed(42)

data_a = np.random.normal(0, 1, 1000)
data_b = np.random.normal(2, 1, 1000)

data_a = np.sort(data_a)
data_b = np.sort(data_b)

distance = np.mean(np.abs(data_a - data_b))

print("Wasserstein Distance:", distance)