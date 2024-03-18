import numpy as np
import matplotlib.pyplot as plt

K = 60
num_r = 1000
num_N0 = 100
num_iterations = 1000
transient_iterations = 100

r_values = np.linspace(1, 4, num_r)
equilibrium_populations = np.zeros((num_r, num_N0))

# Create an array for N0 values
N0_values = np.linspace(0, K, num_N0)

# Iterate over r_values using vectorized operations
for j, N0 in enumerate(N0_values):
    N = np.full_like(r_values, N0, dtype=float)

    for _ in range(transient_iterations):
        N = N * np.exp(r_values * (1 - N / K)) + 4

    for _ in range(num_iterations):
        N = N * np.exp(r_values * (1 - N / K)) + 4

    equilibrium_populations[:, j] = N

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(r_values, equilibrium_populations, '.', markersize=1)
plt.xlabel('r')
plt.ylabel('Equilibrium Population Size')
plt.title('Bifurcation Diagram')
plt.show()
