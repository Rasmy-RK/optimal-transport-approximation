import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

data_a = np.random.normal(0, 1, 1000)
data_b = np.random.normal(2, 1, 1000)

plt.hist(data_a, bins=40, alpha=0.5, label="Distribution A")
plt.hist(data_b, bins=40, alpha=0.5, label="Distribution B")

plt.xlabel("Value")
plt.ylabel("Frequency")
plt.title("Two Probability Distributions")
plt.legend()

plt.show()